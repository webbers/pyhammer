import unittest
from pyhammer.builder import Builder
from pyhammer.reporters.memoryreporter import MemoryReporter

class testBuilder(unittest.TestCase):
    def test_basic(self):
        b = Builder('sample')
        mr = MemoryReporter()
        b.setReporter(mr)
        b.build()




