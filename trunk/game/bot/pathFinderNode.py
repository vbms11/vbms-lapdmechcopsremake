
import config

class PathFinderNode:
    
    x = None
    y = None
    parent = None
    options = [[False for x in xrange(3)] for y in xrange(3)]
    
    def __init__ (self, x, y, parent = None):
        
        self.x = x
        self.y = y
        self.parent = parent
        
        # set options based on level
        if config.game.level.isDriveable(x - 1, y):
            self.options[0][1] = True
        if config.game.level.isDriveable(x, y - 1):
            self.options[1][0] = True
        if config.game.level.isDriveable(x + 1, y):
            self.options[2][1] = True
        if config.game.level.isDriveable(x, y + 1):
            self.options[1][2] = True
        
        # use all parent options
        while parent != None:
            self.useOption(parent.x, parent.y)
            parent = parent.parent
    
    def useOption (self, x, y):
        
        x = 1 + x - self.x
        y = 1 + y - self.y
        
        if x in range(0, 3) and y in range(0, 3):
            self.options[x][y] = False
    
    def hasOptions (self):
        
        return self.options[0][1] or self.options[1][0] or self.options[1][2] or self.options[2][1]
    
    def hasOption (self, x, y):
        
        nx = 1 + x - self.x
        ny = 1 + y - self.y
        return self.options[nx][ny]
        