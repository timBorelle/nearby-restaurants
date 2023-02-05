# coding: utf-8

import sys

def main(argv):
    input_latitude = round(float(argv[0].split("=", 1)[1]), 2)
    input_longitude = round(float(argv[1].split("=", 1)[1]), 2)
    input_radius = round(float(argv[2].split("=", 1)[1]), 2)
    print("input_latitude: ", input_latitude)
    print("input_longitude: ", input_longitude)
    print("input_radius: ", input_radius)

if __name__ == "__main__":
    main(sys.argv[1:])

