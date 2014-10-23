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
    
    def __init__(self):
        '''
        Constructor
        '''
        pass
        
    def init (self):
        
        self.skyDome = SkyDome()
        self.skyDome.init("textures/sky_1.jpg")
        
        self.level = Level()
        self.level.init()
        
        vehicle = LightTank(VehicleType)
        vehicle.init([5.5,5.5,0])
        self.vehicles = [vehicle]
        
        self.selectedVehicle = vehicle
        
        self.camera = Camera()
        
        
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
        
        # set camera
        self.camera.setPosition(*self.selectedVehicle.getCameraPosition());
        self.camera.setDirection(self.selectedVehicle.aimDirection);
        
    def paint (self):
        
        self.camera.loadIdentity()
        
        self.skyDome.paint()
        
        glDisable(GL_TEXTURE_2D)
        
        self.level.paint()
        
        for vehicle in self.vehicles:
            vehicle.paint()
        
        glEnable(GL_TEXTURE_2D)
    
    def moveMouse (self, x, y):
        
        self.selectedVehicle.moveAim(x, y);
    