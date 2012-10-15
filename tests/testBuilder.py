import unittest
from pyhammer.builder import Builder
from pyhammer.reporters.bufferedreporter import MemoryReporter

class testBuilder(unittest.TestCase):
    def test_basic(self):
        b = Builder('sample')
        mr = MemoryReporter()
        b.setReporter(mr)
        b.build()
        self.assertEqual(mr.getText(), "\nSTARTING 'sample' BUILD:\n'sample' BUILD COMPLETED.")





