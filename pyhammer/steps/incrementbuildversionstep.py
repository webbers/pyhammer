import re
from pyhammer.steps.abstractstep import AbstractStep

class IncrementBuildVersionStep(AbstractStep):

    def __init__( self, assemblyPath, projectRoot ):
        AbstractStep.__init__( self, "Set Version Step" )
        self.assemblyPath = assemblyPath
        self.projectRoot = projectRoot

    def do( self ):
        f = open(self.assemblyPath, 'r')
        content = f.read()
        f.close()
        
        version = re.search( '"(\d+)\.(\d+)\.(\d+)\.(\d+)"', content )
        
        major = version.group(1)
        minor = version.group(2)
        revision = version.group(3)
        build = int(version.group(4)) + 1
        
        old = version.group(0)
        new = '"' + major + "." + minor + "." + revision + "." + str( build ) + '"'
        
        content = content.replace(old,new)
        
        f = open(self.assemblyPath, 'w')
        print >> f, content
        
        return 1