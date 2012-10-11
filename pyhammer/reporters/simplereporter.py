import datetime
import sys

class ConsoleReporter:
    def __init__(self):
        self.logFile = None
        self.errLogFile = None
        
    def message( self, text, error = False ):
        now = datetime.datetime.now()
        outputMsg = "%s: %s" % ( now.strftime("%d/%m/%Y %H:%M:%S"), text )
        
        if not error:
            print(outputMsg)
        else:
            sys.stderr.write(outputMsg)

    def success( self, text ):
        self.message( "SUCCESS: %s" % text )

    def failure( self, text ):
        self.message( "FAILURE: %s" % text, True )