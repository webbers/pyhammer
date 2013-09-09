# -*- coding: utf-8 -*-
from pyhammer.filters.filefilter import FileFilter

class PythonFileFilter(FileFilter):
    def __init__( self ):
        FileFilter.__init__( self, exclude = ['*\\.svn\\*', '*\\testdata\\*', '*\\install\\*', '*\\docs\\*',
                                              '*\\pub\\*', '*\\libs\\*', '*\\bld\\*', 'test_*', '*_publish.py',
                                              '*_test.py', '*.pyc', '*.wpr'] )
