# test_with_pytest.py

from src import main
import pytest

latitude = 48.8319929 
longitude = 2.3245488
location = (latitude, longitude)

def test_always_passes():
    assert True

def test_loading_with_no_empty_data():
    geojson_file = "./data/restaurants_paris.geojson"
    assert len(main.load_data(geojson_file)) > 0

def test_calculate_distance_between_two_points():
    location1 = location
    location2 = location
    assert main.calculate_distance_between_two_points(location1, location2) == 0.0

def test_query_search_with_one_result():
    data = {
        "features": [
            {
                "properties": {
                    "name": "Le Severo"
                },
                "geometry": { 
		            "type": "Point", 
		            "coordinates": [ 2.3245488, 48.8319929 ] 
	            } 
            },
            {
                "properties": {
                    "name": "Chez Jenny"
                },
                "geometry": { 
		            "type": "Point", 
		            "coordinates": [ 2.3646613, 48.8660027 ] 
	            } 
            },
        ]
    }
    latitude = 48.8319929
    longitude = 2.3245488
    radius = 0.0
    assert len(main.query_search(data, latitude, longitude, radius)) == 1
