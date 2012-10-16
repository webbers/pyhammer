import sys
from pyhammer.reporters.consolereporter import ConsoleReporter
from pyhammer.steps.abstractstep import AbstractStep

class MultiTextStep(AbstractStep):

    def __init__( self, text ):
        AbstractStep.__init__( self, "Multi Step" )
        self.text = text

    def do( self ):
        Builder.keys = Builder.steps.keys()

        items = self.text.split(" ")

        for i, stepName in enumerate( items ):
            if not Builder.build(stepName):
                return False
        return True

class Builder(AbstractStep):
    __postBuildStep = None
    __buildResult = True
    __errorCount = 0
    __keys = []
    steps = {}
    reporter = ConsoleReporter()

    @staticmethod
    def runBuild():
        step = 'default'
        if len(sys.argv) > 1:
            step =sys.argv[1]
        sys.exit(Builder.build(step)==0)

    @staticmethod
    def build( name = "default" ):
        steps = {}
        Builder.keys = Builder.steps.keys()

        if name == "default":
            for i, stepName in enumerate( Builder.steps ):
                if not isinstance(Builder.steps[stepName], MultiTextStep):
                    steps[stepName] = Builder.steps[stepName]
        else:
            if any(name in k for k in Builder.keys):
                steps[name] = Builder.steps[name]

        if len(steps) == 0:
            Builder.reporter.failure("Step \"%s\" not found" % name)
            return 0

        for i, stepName in enumerate( steps ):
            step = steps[stepName]
            stepType = step.__class__.__name__
            Builder.reporter.message( "Running '%s (%s)' step (%d of %d):" % ( stepName, stepType, i+1, len( steps ) ) )

            if step.build():
                Builder.reporter.success( "STEP '%s (%s)' COMPLETED" % ( stepName, stepType ) )
            else:
                Builder.reporter.failure( "STEP '%s (%s)' FAILED"% ( stepName, stepType ) )
                Builder.__buildResult = False
                Builder.__errorCount += 1
                if not step.ignoreFail:
                    Builder.reporter.failure( "BUILD FAILED" )
                    return False
        
        if Builder.__postBuildStep:
            if Builder.__buildResult:
                Builder.__postBuildStep.build()
        return Builder.__buildResult

    @staticmethod
    def addStep( name, step, ignoreFail = False ):
        if not isinstance(step, str):
            step.setReporter( Builder.reporter )
            step.ignoreFail = ignoreFail
        else:
            step = MultiTextStep(step)
        Builder.steps[name] = step

    @staticmethod
    def getErrorCount( self ):
        return self.__errorCount
