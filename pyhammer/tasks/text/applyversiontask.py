import re
from pyhammer.tasks.taskbase import TaskBase

class ApplyVersionTask(TaskBase):

    def __init__( self, assemblyPath, setupScriptPath ):
        super().__init__()
        self.__assemblyPath = assemblyPath
        self.__setupScriptPath = setupScriptPath

    def do( self ):
        items = []
        if type(self.__setupScriptPath) is str:
            items.append(self.__setupScriptPath)
        else:
            items = self.__setupScriptPath

        for i, item in enumerate( items ):
            if not self.process(item):
                return False
        return True

    def process( self, item ):
        f = open(self.__assemblyPath, 'r')
        content = f.read()
        f.close()

        version = re.search( '(\d+)\.(\d+)\.(\d+)\.(\d+)', content )
        groups = 4
        if not version:
            version = re.search( '(\d+)\.(\d+)\.(\d+)', content )
            groups = 3
            if not version:
                self.reporter.failure("Can not found version in file: %s" % self.__assemblyPath)
                return False

        version = version.group(0)

        f = open(item, 'r')
        content = f.read()
        f.close()

        if groups == 4:
            oldVersion = re.search( '(\d+)\.(\d+)\.(\d+)\.(\d+)', content )
        else:
            if groups == 3:
                oldVersion = re.search( '(\d+)\.(\d+)\.(\d+)', content )
            else:
                self.reporter.failure("Can not found version in file: %s" % item)
                return False

        oldVersion = oldVersion.group(0)

        content = content.replace( oldVersion, version )

        self.reporter.message( "Changing from version %s to %s on file %s" % ( oldVersion, version, item ) )

        f = open(item, 'w')
        f.write(content)
        f.close()

        return True