import os
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class MsTestTask(TaskBase):
    """Cs UnitTest Step"""

    def __init__( self, csTestDllPath ):
        TaskBase().__init__()

        self.command = """MSTest.exe /testcontainer:%s""" % ( csTestDllPath )
        self.csTestDllPath = csTestDllPath

    def do( self ):
        self.reporter.message( "RUN CS UNITTEST: %s" % self.csTestDllPath )

        print(self.command)

        result = execProg( self.command, self.reporter, os.path.dirname(self.csTestDllPath) ) == 0
        return result


