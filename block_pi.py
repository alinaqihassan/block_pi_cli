#!/usr/bin/python3
# nonvisual versions
import math, sys
if len(sys.argv) != 2:
    print('Invalid No. of arguments')
    print('You must give one argument')
    exit()

class Object:
    def __init__(self, mass, velocity, distance):
        self.mass = mass
        self.velocity = velocity
        self.distance = distance

a = Object(1, 0, 10)
b = Object(100**(int(sys.argv)-1), -10, 100)

line_vector = (math.sqrt(b.mass), math.sqrt(a.mass))
theta = math.atan(line_vector[1]/line_vector[0])

pi = int(180/theta)

print(pi)
