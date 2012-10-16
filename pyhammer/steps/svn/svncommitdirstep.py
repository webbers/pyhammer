from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import execProg

class SvnCommitDirStep(AbstractStep):
    """Svn Commit Dir Step"""

    def __init__( self, dir, add, user, pwd ):
        AbstractStep.__init__( self, "Svn Commit Dir" )
        
        self.dir = dir
        self.add = add
        self.user = user
        self.pwd = pwd

    def do( self ):
        self.reporter.message( "COMMIT DIR: %s" % self.dir )
        addResult = True
        if self.add:
            command = "svn add --force *.*"
            addResult = execProg( command, self.reporter, self.dir ) == 0
            
        if addResult :
            commitMessage = "Commited by Build"
            command = "svn commit -m \"%s\"" % commitMessage
            
            if self.user:
                command += " --username %s --password %s" % (self.user, self.pwd)
            self.reporter.message( "SVN COMMIT DIR: %s" % self.dir )
            return execProg( command, self.reporter, self.dir ) == 0
        return False