"""
    everything directly related to the OpenWeather api
"""

import os
from collections import namedtuple
from datetime import datetime
import requests


from werkzeug.exceptions import InternalServerError, NotFound

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement

OPEN_WEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"

EXCLUDED = ["current", "minutely", "hourly", "alerts"]


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
    list of the Weather namedtuple
        weather: list[str]
            https://openweathermap.org/weather-conditions
        temperature: float
            fahrenheit
        precipitation: int
            probability of precipitation
            from 0 to 100
        clouds: int
            percentage of cloud cover
            from 0 to 100
        month: int
        day: int
        hour: int
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
        weather = list(map(_format_weather_entry, data["list"]))
        return weather
    except (InternalServerError, NotFound, KeyError, TypeError):
        print("failed response")
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
    list of the Weather namedtuple
        weather: list[str]
            https://openweathermap.org/weather-conditions
        temperature: float
            fahrenheit
        precipitation: int
            probability of precipitation
            from 0 to 100
        clouds: int
            percentage of cloud cover
            from 0 to 100
        month: int
        day: int
        hour: int
    """
    try:
        response = requests.get(
            f"{BASE_URL}/onecall",
            params={
                "appid": OPEN_WEATHER_KEY,
                "lat": latitude,
                "lon": longitude,
                "units": "imperial",
                "exclude": ",".join(EXCLUDED),
            },
        )
        data = response.json()
        weather = _format_weather_entry(data["daily"][0])
        return weather
    except (InternalServerError, NotFound, KeyError, TypeError):
        print("failed response")
        return []


def _format_weather_entry(data):
    """
    formats the weather entry to be more useful
    """

    _weather = data["weather"][0]["main"]
    _temperature = data["temp"]["day"]
    _precipitation = data["pop"]
    _clouds = data["clouds"]

    _forecast = {}

    _forecast["weather"] = _weather
    _forecast["temperature"] = _temperature
    _forecast["precipitation"] = _precipitation
    _forecast["clouds"] = _clouds

    return _forecast
