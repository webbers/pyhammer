# -*- coding: utf-8 -*-
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsPublishWebsiteTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath, publishProfile, visualStudioVersion = "12.0", buildMode = "Release" ):
        super(MsPublishWebsiteTask, self).__init__()
        
        msBuildPath = "msbuild.exe"
        self.command = "\"%s\" \"%s\" /p:Configuration=%s /p:DeployOnBuild=true /p:PublishProfile=%s /p:VisualStudioVersion=%s " % ( msBuildPath, csProjectPath, buildMode, publishProfile, visualStudioVersion)
        self.csProjectPath = csProjectPath

    def do( self ):
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter ) == 0
    