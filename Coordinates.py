#Author: Diego Ramírez Barba
#Version: 1.0.0
#License: MIT

import random
from math import radians, sqrt, asin, sin, cos

#Create Data type
class Location:
    def __init__(self, latitude, longitude) : #constructor
        self.latitude = latitude # 90N and 90S 0 -> Ecuador
        self.longitude = longitude # 180E and 180W 0 -> Greenwhich Meridian

#Generate random coordinates
def generate_random_longitude_latitude():
    latitude = ("{0:.4f}".format(random.uniform(-90, 90)))
    longitude = ("{0:.4f}".format(random.uniform(-180, 180)))
    data = Location(float(latitude),float(longitude))
    return data

#Generate a method that parse the coordinates to format "25.344 N, 63.5532 W,"
def parse_coordinates(data):
    
    if(data.latitude < 0):
        data.latitude = str(abs(data.latitude)) + ' S,'
    else:
        data.latitude = str(data.latitude) + ' N,'
    if(data.longitude < 0):
        data.longitude = str(abs(data.longitude)) + ' W,'
    else:
        data.longitude = str(data.longitude) + ' E,'
    
    print(data.latitude + ' ' + data.longitude)

    return data

#Great circle distance 
#This method converts the data to DMS (Ddec) and the DMS to Radians and returns the distance between A and B
#Haversine formula 2r *arcsin(sqrt(sin^2(diflat/2) + cos(lat1) * cos(lat2) * sin^2(diflong/2)))
def great_circle_distance(pointA, pointB):
    R = 6371 # radius of earth in Km
    x1 = pointA.latitude
    y1 = pointA.longitude
    x2 = pointB.latitude
    y2 = pointB.longitude

    parse_coordinates(pointA)
    parse_coordinates(pointB)

    y1, x1, y2, x2 = map(radians, [y1, x1, y2, x2])

    dif_lat = x2 - x1
    dif_lon = y2 - y1

    x = sin(dif_lat/2)**2 + cos(x1) * cos(x2) * sin(dif_lon/2)**2 
    y = sqrt(x)
    if(y > 1):
        print("Error in the limits of the haversine formula") # The long haversine formula is needed
        return -1
    else:
        z = asin(sqrt(x)) 
        haversine = 2 * R * z

    print(str(round(haversine,4)) + ' Km')

    return haversine

pointA = generate_random_longitude_latitude()
pointB = generate_random_longitude_latitude()
great_circle_distance(pointA,pointB)
