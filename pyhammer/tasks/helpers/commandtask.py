from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class CommandTask(TaskBase):
    """Cs UnitTest Step"""

    def __init__( self, command, path = None):
        TaskBase().__init__()
        self.path = path
        self.command = command

    def do( self ):
        self.reporter.message( "RUN COMMAND: %s" % self.command )
        result = execProg( self.command, self.reporter, self.path) == 0
        return result


