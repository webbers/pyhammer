import datetime

class ConsoleReporter:
    def __init__(self):
        self.logFile = None
        self.errLogFile = None
        
    def message( self, text, error = False ):
        now = datetime.datetime.now()
        print(text)

    def success( self, text ):
        self.message( "SUCCESS: %s" % text )

    def failure( self, text ):
        self.message( "FAILURE: %s" % text, True )