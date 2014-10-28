'''
Created on Oct 16, 2014

@author: vbms
'''
from math import floor
from scene.sceneTile import SceneTile
from scene.buildingTile import BuildingTile
from scene.roadTile import RoadTile
from scene.baseTile import BaseTile
from scene.pathmentTile import PathmentTile
import config

class Level():
    '''
    classdocs
    '''
    level = None
    levelSize = None
    outOfBoundsSize = None
    levelFile = None
    bases = None
    
    def __init__(self, levelFile):
        '''
        Constructor
        '''
        self.levelFile = levelFile
        self.bases = []
    
    def init (self):
        
        print "initializing level"
        
        # load level
        self.loadLevelFile()
        
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
    
    def getLevelGridCoordinate (self, x, y, outOfBounds):
        
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
        
        return (x, y)
    
    def getTile (self, x, y, outOfBounds = False):
        
        coordinates = self.getLevelGridCoordinate(x, y, outOfBounds)
        
        if coordinates == False:
            return False
        
        return self.level[coordinates[1]][coordinates[0]]
    
    def isRoad (self, x, y, outOfBounds = False):
        
        coordinates = self.getLevelGridCoordinate(x, y, outOfBounds)
        
        if coordinates == False:
            return False
        
        return isinstance(self.level[coordinates[1]][coordinates[0]], RoadTile)
    
    def isDriveable (self, x, y, outOfBounds = False):
        
        coordinates = self.getLevelGridCoordinate(x, y, outOfBounds)
        
        if coordinates == False:
            return False
        
        return isinstance(self.level[coordinates[1]][coordinates[0]], RoadTile) or isinstance(self.level[coordinates[1]][coordinates[0]], PathmentTile)
    
    def loadLevelFile (self):
        
        # read the file
        f = open(self.levelFile)
        lines = f.read().splitlines()
        f.close()
        
        sizeY = len(lines)
        sizeX = len(lines[0])
        
        self.level = [[0 for x in xrange(sizeX)] for y in xrange(sizeY)]
        self.levelSize = [sizeX, sizeY]
        self.outOfBoundsSize = 0
        
        for y in xrange(0, sizeY):
            for x in xrange(0, sizeX):
                type = lines[y][x]
                if type == "#":
                    self.level[y][x] = BuildingTile(SceneTile, (x, y, 0))
                elif type == "X":
                    base = BaseTile(SceneTile, (x, y, 0))
                    self.bases.append(base)
                    self.level[y][x] = base
                elif type == "+":
                    self.level[y][x] = RoadTile(SceneTile, (x, y, 0))
                elif type == "-":
                    self.level[y][x] = PathmentTile(SceneTile, (x, y, 0))
        
    def getUnitsOnTile (self, x, y, outOfBounds = False):
        
        coordinates = self.getLevelGridCoordinate(x, y, outOfBounds)
        units = []
        
        for vehicle in config.game.vehicles:
            onX = False
            onY = False
            # unit x+
            if vehicle.position[0] > coordinates[0] and  vehicle.position[0] < coordinates[0] + 1:
                onX = True
            # unit y+
            if vehicle.position[1] > coordinates[1] and  vehicle.position[1] < coordinates[1] + 1:
                onY = True
            #TODO
            # unit x-
            if not onX and vehicle.position[0] < coordinates[0] and  vehicle.position[0] + vehicle.boundingBox[0] > coordinates[0]:
                onX = True
            # unit y-
            if not onY and vehicle.position[1] < coordinates[1] and  vehicle.position[1] + vehicle.boundingBox[1] > coordinates[1]:
                onY = True
            
            if onX and onY:
                units.append(vehicle)
        
        return units