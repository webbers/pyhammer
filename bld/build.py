import os
import sys

rootDir = os.path.join( os.getcwd(), '..' )
sys.path.append(rootDir)


from pyhammer.builder import Builder
from pyhammer.filters.pythonfilefilter import PythonFileFilter
from pyhammer.steps.helper.runcommandstep import RunCommandStep
from pyhammer.steps.io.copyfilteredfilesstep import CopyFilteredFilesStep
from pyhammer.steps.io.deltreestep import DelTreeStep
from pyhammer.steps.svn.svndeletestep import SvnDeleteStep
from pyhammer.steps.svn.svnimportdirstep import SvnImportDirStep

pubDir = os.path.join( os.getcwd(), '../pub' )
tempDir = os.path.join( os.getcwd(), '../temp' )
srcDir = os.path.join( os.getcwd(), '../pyhammer' )
repoUrl = 'http://cronos:9090/gasrd/Web/pub/pyhammer/trunk'

Builder.addStep( "unittests", RunCommandStep('python -m unittest discover tests', rootDir) )
Builder.addStep( "deltree", DelTreeStep( pubDir ) )
Builder.addStep( "copyfiles", CopyFilteredFilesStep( PythonFileFilter(), srcDir, pubDir ) )
Builder.addStep( "svndelete", SvnDeleteStep(repoUrl))
Builder.addStep( "svnimport", SvnImportDirStep( pubDir, repoUrl ) )

Builder.addStep( "ps", "unittests deltree copyfiles")
Builder.addStep( "ci", "unittests deltree copyfiles svndelete svnimport")

Builder.runBuild()