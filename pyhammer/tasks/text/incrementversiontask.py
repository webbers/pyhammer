import re
from pyhammer.tasks.taskbase import TaskBase

class IncrementVersionTask(TaskBase):

    def __init__( self, assemblyPath, type, blockCount = 4 ):
        super().__init__()
        self.__assemblyPath = assemblyPath
        self.__type = type
        self.__blockCount = blockCount

    def do( self ):
        f = open(self.__assemblyPath, 'r')
        content = f.read()
        f.close()

        new = ""
        old = ""

        if self.__blockCount == 4:
            version = re.search( '(\d+)\.(\d+)\.(\d+)\.(\d+)', content )

            if not version:
                self.reporter.failure("Can not found version in file: %s" % self.__assemblyPath)

            major = int(version.group(1))
            minor = int(version.group(2))
            revis = int(version.group(3))
            build = int(version.group(4))
            old = version.group(0)

            if self.__type == "minor":
                minor += 1
            elif self.__type == "revision":
                revis += 1
            elif self.__type == "build":
                build += 1
            else:
                self.reporter.failure("Version block not found: %s" % self.__type)
                return False

            new = str(major) + "." + str(minor) + "." + str(revis) + "." + str(build)

        elif self.__blockCount == 3:
            version = re.search( '(\d+)\.(\d+)\.(\d+)', content )

            if not version:
                self.reporter.failure("Can not found version in file: %s" % self.__assemblyPath)

            major = int(version.group(1))
            minor = int(version.group(2))
            revis = int(version.group(3))
            old = version.group(0)

            if self.__type == "minor":
                minor += 1
            elif self.__type == "revision":
                revis += 1
            else:
                self.reporter.failure("Version block not found: %s" % self.__type)
                return False

            new = str(major) + "." + str(minor) + "." + str(revis)
        
        content = content.replace(old,new)
        
        f = open(self.__assemblyPath, 'w')
        f.write(content)
        f.close()
        
        return True