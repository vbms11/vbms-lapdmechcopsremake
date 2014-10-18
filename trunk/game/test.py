'''
Created on Oct 18, 2014

@author: vbms
'''
from math import degrees, atan2, cos, sin, radians
from Vector3d import Vec3


travelDirection = Vec3(1,0.1,0)

angle = 5
print "angle: ", angle
vec = Vec3(cos(radians(angle)),sin(radians(angle)),0)
print "x: ", vec.x, " y: ", vec.y

newAngle = ((degrees(atan2(vec.y, vec.x)) + 360) % 360)
print "new: ", newAngle



