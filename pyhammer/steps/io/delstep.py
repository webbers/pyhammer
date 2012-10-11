import os
from pyhammer.steps.abstractstep import AbstractStep

class DelStep(AbstractStep):
    """Del Step"""

    def __init__( self, srcPath ):
        AbstractStep.__init__(self, "Del")
        self.srcPath = srcPath
        
    def do( self ):
        try:
            os.system( 'del "' +  self.srcPath  + '"' )
        except:
            self.reporter.message( 'del falhou "' +  self.srcPath  + '"'  )
        pass
        return True
        