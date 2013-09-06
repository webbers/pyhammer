import sys
import traceback
from pyhammer.reporters.consolereporter import ConsoleReporter
from pyhammer.tasks.taskbase import TaskBase

class MultiTask(TaskBase):

    def __init__( self, text ):
        super(MultiTask, self).__init__()
        self.text = text

    def do( self ):
        Builder.keys = Builder.steps.keys()
        if not isinstance(self.text, list):
            items = self.text.split(" ")
        else:
            items = self.text

        for i, stepName in enumerate( items ):
            if not Builder.build(stepName):
                return False
        return True

class Builder(TaskBase):
    __postBuildStep = None
    __buildResult = True
    __errorCount = 0
    __keys = []
    steps = {}
    reporter = ConsoleReporter()

    @staticmethod
    def runBuild(step = None):
        if step is None and len(sys.argv) > 1:
            step =sys.argv[1]
        if step is None:
            step = 'deafult'
        sys.exit(Builder.build(step)==0)

    @staticmethod
    def build( name = "default" ):
        steps = {}
        Builder.keys = Builder.steps.keys()
		
        if any(name in k for k in Builder.keys):
            steps[name] = Builder.steps[name]
            
        if len(steps) == 0:
            Builder.reporter.failure("Step \"%s\" not found" % name)
            return 0

        for i, stepName in enumerate( steps ):
            step = steps[stepName]
            stepType = step.__class__.__name__
            Builder.reporter.message( "" )
            Builder.reporter.message( "Running '%s (%s)'" % ( stepName, stepType ) )

            try:
                result = step.build()
            except Exception as e:
                Builder.reporter.failure(traceback.format_exc())
                Builder.reporter.failure(e)
                result = False

            if not result:
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
    def addTask( name, step, ignoreFail = False ):
        if not isinstance(step, str) and not isinstance(step, list):
            step.setReporter( Builder.reporter )
            step.ignoreFail = ignoreFail
        else:
            step = MultiTask(step)
        Builder.steps[name] = step

    @staticmethod
    def getErrorCount( self ):
        return self.__errorCount
