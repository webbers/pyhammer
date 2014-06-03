# -*- coding: utf-8 -*-
import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class VsTestTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath, outputDir, target = "Rebuild", mode = "Release", visualStudioVersion = "12.0" ):
        super(MsBuildTask, self).__init__()
        
        msBuildPath = "vstest.console.exe"
        self.command = "\"%s\" \"%s\" /t:%s /property:Configuration=%s;VisualStudioVersion=%s;OutDir=\"%s\"\\ " % ( msBuildPath, csProjectPath, target, mode, visualStudioVersion, outputDir )
        self.csProjectPath = csProjectPath
        self.workingDir = os.path.dirname(csProjectPath)

    def do( self ):
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter, self.workingDir ) == 0