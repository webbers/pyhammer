from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import svnList, execProg, isList

class SvnDeleteStep(AbstractStep):
    """Svn Delete Step"""

    def __init__( self, dir, failOnError = False ):
        AbstractStep.__init__( self, "Svn Delete" )
        self.dir = dir
        self.failOnError = failOnError

    def do( self ):
        self.reporter.message( "DELETE: %s" % self.dir )
        items = svnList(self.dir, self.reporter)

        if not isList(items):
            if self.failOnError:
                return 0
            else:
                return 1

        for path in items:
            command = "svn delete --force \"%s\" -m \"Build\"" % (self.dir + "/" + path)
            self.reporter.message(command)
            execProg( command, self.reporter ) == 0
        return 1
