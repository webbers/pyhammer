# -*- coding: utf-8 -*-
from pyhammer.filters.filefilter import FileFilter

class JarFileFilter(FileFilter):
    def __init__( self ):
        FileFilter.__init__( self, include = ['*.jar'])
