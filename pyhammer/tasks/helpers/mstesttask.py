# -*- coding: utf-8 -*-
import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsTestTask(TaskBase):
    """Cs UnitTest Step"""

    def __init__( self, csTestDllPath ):
        super(MsTestTask, self).__init__()
        self.command = []

        if type(csTestDllPath) == str:
            self.command.append(["""MSTest.exe /testcontainer:\"%s\"""" % ( csTestDllPath ), csTestDllPath])
        else:
            files = [file for file in csTestDllPath if os.path.splitext(file)[1] == '.dll']

            for dllTestPath in files:
                self.command.append(["""MSTest.exe /testcontainer:\"%s\"""" % ( dllTestPath ), dllTestPath])

        self.csTestDllPath = csTestDllPath

    def _isValidTest(self, execResult):
        result = True
        for execItem in execResult:
            if execItem == False:
                result = False

        return result

    def do( self ):
        result = True
        for comm in self.command:
            self.reporter.message( "RUN CS UNITTEST: %s" % comm[1] )
            print(comm)
            result = execProg(comm[0], self.reporter, os.path.dirname(comm[1])) == 0
            if not result:
                break;
        return result