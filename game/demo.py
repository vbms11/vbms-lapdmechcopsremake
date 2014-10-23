import sys, os.path
sys.path.append(os.path.join(os.getcwd(), 'bot'))
sys.path.append(os.path.join(os.getcwd(), 'core'))
sys.path.append(os.path.join(os.getcwd(), 'scene'))
sys.path.append(os.path.join(os.getcwd(), 'textures'))
sys.path.append(os.path.join(os.getcwd(), 'util'))
sys.path.append(os.path.join(os.getcwd(), 'vehicle'))
 
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
 
 
# Main
def main():
    gfx = Video()
    inp = Input()
    gui = GUI()
 
    # Initialize
    try:
        gfx.Initialize()
        inp.Initialize()
        gui.Initialize()
    except InitializationError as error:
        print(error)
        return 1
 
    # Setup the interface
    gui.setupInterface()
 
    # Main Loop
    gfx.EnterMainLoop()
 
    # Done
    # - We will never actually get here.
    gfx.Shutdown()
    return 0
 
# Guard
if __name__ == '__main__':
    sys.exit(main())