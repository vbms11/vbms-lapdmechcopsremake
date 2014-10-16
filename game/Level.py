'''
Created on Oct 16, 2014

@author: vbms
'''
from Building import Building
from Road import Road

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
        
        for y in xrange(0, self.levelSize[1]):
            for x in xrange(0, self.levelSize[0]):
                
                if x % 2 == 0 and y % 2 == 0:
                    self.level[y][x] = Building((x,y,0))
                else:
                    self.level[y][x] = Road((x,y,0))
        
    
    def init (self):
        
        return
    
    def paint (self):
        
        for y in xrange(0, self.levelSize[1]):
            for x in xrange(0, self.levelSize[0]):
                
                if self.level[y][x] != 0:
                    self.level[y][x].paint()
    
    def update (self):
        
        return
    
