'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from random import choice
from util.textureLoader import loadTexture

class BuildingTile ():
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
        
        if BuildingTile.textures == None:
            BuildingTile.textures = []
        #    BuildingTile.textures.append(loadTexture("NeHe.bmp"))
        
        #if self.texture == None:
        #    self.texture = choice(BuildingTile.textures)
    
    def init (self):
        pass
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
        