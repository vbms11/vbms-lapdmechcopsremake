import sys
 
# Import: psyco
try:
    import psyco
    psyco.full()
except ImportError:
    pass
 
# Import: PyCEGUI
import PyCEGUI
 
# Import: User
from errors import InitializationError
 
 
# DemoMenu
class DemoMenu(object):
 
    # Initialize
    def Initialize(self):
        self.GUISheet = PyCEGUI.System.getSingleton().getGUISheet()
 
        # Load the layout
        self.menu = PyCEGUI.WindowManager.getSingleton().loadWindowLayout('DemoMenu.layout')
        return
 
    # connectHandlers
    # - Wrapper method to define the subscription/listener relationships.
    # - If there are a lot, it may behoove the coder to encapsulate them in methods, then call those methods here.
    def connectHandlers(self):
        self.menu.getChild('DemoMenu/Button').subscribeEvent(PyCEGUI.PushButton.EventClicked, self, 'buttonClicked')
        return
 
    # Setup
    def Setup(self):
 
        # Connect the handlers
        self.connectHandlers()
 
        # Attach
        self.GUISheet.addChildWindow(self.menu)
        return
 
    # Handler: buttonClicked
    def buttonClicked(self, args):
        print('buttonClicked')
        return