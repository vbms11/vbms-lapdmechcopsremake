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
        
        self.level = [[0 for x in xrange(self.levelSize[0] + self.outOfBoundsSize * 2)] for y in xrange(self.levelSize[1] + self.outOfBoundsSize * 2)]
        
        # set types
        for y in xrange(0, self.levelSize[1] + self.outOfBoundsSize * 2):
            for x in xrange(0, self.levelSize[0] + self.outOfBoundsSize * 2):
                
                if x % 2 == 0 and y % 2 == 0:
                    if x - 2 < self.outOfBoundsSize or x + 2 > outOfBoundsSize or y - 2 < self.outOfBoundsSize or y - 2 > outOfBoundsSize:
                        self.level[y][x] = BuildingTile((x, y, 0.5))
                    
                    else:
                        self.level[y][x] = RoadTile((x, y, 0.5))
                    self.level[y][x] = BuildingTile((x,y,0))
                else:
                    self.level[y][x] = RoadTile((x,y,0))
        
    def init (self):
        
        # initialize level tiles
        for y in xrange(0, self.levelSize[1] + self.outOfBoundsSize * 2):
            for x in xrange(0, self.levelSize[0] + self.outOfBoundsSize * 2):
                self.level[y][x].init()
        
    
    def paint (self):
        
        for y in xrange(0, self.levelSize[1] + self.outOfBoundsSize * 2):
            for x in xrange(0, self.levelSize[0] + self.outOfBoundsSize * 2):
                if self.level[y][x] != 0:
                    self.level[y][x].paint()
    
    def update (self):
        
        return
    
    def isRoad (self, x, y, outOfBounds = False):
        
        if outOfBounds:
            x = int(x)
            y = int(y)
            maxX = self.levelSize[0]
            maxY = self.levelSize[1]
        else:
            x = self.outOfBoundsSize + int(x)
            y = self.outOfBoundsSize + int(y)
            maxX = self.levelSize[0] + 2 * self.outOfBoundsSize
            maxY = self.levelSize[1] + 2 * self.outOfBoundsSize
        
        if x < 0 or x >= maxX or y < 0 or y >= maxY:
            return False
        
        return isinstance(self.level[y][x], RoadTile)
    
