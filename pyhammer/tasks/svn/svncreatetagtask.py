import re
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnCreateTagTask(TaskBase):
    __dirTrunk = ""
    __dirTag = ""
    __versionFile = ""

    def __init__( self, dirTrunk, dirTag, versionFile = None, encoding = "ISO-8859-1" ):
        super().__init__()
        
        self.__dirTrunk = dirTrunk
        self.__dirTag = dirTag
        self.__versionFile = versionFile
        self.__encoding = encoding

    def do( self ):
        if self.__versionFile is not None:
            f = open(self.__versionFile, 'r', encoding=self.__encoding)
            content = f.read()
            f.close()
            version = re.search( '[\'\"](\d+)\.(\d+)\.(\d+)', content )
            versionNumber = version.group(1) + '.' + version.group(2) + '.' + version.group(3)
            self.__dirTag = self.__dirTag + '/' + versionNumber

        self.reporter.message( "TRUNK DIR: %s" % self.__dirTrunk )
        self.reporter.message( "TAG DIR: %s" % self.__dirTag )
        commitMessage = "Created by Build"
        command = 'svn copy "' + self.__dirTrunk + '" "' + self.__dirTag + '" -m \"'+commitMessage+'\"'

        self.reporter.message( "COMMAND: %s" % command )
        
        return execProg( command, self.reporter ) == 0