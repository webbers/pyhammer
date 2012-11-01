class TaskBase:
    def __init__( self ):
        self.reporter = None
        self.data = None
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

    def setFailureStep( self, failureStep ):
        self.failureStep = failureStep