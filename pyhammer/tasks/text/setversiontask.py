# -*- coding: utf-8 -*-
import re
from pyhammer.tasks.taskbase import TaskBase

class SetVersionTask(TaskBase):

    def __init__(self, assemblyPath, version):
        super(SetVersionTask, self).__init__()
        self.__assemblyPath = assemblyPath
        self.__version = version

    def do( self ):
        items = []
        if type(self.__assemblyPath) is str:
            items.append(self.__assemblyPath)
        else:
            items = self.__assemblyPath

        for i, item in enumerate(items):
            if not self.process(item):
                return False
        return True

    def process( self, item ):

        version = re.search('(\d+)\.(\d+)\.(\d+)\.(\d+)', self.__version)
        if not version:
            version = re.search('(\d+)\.(\d+)\.(\d+)', self.__version)

        if version:
            f = open(item, 'r')
            content = f.read()
            f.close()

            version = re.search('(\d+)\.(\d+)\.(\d+)\.(\d+)', content)
            if not version:
                version = re.search('(\d+)\.(\d+)\.(\d+)', content)
                if not version:
                    self.reporter.failure("Can not found version in file: %s" % item)
                    return False

            old = version.group(0)
            content = content.replace(old, self.__version)

            self.reporter.message("Changing from version %s to %s on file %s" % ( old, self.__version, item))

            f = open(item, 'w')
            f.write(content)
            f.close()

        return True