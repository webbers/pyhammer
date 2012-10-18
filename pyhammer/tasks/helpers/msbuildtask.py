from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsBuildTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath, outputDir, target = "Rebuild", mode = "Release", frameworkVersion = "v4.0.30319" ):
        super().__init__()
        
        msBuildPath = "C:\\WINDOWS\\Microsoft.NET\\Framework\\%s\\msbuild.exe" % frameworkVersion
        self.command = "\"%s\" \"%s\" /t:%s /p:Configuration=%s;TargetFrameworkVersion=%s;OutDir=%s\\ " % ( msBuildPath, csProjectPath, target, mode, frameworkVersion, outputDir )
        self.csProjectPath = csProjectPath

    def do( self ):
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter ) == 0
    