#Author: Diego Ramírez Barba
#Version: 1.0.0
#License: MIT
#Great Circle Distance https://www.movable-type.co.uk/scripts/latlong.html

import unittest
import Coordinates

class Test_Coordinates(unittest.TestCase):

    def test_generate_random_longitude_latitude(self):
        Seed = Coordinates.generate_random_longitude_latitude()
        self.assertTrue(-90 <= Seed.latitude <= 90)
        self.assertFalse(91 <= Seed.latitude <= 180)
        self.assertFalse(-180 <= Seed.latitude <= -91)
        self.assertTrue(-180 <= Seed.longitude <= 180)

    def test_parse_coordinates(self):
        Location = Coordinates.Location(-13.44,120.01)
        result = Coordinates.parse_coordinates(Location)
        self.assertEqual(result.latitude,'13.44 S,')
        self.assertEqual(result.longitude,'120.01 E,')
        Location_one = Coordinates.Location(13.44,-120.01)
        result = Coordinates.parse_coordinates(Location_one)
        self.assertEqual(result.latitude,'13.44 N,')
        self.assertEqual(result.longitude,'120.01 W,')

    def test_great_circle_distance(self):
        LocationA = Coordinates.Location(-13.44,120.01)
        LocationB = Coordinates.Location(13.44,-120.01)
        result = Coordinates.great_circle_distance(LocationA,LocationB)
        #print(str(result))
        self.assertTrue( 13530 <= result <= 13550) # 13540 
        LocationA = Coordinates.Location(-73.44,100.01)
        LocationB = Coordinates.Location(-13.44,20.01)
        result = Coordinates.great_circle_distance(LocationA,LocationB)
        #print(str(result))
        self.assertTrue( 8250 <= result <= 8270) # 8260
    


if __name__ == '__main__':
    unittest.main()