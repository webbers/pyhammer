from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import svnList, execProg, isList

class SvnDeleteTask(TaskBase):
    """Svn Delete Step"""

    def __init__( self, dir, failOnError = False ):
        TaskBase().__init__()
        self.__dir = dir
        self.__failOnError = failOnError

    def do( self ):
        self.reporter.message( "DELETE: %s" % self.__dir )
        items = svnList(self.__dir, self.reporter)

        if not isList(items):
            if self.__failOnError:
                return 0
            else:
                return 1

        for path in items:
            command = "svn delete --force \"%s\" -m \"Build\"" % (self.__dir + "/" + path)
            self.reporter.message(command)
            execProg( command, self.reporter ) == 0
        return 1
