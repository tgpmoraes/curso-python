# Write the class Point as outlined in the instructions
import numpy as np


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return np.sqrt(pow(self.x, 2) + pow(self.y, 2))

    def reflect(self, axis):
        if (axis == 'x'):
            self.y = -1.0 * self.y
        elif (axis == 'y'):
            self.x = -1.0 * self.x
        else:
            print('axis should be only \'x\' or \'y\'')


pt = Point(x=3.0)
pt.reflect("y")
print((pt.x, pt.y))
pt.y = 4.0
print(pt.distance_to_origin())
