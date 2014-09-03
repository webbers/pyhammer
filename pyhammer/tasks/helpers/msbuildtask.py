# -*- coding: utf-8 -*-
import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsBuildTask(TaskBase):
    """Cs Project Build Step"""

    def __init__(self, csProjectPath, outputDir='', target="Rebuild", mode="Release", visualStudioVersion="12.0"):
        super(MsBuildTask, self).__init__()
        
        msBuildPath = "msbuild.exe"

        self.command = "\"%s\" \"%s\" /t:%s /property:Configuration=%s;VisualStudioVersion=%s " % \
                       (msBuildPath, csProjectPath, target, mode, visualStudioVersion)

        if outputDir is not None and outputDir != '':
            self.command = '%s;OutDir=\"%s\"' % (self.command, outputDir)

        self.csProjectPath = csProjectPath
        self.workingDir = os.path.dirname(csProjectPath)

    def do(self):
        self.reporter.message("BUILD CS PROJECT: %s" % self.csProjectPath)
        return execProg( self.command, self.reporter, self.workingDir ) == 0