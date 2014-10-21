'''
Created on Oct 18, 2014

@author: vbms
'''
from math import degrees, atan2, cos, sin, radians
from util.vector3d import Vec3

x = 0
y = 1

v = Vec3(1,0,0)

print "h: ",v.getHorizontalAngle()," v: ",v.getVerticalAngle()

amountX = x * 1
amountY = y * 1
newDirectionX = v.getHorizontalAngle() - amountX
newDirectionY = v.getVerticalAngle() - amountY

print "h: ", newDirectionX, " v: ", newDirectionY

x = cos(radians(newDirectionX))
y = sin(radians(newDirectionX))
z = cos(radians(newDirectionY))
verticalSin = sin(radians(newDirectionY))

v = Vec3(x * verticalSin, y * verticalSin, z)

print "h: ",v.getHorizontalAngle()," v: ",v.getVerticalAngle()


'''
amountX = 0
amountY = 1

v = Vec3(1,0,0)

print "h: ",v.getHorizontalAngle()," v: ",v.getVerticalAngle()

newDirectionX = v.getHorizontalAngle() - amountX
newDirectionY = v.getVerticalAngle() - amountY

print "h: ",newDirectionX," v: ",newDirectionY

x = cos(radians(newDirectionX))
y = sin(radians(newDirectionX))
z = cos(radians(newDirectionY))
verticalSin = sin(radians(newDirectionY))
v = Vec3(x * verticalSin, y * verticalSin, z)

print "h: ",v.getHorizontalAngle()," v: ",v.getVerticalAngle()

'''


'''
v = Vec3(0,0,-1)
print "x: ",v.getHorizontalAngle(), " y: ",degrees(v.getVerticalAngle())


travelDirection = Vec3(1,0.1,0)

angle = 5
print "angle: ", angle
vec = Vec3(cos(radians(angle)),sin(radians(angle)),0)
print "x: ", vec.x, " y: ", vec.y

newAngle = ((degrees(atan2(vec.y, vec.x)) + 360) % 360)
print "new: ", newAngle


'''
