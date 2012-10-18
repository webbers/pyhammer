import distutils
import shutil
from pyhammer.steps.abstractstep import AbstractStep

class CopyDirStep(AbstractStep):
    """Copy Dir Step"""

    def __init__( self, srcDir, destDir ):
        AbstractStep.__init__( self, "Copy Dir" )
        
        self.srcDir = srcDir
        self.destDir = destDir
        
    def do( self ):
        self.reporter.message( "COPY DIR: %s => %s" % ( self.srcDir, self.destDir ) )        
        return shutil.copytree( self.srcDir, self.destDir )