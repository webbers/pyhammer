import distutils.file_util
from pyhammer.steps.abstractstep import AbstractStep

class CopyFileStep(AbstractStep):
    """Copy File Step"""

    def __init__( self, srcFile, destFile, overwrite = 1, makeDir = 1 ):
        AbstractStep.__init__( self, "Copy File" )
        self.srcFile = srcFile
        self.destFile = destFile
        self.overwrite = overwrite
        self.makeDir = makeDir

    def do( self ):
        self.reporter.message( "COPY FILE: %s => %s" % ( self.srcFile, self.destFile ) )
        result = distutils.file_util.copy_file(self.srcFile, self.destFile) #result = StCommon.CopyFile( self.srcFile, self.destFile, self.overwrite, self.makeDir )
        return result