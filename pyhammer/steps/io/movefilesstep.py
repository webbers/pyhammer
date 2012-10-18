import os
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import moveFile

class MoveFilesStep(AbstractStep):
    """Move Files Step"""

    def __init__( self, files, srcDir, destDir ):
        AbstractStep.__init__( self, "Move Files" )
        self.srcDir = srcDir
        self.destDir = destDir
        self.files = files


    def do( self ):
        self.reporter.message( "MOVE FILES: %s => %s" % ( self.srcDir, self.destDir ) )

        for fp in self.files:
            relPath = fp.lower().replace( os.path.realpath( self.srcDir ).lower(), "" )
            destPath = os.path.realpath( self.destDir ) + relPath
            self.reporter.message(fp)
           
            if not moveFile( fp, destPath ):
                self.reporter.failure("move %s to %s" % (fp, destPath))
                return False  
        return True
    
    def setFiles( self, files ):
        self.files = files