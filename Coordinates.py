#Author: Diego Ramírez Barba
#Version: 1.0.0
#License: MIT

import random

#Create Data type
class Coordinates:
    def __init__(self, latitude, longitude) : #constructor
        self.latitude = latitude # 90N and 90S 0 -> Ecuador
        self.longitude = longitude # 180E and 180W 0 -> Greenwhich Meridian

#Generate random coordinates and parse to format "25.344 N, 63.5532 W"
def generate_random_longitude_latitude():
    latitude = ("{0:.4f}".format(random.uniform(0, 90))) + ' ' + random.choice('NS') + ', '
    longitude = ("{0:.4f}".format(random.uniform(0, 180))) + ' ' + random.choice('EW') + ', '
    data = Coordinates(latitude,longitude)
    return data

#Great circle distance
def great_circle_distance(data):
    print(data.latitude + data.longitude)

#generate the unit testing

coord = generate_random_longitude_latitude()
great_circle_distance(coord)
