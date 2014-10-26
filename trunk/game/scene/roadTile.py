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

class RoadTile (SceneTile):
    '''
    classdocs
    '''
    
    position = None
    
    straightTextures = None
    cornerTexture = None
    junction3Texture = None
    junction4Texture = None
    pathmentTexture = None
    texture = None
    rotation = None
    displayListId = None
    
    def __init__(self, sceneTile, position = (0,0,0)):
        '''
        Constructor
        '''
        self.position = position
        
        self.straightTextures = [
            loadTexture("textures/roadStraight1.jpg"),
            loadTexture("textures/roadStraight2.jpg"),
            loadTexture("textures/roadStraight3.jpg"),
            loadTexture("textures/roadStraight4.jpg")
        ]
        self.cornerTexture = loadTexture("textures/roadCorner.jpg")
        self.junction3Texture = loadTexture("textures/roadJunction3.jpg")
        self.junction4Texture = loadTexture("textures/roadJunction4.jpg")
        self.pathmentTexture = loadTexture("textures/roadPathment.jpg")
        
        #self.texture = Road.textures[0]
    
    def init (self):
        
        countNeighbors = 0
        neighbors = [False, False, False, False]
        
        if self.position[0] > 0 and config.game.level.isRoad(self.position[0] - 1, self.position[1], True):
            countNeighbors += 1
            neighbors[2] = True
        if self.position[0] < config.game.level.levelSize[0] - 1 and config.game.level.isRoad(self.position[0] + 1, self.position[1], True):
            countNeighbors += 1
            neighbors[0] = True
        if self.position[1] > 0 and config.game.level.isRoad(self.position[0], self.position[1] - 1, True):
            countNeighbors += 1
            neighbors[3] = True
        if self.position[1] < config.game.level.levelSize[1] - 1 and config.game.level.isRoad(self.position[0], self.position[1] + 1, True):
            countNeighbors += 1
            neighbors[1] = True
        
        if countNeighbors == 0:
            self.texture = choice(self.straightTextures)
            self.rotation = 0
        elif countNeighbors == 1:
            self.texture = choice(self.straightTextures)
            if neighbors[0] or neighbors[2]:
                self.rotation = 0;
            else:
                self.rotation = 90;
        elif countNeighbors == 2:
            self.texture = self.cornerTexture
            if neighbors[0] and neighbors[3]:
                self.texture = self.cornerTexture
                self.rotation = 0;
            elif neighbors[0] and neighbors[1]:
                self.texture = self.cornerTexture
                self.rotation = 90;
            elif neighbors[1] and neighbors[2]:
                self.texture = self.cornerTexture
                self.rotation = 180;
            elif neighbors[2] and neighbors[3]:
                self.texture = self.cornerTexture
                self.rotation = 270;
            elif neighbors[0] and neighbors[2]:
                self.texture = choice(self.straightTextures)
                self.rotation = choice([0, 180])
            elif neighbors[1] and neighbors[3]:
                self.texture = choice(self.straightTextures)
                self.rotation = choice([90, 270])
        elif countNeighbors == 3:
            self.texture = self.junction3Texture
            if neighbors[0] and neighbors[1] and neighbors[2]:
                self.rotation = 180
            elif neighbors[1] and neighbors[2] and neighbors[3]:
                self.rotation = 270
            elif neighbors[2] and neighbors[3] and neighbors[0]:
                self.rotation = 0
            elif neighbors[3] and neighbors[0] and neighbors[1]:
                self.rotation = 90
        elif countNeighbors == 4:
            self.texture = self.junction4Texture
            self.rotation = 0
        
    def paint (self):
        
        if self.displayListId == None:
            self.displayListId = glGenLists(1);
            glNewList(self.displayListId, GL_COMPILE);
        
            glPushMatrix();
            
            glBindTexture(GL_TEXTURE_2D, self.texture)
            glTranslatef(self.position[0] + 0.5, self.position[1] + 0.5, self.position[2]);
            glRotate(self.rotation, 0.0, 0.0, 1.0)
            
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
        
    
