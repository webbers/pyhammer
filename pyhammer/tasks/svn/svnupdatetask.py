from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnUpdateTask(TaskBase):
    """Svn Update Dir Step"""

    def __init__( self, dir ):
        super(SvnUpdateTask, self).__init__()
        self.dir = dir

    def do( self ):
        self.reporter.message( "SVN UPDATE DIR: %s" % self.dir )
        return execProg( "svn update", self.reporter, self.dir ) == 0