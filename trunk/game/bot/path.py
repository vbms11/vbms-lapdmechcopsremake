
class Path:
    
    pathNodes = None
    
    def __init__ (self, pathNodes):
        
        self.pathNodes = pathNodes
    
    def getNode (self, index):
        
        if len(self.pathNodes) > index:
            return self.pathNodes[index]
        
        return None
