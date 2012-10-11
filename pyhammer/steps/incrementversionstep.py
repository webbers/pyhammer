import re
import subprocess
from pyhammer.steps.abstractstep import AbstractStep

class IncrementVersionStep(AbstractStep):

    def __init__( self, assemblyPath, projectRoot ):
        AbstractStep.__init__( self, "Set Version Step" )
        self.assemblyPath = assemblyPath
        self.projectRoot = projectRoot

    def do( self ):
        process = subprocess.Popen( "svnversion", cwd=self.projectRoot, stdout=subprocess.PIPE )
        revision = re.search( '\d+', process.stdout.readline() ).group(0)
        
        f = open(self.assemblyPath, 'r')
        content = f.read()
        f.close()
        
        version = re.search( '"(\d+)\.(\d+)\.(\d+)\.(\d+)"', content )
        
        major = version.group(1)
        minor = version.group(2)
        build = int(version.group(3)) + 1
        
        old = version.group(0)
        new = '"' + major + "." + minor + "." + str( build ) + "." + revision + '"'
        
        content = content.replace(old,new)
        
        f = open(self.assemblyPath, 'w')
        print >> f, content
        
        return 1