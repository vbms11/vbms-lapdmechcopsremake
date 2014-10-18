'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from random import choice
from TextureLoader import loadTexture

class Building ():
    '''
    classdocs
    '''
    
    textures = None
    texture = None
    position = None

    def __init__(self, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        if Building.textures == None:
            Building.textures = []
            Building.textures.append(loadTexture("NeHe.bmp"))
        
        if self.texture == None:
            self.texture = choice(Building.textures)
    
    def paint (self):
        
        glPushMatrix();
        
        glTranslate(*self.position);
        
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
        
        glPopMatrix()
        