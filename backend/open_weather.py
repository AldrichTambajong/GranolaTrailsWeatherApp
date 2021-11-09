"""
    everything directly related to the OpenWeather api
"""

import os
from datetime import datetime
import requests


from werkzeug.exceptions import InternalServerError, NotFound

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement

OPEN_WEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_forecast_by_city(city: str, state: str):
    """
    Search weather forecast for 5 days with data every 3 hours by city name.

    Parameters
    ----------
    city: str
        name of the city
    state: str
        2-character state code

    Returns
    -------
    list
        cloudiness: int
            percentage of cloud cover
        feel: float
            feels like temperature, fahrenheit
        humidity: int
            humidity percentage
        precipitation: int
            probability of precipitation
        temp: float
            temperature, fahrenheit
        time:
            dt: int
                absolute time of entry
            month: int
            day: int
            hour: int
        visibility: int
            average visibility in meters
        weather: str
            https://openweathermap.org/weather-conditions
        wind: float
            wind speed, mph
    """
    try:
        response = requests.get(
            f"{BASE_URL}/forecast",
            params={
                "appid": OPEN_WEATHER_KEY,
                "q": f"{city},{state},us",
                "units": "imperial",
            },
        )
        data = response.json()
        weather = list(map(format_weather_entry, data["list"]))
        return weather
    except (InternalServerError, NotFound, KeyError, TypeError):
        return []


def get_forecast_by_coordinates(latitude: float, longitude: float):
    """
    Search weather forecast for 5 days with data every 3 hours by city name.

    Parameters
    ----------
    latitude: float
    longitude: float

    Returns
    -------
    list
        cloudiness: int
            percentage of cloud cover
        feel: float
            feels like temperature, fahrenheit
        humidity: int
            humidity percentage
        precipitation: int
            probability of precipitation
        temp: float
            temperature, fahrenheit
        time:
            dt: int
                absolute time of entry
            month: int
            day: int
            hour: int
        visibility: int
            average visibility in meters
        weather: str
            https://openweathermap.org/weather-conditions
        wind: float
            wind speed, mph
    """
    try:
        response = requests.get(
            f"{BASE_URL}/forecast",
            params={
                "appid": OPEN_WEATHER_KEY,
                "lat": latitude,
                "lon": longitude,
                "units": "imperial",
            },
        )
        data = response.json()
        weather = list(map(format_weather_entry, data["list"]))
        return weather
    except (InternalServerError, NotFound, KeyError, TypeError):
        return []


def format_weather_entry(entry):
    """
    formats the weather entry to be more useful
    """

    w_time = datetime.fromtimestamp(entry["dt"])
    entry["time"] = {}
    entry["time"]["dt"] = entry["dt"]
    entry["time"]["month"] = w_time.month
    entry["time"]["day"] = w_time.day
    entry["time"]["hour"] = w_time.hour
    entry["cloudiness"] = entry["clouds"]["all"]
    entry["wind"] = entry["wind"]["speed"]
    for i in range(len(entry["weather"])):
        entry["weather"][i] = entry["weather"][i]["main"]
    entry["weather"] = ",".join(entry["weather"])
    entry["feel"] = entry["main"]["feels_like"]
    entry["humidity"] = entry["main"]["humidity"]
    entry["temp"] = entry["main"]["temp"]
    entry["precipitation"] = entry["pop"]
    del entry["main"]
    del entry["pop"]
    del entry["clouds"]
    del entry["dt"]
    del entry["dt_txt"]
    del entry["sys"]
    return entry
