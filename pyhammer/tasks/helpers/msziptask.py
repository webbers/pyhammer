import os
from os.path import curdir
import zipfile
import shutil
from pyhammer.tasks.taskbase import TaskBase
from pyhammer.filters.filefilter import FileFilter
from pyhammer.utils import execProg

class ZipTask(TaskBase):
    __zf = []
    __zipName = []
    __dirName = []
    __mode = []

    def __init__(self, zipname, dir, mode  ="wb", exclude = None):
        super(ZipTask, self).__init__()
        self.__mode = mode
        self.__dirName = dir
        self.__zipName = zipname
        self.__exclude = exclude
        self.__zf = zipfile.ZipFile(self.__zipName, 'w', zipfile.ZIP_DEFLATED)
        self.__fileFilter = FileFilter(exclude=self.__exclude).Filter(self.__dirName)

    def do(self):
        rootlen = len(self.__dirName) + 1

        for item in self.__fileFilter:
            fn = item
            self.__zf.write(fn, fn[rootlen:])

        return True