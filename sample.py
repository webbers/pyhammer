import os
import sys
from pyhammer.builder import Builder
from pyhammer.filters.pythonfilefilter import PythonFileFilter
from pyhammer.steps.helpers.runcommandstep import RunCommandStep
from pyhammer.steps.io.copyfilteredfilesstep import CopyFilteredFilesStep
from pyhammer.steps.io.deltreestep import DelTreeStep

rootDir = os.path.join( os.getcwd(), '' )
pubDir = os.path.join( os.getcwd(), 'pub' )
tempDir = os.path.join( os.getcwd(), 'temp' )
srcDir = os.path.join( os.getcwd(), 'pyhammer' )
repoUrl = 'http://cronos:9090/gasrd/Web/pub/pyhammer/trunk'

Builder.addStep( "unittests", RunCommandStep('python -m unittest discover tests', rootDir) )
Builder.addStep( "deltree", DelTreeStep( pubDir ) )
Builder.addStep( "copyfiles", CopyFilteredFilesStep( PythonFileFilter(), srcDir, pubDir ) )

Builder.addStep( "ps", "unittests deltree")
Builder.addStep( "ci", "unittests deltree copyfiles")

Builder.build(sys.argv[1])

