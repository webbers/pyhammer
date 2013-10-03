# -*- coding: utf-8 -*-
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.utils import execProg

class SvnImportTask(TaskBase):
    """Svn Commit Dir Step"""

    def __init__( self, dir, repo ):
        super(SvnImportTask, self).__init__()
        
        self.dir = dir
        self.repo = repo

    def do( self ):
        self.reporter.message( "Svn Import: %s => %s" % ( self.dir, self.repo ) )
        commitMessage = "Commited by Build"
        command = "svn import --non-interactive --trust-server-cert -m \"%s\" \"%s\" \"%s\" " % ( commitMessage, self.dir, self.repo )
        return execProg( command, self.reporter, self.dir ) == 0