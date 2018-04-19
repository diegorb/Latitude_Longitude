#Author: Diego Ramírez Barba
#Version: 1.0.0
#License: MIT

import random
from math import radians, sqrt, asin, sin, cos

#Create Data type
class Coordinates:
    def __init__(self, latitude, longitude) : #constructor
        self.latitude = latitude # 90N and 90S 0 -> Ecuador
        self.longitude = longitude # 180E and 180W 0 -> Greenwhich Meridian

#Generate random coordinates
def generate_random_longitude_latitude():
    latitude = ("{0:.4f}".format(random.uniform(0, 90))) + ' ' + random.choice('NS')
    longitude = ' ' + ("{0:.4f}".format(random.uniform(0, 180))) + ' ' + random.choice('EW')
    data = Coordinates(latitude,longitude)
    return data

#Generate a method that parse the coordinates to format "25.344 N, 63.5532 W,"
def parse_coordinates(data):
    data.latitude = data.latitude + ','
    data.longitude = data.longitude + ', '
    return data

#Great circle distance 
#This method converts the data to DMS (Ddec) and the DMS to Radians and returns the distance between A and B
# Haversine formula 2r *arcsin(sqrt(sin^2(diflat/2) + cos(lat1) * cos(lat2) * sin^2(diflong/2)))
def great_circle_distance(pointA, pointB):
    print("Two points")
    

#generate the unit testing

pointA = generate_random_longitude_latitude()
pointB = generate_random_longitude_latitude()
great_circle_distance(pointA,pointB)
