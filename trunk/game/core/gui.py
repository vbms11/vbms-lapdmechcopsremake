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
import demomenu
 
 
# GUI
class GUI(object):
 
    # Initialize: Resources
    def initializeResources(self):
        rp = PyCEGUI.System.getSingleton().getResourceProvider()
        rp.setResourceGroupDirectory('schemes', './datafiles/schemes')
        rp.setResourceGroupDirectory('imagesets', './datafiles/imagesets')
        rp.setResourceGroupDirectory('fonts', './datafiles/fonts')
        rp.setResourceGroupDirectory('layouts', './datafiles/layouts')
        rp.setResourceGroupDirectory('looknfeels', './datafiles/looknfeel')
        rp.setResourceGroupDirectory('schemas', './datafiles/xml_schemas')
        PyCEGUI.Imageset.setDefaultResourceGroup('imagesets')
        PyCEGUI.Font.setDefaultResourceGroup('fonts')
        PyCEGUI.Scheme.setDefaultResourceGroup('schemes')
        PyCEGUI.WidgetLookManager.setDefaultResourceGroup('looknfeels')
        PyCEGUI.WindowManager.setDefaultResourceGroup('layouts')
        parser = PyCEGUI.System.getSingleton().getXMLParser()
        if parser.isPropertyPresent('SchemaDefaultResourceGroup'):
            parser.setProperty('SchemaDefaultResourceGroup', 'schemas')
        return
 
    # Initialize: Defaults
    def initializeDefaults(self):
        sm = PyCEGUI.SchemeManager.getSingleton()
        sm.create('VanillaSkin.scheme')
        sm.create('TaharezLook.scheme')
        PyCEGUI.System.getSingleton().setDefaultMouseCursor('Vanilla-Images', 'MouseArrow')
        return
 
    # Initialize
    def Initialize(self):
        try:
            self.initializeResources()
            self.initializeDefaults()
 
            # GUISheet
            self.GUISheet = PyCEGUI.WindowManager.getSingleton().createWindow('DefaultWindow', 'Root')
            PyCEGUI.System.getSingleton().setGUISheet(self.GUISheet)
        except Exception, msg:
            raise InitializationError(msg)
        return
 
    # Setup
    # - Important: the instance of `demomenu.DemoMenu` has to be bound to this object; if it is
    # a local variable (read: destroyed when it goes out of scope), exceptions will be raised
    # about the `buttonClicked` method not existing. This is a drawback of the type of setup
    # this example uses, and as a consequence of Python being a garbage collected language.
    def Setup(self):
        self.demoMenu = demomenu.DemoMenu()
        self.demoMenu.Initialize()
        self.demoMenu.Setup()
        return
    
    def removeCurrentLayout (self):
        pass
        #.destroyWindow( mRootWindow );
    
    # Setup: Interface
    def setupInterface(self):
        
        # self.removeCurrentLayout()
        
        self.Setup()
        return