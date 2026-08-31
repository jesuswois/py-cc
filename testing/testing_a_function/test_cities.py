import unittest
from population import formatPlace

class TestCityFunctions(unittest.TestCase):
    
    def test_city_country(self):
        formattedPlace = formatPlace("puebla","méxico")
        self.assertEqual(formattedPlace,"Puebla, México.")

    def test_city_country_population(self):
        formattedPlace = formatPlace("Santiago","Chile",5000000)
        self.assertEqual(formattedPlace, "Santiago, Chile - population 5000000.")

unittest.main()