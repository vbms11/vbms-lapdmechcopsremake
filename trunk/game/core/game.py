'''
Created on Oct 18, 2014

@author: vbms
'''
from OpenGL.GL import *
from OpenGL.GLU import *
from camera import Camera
from level import Level
from util.vector3d import Vec3
from vehicle.lightTank import LightTank
from vehicle.vehicleType import VehicleType
from scene.skyDome import SkyDome
from core.gameConfig import GameConfig
from math import ceil
from random import choice, shuffle
from bot.pathFinder import PathFinder

class Game:
    '''
    classdocs
    '''
    
    camera = None
    level = None
    skyDome = None
    
    vehicles = None
    selectedVehicle = None
    
    # controls
    moveForwald = False
    moveBackwald = False
    straffLeft = False
    straffRight = False
    turnLeft = False
    turnRight = False
    
    millis = 0
    
    gameConfig = None
    
    def __init__(self, gameConfig):
        '''
        Constructor
        '''
        self.gameConfig = gameConfig
        
    def init (self):
        
        self.level = Level(self.gameConfig.levelFile)
        self.level.init()
        
        self.skyDome = SkyDome()
        self.skyDome.init("textures/sky_1.jpg")
        
        self.camera = Camera()
        
        self.vehicles = []
        for team in self.gameConfig.teams:
            teamVehicles = self.gameConfig.initialPlayers / len(team.bases)
            vehiclesPerBase = self.gameConfig.initialPlayers / len(team.bases)
            for baseId in team.bases:
                base = self.level.bases[baseId]
                base.owner = team
                vehiclesThisBase = int(ceil(vehiclesPerBase))
                teamVehicles -= vehiclesThisBase
                vehiclePositions = self.getInitialVehiclePositions(base, vehiclesThisBase)
                for vehiclePosition in vehiclePositions:
                    # create and place the vehicle
                    vehicle = LightTank(VehicleType)
                    vehicle.init([vehiclePosition[0], vehiclePosition[1], 0], team)
                    self.vehicles.append(vehicle)
                    # the first vehicle is the players
                    if self.selectedVehicle == None:
                        self.selectedVehicle = vehicle
                        
        pathFinder = PathFinder()
        path = pathFinder.findPath(1,1,17,17)
        print path
    
    def update (self, millis):
        
        self.millis = millis
        
        self.level.update()
        
        # move vehicle
        if self.turnLeft and not self.turnRight:
            self.selectedVehicle.turnLeft()
        if self.turnRight and not self.turnLeft:
            self.selectedVehicle.turnRight()
        if self.moveForwald and not self.moveBackwald:
            self.selectedVehicle.moveForwald()
        if self.moveBackwald and not self.moveForwald:
            self.selectedVehicle.moveBackwald()
        for vehicle in self.vehicles:
            vehicle.update()
        
        # set camera
        self.camera.setPosition(*self.selectedVehicle.getCameraPosition());
        self.camera.setDirection(self.selectedVehicle.aimDirection);
        
    def paint (self):
        
        self.camera.loadIdentity()
        
        self.skyDome.paint()
        
        self.level.paint()
        
        glDisable(GL_TEXTURE_2D)
        
        for vehicle in self.vehicles:
            vehicle.paint()
        
        glEnable(GL_TEXTURE_2D)
    
    def moveMouse (self, x, y):
        
        self.selectedVehicle.moveAim(x, y);
    
    def getInitialVehiclePositions (self, base, vehiclesThisBase):
        
        # make list of drivable tiles around the base
        basePosition = base.position
        baseRoadTiles = []
        for y in range(-1, 2):
            for x in range(-1, 2):
                if self.level.isDriveable(base.position[0] + x, base.position[1] + y):
                    baseRoadTiles.append([base.position[0] + x, base.position[1] + y])
        
        # find out if there is enuph space
        maxVehicles = len(baseRoadTiles) * 4
        vehiclesToProduce = 0
        vehiclesToPlace = vehiclesThisBase
        if vehiclesThisBase > maxVehicles:
            vehiclesToProduce = vehiclesThisBase - maxVehicles
            vehiclesToPlace = maxVehicles
        
        # randomly choose a valid position
        vehiclePositions = []
        possiblePositions = [[0.1,0.1],[0.6,0.1],[0.1,0.6],[0.6,0.6]]
        for vehicle in xrange(vehiclesToPlace):
            foundPosition = False
            position = None
            while foundPosition == False:
                shuffle(possiblePositions)
                roadTile = choice(baseRoadTiles)
                if not self.isVehiclePositionTaken([roadTile[0] + possiblePositions[0][0], roadTile[1] + possiblePositions[0][1]], vehiclePositions):
                    position = [roadTile[0] + possiblePositions[0][0], roadTile[1] + possiblePositions[0][1]]
                    foundPosition = True
                elif not self.isVehiclePositionTaken([roadTile[0] + possiblePositions[1][0], roadTile[1] + possiblePositions[1][1]], vehiclePositions):
                    position = [roadTile[0] + possiblePositions[1][0], roadTile[1] + possiblePositions[1][1]]
                    foundPosition = True
                elif not self.isVehiclePositionTaken([roadTile[0] + possiblePositions[2][0], roadTile[1] + possiblePositions[2][1]], vehiclePositions):
                    position = [roadTile[0] + possiblePositions[2][0], roadTile[1] + possiblePositions[2][1]]
                    foundPosition = True
                elif not self.isVehiclePositionTaken([roadTile[0] + possiblePositions[3][0], roadTile[1] + possiblePositions[3][1]], vehiclePositions):
                    position = [roadTile[0] + possiblePositions[3][0], roadTile[1] + possiblePositions[3][1]]
                    foundPosition = True
            vehiclePositions.append(position)
        return vehiclePositions
    
    def isVehiclePositionTaken (self, vehiclePosition, takenPositions):
        
        for position in takenPositions:
            if position[0] == vehiclePosition[0] and position[1] == vehiclePosition[1]:
                return True
        return False
        