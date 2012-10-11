import re
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import ExecProg

class SvnCreateTagDirStep(AbstractStep):
    """Svn Create Tag Dir Step"""

    def __init__( self, dirTrunk, dirTag, assemblyPath ):
        AbstractStep.__init__( self, "Svn Create Tag" )
        
        self.dirTrunk = dirTrunk
        self.dirTag = dirTag
        self.assemblyPath = assemblyPath

    def do( self ):
        f = open(self.assemblyPath, 'r')
        content = f.read()
        f.close()        
        version = re.search( '"(\d+)\.(\d+)\.(\d+)\.(\d+)"', content )        
        versionNumber = version.group(1) + '.' + version.group(2) + '.' + version.group(3)
        self.dirTag = self.dirTag + '/' + versionNumber
        self.reporter.message( "TRUNK DIR: %s" % self.dirTrunk )
        self.reporter.message( "TAG DIR: %s" % self.dirTag )        
        commitMessage = "Created by Build"
        command = 'svn copy "' + self.dirTrunk + '" "' + self.dirTag + '" -m \"'+commitMessage+'\"'

        self.reporter.message( "COMMAND: %s" % command )
        
        return ExecProg( command, self.reporter ) == 0