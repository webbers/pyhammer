class AbstractStep:
    """Abstract Step"""
    
    def __init__( self, name ):
        self.reporter = None
        self.data = None
        self.name = name
        self.ignoreFail = False
        self.failureStep = None

    def do( self ):
        pass
    
    def build( self ):
        if not self.do():
            if self.failureStep is not None:
                self.failureStep.build()
            return False
        return True
    
    def setReporter( self, reporter ):
        self.reporter = reporter
        if self.failureStep is not None:
            self.failureStep.setReporter( reporter )
        
    def setData( self, data ):
        self.data = data
        if self.failureStep is not None:
            self.failureStep.setData( data )
    
    def setFailureStep( self, failureStep ):
        self.failureStep = failureStep