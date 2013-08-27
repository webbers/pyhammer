import unittest
from pyhammer.builder import Builder
from pyhammer.tasks.taskbase import TaskBase

class DummyStep(TaskBase):
    def __init__(self):
        TaskBase().__init__()
    def do(self):
        return True

class testBuilder(unittest.TestCase):
    def test_basic(self):
        Builder.addTask('default', DummyStep())
        Builder.build('default')

    def test_no_default(self):
        Builder.addTask('dummy', DummyStep())
        Builder.build()




