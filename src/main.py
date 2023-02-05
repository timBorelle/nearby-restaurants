# coding: utf-8

import sys
#import pandas as pd
import json
import haversine as hs
from haversine import Unit
from datetime import datetime

def main(argv):
    input_latitude = float(argv[0].split("=", 1)[1])
    input_longitude = float(argv[1].split("=", 1)[1])
    input_radius = float(argv[2].split("=", 1)[1])
    geojson_file = "./data/restaurants_paris.geojson"
    read_geojson(input_latitude, input_longitude, input_radius, geojson_file)

def read_geojson(input_latitude, input_longitude, input_radius, geojson_file):
    print("read .geojson file ...")
    input_loc = (input_latitude, input_longitude)
    nearby_stations = []
    start_loading = datetime.now()
    with open(geojson_file) as data_file:    
        data = json.load(data_file)
        end_loading = datetime.now()
    print(f"Loading execution time : {(end_loading - start_loading).total_seconds() * 1000} ms.")
    point_data = data["features"][0]["geometry"]
    geometry_type = point_data["type"]
    if geometry_type == "Point":
        latitude = point_data["coordinates"][1]
        longitude = point_data["coordinates"][0]
        current_loc = (latitude, longitude)
        res_radius = calculate_distance_between_two_points(input_loc, current_loc)
        print("res_radius : ", res_radius)
        if res_radius <= input_radius:
            name = data["features"][0]["properties"]["name"]
            station_data = "name:" + name + ",longitude:" + str(longitude) + ",latitude:" + str(latitude) + ",distance:" + str(res_radius)
            nearby_stations.append(station_data)

def calculate_distance_between_two_points(loc1: tuple, loc2: tuple):
    return round(hs.haversine(loc1, loc2, unit=Unit.METERS), 2)

if __name__ == "__main__":
    main(sys.argv[1:])
