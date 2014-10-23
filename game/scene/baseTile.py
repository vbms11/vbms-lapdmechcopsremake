'''
Created on Oct 16, 2014

@author: vbms
'''

from abc import ABCMeta, abstractmethod
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from reportlab.lib.pdfencrypt import padding
from util.vector3d import Vec3
from math import cos, sin, degrees, atan2, radians
from random import choice
from util.textureLoader import loadTexture
import config

class BuildingTile ():
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    textures = None
    texture = None
    position = None

    def __init__(self, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        if BuildingTile.textures == None:
            BuildingTile.textures = []
        #    BuildingTile.textures.append(loadTexture("NeHe.bmp"))
        
        #if self.texture == None:
        #    self.texture = choice(BuildingTile.textures)
    
    def init (self):
        pass
    def paint (self):
        
        glPushMatrix()
        
        glTranslate(*self.position)
        
        self.paintBox(0,0,0,1,1,1)
        
        glPopMatrix()
        