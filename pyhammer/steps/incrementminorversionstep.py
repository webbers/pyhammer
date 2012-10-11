import re
from pyhammer.steps.abstractstep import AbstractStep

class IncrementMinorVersionStep(AbstractStep):

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
        minor = int(version.group(2)) + 1
        revision = version.group(3)
        build = 0
        
        old = version.group(0)
        new = '"' + major + "." + str(minor) + "." + revision + '.0"'
        
        content = content.replace(old,new)
        
        f = open(self.assemblyPath, 'w')
        print >> f, content
        
        return 1