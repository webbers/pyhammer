import re
from pyhammer.reporters.bufferedreporter import BufferedReporter
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import ExecProg

class CheckUnversionedFilesStep( AbstractStep ):
    def __init__( self, baseDir ):
        AbstractStep.__init__( self, "Check Unversioned Files" )
        self.__baseDir = baseDir

    def build( self ):
        br = BufferedReporter()
        ExecProg( "svn status " + self.__baseDir, br, self.__baseDir )
        
        files = re.findall('\?\s+([^\n]+)\n', br.getBuffer() )
        for file in files:
            self.reporter.failure( "Arquivo \"" + file + "\" nao versionado" )
            
        if( len(files) ):
            self.reporter.failure( str(len(files)) + " arquivos nao versionados" )
            return 0
            
        return 1

