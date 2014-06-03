# -*- coding: utf-8 -*-
import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class VsTestTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath ):
        super(VsTestTask, self).__init__()
        
        vsTestPath = "vstest.console.exe"
        self.command = "\"%s\" \"%s\"" % ( vsTestPath, csProjectPath )
        self.csProjectPath = csProjectPath
        self.workingDir = os.path.dirname(csProjectPath)

    def do( self ):
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter, self.workingDir ) == 0