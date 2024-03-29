
import config
from pathFinderNode import PathFinderNode
from pathNode import PathNode
from path import Path

class PathFinder:
    
    startX = None
    startY = None
    endX = None
    endY = None
    
    scoreNodeMap = None
    scoreNodeMapSize = None
    
    def __init__ (self):
        
        pass
    
    def printScoreNodeMap (self):
        for y in xrange(self.scoreNodeMapSize[1]):
            line = ""
            for x in xrange(self.scoreNodeMapSize[0]):
                if self.scoreNodeMap[y][x] == None:
                    char = "-"
                else:
                    char = self.scoreNodeMap[y][x][0]
                line = line + str(char)
            print line
        print "-" * self.scoreNodeMapSize[0]
    
    def findPath (self, startX, startY, endX, endY):
        
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY
        
        level = config.game.level
        # self.scoreNodeMap = [score,node,reachedGoal]
        self.scoreNodeMap = [[None for x in xrange(level.levelSize[0])] for y in xrange(level.levelSize[1])]
        self.scoreNodeMapSize = level.levelSize
        
        currentNode = PathFinderNode(startX, startY)
        self.scoreNodeMap[startY][startX] = [0, currentNode, False]
        
        directionX, directionY, pDirectionX, pDirectionY = self.getDirections(currentNode)
        
        shortestPathLength = None
        if directionX == 0:
            shortestPathLength = pDirectionY
        elif directionY == 0:
            shortestPathLength = pDirectionX
        else:
            shortestPathLength = pDirectionY + pDirectionX - 1
        
        shorterPathPossible = True
        bestPath = None
        bestScore = None
        optionsExist = True
        currentScore = 0
        
        while shorterPathPossible and optionsExist:
            
            #currentScore = 0
            goalReached = False
            
            while optionsExist and not goalReached:
                
                self.printScoreNodeMap()
                if currentScore == 1:
                    pass
                currentScore += 1
                x, y, optionFound = self.getNextDirection(currentNode)
                
                if optionFound and ((self.scoreNodeMap[y][x] != None and self.scoreNodeMap[y][x][0] <= currentScore) or (bestScore != None and currentScore > bestScore)):
                    optionFound = False
                
                if optionFound:
                    # create the path node
                    lastNode = currentNode
                    currentNode.useOption(x, y)
                    # a node at that position already leads to the goal and we have a quicker path
                    if self.scoreNodeMap[y][x] != None and self.scoreNodeMap[y][x][2]:
                        # switch parent to the quicker path parent
                        linkNode = self.scoreNodeMap[y][x][1]
                        linkNode.parent = currentNode
                        self.scoreNodeMap[linkNode.y][linkNode.x] = [currentScore, linkNode, True]
                        currentNode = linkNode
                        # update all child nodes to quicker path parent
                        childNode = self.findChildNode(currentNode)
                        while childNode != None:
                            currentScore += 1
                            childNode.parent = currentNode
                            currentNode = childNode
                            childNode = self.findChildNode(currentNode)
                            self.scoreNodeMap[currentNode.y][currentNode.x][0] = currentScore
                    else:
                        currentNode = PathFinderNode(x, y, currentNode)
                        self.scoreNodeMap[y][x] = [currentScore, currentNode, False]
                    # is goal reached?
                    if x == endX and y == endY:
                        goalReached = True
                else:
                    # do any more options exist
                    print currentScore
                    print " x: ",currentNode.x, " y: ",currentNode.y
                    if currentNode.x == self.startX and currentNode.y == self.startY:
                        optionsExist = False
                        print "i think no more options exist"
                    else:
                        # go back
                        currentNode = currentNode.parent
                        currentScore -= 2
            
            if goalReached:
                print "goal reached score: ", currentScore
                # save path if it got the best score
                if bestScore == None or currentScore < bestScore:
                    bestScore = currentScore
                    bestPath = currentNode
                    self.scoreNodeMap[currentNode.y][currentNode.x] = [bestScore, bestPath, True]
                    if bestScore == shortestPathLength:
                        shorterPathPossible = False
                # save that the path reached the goal
                parentScore = currentScore - 1
                parentNode = currentNode.parent
                while parentNode != None:
                    # didnt reach goal before so save
                    if not self.scoreNodeMap[parentNode.y][parentNode.x][2]:
                        self.scoreNodeMap[parentNode.y][parentNode.x] = [parentScore, parentNode, True]
                    # select next parent node
                    parentScore -= 1 
                    parentNode = parentNode.parent
                # next path starts from parent node
                currentNode = lastNode
                currentScore -= 1
        
        # if a path was found return it
        path = None
        if bestPath != None:
            
            pathNodes = []
            currentNode = self.scoreNodeMap[endY][endX][1]
            while currentNode != None:
                pathNodes.append(PathNode(currentNode.x, currentNode.y))
                currentNode = currentNode.parent
            
            pathNodes.reverse()
            path = Path(pathNodes)
            
        return path
            
    
    def findChildNode (self, currentNode):
        
        if currentNode.x > 0 and self.scoreNodeMap[currentNode.y][currentNode.x - 1] != None and self.scoreNodeMap[currentNode.y][currentNode.x - 1][1] == currentNode:
            return self.scoreNodeMap[currentNode.y][currentNode.x - 1][1]
        if currentNode.x < self.scoreNodeMapSize[0] - 1 and self.scoreNodeMap[currentNode.y][currentNode.x + 1] != None and self.scoreNodeMap[currentNode.y][currentNode.x + 1][1] == currentNode:
            return self.scoreNodeMap[currentNode.y][currentNode.x + 1][1]
        if currentNode.y > 0 and self.scoreNodeMap[currentNode.y - 1][currentNode.x] != None and self.scoreNodeMap[currentNode.y - 1][currentNode.x][1] == currentNode:
            return self.scoreNodeMap[currentNode.y - 1][currentNode.x][1]
        if currentNode.y < self.scoreNodeMapSize[1] - 1 and self.scoreNodeMap[currentNode.y + 1][currentNode.x] != None and self.scoreNodeMap[currentNode.y + 1][currentNode.x][1] == currentNode:
            return self.scoreNodeMap[currentNode.y + 1][currentNode.x][1]
        
        return None
    
    def getNextDirection (self, currentNode):
        
        x = currentNode.x
        y = currentNode.y
        
        directionX, directionY, pDirectionX, pDirectionY = self.getDirections(currentNode)
        
        # always try the shortest distance if its an option
        if pDirectionX <= pDirectionY and directionX < 0 and currentNode.hasOption(x - 1, y):
            return (x - 1, y, True)
        
        if pDirectionX <= pDirectionY and directionX > 0 and currentNode.hasOption(x + 1, y):
            return (x + 1, y, True)
        
        if pDirectionX >= pDirectionY and directionY < 0 and currentNode.hasOption(x, y - 1):
            return (x, y - 1, True)
        
        if pDirectionX >= pDirectionY and directionY > 0 and currentNode.hasOption(x, y + 1):
            return (x, y + 1, True)
        
        # just try going in the right direction
        if directionX < 0 and currentNode.hasOption(x - 1, y):
            return (x - 1, y, True)
        
        if directionX > 0 and currentNode.hasOption(x + 1, y):
            return (x + 1, y, True)
        
        if directionY < 0 and currentNode.hasOption(x, y - 1):
            return (x, y - 1, True)
        
        if directionY > 0 and currentNode.hasOption(x, y + 1):
            return (x, y + 1, True)
        
        # try anything thats still possible
        if currentNode.hasOption(x - 1, y):
            return (x - 1, y, True)
        
        if currentNode.hasOption(x + 1, y):
            return (x + 1, y, True)
        
        if currentNode.hasOption(x, y - 1):
            return (x, y - 1, True)
        
        if currentNode.hasOption(x, y + 1):
            return (x, y + 1, True)
        
        
        return (x, y, False)
    
    # get direction to target from a node
    def getDirections (self, node):
        
        directionX = pDirectionX = self.endX - node.x
        directionY = pDirectionY = self.endY - node.y
        
        if directionX < 0:
            pDirectionX = -directionX
        if directionY < 0:
            pDirectionY = -directionY
        
        return (directionX, directionY, pDirectionX, pDirectionY)
    