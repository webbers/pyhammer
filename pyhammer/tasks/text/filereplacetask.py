from pyhammer.tasks.taskbase import TaskBase

class FileReplaceTask(TaskBase):
    def __init__( self, filename ):
        super().__init__()
        self.__filename = filename
        self.__sentences = []
    
    def addSentence( self, find, replace ):
        self.__sentences.append( [ find, replace] )
    
    def do( self ):
        f = open( self.__filename, 'r' )
        content = f.read()
        f.close()

        for i, sentence in enumerate( self.__sentences ):
            oldContent = content
            content = content.replace( sentence[0], sentence[1] )
            if oldContent == content:
                self.reporter.failure( 'Nao foi possivel encontrar a string' + sentence[0] )
                return 0

        f = open( self.__filename, 'w' )
        f.write( content )
        f.close()
        return True