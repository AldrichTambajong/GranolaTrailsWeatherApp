"""
    everything directly related to the national parks api
"""

# import base64
# import random
import os
import requests

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement

NATIONAL_PARKS_KEY = os.getenv('NATIONAL_PARKS_KEY')
BASE_URL = "developer.nps.gov/api/v1"

from werkzeug.exceptions import InternalServerError, NotFound

def get_activities(activity_ids:list=None, query:str=None, limit:int=50, start:int=0) -> list:
    """
    Returns a list of activities to be found in national parks.

    Parameters
    ----------
    ids: list[str]
        One or more activity unique IDs.
    query: str, optional
        term to search on
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
    activities: list[activity]
        A list of all matching activities

        activity:
            id: str
            name: str
    """
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
        activities = response.json()["data"]
        return activities
    except (InternalServerError, NotFound):
        return []
