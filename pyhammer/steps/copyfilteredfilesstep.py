from pyhammer.steps.copyfilesstep import CopyFilesStep

class CopyFilteredFilesStep(CopyFilesStep):
    """Copy Filtered Files Step"""
    
    def __init__( self, fileFilter, srcDir, destDir, recursive = True ):
        CopyFilesStep.__init__( self, None, srcDir, destDir )
        self.srcDir = srcDir
        self.fileFilter = fileFilter
        self.recursive = recursive
        
    def do( self ):
        filteredFiles = self.fileFilter.Filter( self.srcDir, self.recursive )
        CopyFilesStep.setFiles( self, filteredFiles )
        return CopyFilesStep.do(self)