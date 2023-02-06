# test_with_unittest.py

from src import main
import unittest


class Testing(unittest.TestCase):
    def test_geojson_file_type(self):
        geojson_file = "./data/restaurants_paris.geojson"
        self.assertEqual(type(main.load_data(geojson_file)), dict) 

if __name__ == '__main__':
    unittest.main()
