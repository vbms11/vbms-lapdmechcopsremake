'''
Created on Oct 18, 2014

@author: vbms
'''
from game import Game

class Application:
    '''
    classdocs
    '''
    
    game = None

    def __init__(self, params):
        '''
        Constructor
        '''
        Application.game = Game()
        Application.game.init()