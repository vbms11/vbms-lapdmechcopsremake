'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from random import choice
from util.textureLoader import loadTexture
from scene.sceneTile import SceneTile

class BuildingTile (SceneTile):
    '''
    classdocs
    '''
    
    textures = None
    texture = None
    position = None
    displayListId = None

    def __init__(self, sceneTile, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        if BuildingTile.textures == None:
            BuildingTile.textures = []
            BuildingTile.textures.append(loadTexture("textures/building1.jpg"))
            BuildingTile.textures.append(loadTexture("textures/building2.jpg"))
            BuildingTile.textures.append(loadTexture("textures/building3.jpg"))
        
        self.texture = choice(BuildingTile.textures)
    
    def init (self):
        pass
    def paint (self):
        
        if self.displayListId == None:
            self.displayListId = glGenLists(1);
            glNewList(self.displayListId, GL_COMPILE);
            
            glBindTexture(GL_TEXTURE_2D, self.texture)
            
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
            
            glEndList()
        
        glCallList(self.displayListId)
        