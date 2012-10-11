from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import svnList, ExecProg

class SvnDeleteStep(AbstractStep):
    """Svn Delete Step"""

    def __init__( self, dir ):
        AbstractStep.__init__( self, "Svn Delete Dir" )
        self.dir = dir

    def do( self ):
        self.reporter.message( "DELETE: %s" % self.dir )
        
        for path in svnList(self.dir, self.reporter):
            command = "svn delete --force \"%s\" -m \"Build\"" % (self.dir + "/" + path)
            print(command)
            ExecProg( command, self.reporter ) == 0
        return 1
