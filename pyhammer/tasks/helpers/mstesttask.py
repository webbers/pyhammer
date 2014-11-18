# -*- coding: utf-8 -*-
import os
from pyhammer.filters.mstestfilefilter import MsTestFileFilter
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsTestTask(TaskBase):
    """Cs UnitTest Step"""

    def __init__( self, csTestDllPath = "", testSettingsPath = "", baseDir = "", buildMode = "", exclude = []):
        super(MsTestTask, self).__init__()

        self.__csTestDllPath = csTestDllPath
        self.__testSettingsPath = testSettingsPath
        self.__baseDir = baseDir
        self.__buildMode = buildMode
        self.__exclude = exclude

    def do( self ):
        command = []
        testSettingsCommand = ""
        if self.__testSettingsPath != "":
            testSettingsCommand = "/testsettings:\"%s\"" % self.__testSettingsPath

        if len(self.__csTestDllPath) == 0 and len(self.__baseDir) != 0:
            self.__csTestDllPath = MsTestFileFilter(self.__buildMode, self.__exclude).Filter(self.__baseDir)

        if type(self.__csTestDllPath) == str:
            command.append(["""MSTest.exe /testcontainer:\"%s\" %s""" % (self.__csTestDllPath, testSettingsCommand), self.__csTestDllPath])
        else:
            files = [file for file in self.__csTestDllPath if os.path.splitext(file)[1] == '.dll']

            for dllTestPath in files:
                command.append(["""MSTest.exe /testcontainer:\"%s\" %s""" % (dllTestPath, testSettingsCommand), dllTestPath])

        result = True
        for comm in command:
            self.reporter.message("RUN CS UNITTEST: %s" % comm[1])
            print(comm)
            result = execProg(comm[0], self.reporter, os.path.dirname(comm[1])) == 0
            if not result:
                break;
        return result

    def _isValidTest(self, execResult):
        result = True
        for execItem in execResult:
            if execItem == False:
                result = False

        return result
