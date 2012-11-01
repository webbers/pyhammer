import os
import shutil
import subprocess
import fnmatch
import sys

def walkDir( root, recursive=0, pattern='*', return_folders=0 ):
    # initialize
    result = []

    # must have at least root folder
    try:
        names = os.listdir(root)
    except os.error:
        return result

    # expand pattern
    pattern = pattern or '*'
    pat_list = pattern.split(';')

    # check each file
    for name in names:
        fullname = os.path.normpath(os.path.join(root, name))

        # grab if it matches our pattern and entry type
        for pat in pat_list:
            if fnmatch.fnmatch(name, pat):
                if os.path.isfile(fullname) or (return_folders and os.path.isdir(fullname)):
                    result.append(fullname)
                continue

        # recursively scan other folders, appending results
        if recursive:
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                result += walkDir(fullname, recursive, pattern, return_folders)

    return result
    
def execProg( FilePath, reporter, cwd = None ):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen( FilePath, cwd=cwd, stdout=subprocess.PIPE, startupinfo=startupinfo )
    lines = process.stdout.readlines()
    for line in lines:
        reporter.message( line.decode('ISO 8859-1').replace('\r\n', '') )
    return process.wait()

def execProg2( FilePath, cwd = None ):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen( FilePath, cwd=cwd, stdout=subprocess.PIPE, startupinfo=startupinfo )
    items = []
    lines = process.stdout.readlines()
    for line in lines:
        items.append(line.decode('ISO 8859-1').replace('\r\n', ''))
    return items

def moveFile(filename1, filename2):
    if not os.path.exists(os.path.dirname(filename2)):
        os.makedirs(os.path.dirname(filename2))
    shutil.move( filename1, os.path.dirname(filename2) )
    if os.path.isfile (filename2): return True
    return False

def svnList(path, reporter):
    items = execProg2('svn list ' + path)

    if isList(items):
        return items

    reporter.failure('Error reading path: ' + path)
    return items

def isList(items):
    return isinstance(items, (list, tuple))

def execfile(file):
    with open(file, "r") as fh:
        exec(fh.read()+"\n")