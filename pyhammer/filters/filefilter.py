import os
import fnmatch
from pyhammer.utils import WalkDir


class FileFilter:
    AllPtn = []
    FileNamePtn = []
    ExtPtn = []

    def __init__( self, AllPtn, FileNamePtn, ExtPtn, AllPtnFlag = False, FileNamePtnFlag = False, ExtPtnFlag = False ):
        #Flag True para inclusao e False para exclusao
        self.AllPtn = AllPtn
        self.FileNamePtn = FileNamePtn
        self.ExtPtn = ExtPtn
        self.AllPtnFlag = AllPtnFlag
        self.FileNamePtnFlag = FileNamePtnFlag
        self.ExtPtnFlag = ExtPtnFlag
        
    def Filter( self, Dir, Recurvise = True ):
        Files = WalkDir( Dir, Recurvise )
        FilteredFiles = []
        for fp in Files:
            if self.IsValidFile( fp, Dir ):
                FilteredFiles.append( fp )
        return FilteredFiles
    
    def IsValidFile( self, fp, BaseDir ):
        fp = fp.lower().replace( BaseDir.lower(), '' )
        fn = os.path.basename( fp )
        ext = os.path.splitext( fp )[1].lower()
        
        # Retira por path completo (jah sem o BaseDir)
        for ptn in self.AllPtn:
            if fnmatch.fnmatch( fp, ptn ):
                if self.AllPtnFlag:
                    return True
                return False
            
        # Retira por filename
        for ptn in self.FileNamePtn:
            if fnmatch.fnmatch( fn, ptn ):
                if self.FileNamePtnFlag:
                    return True
                return False
            
        # Retira por extensao
        for ptn in self.ExtPtn:
            if fnmatch.fnmatch( ext, ptn ):
                if self.ExtPtnFlag:
                    return True
                return False
            
        if not self.AllPtn:
            return False
        
        if not self.FileNamePtn:
            return False
        
        if not self.ExtPtn:
            return False
        
        return True