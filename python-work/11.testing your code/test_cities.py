#test dor fucntion 'city_functions.py'
import unittest
from city_functions import city


class CityTestcase(unittest.TestCase):
    """Testing for names like Santiago, Chile"""
    def test_city_country(self):
        """oes a simple city and country pair work?"""
        city_func = city('santiago', 'chile')
        self.assertEqual(city_func, 'Santiago, Chile')
        
    def test_city_country_population(self):
        """Return a string like 'Santiago, Chile - population 5000000'."""
        city_func = city('santiago', 'chile', 3543)
        self.assertEqual(city_func, 'Santiago, Chile - population 3543')


if __name__ == '__main__':
    unittest.main()



