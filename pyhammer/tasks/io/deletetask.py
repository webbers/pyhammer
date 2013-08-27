import os
import shutil
from pyhammer.tasks.taskbase import TaskBase

class DeleteTask(TaskBase):
    def __init__(self, srcDir):
        TaskBase().__init__()
        self.srcDir = srcDir

    def do(self):
        items = []

        if  type(self.srcDir) is str:
            items.append(self.srcDir)
        else:
            items = self.srcDir

        for i, item in enumerate(items):
            if not self.process(item):
                return False

        return True

    def process( self, item ):
        self.reporter.message( "Deleting: %s" % item)
        if os.path.exists( item ):
            if os.path.isdir( item):
                shutil.rmtree( item )
            else:
                os.remove( item )
        return True
