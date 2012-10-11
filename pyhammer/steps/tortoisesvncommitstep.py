import subprocess

#---------------------------------------------------------------------
from pyhammer.steps.abstractstep import AbstractStep

class TortoiseSvnCommitStep( AbstractStep ):
    #--------------------------------------------------------------------
    def __init__( self, path ):
        AbstractStep.__init__( self, "SvnCommit" )
        self.__path  = path

    #---------------------------------------------------------------------
    def RunCmd( self, CmdLine, CmdDir = None ):
        p = subprocess.Popen( CmdLine, cwd = CmdDir )
        return p.wait()

    #--------------------------------------------------------------------
    def build( self ):
        self.RunCmd( "TortoiseProc /command:commit /path:" + self.__path )
        return True