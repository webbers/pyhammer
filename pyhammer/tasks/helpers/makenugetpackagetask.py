# -*- coding: utf-8 -*-
import os
import ntpath
import glob
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MakeNugetPackageTask(TaskBase):
    """Make Nuget Package Task"""

    def __init__( self, csProjectPath, solutionDir, tempDir, publishDir, visualStudioVersion = "12.0" ):
        super(MakeNugetPackageTask, self).__init__()

        self.csProjectPath = csProjectPath
        self.solutionDir = solutionDir
        self.tempDir = tempDir
        self.publishDir = publishDir
        self.visualStudioVersion = visualStudioVersion

    def do( self ):
        self.reporter.message( "MAKING NUGET PACKAGE FROM: %s" % ntpath.basename(self.csProjectPath) )

        result = execProg("msbuild.exe \"%s\" /t:Rebuild /p:Configuration=Release;VisualStudioVersion=%s" % ( self.csProjectPath, self.visualStudioVersion ), self.reporter, self.solutionDir)
        if(not result == 0):
            return False

        result = execProg("nuget.exe pack \"%s\" -IncludeReferencedProjects -prop Configuration=Release -OutputDirectory \"%s\"" % (self.csProjectPath, self.tempDir), self.reporter)
        if(not result == 0):
            return False

        if(self.publishDir is not None):
            os.chdir(self.tempDir)
            files = glob.glob("*.nupkg")

            result = execProg("nuget.exe push \"%s\" -Source \"%s\"" % (files[0], self.publishDir), self.reporter)
            os.remove(files[0])
            if(not result == 0):
                return False


        return True
    