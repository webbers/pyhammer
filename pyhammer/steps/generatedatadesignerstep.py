import os

from steps.abstractstep import *
from util import *

sqlMetalPath = os.path.join( os.path.dirname( __file__ ), "../../res/tools/sqlMetal/SqlMetal.exe" )

class GenerateDataDesginerStep(AbstractStep):
    """SqlMetal Step"""

    def __init__( self, dbmlFile, outputFile ):
        AbstractStep.__init__( self, "Generate Data Designer" )
        self.__dbmlFile = dbmlFile
        self.__outputFile = outputFile

    def do( self ):
        self.reporter.message("generating data designer file in %s" % (self.__outputFile))
        commandLine = '/code:' + self.__outputFile + ' ' + self.__dbmlFile
        return ExecProg( '"' + sqlMetalPath + '" ' + commandLine, self.reporter ) == 0
        