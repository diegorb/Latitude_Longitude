#Author: Diego Ramírez Barba
#Version: 1.0.0
#License: MIT

import random
from math import radians, sqrt, asin, sin, cos, atan2

#Create Data type
class Coordinates:
    def __init__(self, latitude, longitude) : #constructor
        self.latitude = latitude # 90N and 90S 0 -> Ecuador
        self.longitude = longitude # 180E and 180W 0 -> Greenwhich Meridian

#Generate random coordinates
def generate_random_longitude_latitude():
    latitude = ("{0:.4f}".format(random.uniform(-90, 90)))
    longitude = ("{0:.4f}".format(random.uniform(-180, 180)))
    data = Coordinates(float(latitude),float(longitude))
    return data

#Generate a method that parse the coordinates to format "25.344 N, 63.5532 W,"
def parse_coordinates(data):

      #if(x1.find('N')):
     #   x1 = x1.replace("N", "")
      #  x1 = float(x1)
    #else:
     #   x1 = x1.replace("S", "")
      #  x1 = float(x1)

    data.latitude = data.latitude + random.choice('NS') + ', '
    data.longitude = data.longitude + random.choice('EW') + ', '
    return data

#Great circle distance 
#This method converts the data to DMS (Ddec) and the DMS to Radians and returns the distance between A and B
# Haversine formula 2r *arcsin(sqrt(sin^2(diflat/2) + cos(lat1) * cos(lat2) * sin^2(diflong/2)))
def great_circle_distance(pointA, pointB):
    R = 6371 # radius of earth
    x1 = pointA.latitude
    y1 = pointA.longitude
    x2 = pointB.latitude
    y2 = pointB.longitude

    print(str(x1) + ' ' + str(y1))
    print(str(x2) + ' ' + str(y2))

    y1, x1, y2, x2 = map(radians, [y1, x1, y2, x2])

    dif_lat = x2 - x1
    dif_lon = y2 - y1

    x = sin(dif_lat/2)**2 + cos(x1) * cos(x2) * sin(dif_lon/2)**2
    y = asin(sqrt(x)) 
    haversine = 2 * R * y

    print(str("{0:.4f}".format(haversine) + ' Km'))
    return haversine

#generate the unit testing

pointA = generate_random_longitude_latitude()
pointB = generate_random_longitude_latitude()
great_circle_distance(pointA,pointB)
