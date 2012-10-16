import unittest
from pyhammer.builder import Builder
from pyhammer.steps.abstractstep import AbstractStep

class DummyStep(AbstractStep):
    def __init__(self):
        AbstractStep.__init__(self, "bla")
    def do(self):
        return True

class testBuilder(unittest.TestCase):
    '''def test_basic(self):
        Builder.addStep('default', DummyStep())
        Builder.build('default')'''

    def test_no_default(self):
        Builder.addStep('dummy', DummyStep())
        Builder.build()




