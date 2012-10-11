from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import ExecProg

class SvnImportDirStep(AbstractStep):
    """Svn Commit Dir Step"""

    def __init__( self, dir, repo ):
        AbstractStep.__init__( self, "Svn Import Dir" )
        
        self.dir = dir
        self.repo = repo

    def do( self ):
        self.reporter.message( "IMPORT DIR: %s => %s" % ( self.dir, self.repo ) )
        commitMessage = "Commited by Build"
        command = "svn import -m \"%s\" \"%s\" \"%s\" " % ( commitMessage, self.dir, self.repo )
        self.reporter.message( "SVN IMPORT DIR: %s" % self.dir )
        return ExecProg( command, self.reporter, self.dir ) == 0