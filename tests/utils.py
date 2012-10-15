from pyhammer.steps.abstractstep import AbstractStep

class ApproveStep(AbstractStep):
    def __init__(self):
        AbstractStep.__init__(self, "ApproveStep")
    def do( self ):
        return True

class ReportStep(AbstractStep):
    def __init__(self):
        AbstractStep.__init__(self, "ReportStep")
    def do( self ):
        self.reporter.message('ok')
        return True