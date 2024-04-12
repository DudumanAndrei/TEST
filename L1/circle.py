import math

class Circle():
    '''
    Class representing a circle and calculate the area of circle
    '''
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * (self.radius ** 2)