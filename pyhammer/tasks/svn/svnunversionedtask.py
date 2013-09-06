import re
from pyhammer.reporters.memoryreporter import MemoryReporter
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnUnversionedTask( TaskBase ):
    def __init__( self, baseDir ):
        super(SvnUnversionedTask, self).__init__()
        self.__baseDir = baseDir

    def build( self ):
        br = MemoryReporter()
        execProg( "svn status " + self.__baseDir, br, self.__baseDir )
        
        files = re.findall('\?\s+([^\n]+)\n', br.getText() )
        for file in files:
            self.reporter.failure( "File \"" + file + "\" is not versioned" )
            
        if len(files):
            self.reporter.failure( str(len(files)) + " files not versioned" )
            return 0
            
        return 1

