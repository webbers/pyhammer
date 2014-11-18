# -*- coding: utf-8 -*-
import os
from pyhammer.filters.mstestfilefilter import MsTestFileFilter
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsTestTask(TaskBase):
    """Cs UnitTest Step"""

    def __init__( self, csTestDllPath = "", testSettingsPath = "", baseDir = "", buildMode = "", exclude = []):
        super(MsTestTask, self).__init__()
        self.command = []

        testSettingsCommand = ""
        if testSettingsPath != "":
            testSettingsCommand = "/testsettings:\"%s\"" % testSettingsPath

        if len(csTestDllPath) == 0 and len(baseDir) != 0:
            csTestDllPath = MsTestFileFilter(buildMode, exclude).Filter(baseDir)

        if type(csTestDllPath) == str:
            self.command.append(["""MSTest.exe /testcontainer:\"%s\" %s""" % ( csTestDllPath, testSettingsCommand ), csTestDllPath])
        else:
            files = [file for file in csTestDllPath if os.path.splitext(file)[1] == '.dll']

            for dllTestPath in files:
                self.command.append(["""MSTest.exe /testcontainer:\"%s\" %s""" % ( dllTestPath, testSettingsCommand ), dllTestPath])

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