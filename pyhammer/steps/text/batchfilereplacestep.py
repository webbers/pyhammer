from pyhammer.steps.abstractstep import AbstractStep

class BatchFileReplaceStep(AbstractStep):
    """File Replace Step"""

    def __init__( self, filename ):
        AbstractStep.__init__( self, "Batch File Replace" )
        self.filename = filename
        self.__sentences = []
    
    def addSentence( self, find, replace ):
        self.__sentences.append( [ find, replace] )
    
    def do( self ):
        try:
            f = open( self.filename, 'r' )
            content = f.read()
            f.close()
            
            for i, sentence in enumerate( self.__sentences ):
                oldcontent = content
                content = content.replace( sentence[0], sentence[1] )
                if oldcontent == content:
                    self.reporter.failure( 'Nao foi possivel encontrar a string' + sentence[0] )
                    return 0
                
            f = open( self.filename, 'w' )
            f.write( content )
            f.close()
            
            return 1
        except:
            return 0