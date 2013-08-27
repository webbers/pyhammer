import subprocess
from pyhammer.tasks.taskbase import TaskBase

class TortoiseSvnCommitTask( TaskBase ):

    def __init__( self, path ):
        TaskBase().__init__()
        self.__path  = path

    def RunCmd( self, CmdLine, CmdDir = None ):
        p = subprocess.Popen( CmdLine, cwd = CmdDir )
        return p.wait()

    def build( self ):
        self.RunCmd( "TortoiseProc /command:commit /path:" + self.__path )
        return True