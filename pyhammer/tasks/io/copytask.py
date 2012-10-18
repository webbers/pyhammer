import os
import shutil
from pyhammer.filters.filefilter import FileFilter
from pyhammer.tasks.taskbase import TaskBase

class CopyTask(TaskBase):
    def __init__(self, srcDir, destDir, fileFilter=None):
        super().__init__()
        self.destDir = destDir
        self.srcDir = srcDir
        if fileFilter is None:
            self.fileFilter = FileFilter()
        else:
            self.fileFilter = fileFilter

    def do( self ):
        return self.__copyFileList(self.fileFilter, self.srcDir, self.destDir, self.reporter)

    def __copyFileList(self, fileFilter, srcDir, destDir, reporter):
        files = fileFilter.Filter( srcDir )
        reporter.message( "Copying files: %s => %s" % ( srcDir, destDir ) )
        for fp in files:
            relPath = fp.lower().replace( os.path.realpath( srcDir ).lower(), "" )
            destPath = os.path.realpath( destDir ) + relPath
            reporter.message(fp)

            if not os.path.exists(os.path.dirname(destPath)):
                os.makedirs(os.path.dirname(destPath))

            if not shutil.copyfile(fp, destPath):
                reporter.failure("copying %s to %s" % (fp, destPath))
                return False
        return True
