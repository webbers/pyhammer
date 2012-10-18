import os
import shutil
from pyhammer.tasks.taskbase import TaskBase

class DeleteTask(TaskBase):
    def __init__(self, srcDir):
        super().__init__()
        self.srcDir = srcDir
        
    def do( self ):
        self.reporter.message( "Deleting: %s" % self.srcDir)
        if os.path.exists( self.srcDir ):
            if os.path.isdir(self.srcDir):
                shutil.rmtree(self.srcDir )
            else:
                os.remove( self.srcDir )
        return True