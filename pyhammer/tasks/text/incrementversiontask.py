import re
from pyhammer.tasks.taskbase import TaskBase

class IncrementVersionTask(TaskBase):

    def __init__( self, assemblyPath, type ):
        super().__init__()
        self.__assemblyPath = assemblyPath
        self.__type = type

    def do( self ):
        items = []
        if type(self.__assemblyPath) is str:
            items.append(self.__assemblyPath)
        else:
            items = self.__assemblyPath

        for i, item in enumerate( items ):
            if not self.process(item):
                return False
        return True

    def process( self, item ):
        f = open(item, 'r')
        content = f.read()
        f.close()

        version = re.search( '(\d+)\.(\d+)\.(\d+)\.(\d+)', content )
        size = 4
        if not version:
            version = re.search( '(\d+)\.(\d+)\.(\d+)', content )
            size = 3
            if not version:
                self.reporter.failure("Can not found version in file: %s" % item)
                return False

        old = version.group(0)
        major = int(version.group(1))
        minor = int(version.group(2))
        revis = int(version.group(3))

        build = None
        if size == 4:
            build = int(version.group(4))

        if self.__type == "minor":
            minor += 1
            revis = 0
        elif self.__type == "revision":
            revis += 1
        elif self.__type == "build":
            if build is not None:
                build += 1
        else:
            self.reporter.failure("Version block '%s' not found on file %s" % ( self.__type, item ) )
            return False

        new = str(major) + "." + str(minor) + "." + str(revis)
        if build is not None:
            new += "." + str(build)

        content = content.replace(old,new)
        self.reporter.message( "Changing from version %s to %s on file %s" % ( old, new, item ) )

        f = open(item, 'w')
        f.write(content)
        f.close()

        return True