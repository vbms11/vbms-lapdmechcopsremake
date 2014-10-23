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

class BaseTile ():
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    textures = None
    texture = None
    position = None
    
    owner = None
    defaultColor = (1.0, 1.0, 1.0)
    
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
        
        color = self.defaultColor
        if self.owner == None:
            color = self.owner.color
        
        self.paintBounds(-1 + 0.01, -1 + 0.01, -1 + 0.01, 3 + 0.02, 3 + 0.02, 0.02, *color)
        
        glPopMatrix()
    
    def paintBounds (self, posX, posY, posZ, sizeX, sizeY, sizeZ, colorR, colorG, colorB):
        
        glPushMatrix()
        glDissable(GL_TEXTURE_2D)
        
        glBegin(GL_QUAD_STRIP)
        
        glColor4f(colorR, colorG, colorB, 1.0)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(0.0, 0.0, 0.0)
        
        glColor4f(colorR, colorG, colorB, 0.0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(0.0, 0.0, sizeZ)
        
        glColor4f(colorR, colorG, colorB, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(sizeX, 0.0, 0.0)
        
        glColor4f(colorR, colorG, colorB, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(sizeX, 0.0, sizeZ)
        
        glColor4f(colorR, colorG, colorB, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(sizeX, sizeY, 0.0)
        
        glColor4f(colorR, colorG, colorB, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(sizeX, sizeY, sizeZ)
        
        glColor4f(colorR, colorG, colorB, 1.0)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(0.0, sizeY, 0.0)
        
        glColor4f(colorR, colorG, colorB, 0.0)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0.0, sizeY, sizeZ)
        
        glEnd()
        
        glEnable(GL_TEXTURE_2D)
        glPopMatrix()
        