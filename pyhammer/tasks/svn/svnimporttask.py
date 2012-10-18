from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnImportTask(TaskBase):
    """Svn Commit Dir Step"""

    def __init__( self, dir, repo ):
        super().__init__()
        
        self.dir = dir
        self.repo = repo

    def do( self ):
        self.reporter.message( "IMPORT DIR: %s => %s" % ( self.dir, self.repo ) )
        commitMessage = "Commited by Build"
        command = "svn import -m \"%s\" \"%s\" \"%s\" " % ( commitMessage, self.dir, self.repo )
        self.reporter.message( "SVN IMPORT DIR: %s" % self.dir )
        return execProg( command, self.reporter, self.dir ) == 0