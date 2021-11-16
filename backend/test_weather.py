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
                "dt": 1636995600,
                "sunrise": 1636978203,
                "sunset": 1637015629,
                "moonrise": 1637009520,
                "moonset": 1636965360,
                "moon_phase": 0.39,
                "temp": {
                    "day": 54.91,
                    "min": 43.93,
                    "max": 58.41,
                    "night": 47.19,
                    "eve": 50.4,
                    "morn": 44.6,
                },
                "feels_like": {
                    "day": 51.51,
                    "night": 46.49,
                    "eve": 47.59,
                    "morn": 39.97,
                },
                "pressure": 1024,
                "humidity": 30,
                "dew_point": 24.06,
                "wind_speed": 9.48,
                "wind_deg": 304,
                "wind_gust": 23.89,
                "weather": [
                    {
                        "id": 800,
                        "main": "Clear",
                        "description": "clear sky",
                        "icon": "01d",
                    }
                ],
                "clouds": 3,
                "pop": 0.5,
                "uvi": 3.26,
            },
            EXPECTED: {
                "condition": "Clear",
                "temperature": 54.91,
                "precipitation": 50,
                "clouds": 3,
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

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
