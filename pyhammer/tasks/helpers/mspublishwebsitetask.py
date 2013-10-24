# -*- coding: utf-8 -*-
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsPublishWebsiteTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath, publishProfile, frameworkVersion = "v4.0.30319" ):
        super(MsPublishWebsiteTask, self).__init__()
        
        msBuildPath = "C:\\WINDOWS\\Microsoft.NET\\Framework\\%s\\msbuild.exe" % frameworkVersion
        self.command = "\"%s\" \"%s\" /p:Configuration=Release /p:DeployOnBuild=true /p:PublishProfile=%s " % ( msBuildPath, csProjectPath, publishProfile)
        self.csProjectPath = csProjectPath

    def do( self ):
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter ) == 0
    