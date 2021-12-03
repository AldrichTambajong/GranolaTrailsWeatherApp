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

import open_weather

INPUT = "input"
EXPECTED = "expected"


class ParksTests(unittest.TestCase):
    """
    tests for the database actions
    """

    def setUp(self):
        # pylint: disable=line-too-long
        self.success_test_params = {
            INPUT: {
                "dt": 1638295200,
                "sunrise": 1638277812,
                "sunset": 1638315313,
                "moonrise": 1638262680,
                "moonset": 1638306300,
                "moon_phase": 0.86,
                "temp": {
                    "day": 68.18,
                    "min": 50.97,
                    "max": 72.52,
                    "night": 60.78,
                    "eve": 63.19,
                    "morn": 51.51,
                },
                "feels_like": {
                    "day": 66.4,
                    "night": 60.31,
                    "eve": 62.17,
                    "morn": 50.07,
                },
                "pressure": 1020,
                "humidity": 36,
                "dew_point": 39.78,
                "wind_speed": 10,
                "wind_deg": 177,
                "wind_gust": 16.75,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d",
                    }
                ],
                "clouds": 5,
                "pop": 0,
                "uvi": 4.04,
            },
            EXPECTED: {
                "condition": "Clear",
                "current": 68.18,
                "low": 50.97,
                "high": 72.52,
                "precipitation": 0,
                "clouds": 5,
            },
        }

        # pylint: enable=line-too-long

    def test_park_formatting(self):
        """
        case where the formatting was correct
        """
        test = self.success_test_params
        input_data = test[INPUT]
        expected = test[EXPECTED]
        actual = open_weather._format_weather_entry(input_data)

        print(actual)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
