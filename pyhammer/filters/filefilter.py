# -*- coding: utf-8 -*-
import fnmatch
from pyhammer.utils import walkDir


class FileFilter:
    __include = []
    __exclude = []

    def __init__( self, include = None, exclude = None ):
        self.__include = include
        self.__exclude = exclude

    def Filter( self, dir, recurvise = True ):
        files = walkDir( dir, recurvise )
        filteredFiles = []
        for filePath in files:
            if self.__isValidFile( filePath, dir ):
                filteredFiles.append( filePath )
        return filteredFiles

    def __isValidFile( self, filePath, baseDir ):
        filePath = filePath.lower().replace( baseDir.lower(), '' )

        valid = True

        if self.__include is not None:
            for pattern in self.__include:
                valid = fnmatch.fnmatch( filePath, pattern )
                if valid:
                    break

        if self.__exclude is not None:
            for pattern in self.__exclude:
                valid = not fnmatch.fnmatch( filePath, pattern )
                if not valid:
                    break

        return valid