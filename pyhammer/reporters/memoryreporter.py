class MemoryReporter:
    def __init__( self ):
        self._memory = ""
    def message( self, message, error = False ):
        self._memory += "\n" + message
    def getText( self ):
        return self._memory
