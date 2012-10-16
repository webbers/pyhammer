from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import execProg

class SvnUpdateDirStep(AbstractStep):
    """Svn Update Dir Step"""

    def __init__( self, dir ):
        AbstractStep.__init__( self, "Svn Update Dir" )
        self.dir = dir

    def do( self ):
        self.reporter.message( "SVN UPDATE DIR: %s" % self.dir )
        return execProg( "svn update", self.reporter, self.dir ) == 0