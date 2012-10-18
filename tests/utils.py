from pyhammer.tasks.taskbase import TaskBase

class ApproveStep(TaskBase):
    def __init__(self):
        super().__init__()
    def do( self ):
        return True

class ReportStep(TaskBase):
    def __init__(self):
        super().__init__()
    def do( self ):
        self.reporter.message('ok')
        return True