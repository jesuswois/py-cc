import unittest
from city_functions import formatPlace

class TestCityFunctions(unittest.TestCase):
    
    def test_city_country(self):
        formattedPlace = formatPlace("puebla","méxico")
        self.assertEqual(formattedPlace,"Puebla, México.")

unittest.main()