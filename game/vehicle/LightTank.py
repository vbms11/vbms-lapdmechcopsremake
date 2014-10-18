'''
Created on Oct 17, 2014

@author: vbms
'''
from OpenGL.GL import *
from OpenGL.GLUT import *
from VehicleType import VehicleType
from math import atan2, degrees

class LightTank (VehicleType):
    '''
    classdocs
    '''

    def __init__(self, vehicleType):
        '''
        Constructor
        '''
        self.speed = 0.2
        self.rotateSpeed = 40
    
    def init (self, position):
        
        self.position = position
        self.boundingBox = (0.2,0.2,0.2)
        
    def paint (self):
        
        glPushMatrix();
        
        glTranslate(*self.position);
        
        self.paintBoundingBox()
        
        # paint tracks
        glPushMatrix()
        glTranslate(self.boundingBox[0] / 2, self.boundingBox[1] / 2, 0);
        glRotatef(((degrees(atan2(self.travelDirection.y, self.travelDirection.x)) + 360) % 360), 0, 0, 1);
        glTranslate(-self.boundingBox[0] / 2, -self.boundingBox[1] / 2, 0);
        self.paintBox(5 * 0.02, 8.5 * 0.02, 1.5 * 0.02, 10 * 0.02, 3 * 0.02, 3 * 0.02);
        self.paintBox(5 * 0.02, 1.5 * 0.02, 1.5 * 0.02, 10 * 0.02, 3 * 0.02, 3 * 0.02);
        self.paintBox(5 * 0.02, 5 * 0.02, 2.5 * 0.02, 4 * 0.02, 4 * 0.02, 3 * 0.02);
        glPopMatrix()
        
        # paint turret
        self.paintBox(5 * 0.02, 5 * 0.02, 5.5 * 0.02, 6 * 0.02, 6 * 0.02, 3 * 0.02);
        #self.paintCylinder(9, 5, 2.5, 2, 0.5, 0.2);, 0.02
        
        glPopMatrix()
        
    def update (self):
        pass
    