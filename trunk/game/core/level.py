'''
Created on Oct 16, 2014

@author: vbms
'''
from scene.buildingTile import BuildingTile
from scene.roadTile import RoadTile
from math import floor

class Level():
    '''
    classdocs
    '''
    level = None
    levelSize = None
    outOfBoundsSize = None

    def __init__(self, levelSize = (10,10), outOfBoundsSize = 10):
        '''
        Constructor
        '''
        self.levelSize = levelSize
        self.outOfBoundsSize = outOfBoundsSize
        
        print "initializing level"
        
        self.level = [[0 for x in xrange(self.levelSize[0])] for y in xrange(self.levelSize[1])]
        
        # set types
        for y in xrange(0, self.levelSize[1]):
            for x in xrange(0, self.levelSize[0]):
                
                if x % 2 == 0 and y % 2 == 0:
                    self.level[y][x] = BuildingTile((x,y,0))
                else:
                    self.level[y][x] = RoadTile((x,y,0))
        
    def init (self):
        
        # initialize level tiles
        for y in xrange(0, self.levelSize[1]):
            for x in xrange(0, self.levelSize[0]):
                self.level[y][x].init()
        
    
    def paint (self):
        
        for y in xrange(0, self.levelSize[1]):
            for x in xrange(0, self.levelSize[0]):
                
                if self.level[y][x] != 0:
                    self.level[y][x].paint()
    
    def update (self):
        
        return
    
    def isRoad (self, x, y):
        
        x = int(x)
        y = int(y)
        
        if x < 0 or x >= self.levelSize[0] or y < 0 or y >= self.levelSize[1]:
            return False
        
        return isinstance(self.level[y][x], RoadTile)
    
