import os
import sys
from pyhammer.builder import Builder
from pyhammer.filters.pythonfilefilter import PythonFileFilter
from pyhammer.steps.helper.runcommandstep import RunCommandStep
from pyhammer.steps.io.copyfilteredfilesstep import CopyFilteredFilesStep
from pyhammer.steps.io.deltreestep import DelTreeStep
from pyhammer.steps.svn.svndeletestep import SvnDeleteStep
from pyhammer.steps.svn.svnimportdirstep import SvnImportDirStep

rootDir = os.path.join( os.getcwd(), '..' )
pubDir = os.path.join( os.getcwd(), '../pub' )
tempDir = os.path.join( os.getcwd(), '../temp' )
srcDir = os.path.join( os.getcwd(), '../pyhammer' )
repoUrl = 'http://cronos:9090/gasrd/Web/pub/pyhammer/trunk'

bp = Builder( "PyHammer Build" )

bp.addStep( RunCommandStep('python -m unittest discover tests', rootDir))
bp.addStep( DelTreeStep( pubDir ) )
bp.addStep( CopyFilteredFilesStep( PythonFileFilter(), srcDir, pubDir ) )
bp.addStep( SvnDeleteStep(repoUrl))
bp.addStep( SvnImportDirStep( pubDir, repoUrl ) )

if not bp.build():
    sys.exit(1)
    