from pyhammer.reporters.simplereporter import ConsoleReporter
from pyhammer.steps.abstractstep import AbstractStep

class Builder(AbstractStep):
    def __init__( self, name = "", reporter = None ):
        AbstractStep.__init__( self, name )
        self.__postBuildStep = None
        self.__buildResult = True
        self.__errorCount = 0
        self.__steps = []
        if reporter:
            self.reporter = reporter
        else:
            self.reporter = ConsoleReporter()

    def build( self ):
        self.reporter.message( "STARTING '%s' BUILD:" % self.name )
        for i, step in enumerate( self.__steps ):
            self.reporter.message( "RUNNING STEP '%s' (step %d of %d):" % ( step.name, i+1, len( self.__steps ) ) )

            if step.build():
                self.reporter.success( "STEP '%s' COMPLETED" % step.name )
                self.reporter.message( "------------------------------------------------------------" )
            else:
                self.reporter.failure( "STEP '%s' FAILED" % step.name )
                self.reporter.message( "------------------------------------------------------------" )
                self.__buildResult = False
                self.__errorCount += 1
                if not step.ignoreFail:
                    self.reporter.failure( "'%s' BUILD FAILED." % self.name )
                    return False
        
        if self.__postBuildStep:
            if self.__buildResult:
                self.__postBuildStep.build()
        
        self.reporter.message( "'%s' BUILD COMPLETED." % self.name, not self.__buildResult )
        
        return self.__buildResult

    def setPostBuildStep( self, postBuildStep ):
        postBuildStep.setReporter( self.reporter )
        if self.data and not postBuildStep.getData():
            postBuildStep.setData( self.data )
        self.__postBuildStep = postBuildStep

    def addStep( self, step, ignoreFail = False ):
        step.setReporter( self.reporter )
        step.ignoreFail = ignoreFail
        if self.data and not step.getData():
            step.setData( self.data )
        self.__steps.append( step )
        
    def setData( self, data ):
        for step in self.__steps:
            step.setData( data )
        if self.__postBuildStep:
            self.__postBuildStep.setData( data )
        self.data = data

    def getErrorCount( self ):
        return self.__errorCount
