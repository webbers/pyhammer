from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnCommitTask(TaskBase):
    def __init__( self, dir, add, user, pwd ):
        super().__init__()
        
        self.__dir = dir
        self.__add = add
        self.__user = user
        self.__pwd = pwd

    def do( self ):
        self.reporter.message( "COMMIT: %s" % self.__dir )
        addResult = True
        if self.__add:
            command = "svn add --force *.*"
            addResult = execProg( command, self.reporter, self.__dir ) == 0
            
        if addResult :
            commitMessage = "Commited by Build"
            command = "svn commit -m \"%s\"" % commitMessage
            
            if self.__user:
                command += " --username %s --password %s" % (self.__user, self.__pwd)
            self.reporter.message( "SVN COMMIT DIR: %s" % self.__dir )
            return execProg( command, self.reporter, self.__dir ) == 0
        return False