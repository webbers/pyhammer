from pyhammer.tasks.taskbase import TaskBase

class FileReplaceTask(TaskBase):
    """File Replace Step"""

    def __init__( self, filename ):
        super().__init__()
        self.filename = filename
        self.__sentences = []
    
    def addSentence( self, find, replace ):
        self.__sentences.append( [ find, replace] )
    
    def do( self ):
        f = open( self.filename, 'r' )
        content = f.read()
        f.close()

        for i, sentence in enumerate( self.__sentences ):
            oldContent = content
            content = content.replace( sentence[0], sentence[1] )
            if oldContent == content:
                self.reporter.failure( 'Nao foi possivel encontrar a string' + sentence[0] )
                return 0

        f = open( self.filename, 'w' )
        f.write( content )
        f.close()
        return True