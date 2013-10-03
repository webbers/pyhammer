# -*- coding: utf-8 -*-
import re
import codecs
from pyhammer.tasks.taskbase import TaskBase

class ApplyVersionTask(TaskBase):

    def __init__( self, assemblyPath, setupScriptPath, encoding=None, encodingSecond=None):
        super(ApplyVersionTask, self).__init__()
        self.__assemblyPath = assemblyPath
        self.__setupScriptPath = setupScriptPath
        self.__encoding = encoding
        self.__encodingSecond = encodingSecond

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
        f = None
        if not self.__encoding is None:
            f = codecs.open(self.__assemblyPath, 'r', encoding=self.__encoding)
        else:
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

        major = int(version.group(1))
        minor = int(version.group(2))
        revis = int(version.group(3))

        build = None
        if groups == 4:
            build = int(version.group(4))

        if not self.__encodingSecond is None:
            f = codecs.open(item, 'r', encoding=self.__encodingSecond)
        else:
            f = open(item, 'r')
        
        content = f.read()
        f.close()
        
        oldVersion = re.search( '(\d+)\.(\d+)\.(\d+)\.(\d+)', content )
        
        if not oldVersion:
            oldVersion = re.search( '(\d+)\.(\d+)\.(\d+)', content )
            groups = 3
            if not oldVersion:
                self.reporter.failure("Can not found version in file: %s" % item)
                return False

        oldVersion = oldVersion.group(0)

        version = str(major)+"."+str(minor)+"."+str(revis)
        if groups == 4:
            version = str(major)+"."+str(minor)+"."+str(revis)+"."+str(build)


        content = content.replace( oldVersion, version )

        self.reporter.message( "Changing from version %s to %s on file %s" % ( oldVersion, version, item ) )

        try:        
            if not self.__encodingSecond is None:
                f = codecs.open(item, 'w', encoding=self.__encodingSecond)
                f.write(content)
            else:
                f = open(item, 'w')
                print >> f, content
            
        except:
            self.reporter.failure("Can not write file: %s" % item)
            return False
        finally:
            f.close()

        return True