'''
Created on Oct 16, 2014

@author: vbms
'''
from OpenGL.raw.GLU import gluLookAt
from Vector3d import Vec3
from math import sin, cos

class Camera():
    '''
    classdocs
    '''
    
    position = None
    direction = None
    
    def __init__(self, position = (0,0,0), direction = Vec3(1,0,0)):
        '''
        Constructor
        '''
        self.position = position
        self.direction = direction
        
    def loadIdentity (self):
        
        gluLookAt(*self.position, self.direction.x, self.direction.y, self.direction.z, 0, 0, 1)
    
    def move (self, amount):
        
        self.position += amount
    
    def rotate (self, vertical, horizontal):
        
        x = sin(horizontal)
        y = cos(horizontal)
        z = sin(vertical)
        verticalCos = cos(vertical)
        self.direction += Vec3(x * verticalCos, y * verticalCos, z)
    
    def lookAt (self, position = (0,0,0)):
        
        self.direction = Vec3(*(position - self.position))
        self.direction.normalize()
    
