
from Math import floor
from Random import choise
import config
from bot.pathFinder import PathFinder
from util.vector3d import Vec3

class BotBase:
    
    vehicle = None
    
    def update (self):
        pass
    
    def getPath (self, startX, startY, endX, endY):
        
        startX = floor(startX)
        startY = floor(startY)
        
        return PathFinder().findPath(startX, startY, endX, endY)
    
    def getUnitsOnTile (self, tileX, tileY):
        
        return config.game.level.getUnitsOnTile(tileX, tileY)
    
    def getUnitsInDirection (self, pointX, pointY, dirX, dirY):
        
        units = []
        
        pointX = floor(pointX)
        pointY = floor(pointY)
        
        tile = config.game.level.isDriveable(pointX, pointY)
        
        # along the x axis
        if dirX != 0:
            amount = pointX
            while config.game.level.isDriveable(pointX, pointY):
                units.append(config.game.level.getUnitsOnTile(pointX, pointY))
                pointX += dirX
        # along the y axis
        elif pointY != 0:
            amount = pointY
            while config.game.level.isDriveable(pointX, pointY):
                units.append(config.game.level.getUnitsOnTile(pointX, pointY))
                pointY += dirY
        
        return units
    
    def getUnitsInSight (self, position, viewDirection):
        
        units = []
        angle = viewDirection.getHorizontalAngle()
        
        if angle < 22.5 or angle > 337.5:
            units = self.getUnitsInDirection (position[0], position[1], 1, 0)
        elif angle < 67.5 or angle > 22.5:
            units = self.getUnitsInDirection(position[0], position[1], 1, 0) + self.getUnitsInDirection(position[0], position[1], 0, 1)
        elif angle < 112.5 or angle > 67.5:
            units = self.getUnitsInDirection (position[0], position[1], 0, 1)
        elif angle < 157.5 or angle > 112.5:
            units = self.getUnitsInDirection (position[0], position[1], 0, 1) + self.getUnitsInDirection (position[0], position[1], -1, 0)
        elif angle < 202.5 or angle > 157.5:
            units = self.getUnitsInDirection (position[0], position[1], -1, 0)
        elif angle < 247.5 or angle > 202.5:
            units = self.getUnitsInDirection (position[0], position[1], 0, -1) + self.getUnitsInDirection (position[0], position[1], -1, 0)
        elif angle < 292.5 or angle > 247.5:
            units = self.getUnitsInDirection (position[0], position[1], 0, -1)
        elif angle < 337.5 or angle > 292.5:
            units = self.getUnitsInDirection (position[0], position[1], 0, -1) + self.getUnitsInDirection (position[0], position[1], 1, 0)
        
        return units
    
    def pickRandomDrivableTile (self):
        
        wayPointX = None
        wayPointY = None
        levelSize = config.game.level.levelSize
        xRange = xrange(levelSize[0])
        yRange = xrange(levelSize[1])
        found = False
        while not found:
            wayPointX = choise(xRange)
            wayPointY = choise(yRange)
            if config.game.level.isDriveable(wayPointX, wayPointY):
                found = True
        
        return (wayPointX, wayPointY)
    
    def getLocationsAtBase (self, base):
    
        locations = []
        
        if config.game.level.isDriveable(base.x - 1, base.y):
            locations.append((base.x - 1, base.y))
        
        return locations
        
    
    def randomLocationAtBase (self, base):
        
        return choise(self.getLocationsAtBase(base))
    
    def getUnitsAtBase (self, base):
        
        units = []
        
        for locationAtBase in self.getLocationsAtBase(base):
            
            for unitAtBase in self.getUnitsOnTile(locationAtBase.x, locationAtBase.y):
                
                units.append(unitAtBase)
                
        return units
    
    def getEnemyUnitsAtBase (self, base):
        
        enemys = []
        
        for unitAtBase in self.getUnitsAtBase(base):
        
            if unitAtBase.team != self.vehicle.team:
                
                enemys.append(unitAtBase)
        
        return enemys
    
    def getEnemyUnitsInSight (self, position, viewDirection):
        
        enemyUnits = []
        
        for unit in self.getUnitsInSight(position, viewDirection):
            if unit.team != self.vehicle.team:
                enemyUnits.append(unit)
        
        return enemyUnits
    
    def getClosestUnit (self, units):
        
        distance = {}
        for unit in units:
            center = unit.getCenterOfBoundingBox()
            distance = Vec3(self.vehicle.position[0] - center[0], self.vehicle.position[1] - center[1], self.vehicle.position[2] - center[2]).length()
            
            
    