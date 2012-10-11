import os
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import removeDir

class DelTreeStep(AbstractStep):
    """DelTree Step"""

    def __init__( self, srcDir ):
        AbstractStep.__init__(self, "DelTree")
        self.srcDir = srcDir
        
    def do( self ):
        self.reporter.message( "DELTREE: %s" % self.srcDir)

        if os.path.exists( self.srcDir ):
            try:
                removeDir( self.srcDir )            
                return True
            except:
                print("error")
                return False
        else:
            return True