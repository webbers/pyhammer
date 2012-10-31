from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class GitCheckoutTask(TaskBase):
    def __init__( self, branch, dir ):
        super().__init__()

        self.__branch = branch
        self.__dir = dir

    def do( self ):
        self.reporter.message( "Git Checkout %s on %s" % (self.__branch, self.__dir) )
        return execProg( "git checkout %s" % self.__branch, self.reporter, self.__dir ) == 0