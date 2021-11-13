"""
    everything directly related to the national parks api
"""

# import base64
# import random
import os
import random
import requests

from werkzeug.exceptions import InternalServerError, NotFound

# pylint: disable=import-error
from open_weather import get_forecast_by_coordinates

# pylint: enable=import-error

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement

NATIONAL_PARKS_KEY = os.getenv("NATIONAL_PARKS_KEY")
BASE_URL = "https://developer.nps.gov/api/v1"

MAX_LIMIT = 1000000

__ALL_ACTIVITIES = None


def _park_from_data(data):
    """
    takes in the info for a park from /parks
    returns a clean object

    Park
    ----
    description: str
    id: str
    img: str
    name: str
    parkCode: str
    url: str
    weather:
        clouds: int
            0 to 100, percentage
        precipitation: int
            0 to 100, percentage
        temperature: float
        weather: str
            short description of weather
            https://openweathermap.org/weather-conditions
    """

    _description = data["description"]
    _id = data["id"]
    _img = ""
    if data["images"]:
        _img = data["images"][0]["url"]
    _name = data["fullName"]
    _url = data["url"]
    _lat_long = data["latLong"].split(",")
    _latitude = _lat_long[0].split(":")[1]
    _longitude = _lat_long[1].split(":")[1]
    _weather = get_forecast_by_coordinates(_latitude, _longitude)

    park = {
        "id": _id,
        "name": _name,
        "description": _description,
        "url": _url,
        "img": _img,
        "weather": _weather,
    }

    return park


# pylint: disable=too-many-arguments
def get_parks_and_weather(
    activity_ids: list = None,
    state: str = "",
    query: str = None,
    limit: int = 5,
    sort: bool = False,
) -> list:
    """
    Retrieve national parks that are related to particular categories of activity
    (astronomy, hiking, wildlife watching, etc.).

    Parameters
    ----------
    activity_ids: list[str], optional
        A list of activity IDs.
    state: str
        2-character state code
    query: str, optional
        A string to search for.
    limit: int, default 50
        Number of results to return per request.
    sort: bool, default False
        True: sorted by name
        False: random

    Returns
    -------
    list
        description: str
        id: str
        img: str
        name: str
        parkCode: str
        url: str
        weather:
            clouds: int
                0 to 100, percentage
            precipitation: int
                0 to 100, percentage
            temperature: float
            weather: str
                short description of weather
                https://openweathermap.org/weather-conditions
    """
    if activity_ids is None:
        activity_ids = []
    try:
        response = requests.get(
            f"{BASE_URL}/activities/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "id": ",".join(activity_ids),
                "q": query,
                "limit": MAX_LIMIT,
            },
        )
        data = response.json()["data"][0]["parks"]
        data_state = list(filter(lambda p: state in p["states"], data))
        if sort:
            data_state = data_state[:limit]
        else:
            data_state = random.sample(data_state, limit)
        codes = list(map(lambda p: p["parkCode"], data_state))
        parks = []
        for index, value in enumerate(codes):
            parks.append(get_parks(park_codes=[value], limit=1)[0])
            if index > limit:
                break
        return parks
    except (InternalServerError, NotFound, TypeError) as error:
        print(error)
        return []


# pylint: enable=too-many-arguments


# pylint: disable=too-many-arguments
def get_parks(
    query: str = None,
    park_codes: list = None,
    state_code: str = None,
    limit: int = 5,
    start: int = 0,
    sort: str = "fullName",
) -> list:
    """
    Retrieve data about national parks
    (addresses, contacts, description, hours of operation, etc.).

    Parameters
    ----------
    query: str, optional
        A string to search for.

    park_codes: list[str], optional
        list of 4-character park codes

    state_code: str, optional
        2-character state codes

    limit: int, default 50
        Number of results to return per request.

    start: int, default 0
        Get the next [limit] results starting with this number.

    sort: str, default fullName
        A comma delimited list of fields to sort the results by.
        Ascending order is assumed for each field unless the field
        name is prefixed with the unary negative which implies
        descending order.

    Returns
    -------
    list
        description: str
        id: str
        img: str
        name: str
        parkCode: str
        url: str
        weather:
            clouds: int
                0 to 100, percentage
            precipitation: int
                0 to 100, percentage
            temperature: float
            weather: str
    """

    if park_codes is None:
        park_codes = []

    try:
        response = requests.get(
            f"{BASE_URL}/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "q": query,
                "parkCode": ",".join(park_codes),
                "stateCode": state_code,
                "limit": limit,
                "start": start,
                "sort": sort,
            },
        )
        data = response.json()["data"]
        parks = list(map(_park_from_data, data))
        return parks
    except (InternalServerError, NotFound, TypeError):
        return []


# pylint: enable=too-many-arguments


def get_activities(
    query: str = None, activity_ids: list = None, limit: int = 50, start: int = 0
) -> list:
    """
    Retrieve categories of activities (astronomy, hiking, wildlife watching, etc.)
    possible in national parks.

    Parameters
    ----------
    query: str, optional
        term to search on
    ids: list[str], optional
        One or more activity unique IDs.
    limit: int, default 50
        Number of results to return per request.
    start: int, default 0
        Get the next [limit] results starting with this number.

    Returns
    -------
    list[activity]
        A list of all matching activities

        activity:
            id: str
            name: str
    """

    if query:
        query = query.title()

    try:
        response = requests.get(
            f"{BASE_URL}/activities",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "ids": activity_ids,
                "q": query,
                "limit": limit,
                "start": start,
            },
        )
        data = response.json()["data"]
        return data
    except (InternalServerError, NotFound, TypeError):
        return []


def get_all_activities():
    """
    Retrieve all categories of activities (astronomy, hiking, wildlife watching, etc.)
    possible in national parks.

    Returns
    -------
    list[activity]
        A list of all activities

        activity:
            id: str
            name: str
    """

    global __ALL_ACTIVITIES

    if not __ALL_ACTIVITIES:
        __ALL_ACTIVITIES = get_activities(limit=MAX_LIMIT)
    return __ALL_ACTIVITIES


def find_activity(query: str):
    """
    Retrieve all categories of activities (astronomy, hiking, wildlife watching, etc.)
    possible in national parks.

    Parameters
    ----------
    query: str
        name to search activites by

    Returns
    -------
    list[activity]
        A list of all matching activities

        activity:
            id: str
            name: str
    """

    activities = get_all_activities()
    matches = list(filter(lambda a: query.lower() in a["name"].lower(), activities))
    return matches
