import subprocess
import re
from pyhammer.steps.abstractstep import AbstractStep

class ApplyVersionStep(AbstractStep):

    def __init__( self, assemblyPath, documentPath, projectRoot ):
        AbstractStep.__init__( self, "Apply Version Step" )
        self.assemblyPath = assemblyPath
        self.documentPath = documentPath
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
        build = int(version.group(3))
        old = version.group(0)
        new = major + "." + minor + "." + str( build ) # + "." + revision
        
        f = open(self.documentPath, 'r')
        content = f.read()
        f.close()	
        version = re.search( '(\d+)\.(\d+)\.(\d+)', content )
        old = version.group(0)
        content = content.replace(old,new)
        
        f = open(self.documentPath, 'w')
        print >> f, content
        
        return 1