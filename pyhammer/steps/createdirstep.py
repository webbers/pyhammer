import os
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import createDir

class CreateDirStep(AbstractStep):
    """Create Dir Step"""

    def __init__( self, srcDir ):
        AbstractStep.__init__(self, "Create Dir")
        self.srcDir = srcDir
        
    def do( self ):
        self.reporter.message( "CREATE DIR: %s" % ( self.srcDir ) ) 

        if os.path.exists( self.srcDir ):
            #try:   
                createDir( self.srcDir )            
                return True
            #except:
                print("error")
                return False
        else:
            return True