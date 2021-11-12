"""
    everything directly related to the national parks api
"""

# import base64
# import random
import os
import random
from collections import namedtuple
import requests

from werkzeug.exceptions import InternalServerError, NotFound

from open_weather import get_forecast_by_coordinates

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
    """

    _description = data["description"]
    _id = data["id"]
    _img = ""
    if data["images"]:
        _img = data["images"][0]["url"]
    _name = data["fullName"]
    _url = data["url"]
    _latLong = data["latLong"].split(",")
    _latitude = _latLong[0].split(":")[1]
    _longitude = _latLong[1].split(":")[1]
    _weather = get_forecast_by_coordinates(_latitude, _longitude)

    park = {}

    park["id"] = _id
    park["name"] = _name
    park["description"] = _description
    park["url"] = _url
    park["img"] = _img
    park["weather"] = _weather

    return park


def get_parks_by_activities(
    query: str = None,
    activity_ids: list = None,
    limit: int = 5,
    start: int = 0,
    sort: str = None,
    state: str = "",
) -> list:
    """
    Retrieve national parks that are related to particular categories of activity
    (astronomy, hiking, wildlife watching, etc.).

    Parameters
    ----------
    query: str, optional
        A string to search for.
    ids: list[str], optional
        A list of activity IDs.
    limit: int, default 50
        Number of results to return per request.
    start: int, default 0
        Get the next [limit] results starting with this number.
    sort: str, optional
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
    if activity_ids == None:
        activity_ids = []
    try:
        response = requests.get(
            f"{BASE_URL}/activities/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "id": ",".join(activity_ids),
                "q": query,
                "limit": MAX_LIMIT,
                "start": start,
                "sort": sort,
            },
        )
        data = response.json()["data"][0]["parks"]
        data_state = random.sample(
            list(filter(lambda p: state in p["states"], data)), limit
        )
        codes = list(map(lambda p: p["parkCode"], data_state))
        parks = []
        for i in range(len(codes)):
            parks.append(get_parks(park_codes=[codes[i]], limit=1)[0])
            if i > limit:
                break
        return parks
    except (InternalServerError, NotFound, TypeError) as e:
        print(e)
        return []


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

    if park_codes == None:
        park_codes = []

    try:
        response = requests.get(
            f"{BASE_URL}/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "q": query,
                "parkCode": ",".join(park_codes),
                # "stateCode": state_code,
                # "limit": limit,
                # "start": start,
                # "sort": sort,
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
