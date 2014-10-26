'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from util.textureLoader import loadTexture
import config
from random import random, choice
from scene.sceneTile import SceneTile

class PathmentTile (SceneTile):
    '''
    classdocs
    '''
    
    position = None
    
    textures = None
    texture = None
    
    displayListId = None
    
    def __init__(self, sceneTile, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        self.textures = [
            loadTexture("textures/roadPathment.jpg")
        ]
        self.texture = self.textures[0]
        
        #self.texture = Road.textures[0]
    
    def init (self):
        
        pass
        
    def paint (self):
        
        if self.displayListId == None:
            self.displayListId = glGenLists(1);
            glNewList(self.displayListId, GL_COMPILE);
        
            glPushMatrix();
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTranslatef(self.position[0] + 0.5, self.position[1] + 0.5, self.position[2]);
            
            glBegin(GL_QUADS)
            
            glNormal3f(0,0,1)
            glTexCoord2f(0.0, 0.0) 
            glVertex3f(-0.5, -0.5, 0)
            glTexCoord2f(1.0, 0.0)
            glVertex3f(0.5, -0.5, 0)
            
            glTexCoord2f(1.0, 1.0)
            glVertex3f(0.5, 0.5, 0)
            glTexCoord2f(0.0, 1.0)
            glVertex3f(-0.5, 0.5, 0)
            
            glEnd()
            
            glPopMatrix()
            
            glEndList()
        
        glCallList(self.displayListId)
        
    
