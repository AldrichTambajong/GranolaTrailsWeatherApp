"""
    everything directly related to the national parks api
"""

# import base64
# import random
import os
import requests

from werkzeug.exceptions import InternalServerError, NotFound

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement

NATIONAL_PARKS_KEY = os.getenv("NATIONAL_PARKS_KEY")
BASE_URL = "https://developer.nps.gov/api/v1"

MAX_LIMIT = 1000000

__ALL_ACTIVITIES = None


def __park_from_data(data):
    """
    takes in the info for a park from /parks
    returns a clean object

    Park
    ----
    activities: list
        id: str
        name: str
    description: str
    directionsInfo: str
    directionsURL: str
    id: str
    images: list
        credit: str
        altText: str
        title: str
        id: int
        caption: str
        url: str
    latitude: float
    longitude: float
    name: str
    parkCode: str
    states: list[str]
        list of 2-character state codes
    url: str

    """
    park = {}
    park["activities"] = data["activities"]
    park["directions_info"] = data["directionsInfo"]
    park["id"] = data["id"]
    park["images"] = data["images"]

    lat, long = data["latLong"].split(",")
    park["latitude"] = float(lat.split(":")[1])
    park["longitude"] = float(long.split(":")[1])

    park["name"] = data["fullName"]
    park["park_code"] = data["parkCode"]
    park["states"] = data["states"].split(",")
    park["url"] = data["url"]

    return park


def get_parks_by_activities(
    query: str = None,
    activity_ids: list = None,
    limit: int = 50,
    start: int = 0,
    sort: str = None,
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
    list[activity_parks]

        activity_parks:
            id: str
            name: str
            parks: [park]

        park:
            states: str
                comma separated 2-character state codes
            parkCode: str
            designation: str
            fullName: str
            url: str
            name: str
    """
    try:
        response = requests.get(
            f"{BASE_URL}/activities/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "ids": activity_ids,
                "q": query,
                "limit": limit,
                "start": start,
                "sort": sort,
            },
        )
        data = response.json()["data"]
        return data
    except (InternalServerError, NotFound, TypeError):
        return []


# pylint: disable=too-many-arguments
def get_parks(
    query: str = None,
    park_codes: list = None,
    state_code: str = None,
    limit: int = 50,
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
        activities: list
            id: str
            name: str
        description: str
        directionsInfo: str
        directionsURL: str
        id: str
        images: list
            credit: str
            altText: str
            title: str
            id: int
            caption: str
            url: str
        latitude: float
        longitude: float
        name: str
        parkCode: str
        states: list[str]
            list of 2-character state codes
        url: str
    """
    if not park_codes:
        park_codes = []

    if park_codes and not isinstance(park_codes, list):
        park_codes = list(park_codes)

    try:
        response = requests.get(
            f"{BASE_URL}/parks",
            params={
                "api_key": NATIONAL_PARKS_KEY,
                "q": query,
                "parkCode": park_codes,
                "stateCode": state_code,
                "limit": limit,
                "start": start,
                "sort": sort,
            },
        )
        data = response.json()["data"]
        parks = list(map(__park_from_data, data))
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
