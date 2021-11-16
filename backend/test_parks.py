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
                "id": "81AFEB37-7119-4BF1-B65B-806BAB973FFD",
                "url": "https://www.nps.gov/ocmu/index.htm",
                "fullName": "Ocmulgee Mounds National Historical Park",
                "parkCode": "ocmu",
                "description": "Welcome to Ocmulgee Mounds National Historical Park. This park is a prehistoric American Indian site, where many different American Indian cultures occupied this land for thousands of years. American Indians first came here during the Paleo-Indian Period hunting Ice Age mammals. Around 900 CE, the Mississippian Period began, and people constructed mounds for their elite, which remain here today.",
                "latitude": "32.83816576",
                "longitude": "-83.60224853",
                "latLong": "lat:32.83816576, long:-83.60224853",
                "activities": [
                    {
                        "id": "7CE6E935-F839-4FEC-A63E-052B1DEF39D2",
                        "name": "Biking",
                    },
                    {
                        "id": "AE42B46C-E4B7-4889-A122-08FE180371AE",
                        "name": "Fishing",
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
                        "id": "BFF8C027-7C8F-480B-A5F8-CD8CE490BFBA",
                        "name": "Hiking",
                    },
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
                    {
                        "id": "0C0D142F-06B5-4BE1-8B44-491B90F93DEB",
                        "name": "Park Film",
                    },
                    {
                        "id": "C8F98B28-3C10-41AE-AA99-092B3B398C43",
                        "name": "Museum Exhibits",
                    },
                    {
                        "id": "24380E3F-AD9D-4E38-BF13-C8EEB21893E7",
                        "name": "Shopping",
                    },
                    {
                        "id": "43800AD1-D439-40F3-AAB3-9FB651FE45BB",
                        "name": "Gift Shop and Souvenirs",
                    },
                ],
                "topics": [
                    {
                        "id": "7F81A0CB-B91F-4896-B9A5-41BE9A54A27B",
                        "name": "Archeology",
                    },
                    {
                        "id": "3B0D607D-9933-425A-BFA0-21529AC4734C",
                        "name": "Military",
                    },
                    {
                        "id": "E411F474-A530-4804-9D23-1D94C78B41E4",
                        "name": "Infantry and Militia",
                    },
                    {
                        "id": "6A3658B4-FB6E-4E23-A63A-9AEF11988831",
                        "name": "Battlefields",
                    },
                    {
                        "id": "A1BAF33E-EA84-4608-A888-4CEE9541F027",
                        "name": "Native American Heritage",
                    },
                    {
                        "id": "27BF8807-54EA-4A3D-B073-AA7AA361CD7E",
                        "name": "Wars and Conflicts",
                    },
                    {
                        "id": "A8E54356-20CD-490E-B34D-AC6A430E6F47",
                        "name": "Civil War",
                    },
                    {
                        "id": "0D00073E-18C3-46E5-8727-2F87B112DDC6",
                        "name": "Animals",
                    },
                    {
                        "id": "921D1471-5F6B-47D5-918D-389E7106083A",
                        "name": "Alligators or Crocodiles",
                    },
                    {"id": "957EF2BD-AC6C-4B7B-BD9A-87593ADC6691", "name": "Birds"},
                    {"id": "1608649A-E7D7-4529-BD83-074C90F9FB68", "name": "Fish"},
                    {
                        "id": "393F60FB-80D6-46F7-B0FB-BBF3C90F59FD",
                        "name": "Tortoises and Turtles",
                    },
                    {
                        "id": "5BE55D7F-BDB6-4E3D-AC35-2D8EBB974417",
                        "name": "Trails",
                    },
                    {
                        "id": "1365C347-952C-475A-B755-731DD523C195",
                        "name": "Wetlands",
                    },
                ],
                "states": "GA",
                "contacts": {
                    "phoneNumbers": [
                        {
                            "phoneNumber": "4787528257",
                            "description": "",
                            "extension": "222",
                            "type": "Voice",
                        },
                        {
                            "phoneNumber": "4787528259",
                            "description": "",
                            "extension": "",
                            "type": "Fax",
                        },
                    ],
                    "emailAddresses": [
                        {
                            "description": "",
                            "emailAddress": "ocmu_administration@nps.gov",
                        }
                    ],
                },
                "entranceFees": [
                    {
                        "cost": "0.00",
                        "description": "Admission is FREE. Except for special events sponsored by the Ocmulgee Mounds Association no fees are charged to enter and visit Ocmulgee Mounds National Historical Park. During the special events of the Ocmulgee Indian Celebration (third weekend in September) event fee is $6.00 for 13 &up, 6-12 $3.00, 5 &under are free and active military with I.D. $3.00. The spring Lantern light Tours (March) an event fee of $5.00 is charged for anyone 13 years and older.",
                        "title": "Ocmulgee Mounds National Historical Park Fees",
                    }
                ],
                "entrancePasses": [
                    {
                        "cost": "0.00",
                        "description": "We do not carry the Entrance Passes at the park.",
                        "title": "No Entrance Passes Available at Ocmulgee Mounds NHP",
                    }
                ],
                "fees": [],
                "directionsInfo": "Drive on I-75 to Macon. Exit I-75 onto I-16 east (exit on left) . Get off I-16 at exit 2 (Coliseum Drive), take a left under the highway and proceed to where Coliseum Dr. ends at Emery Highway. Turn right on Emery Highway and proceed to the third light. Our entrance is on the right side of the road.",
                "directionsUrl": "https://www.nps.gov/ocmu/planyourvisit/directions.htm",
                "operatingHours": [
                    {
                        "exceptions": [
                            {
                                "exceptionHours": {},
                                "startDate": "2022-01-01",
                                "name": "New Year's Day",
                                "endDate": "2022-01-01",
                            },
                            {
                                "exceptionHours": {},
                                "startDate": "2021-11-25",
                                "name": "Thanksgiving Day",
                                "endDate": "2021-11-25",
                            },
                            {
                                "exceptionHours": {},
                                "startDate": "2021-12-25",
                                "name": "Christmas Day",
                                "endDate": "2021-12-25",
                            },
                        ],
                        "description": "Ocmulgee Mounds National Historical Park   \n\nPark grounds and walking trails from 8:00 to 5:00 pm daily.\n\nThe Visitor Center and Earth Lodge are open from 9:00 am-5:00 pm daily.",
                        "standardHours": {
                            "wednesday": "8:00AM - 5:00PM",
                            "monday": "8:00AM - 5:00PM",
                            "thursday": "8:00AM - 5:00PM",
                            "sunday": "8:00AM - 5:00PM",
                            "tuesday": "8:00AM - 5:00PM",
                            "friday": "8:00AM - 5:00PM",
                            "saturday": "8:00AM - 5:00PM",
                        },
                        "name": "Ocmulgee Mounds National Historical Park & Visitor Center",
                    }
                ],
                "addresses": [
                    {
                        "postalCode": "31217",
                        "city": "Macon",
                        "stateCode": "GA",
                        "line1": "1207 Emery Hwy",
                        "type": "Physical",
                        "line3": "",
                        "line2": "",
                    },
                    {
                        "postalCode": "31217",
                        "city": "Macon",
                        "stateCode": "GA",
                        "line1": "1207 Emery Hwy",
                        "type": "Mailing",
                        "line3": "",
                        "line2": "",
                    },
                ],
                "images": [
                    {
                        "credit": "NPS",
                        "title": "Great Temple and Lesser Temple Mound",
                        "altText": "mounds",
                        "caption": "The Great Temple Mound is the largest mound at the park, it stands at 55 feet tall.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C797774-1DD8-B71B-0B2DA9E973C5AD89.jpg",
                    },
                    {
                        "credit": "NPS",
                        "title": "Earth Lodge",
                        "altText": "earth lodge",
                        "caption": "The Earth Lodge was used as a council chamber for the Mississippian Culture (900-1600)",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C79785B-1DD8-B71B-0B44360C5B1FA126.jpg",
                    },
                    {
                        "credit": "NPS",
                        "title": "Earth Lodge Floor",
                        "altText": "earth lodge floor",
                        "caption": "The earth Lodge floor is original it was carbon dated to 1015.",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C79797E-1DD8-B71B-0B467EFC07A0E785.jpg",
                    },
                    {
                        "credit": "NPS",
                        "title": "The Funeral Mound",
                        "altText": "funeral mound",
                        "caption": "The Funeral Mound was by prehistoric cultures to bury their dead. Today there are still remains instead the mound",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C797A83-1DD8-B71B-0B4E120BDF11316B.jpg",
                    },
                    {
                        "credit": "NPS",
                        "title": "Clovis Point",
                        "altText": "spear point",
                        "caption": "This Clovis point is the first spear found east of the Mississippi River. It was carbon dated to 10,000 BC",
                        "url": "https://www.nps.gov/common/uploads/structured_data/3C797C6B-1DD8-B71B-0B82D63B083D1850.jpg",
                    },
                ],
                "weatherInfo": "Macon has a humid subtropical climate (Köppen climate classification Cfa). The normal monthly mean temperature ranges from 46.3 °F (7.9 °C) in January to 81.8 °F (27.7 °C) in July. On average, there are 4.8 days with 100 °F (38 °C Winter's are mild. Temps ranging from 30 degrees to 50 degrees. Spring is mild but wet. Temps ranging from 50 degrees to low 70 degrees. Summers are hot and very humid. Temp ranging from upper 80 degrees to 100 degrees. Fall is pleasant. Temps ranging from 60 to 80 degrees.",
                "name": "Ocmulgee Mounds",
                "designation": "National Historical Park",
            },
            WEATHER: {
                "condition": "Clear",
                "temperature": 62.78,
                "precipitation": 0,
                "clouds": 4,
            },
            OUTPUT: {
                "id": "81AFEB37-7119-4BF1-B65B-806BAB973FFD",
                "name": "Ocmulgee Mounds National Historical Park",
                "description": "Welcome to Ocmulgee Mounds National Historical Park. This park is a prehistoric American Indian site, where many different American Indian cultures occupied this land for thousands of years. American Indians first came here during the Paleo-Indian Period hunting Ice Age mammals. Around 900 CE, the Mississippian Period began, and people constructed mounds for their elite, which remain here today.",
                "url": "https://www.nps.gov/ocmu/index.htm",
                "img": "https://www.nps.gov/common/uploads/structured_data/3C797774-1DD8-B71B-0B2DA9E973C5AD89.jpg",
                "weather": {
                    "condition": "Clear",
                    "temperature": 62.78,
                    "precipitation": 0,
                    "clouds": 4,
                },
            },
        }

        # pylint: enable=line-too-long

    @patch("national_parks.get_forecast_by_coordinates")
    def test_park_formatting(self, mock_weather):
        """
        case where the formatting was correct
        """
        test = self.success_test_params
        park_data = test[PARK_DATA]
        weather = test[WEATHER]
        expected = test[OUTPUT]
        mock_weather.return_value = weather
        actual = national_parks._park_from_data(park_data)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
