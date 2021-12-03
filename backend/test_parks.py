"""
    tests.py

    Performs some basic testing
"""

# pylint: disable=no-member
# pylint: disable=wrong-import-position
# pylint: disable=invalid-envvar-default
# pylint: disable=global-statement
# pylint: disable=import-error
# pylint: disable=protected-access

import unittest

from unittest.mock import MagicMock, patch
import open_weather
import national_parks

KEY_INPUT = "input"
KEY_EXPECTED = "expected"
KEY_LENGTH = "length"
PARK_DATA = "park"
WEATHER = "weather"
OUTPUT = "expected"


class ParksTests(unittest.TestCase):
    """
    tests for the database actions
    """

    def setUp(self):
        # pylint: disable=line-too-long
        self.success_test_params = {
            PARK_DATA: {
                "id": "CCE1AD17-9B13-4D74-9CAC-0278D5477316",
                "url": "https://www.nps.gov/saan/index.htm",
                "fullName": "San Antonio Missions National Historical Park",
                "parkCode": "saan",
                "description": "Welcome to San Antonio Missions, a National Park Service site and the only UNESCO World Heritage Site in Texas. After 10,000 years, the people of South Texas were faced with drought, European diseases, and colonization. In the early 1700s, many Native people of South Texas foreswore their traditional life to become Spanish, accepting a new religion and agrarian lifestyle in hopes of survival.",
                "latitude": "29.31262089",
                "longitude": "-98.4289522",
                "latLong": "lat:29.31262089, long:-98.4289522",
                "activities": [
                    {
                        "id": "09DF0950-D319-4557-A57E-04CD2F63FF42",
                        "name": "Arts and Culture",
                    },
                    {"id": "7CE6E935-F839-4FEC-A63E-052B1DEF39D2", "name": "Biking"},
                    {
                        "id": "8D778629-F603-4C50-A121-6F4BB2FE2C4B",
                        "name": "Road Biking",
                    },
                    {"id": "1DFACD97-1B9C-4F5A-80F2-05593604799E", "name": "Food"},
                    {
                        "id": "C6D3230A-2CEA-4AFE-BFF3-DC1E2C2C4BB4",
                        "name": "Picnicking",
                    },
                    {
                        "id": "B33DC9B6-0B7D-4322-BAD7-A13A34C584A3",
                        "name": "Guided Tours",
                    },
                    {
                        "id": "A0631906-9672-4583-91DE-113B93DB6B6E",
                        "name": "Self-Guided Tours - Walking",
                    },
                    {
                        "id": "C7D5A145-F8EB-4C37-9E92-2F6C6206B196",
                        "name": "Self-Guided Tours - Auto",
                    },
                    {"id": "42FD78B9-2B90-4AA9-BC43-F10E9FEA8B5A", "name": "Hands-On"},
                    {
                        "id": "31F88DA6-696F-441F-89CF-D7B1415C4CB9",
                        "name": "Citizen Science",
                    },
                    {
                        "id": "19A59EFB-DF4B-4049-9EE1-A784CAC9C70C",
                        "name": "Arts and Crafts",
                    },
                    {"id": "4D224BCA-C127-408B-AC75-A51563C42411", "name": "Paddling"},
                    {"id": "F353A9ED-4A08-456E-8DEC-E61974D0FEB6", "name": "Kayaking"},
                    {
                        "id": "DF4A35E0-7983-4A3E-BC47-F37B872B0F25",
                        "name": "Junior Ranger Program",
                    },
                    {
                        "id": "0B685688-3405-4E2A-ABBA-E3069492EC50",
                        "name": "Wildlife Watching",
                    },
                    {
                        "id": "5A2C91D1-50EC-4B24-8BED-A2E11A1892DF",
                        "name": "Birdwatching",
                    },
                    {"id": "0C0D142F-06B5-4BE1-8B44-491B90F93DEB", "name": "Park Film"},
                    {
                        "id": "C8F98B28-3C10-41AE-AA99-092B3B398C43",
                        "name": "Museum Exhibits",
                    },
                    {"id": "24380E3F-AD9D-4E38-BF13-C8EEB21893E7", "name": "Shopping"},
                    {
                        "id": "467DC8B8-0B7D-436D-A026-80A22358F615",
                        "name": "Bookstore and Park Store",
                    },
                ],
                "topics": [
                    {
                        "id": "69693007-2DF2-4EDE-BB3B-A25EBA72BDF5",
                        "name": "Architecture and Building",
                    },
                    {
                        "id": "7F81A0CB-B91F-4896-B9A5-41BE9A54A27B",
                        "name": "Archeology",
                    },
                    {"id": "A0C86055-4C79-4F70-9D2E-6B9B738290D0", "name": "Ruins"},
                    {
                        "id": "7F12224B-217A-4B07-A4A2-636B1CE7F221",
                        "name": "Colonization and Settlement",
                    },
                    {
                        "id": "12EA2B56-17EC-410A-A10D-BFBA87A0669B",
                        "name": "Explorers and Expeditions",
                    },
                    {
                        "id": "1F833C99-A75D-4F9E-9256-B96523485466",
                        "name": "Farming and  Agriculture",
                    },
                    {
                        "id": "9FCC01C6-F068-4A05-9A78-23FEBFADAF56",
                        "name": "Latino American Heritage",
                    },
                    {
                        "id": "A1BAF33E-EA84-4608-A888-4CEE9541F027",
                        "name": "Native American Heritage",
                    },
                    {
                        "id": "518B32FB-339D-4C52-B2C2-04BF406AA4B0",
                        "name": "Religion and Spirituality",
                    },
                    {"id": "039CDC0F-6408-473D-9C9F-83B3B8A1E069", "name": "Missions"},
                    {"id": "98F41FDF-B73F-4B68-8010-53CCB2891E3B", "name": "Churches"},
                    {
                        "id": "3CDB67A9-1EAC-408D-88EC-F26FA35E90AF",
                        "name": "Schools and Education",
                    },
                    {"id": "0D00073E-18C3-46E5-8727-2F87B112DDC6", "name": "Animals"},
                ],
                "states": "TX",
                "contacts": {
                    "phoneNumbers": [
                        {
                            "phoneNumber": "2109321001",
                            "description": "",
                            "extension": "",
                            "type": "Voice",
                        },
                        {
                            "phoneNumber": "2105341106",
                            "description": "",
                            "extension": "",
                            "type": "Fax",
                        },
                    ],
                    "emailAddresses": [
                        {
                            "description": "",
                            "emailAddress": "SAAN_Interpretation@nps.gov",
                        }
                    ],
                },
                "entranceFees": [
                    {
                        "cost": "0.00",
                        "description": "Entrance to the park is free.",
                        "title": "Entrance Fee",
                    }
                ],
                "entrancePasses": [],
                "fees": [],
                "directionsInfo": "Park Headquarter's is located 4 miles south of downtown San Antonio. The four mission sites lay as a chain south of downtown. Mission Concepción is 3 miles, Mission San José and the park visitor center is 6 miles south, Mission San Juan is 3 miles south of San José, and Mission Espada lays another mile beyond. Written directions and GPS addresses can be found at the link below.",
                "directionsUrl": "http://www.nps.gov/saan/planyourvisit/directions.htm",
                "operatingHours": [
                    {
                        "exceptions": [
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2022-01-01",
                                "name": "Closed",
                                "endDate": "2022-01-01",
                            }
                        ],
                        "description": "Following guidance from the CDC and recommendations from state and local public health in consultation with NPS Public Health Service officers, Park Store is open 9 am to 1 pm and 2 pm to 5 pm, 7 days/week. Park grounds are open. Park grounds are closed on Thanksgiving Day, Christmas Day, and New Year's Day.",
                        "standardHours": {
                            "wednesday": "Sunrise to Sunset",
                            "monday": "Sunrise to Sunset",
                            "thursday": "Sunrise to Sunset",
                            "sunday": "Sunrise to Sunset",
                            "tuesday": "Sunrise to Sunset",
                            "friday": "Sunrise to Sunset",
                            "saturday": "Sunrise to Sunset",
                        },
                        "name": "San Antonio Missions National Historical Park",
                    },
                    {
                        "exceptions": [
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2022-01-01",
                                "name": "New Years Day",
                                "endDate": "2022-01-01",
                            },
                            {
                                "exceptionHours": {"saturday": "Closed"},
                                "startDate": "2022-01-01",
                                "name": "New Year's Day 2022",
                                "endDate": "2022-01-01",
                            },
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2021-12-25",
                                "name": "Christmas Day",
                                "endDate": "2021-12-25",
                            },
                        ],
                        "description": "The Visitor Center at Mission San José includes the Park Store and an information desk. Visit the Visitor Center for park information or to pick up your Junior Ranger booklet! Park Store is located inside of the Visitor Center and is open 10 am to 12 pm and 1 pm to 4 pm, 7 days/week.",
                        "standardHours": {
                            "wednesday": "9:00AM - 5:00PM",
                            "monday": "9:00AM - 5:00PM",
                            "thursday": "9:00AM - 5:00PM",
                            "sunday": "9:00AM - 5:00PM",
                            "tuesday": "9:00AM - 5:00PM",
                            "friday": "9:00AM - 5:00PM",
                            "saturday": "9:00AM - 5:00PM",
                        },
                        "name": "Mission San José",
                    },
                    {
                        "exceptions": [
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2022-01-01",
                                "name": "New Years Day",
                                "endDate": "2022-01-01",
                            },
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2022-11-25",
                                "name": "Thanksgiving Day",
                                "endDate": "2022-11-25",
                            },
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2021-12-25",
                                "name": "Christmas Day",
                                "endDate": "2021-12-25",
                            },
                        ],
                        "description": "The contact station at Mission Concepción operates on a 9:00 am to 5:00 pm schedule.",
                        "standardHours": {
                            "wednesday": "9:00AM - 5:00PM",
                            "monday": "9:00AM - 5:00PM",
                            "thursday": "9:00AM - 5:00PM",
                            "sunday": "9:00AM - 5:00PM",
                            "tuesday": "9:00AM - 5:00PM",
                            "friday": "9:00AM - 5:00PM",
                            "saturday": "9:00AM - 5:00PM",
                        },
                        "name": "Contact Station at Mission Concepción",
                    },
                    {
                        "exceptions": [
                            {
                                "exceptionHours": {
                                    "wednesday": "Closed",
                                    "monday": "Closed",
                                    "thursday": "Closed",
                                    "sunday": "Closed",
                                    "tuesday": "Closed",
                                    "friday": "Closed",
                                    "saturday": "Closed",
                                },
                                "startDate": "2022-01-01",
                                "name": "New Years Day",
                                "endDate": "2022-01-01",
                            }
                        ],
                        "description": "Contact Stations at the two southern mission sites, Mission Espada and Mission San Juan, open at 10:00 am.",
                        "standardHours": {
                            "wednesday": "9:00AM - 5:00PM",
                            "monday": "9:00AM - 5:00PM",
                            "thursday": "9:00AM - 5:00PM",
                            "sunday": "9:00AM - 5:00PM",
                            "tuesday": "9:00AM - 5:00PM",
                            "friday": "9:00AM - 5:00PM",
                            "saturday": "9:00AM - 5:00PM",
                        },
                        "name": "Mission Espada and Mission San Juan",
                    },
                ],
                "addresses": [
                    {
                        "postalCode": "78214",
                        "city": "San Antonio",
                        "stateCode": "TX",
                        "line1": "Visitor Center at Mission San José",
                        "type": "Physical",
                        "line3": "",
                        "line2": "6701 San Jose Drive",
                    },
                    {
                        "postalCode": "78210",
                        "city": "San Antonio",
                        "stateCode": "TX",
                        "line1": "Headquarters",
                        "type": "Mailing",
                        "line3": "",
                        "line2": "2202 Roosevelt Avenue",
                    },
                ],
                "images": [
                    {
                        "credit": "NPS Photo",
                        "title": "Mission Espada, World Heritage Site",
                        "altText": "Mission Espada, World Heritage Site",
                        "caption": "A part of Mission Espada's ranch is located 30 miles south-east, outside of Floresville, TX.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C7DAC12-1DD8-B71B-0B52A18E18ADF8B7.jpg",
                    },
                    {
                        "credit": "NPS Photo.",
                        "title": "Tours of Mission San José",
                        "altText": "Park Ranger leads a tour through Mission San José",
                        "caption": "Catch a tour at Mission San José at 10:00, 11:00, 1:00 and 3:00 daily.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/A1F5E6C0-1DD8-B71B-0B23C3B88803DB0B.jpg",
                    },
                    {
                        "credit": "NPS Photo.",
                        "title": "Rose Window at Mission San Jose",
                        "altText": "Rose window at mission San Jose, with linestone carvings surrounding a small glass window.",
                        "caption": "The Rose Window is a famous feature of Mission San Jose.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/D5A9A6DD-DAAA-BD2B-2AE4B53C57B3E1C0.jpg",
                    },
                    {
                        "credit": "NPS Photo.",
                        "title": "Mission San Jose sunset",
                        "altText": "Mission San Jose church and convento during the golden hour with tree",
                        "caption": "Explore 18th century mission sites like Mission San Jose.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/1D36B273-BA5C-39AB-F75912DA746E3D67.jpg",
                    },
                    {
                        "credit": "NPS Photo.",
                        "title": "Mission Concepcion Convento & Church",
                        "altText": "Mission Concepcion convento with church in background.",
                        "caption": "Mission Concepcion is the nation's oldest unrestored stone church.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/1D4C640B-AC88-ED51-59AE87D041A0B129.jpg",
                    },
                ],
                "weatherInfo": "Over the course of a year, the temperature typically varies from 40°F to 95°F and is rarely below 29°F or above 100°F. The warm season lasts from May through September with an average daily high temperature above 90°F and a low of 75°F. The cold season lasts from November through February with an average daily high below 68°F and an average low of 40°F. The relative humidity ranges from 40-80% over the course of the year, which can be very uncomfortable to many people.",
                "name": "San Antonio Missions",
                "designation": "National Historical Park",
            },
            WEATHER: {
                "clouds": 5,
                "condition": "Drizzle",
                "current": 68.18,
                "high": 72.52,
                "low": 50.97,
                "precipitation": 0.05,
            },
            OUTPUT: {
                "activities": {
                    "bouldering": True,
                    "camping": False,
                    "fishing": True,
                    "hiking": True,
                    "offroading": True,
                },
                "description": "Welcome to San Antonio Missions, a National Park Service site and the only UNESCO World Heritage Site in Texas. After 10,000 years, the people of South Texas were faced with drought, European diseases, and colonization. In the early 1700s, many Native people of South Texas foreswore their traditional life to become Spanish, accepting a new religion and agrarian lifestyle in hopes of survival.",
                "id": "CCE1AD17-9B13-4D74-9CAC-0278D5477316",
                "img": "https://www.nps.gov/common/uploads/structured_data/3C7DAC12-1DD8-B71B-0B52A18E18ADF8B7.jpg",
                "name": "San Antonio Missions National Historical Park",
                "url": "https://www.nps.gov/saan/index.htm",
                "weather": {
                    "clouds": 5,
                    "condition": "Drizzle",
                    "current": 68.18,
                    "high": 72.52,
                    "low": 50.97,
                    "precipitation": 5,
                },
            },
        }

        # pylint: enable=line-too-long

    @patch("national_parks.get_forecast_by_coordinates")
    def test_park_formatting(self, mock_weather):
        """
        case where the formatting was correct
        """
        self.maxDiff = None
        test = self.success_test_params
        park_data = test[PARK_DATA]
        weather = test[WEATHER]
        expected = test[OUTPUT]
        mock_weather.return_value = weather
        actual = national_parks._park_from_data(park_data)

        print(actual)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
