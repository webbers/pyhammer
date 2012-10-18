import os
from pyhammer.steps.text.incrementversionstep import IncrementVersionStep
from pyhammer.builder import Builder
from pyhammer.filters.pythonfilefilter import PythonFileFilter
from pyhammer.steps.helpers.runcommandstep import RunCommandStep
from pyhammer.steps.io.copyfilteredfilesstep import CopyFilteredFilesStep
from pyhammer.steps.io.deltreestep import DelTreeStep
from pyhammer.steps.svn.svndeletestep import SvnDeleteStep
from pyhammer.steps.svn.svnimportdirstep import SvnImportDirStep

#-Paths-----------------------------------------------------------------------------------------------------------------
rootDir = os.path.join( os.getcwd(), '..' )
pubDir = os.path.join( os.getcwd(), '../pub' )
tempDir = os.path.join( os.getcwd(), '../temp' )
srcDir = os.path.join( os.getcwd(), '../pyhammer' )
versionFile = os.path.join( os.getcwd(), '../setup.py' )
repoUrl = 'http://cronos:9090/gasrd/Web/pub/pyhammer/trunk'

#-Steps-----------------------------------------------------------------------------------------------------------------
Builder.addStep( "unittests", RunCommandStep('python -m unittest discover tests', rootDir) )
Builder.addStep( "del-pub", DelTreeStep( pubDir ) )
Builder.addStep( "copyfiles", CopyFilteredFilesStep( PythonFileFilter(), srcDir, pubDir ) )
Builder.addStep( "svndelete", SvnDeleteStep(repoUrl))
Builder.addStep( "svnimport", SvnImportDirStep( pubDir, repoUrl ) )
Builder.addStep( "pip-upload", RunCommandStep( 'python setup.py sdist upload', rootDir ) )
Builder.addStep( "increment-rev", IncrementVersionStep(versionFile, "revision", 3))
Builder.addStep( "increment-min", IncrementVersionStep(versionFile, "minor", 3))

#-Root steps------------------------------------------------------------------------------------------------------------
Builder.addStep( "ps", "unittests")
Builder.addStep( "ci", "unittests del-pub copyfiles svndelete svnimport del-pub")
Builder.addStep( "publish-rev", "unittests increment-rev pip-upload")
Builder.addStep( "publish-min", "unittests increment-min pip-upload")

Builder.runBuild()