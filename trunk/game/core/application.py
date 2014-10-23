'''
Created on Oct 18, 2014

@author: vbms
'''

# Import: psyco
try:
    import psyco
    psyco.full()
except ImportError:
    pass
 
# Import: User
from errors import InitializationError
from input import Input
from video import Video
from gui import GUI
from game import Game

class Application:
    '''
    classdocs
    '''
    
    _instance = None
    
    state = None
    state_mainMenu = 1
    state_optionsMenu = 2
    state_creditsMenu = 3
    state_newGameMenu = 4
    state_inGameMenu = 5
    
    gfx = Video()
    inp = Input()
    gui = GUI()
    
    def __new__(cls, *args, **kwargs):
        
        if not cls._instance:
            cls._instance = super(Application, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def run (self):
        
        # initialize
        try:
            self.gfx.Initialize()
            self.inp.Initialize()
            self.gui.Initialize()
        except InitializationError as error:
            print(error)
            return 1

        # Setup the interface
        self.gui.setupInterface()
        
        # set the initial state
        self.setState(self.state_mainMenu)
        
        # Main Loop
        self.gfx.EnterMainLoop()
        
        # Done
        # - We will never actually get here.
        self.gfx.Shutdown()
        
        return 0
    
    def setState (self, state):
        
        self.state = state
        
        if state == self.state_mainMenu:
            pass
        elif state == self.state_optionsMenu:
            pass
        elif state == self.state_creditsMenu:
            pass
        elif state == self.state_newGameMenu:
            pass
        elif state == self.state_inGameMenu:
            pass
    