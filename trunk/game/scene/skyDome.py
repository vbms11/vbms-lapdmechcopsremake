'''
Created on Oct 18, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from util.textureLoader import loadSphereTexture, destroyTexture

import config
from math import sqrt

class SkyDome:
    '''
    classdocs
    '''
    
    texture = None
    displayListId = None
    radius = None
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def init (self, filename):
        
        self.texture = loadSphereTexture(filename)
        levelSize = config.game.level.levelSize[0] / 2 + config.game.level.outOfBoundsSize
        self.radius = sqrt(levelSize * levelSize + levelSize * levelSize) + 2
    
    def destroy (self):
        
        destroyTexture(self.texture)
        glDeleteLists(self.displayListId)
    
    def update (self):
        pass
        
    def paint (self):
        
        if self.displayListId == None:
            self.displayListId = glGenLists(1);
            quadratic = gluNewQuadric() 
            gluQuadricTexture(quadratic, GL_TRUE)
            glTexGeni(GL_S, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
            glTexGeni(GL_T, GL_TEXTURE_GEN_MODE, GL_SPHERE_MAP)
            glNewList(self.displayListId, GL_COMPILE);
            
            glDisable(GL_LIGHTING)
            glPushMatrix()
            glTranslatef(config.game.level.levelSize[0] / 2, config.game.level.levelSize[1] / 2, 0);
            glBindTexture(GL_TEXTURE_2D, self.texture)
            gluSphere(quadratic, self.radius, 32, 32)
            glPopMatrix()
            glEnable(GL_LIGHTING)
            
            glEndList()
            gluDeleteQuadric(quadratic)
        
        glCallList(self.displayListId)
    