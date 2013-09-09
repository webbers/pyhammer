# -*- coding: utf-8 -*-
import os
import sys
import argparse
from pyhammer.tasks.text.incrementversiontask import IncrementVersionTask
from pyhammer.builder import Builder
from pyhammer.filters.pythonfilefilter import PythonFileFilter
from pyhammer.tasks.helpers.commandtask import CommandTask
from pyhammer.tasks.io.copytask import CopyTask
from pyhammer.tasks.io.deletetask import DeleteTask
from pyhammer.tasks.svn.svndeletetask import SvnDeleteTask
from pyhammer.tasks.svn.svnimporttask import SvnImportTask

#-Argument-Parser-------------------------------------------------------------------------------------------------------
parser = argparse.ArgumentParser()
parser.add_argument( '--build', type=str, required=True )
args = parser.parse_args()

#-Paths-----------------------------------------------------------------------------------------------------------------
rootDir = os.path.join( os.getcwd(), '..' )
pubDir = os.path.join( os.getcwd(), '../pub' )
tempDir = os.path.join( os.getcwd(), '../temp' )
srcDir = os.path.join( os.getcwd(), '../pyhammer' )
versionFile = os.path.join( os.getcwd(), '../setup.py' )
repoUrl = 'https://cronos/svn/Web/pub/pyhammer/trunk'

#-Tasks-----------------------------------------------------------------------------------------------------------------
Builder.addTask( "unittests", CommandTask('python -m unittest discover tests', rootDir) )
Builder.addTask( "del-pub", DeleteTask( pubDir ) )
Builder.addTask( "copyfiles", CopyTask( srcDir, pubDir, PythonFileFilter() ) )
Builder.addTask( "svndelete", SvnDeleteTask(repoUrl))
Builder.addTask( "svnimport", SvnImportTask( pubDir, repoUrl ) )
Builder.addTask( "pip-upload", CommandTask( 'python setup.py sdist upload', rootDir ) )
Builder.addTask( "increment-rev", IncrementVersionTask(versionFile, "revision"))
Builder.addTask( "increment-min", IncrementVersionTask(versionFile, "minor"))

#-Root tasks------------------------------------------------------------------------------------------------------------
Builder.addTask( 'ps',              [ 'unittests' ] )
Builder.addTask( 'ci',              [ 'del-pub', 'copyfiles', 'svndelete', 'svnimport', 'del-pub' ] )
Builder.addTask( 'publish-rev',     [ 'unittests', 'increment-rev', 'pip-upload' ] )
Builder.addTask( 'publish-min',     [ 'unittests', 'increment-min', 'pip-upload' ] )

Builder.runBuild(args.build)