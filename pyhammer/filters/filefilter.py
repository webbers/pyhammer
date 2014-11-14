# -*- coding: utf-8 -*-
import fnmatch
from pyhammer.utils import walkDir


class FileFilter:
    __include = []
    __exclude = []

    def __init__( self, include = None, exclude = None, folderPattern = None ):
        self.__include = include
        self.__exclude = exclude
        self.__folderPattern = folderPattern

    def Filter( self, dir, recurvise = True):
        files = walkDir( dir, recurvise, self.__folderPattern )
        filteredFiles = []
        for filePath in files:
            if self.__isValidFile( filePath, dir ):
                filteredFiles.append( filePath )
        return filteredFiles

    def __isValidFile( self, filePath, baseDir ):
        filePath = filePath.lower().replace( baseDir.lower(), '' )

        valid = True

        if self.__exclude is not None:
            for pattern in self.__exclude:
                valid = fnmatch.fnmatch( filePath, pattern )
                if valid:
                    return False
                    break

        if self.__include is not None:
            for pattern in self.__include:
                valid = fnmatch.fnmatch( filePath, pattern )
                if valid:
                    return True
                    break

        return valid