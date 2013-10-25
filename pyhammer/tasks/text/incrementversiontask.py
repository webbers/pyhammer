# -*- coding: utf-8 -*-
import re
import codecs
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg2

class IncrementVersionTask(TaskBase):

    def __init__(self, assemblyPath, type, encoding = None, projectRoot = '',  useSvnBuild = True):
        super(IncrementVersionTask, self).__init__()
        self.__assemblyPath = assemblyPath
        self.__type = type
        self.__encoding = encoding
        self.__useSvnBuild = useSvnBuild
        self.__projectRoot = projectRoot

    def do(self):
        items = []
        if type(self.__assemblyPath) is str:
            items.append(self.__assemblyPath)
        else:
            items = self.__assemblyPath

        for i, item in enumerate( items ):
            if not self.process(item):
                return False
        return True

    def process(self, item):
        
        f = None
        try:
            if not self.__encoding is None:
                f = codecs.open(item, 'r', encoding=self.__encoding)
            else:
                f = open(item, 'r')
                
            content = f.read()
        except IOError as e:
            self.reporter.failure("Can not read file: %s" % item)
            return False
        finally:
            if f is not None:
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

        if self.__useSvnBuild and self.__projectRoot != '' and size == 4:
            prog = execProg2("svnversion", cwd=self.__projectRoot)
            build = prog[0]
            build = build.split(':')
            if len(build) > 1:
                build = build[1]
            else:
                build = build[0]
            if build[len(build)-1] == 'M' or build[len(build)-1] == 'S' or build[len(build)-1] == 'P':
                build = build[0:len(build)-1]

        new = str(major) + "." + str(minor) + "." + str(revis)
        if build is not None:
            new += "." + str(build)

        content = content.replace(old,new)
        self.reporter.message( "Changing from version %s to %s on file %s" % ( old, new, item ) )
        
        try:
            if not self.__encoding is None:
                f = codecs.open(item, 'w', encoding=self.__encoding)
                f.write(content)
            else:
                f = open(item, 'w')
                f.write(content)
        except IOError as e:
            self.reporter.message(e)
            self.reporter.failure("Can not write file: %s" % item)
            return False
        finally:
            f.close()

        return True