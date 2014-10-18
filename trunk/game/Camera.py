'''
Created on Oct 16, 2014

@author: vbms
'''
from OpenGL.raw.GLU import gluLookAt
from Vector3d import Vec3
from math import sin, cos, radians

class Camera():
    '''
    classdocs
    '''
    
    position = None
    direction = None
    
    def __init__(self, position = [0,0,0], direction = Vec3(1,0,0)):
        '''
        Constructor
        '''
        self.position = position
        self.direction = direction
    
    def setPosition (self, x, y, z):
        
        self.position[0] = x
        self.position[1] = y
        self.position[2] = z
    
    def setDirection (self, direction):
        
        self.direction = direction
    
    def loadIdentity (self):
        
        gluLookAt(self.position[0], self.position[1], self.position[2], self.position[0] + self.direction.x, self.position[1] + self.direction.y, self.position[2] + self.direction.z, 0, 0, 1)
        #gluLookAt(self.position[0], self.position[1], self.position[2], 5, 5.1, 0, 0, 0, 1)
    
    def move (self, amount):
        
        self.position += amount
    
    def rotate (self, vertical, horizontal):
        
        x = cos(radians(horizontal))
        y = sin(radians(horizontal))
        z = sin(radians(vertical))
        verticalCos = cos(radians(vertical))
        self.direction += Vec3(x * verticalCos, y * verticalCos, z)
    
    def lookAt (self, position = (0,0,0)):
        
        self.direction = Vec3(*(position - self.position))
        self.direction.normalize()
    
