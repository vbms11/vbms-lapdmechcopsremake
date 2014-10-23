
class PathFinderNode:
    
    x = None
    y = None
    parent = None
    options = [[True for x in xrange(3)] for y in xrange(3)]
    
    def __init__ (self, x, y, parent = None):
        
        self.x = x
        self.y = y
        self.parent = parent
        
        # use all parent options
        while parent != None:
            self.useOption(parent.x, parent.y)
            parent = parent.parent
        
        # set options based on level
        if game.level.isRoad(x + 1, y + 0):
            self.options[x + 1][y + 0] = False
        if game.level.isRoad(x + 0, y + 1):
            self.options[x + 0][y + 1] = False
        if game.level.isRoad(x + 2, y + 1):
            self.options[x + 2][y + 1] = False
        if game.level.isRoad(x + 1, y + 2):
            self.options[x + 1][y + 2] = False
    
    def useOption (self, x, y):
        
        x = 1 + self.x - x
        y = 1 + self.y - y
        
        if x in range(0, 2) and y in range(0, 2):
            self.options[1 + self.x - x][1 + self.y - y] = False
    
    def hasOptions (self):
        
        return self.options[0][1] or self.options[1][0] or self.options[1][2] or self.options[2][1]
    
    def hasOption (self, x, y):
        
        return self.options[1 + self.x - x][1 + self.y - y]
        