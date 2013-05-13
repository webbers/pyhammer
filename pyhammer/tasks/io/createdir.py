import os
import shutil
from pyhammer.tasks.taskbase import TaskBase

class CreateDirTask(TaskBase):
    def __init__(self, srcDir):
        super().__init__()
        self.srcDir = srcDir
        
    def do( self ):
        self.reporter.message( "Creating Directory: %s" % self.srcDir)

        if ( os.path.exists( self.srcDir ) == 0):
            absPath = os.path.abspath( self.srcDir )

            if os.path.exists( absPath ):
                return False

            if os.name == "nt":
                cmd = """mkdir "%s" """ % absPath
            else:
                cmd = """md -rf "%s" """ % absPath
            print(cmd)
            os.system( cmd )
            return ( os.path.exists( absPath ) )
        else:
            return True