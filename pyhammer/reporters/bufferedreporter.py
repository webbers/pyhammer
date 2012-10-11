class BufferedReporter:
    def __init__( self ):
        self.__buffer = "";
    def message( self, message ):
        self.__buffer += "\n" + message
    def getBuffer( self ):
        return self.__buffer
