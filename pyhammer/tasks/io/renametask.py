import os
from pyhammer.tasks.taskbase import TaskBase

class RenameTask(TaskBase):
    def __init__(self, src, dst):
        super().__init__()
        self.__src = src
        self.__dst = dst

    def do( self ):
        self.reporter.message( "Renaming %s to %s" % (self.__src, self.__dst) )
        if not os.path.exists( self.__src ):
            self.reporter.message('Source file not exists: %s' % self.__src )
            return False
        if os.path.exists(self.__dst):
            self.reporter.message('Destination file already exists: %s' % self.__dst )
            return False

        os.rename(self.__src, self.__dst)
        return True