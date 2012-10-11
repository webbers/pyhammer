from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import ExecProg

class SvnCreateCustomTagDirStep(AbstractStep):
    """Svn Create Tag Dir Step"""

    def __init__( self, dirTrunk, dirTag ):
        AbstractStep.__init__( self, "Svn Create Tag" )
        
        self.dirTrunk = dirTrunk
        self.dirTag = dirTag

    def do( self ):
        self.reporter.message( "TRUNK DIR: %s" % self.dirTrunk )
        self.reporter.message( "TAG DIR: %s" % self.dirTag )        
        commitMessage = "Created by Build"
        command = 'svn copy ' + self.dirTrunk + ' ' + self.dirTag + ' -m \"'+commitMessage+'\"'
        return ExecProg( command, self.reporter, self.dirTrunk ) == 0