'''
Created on Oct 16, 2014

@author: vbms
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from TextureLoader import loadTexture

class Road ():
    '''
    classdocs
    '''
    
    texture = None
    textures = None
    position = None
    
    def __init__(self, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        if Road.textures == None:
            Road.textures = []
            #Road.textures.append(loadTexture("floor.bmp"))
        
        #self.texture = Road.textures[0]
    
    def paint (self):
        
        glPushMatrix();
        
        glTranslate(*self.position);
        
        glBegin(GL_QUADS)
        
        glTexCoord2f(1.0, 1.0) 
        glVertex3f(0, 0, 0)
        
        glTexCoord2f(0.0, 1.0)
        glVertex3f(1.0, 0, 0)
        
        glTexCoord2f(0.0, 0.0)
        glVertex3f(1.0, 1.0, 0)
        
        glTexCoord2f(1.0, 0.0)
        glVertex3f(0, 1.0, 0)
        
        glEnd()
        
        glPopMatrix()
    
