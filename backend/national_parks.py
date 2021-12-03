"""
    everything directly related to the national parks api
"""

# import base64
# import random
import os
import re
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

ACTIVITIES = {
    "arts_and_culture": "09DF0950-D319-4557-A57E-04CD2F63FF42",
    "astronomy": "13A57703-BB1A-41A2-94B8-53B692EB7238",
    "auto_and_atv": "5F723BAD-7359-48FC-98FA-631592256E35",
    "biking": "7CE6E935-F839-4FEC-A63E-052B1DEF39D2",
    "boating": "071BA73C-1D3C-46D4-A53C-00D5602F7F0E",
    "camping": "A59947B7-3376-49B4-AD02-C0423E08C5F7",
    "canyoneering": "07CBCA6A-46B8-413F-8B6C-ABEDEBF9853E",
    "caving": "BA316D0F-92AE-4E00-8C80-DBD605DC58C3",
    "climbing": "B12FAAB9-713F-4B38-83E4-A273F5A43C77",
    "compass_and_gps": "C11D3746-5063-4BD0-B245-7178D1AD866C",
    "dog_sledding": "8C495067-8E94-4D78-BBD4-3379DACF6550",
    "fishing": "AE42B46C-E4B7-4889-A122-08FE180371AE",
    "flying": "D72206E4-6CD1-4441-A355-F8F1827466B1",
    "food": "1DFACD97-1B9C-4F5A-80F2-05593604799E",
    "golfing": "3F3ABD16-2C52-4EAA-A1F6-4235DE5686F0",
    "guided_tours": "B33DC9B6-0B7D-4322-BAD7-A13A34C584A3",
    "hands-on": "42FD78B9-2B90-4AA9-BC43-F10E9FEA8B5A",
    "hiking": "BFF8C027-7C8F-480B-A5F8-CD8CE490BFBA",
    "horse_trekking": "0307955A-B65C-4CE4-A780-EB36BAAADF0B",
    "hunting_and_gathering": "8386EEAF-985F-4DE8-9037-CCF91975AC94",
    "ice_skating": "5FF5B286-E9C3-430E-B612-3380D8138600",
    "junior_ranger_program": "DF4A35E0-7983-4A3E-BC47-F37B872B0F25",
    "living_history": "B204DE60-5A24-43DD-8902-C81625A09A74",
    "museum_exhibits": "C8F98B28-3C10-41AE-AA99-092B3B398C43",
    "paddling": "4D224BCA-C127-408B-AC75-A51563C42411",
    "park_film": "0C0D142F-06B5-4BE1-8B44-491B90F93DEB",
    "playground": "7779241F-A70B-49BC-86F0-829AE332C708",
    "scuba_diving": "42CF4021-8524-428E-866A-D33097A4A764",
    "shopping": "24380E3F-AD9D-4E38-BF13-C8EEB21893E7",
    "skiing": "F9B1D433-6B86-4804-AED7-B50A519A3B7C",
    "snorkeling": "3EBF7EAC-68FC-4754-B6A4-0C38A1583D45",
    "snow_play": "C38B3C62-1BBF-4EA1-A1A2-35DE21B74C17",
    "snowmobiling": "7C912B83-1B1B-4807-9B66-97C12211E48E",
    "snowshoeing": "01D717BC-18BB-4FE4-95BA-6B13AD702038",
    "surfing": "AE3C95F5-E05B-4A28-81DD-1C5FD4BE88E2",
    "swimming": "587BB2D3-EC35-41B2-B3F7-A39E2B088AEE",
    "team_sports": "94369BFD-F186-477E-8713-AE2A745154DA",
    "tubing": "4D06CEED-90C6-4B69-B264-32CC90B69BA6",
    "water_skiing": "8A1C7B17-C2C6-4F7C-9539-EA1E19971D80",
    "wildlife_watching": "0B685688-3405-4E2A-ABBA-E3069492EC50",
}


DRIZZLE_LIMIT = 5
COLD_LIMIT = 32
HOT_LIMIT = 90


def go_hiking(weather):
    return (
        weather["condition"] in ["Clear", "Clouds", "Drizzle"]
        and weather["precipitation"] <= DRIZZLE_LIMIT
    )


def go_fishing(weather):
    return (
        weather["condition"] in ["Clear", "Clouds", "Drizzle"]
        and weather["precipitation"] <= DRIZZLE_LIMIT
        and COLD_LIMIT <= weather["low"]
        and weather["high"] <= HOT_LIMIT
    )


def go_offroading(weather):
    return (
        weather["condition"] in ["Clear", "Clouds", "Drizzle"]
        and weather["precipitation"] <= DRIZZLE_LIMIT
    )


def go_camping(weather):
    return weather["condition"] in ["Clear", "Clouds"]


def go_bouldering(weather):
    return (
        weather["condition"] in ["Clear", "Clouds", "Drizzle"]
        and weather["precipitation"] <= DRIZZLE_LIMIT
    )


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

    _description = re.findall(r"[^?!.]+[?!.]", _description)[0]

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

    _activities = {
        "hiking": go_hiking(_weather),
        "fishing": go_fishing(_weather),
        "offroading": go_offroading(_weather),
        "camping": go_camping(_weather),
        "bouldering": go_bouldering(_weather),
    }

    park = {
        "id": _id,
        "name": _name,
        "description": _description,
        "url": _url,
        "img": _img,
        "weather": _weather,
        "activities": _activities,
    }

    return park


def get_parks_and_weather(
    activity_ids: list = None,
    state: str = "",
    query: str = None,
    limit: int = 4,
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
    else:
        activity_ids = map(lambda a: ACTIVITIES[a], activity_ids)
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
        if data_state:
            amount = min(len(data_state), limit)
            if sort:
                data_state = data_state[:amount]
            else:
                data_state = random.sample(data_state, amount)
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
