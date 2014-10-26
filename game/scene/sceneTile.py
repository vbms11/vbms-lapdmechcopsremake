'''
Created on Oct 19, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from random import choice
from util.textureLoader import loadTexture
from abc import ABCMeta

class SceneTile:
    '''
    classdocs
    '''
    __metaclass__ = ABCMeta
    
    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def paintBox (self, posX, posY, posZ, sizeX, sizeY, sizeZ):
        
        glBegin(GL_QUADS)
        
        glNormal3f(0, 0, 1)
        glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(0, 1.0, 1.0)
        
        glNormal3f(0, 0, -1)
        glTexCoord2f(1.0, 0.0); glVertex3f(0, 0, 0)
        glTexCoord2f(1.0, 1.0); glVertex3f(0, 1.0, 0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 0, 0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, 0, 0)
        
        glNormal3f(0, 1, 0)
        glTexCoord2f(0.0, 1.0); glVertex3f(0, 1.0, 0)
        glTexCoord2f(0.0, 0.0); glVertex3f(0, 1.0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 0)
        
        glNormal3f(0, -1, 0)
        glTexCoord2f(1.0, 1.0); glVertex3f(0, 0, 0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 0, 0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, 0, 1.0)
        glTexCoord2f(1.0, 0.0); glVertex3f(0, 0, 1.0)
        
        glNormal3f(1, 0, 0)
        glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 0, 0)
        glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 0)
        glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
        glTexCoord2f(0.0, 0.0); glVertex3f(1.0, 0, 1.0)
        
        glNormal3f(-1, 0, 0)
        glTexCoord2f(0.0, 0.0); glVertex3f(0, 0, 0)
        glTexCoord2f(1.0, 0.0); glVertex3f(0, 0, 1.0)
        glTexCoord2f(1.0, 1.0); glVertex3f(0, 1.0, 1.0)
        glTexCoord2f(0.0, 1.0); glVertex3f(0, 1.0, 0)
        
        glEnd()