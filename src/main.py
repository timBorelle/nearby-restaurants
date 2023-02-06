# coding: utf-8

import sys
import json
import haversine as hs
from haversine import Unit
from datetime import datetime
import logging

logging.basicConfig()
logger = logging.getLogger("execution-time")
logger.setLevel(logging.INFO)

#input_latitude = 0.0
#input_longitude = 0.0
#input_radius = 0.0

def main(argv):
    geojson_file = "./data/restaurants_paris.geojson"
    data = load_data(geojson_file)
    latitude = float(argv[0].split("=", 1)[1])
    longitude = float(argv[1].split("=", 1)[1])
    radius = float(argv[2].split("=", 1)[1])
    nearby_stations = query_search(data, latitude, longitude, radius)
    show_output(nearby_stations)

# load geojson data file 
def load_data(geojson_file):
    start_loading = datetime.now()
    with open(geojson_file) as data_file:    
        data = json.load(data_file)
        end_loading = datetime.now()
    logger.debug("{} ran in {} ms.".format(load_data.__name__, (end_loading - start_loading).total_seconds() * 1000))
    return data

# calculate distance between two point
def calculate_distance_between_two_points(loc1: tuple, loc2: tuple):
    return round(hs.haversine(loc1, loc2, unit=Unit.METERS), 2)

def query_search(data, latitude, longitude, radius):
    start_query_search = datetime.now()
    input_loc = (latitude, longitude)
    nearby_stations = []
    # iterate over each restaurant
    for r in data["features"]:
        point_data = r["geometry"]
        geometry_type = point_data["type"]
        if geometry_type == "Point":
            latitude = point_data["coordinates"][1]
            longitude = point_data["coordinates"][0]
            current_loc = (latitude, longitude)
            res_radius = calculate_distance_between_two_points(input_loc, current_loc)
            if res_radius <= radius:
                name = r["properties"]["name"]
                station_data = "name:" + name + ",longitude:" + str(longitude) + ",latitude:" + str(latitude) + ",distance:" + str(res_radius)
                # add station data to nearby_stations list
                nearby_stations.append(station_data)
    end_query_search = datetime.now()
    logger.debug("{} ran in {} ms.".format(query_search.__name__, (end_query_search - start_query_search).total_seconds() * 1000))
    return nearby_stations

    
def show_output(nearby_stations: list):
    if len(nearby_stations) != 0:
        for elem in nearby_stations:
            print(elem)

if __name__ == "__main__":
    argv = sys.argv[1:]
    main(argv)
