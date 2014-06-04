# -*- coding: utf-8 -*-
import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class VsTestTask(TaskBase):
    """Cs Project Build Step"""

    def __init__( self, csProjectPath ):
        super(VsTestTask, self).__init__()
        
        self.command = """vstest.console.exe \"%s\"""" % ( csProjectPath )
        self.csProjectPath = csProjectPath

    def do( self ):
        self.reporter.message( self.command )
        self.reporter.message( self.csProjectPath )
        self.reporter.message( "BUILD CS PROJECT: %s" % self.csProjectPath )
        return execProg( self.command, self.reporter, os.path.dirname(self.csProjectPath) ) == 0