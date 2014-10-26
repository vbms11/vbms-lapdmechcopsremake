'''
Created on Oct 18, 2014

@author: vbms
'''

import sys

try:
    import psyco
    psyco.full()
except ImportError:
    pass

__version__ = '0.1'
__date__ = ''
__author__ = 'Silvester Muhlhaus <silkyfx@gmail.com>'

windowTitel = "Robot War Arena"
windowWidth = 640
windowHeight = 480            

ESCAPE = '\033'
key_moveForwald = "w"
key_moveBackwald = "s"
key_straffLeft = ""
key_straffRight = ""
key_turnLeft = "a"
key_turnRight = "d"

window = 0
game = None
lastFrameTime = None

centerMouse = True;
mouseSensitifiy = 0.1;

roadsTextured = False
buildingsTextured = False

textureMode_nearest = 1
textureMode_linear = 2
textureMode_mipmap = 3
textureMode = textureMode_mipmap



