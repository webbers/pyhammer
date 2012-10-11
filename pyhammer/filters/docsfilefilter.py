from pyhammer.filters.filefilter import FileFilter

class DocsFileFilter(FileFilter):
    def __init__( self ):
        FileFilter.__init__( self, [], [], ['.doc','.pdf'], True )
