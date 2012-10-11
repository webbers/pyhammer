import os
import shutil

__author__ = 'afonso.oliveira'
import subprocess

def WalkDir( root, recurse=0, pattern='*', return_folders=0 ):
    import fnmatch, os, string

    # initialize
    result = []

    # must have at least root folder
    try:
        names = os.listdir(root)
    except os.error:
        return result

    # expand pattern
    pattern = pattern or '*'
    pat_list = string.splitfields( pattern , ';' )

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
        if recurse:
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                result = result + WalkDir( fullname, recurse, pattern, return_folders )

    return result
    
def ExecProg( FilePath, reporter, cwd = None ): 
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen( FilePath, cwd=cwd, stdout=subprocess.PIPE, startupinfo=startupinfo )
    lines = process.stdout.readlines()
    for line in lines:
        reporter.message( line.replace( "\r\n", "" ) )
    return process.wait()

def copyfile(filename1, filename2):
    if not os.path.exists(os.path.dirname(filename2)):
        os.makedirs(os.path.dirname(filename2))
    shutil.copy( filename1, os.path.dirname(filename2) )
    if os.path.isfile (filename2): return True
    return False

def createDir(path):
    AbsPath = os.path.abspath( path )
    if os.path.exists( AbsPath ):
        return False

    if os.name == "nt":
        cmd = """mkdir /S /Q "%s" """ % AbsPath
    else:
        cmd = """md -rf "%s" """ % AbsPath

    os.system( cmd )
    return ( os.path.exists( AbsPath ) )

def removeDir(path):
    AbsPath = os.path.abspath( path )
    if not os.path.exists( AbsPath ):
        return False

    if os.name == "nt":
        cmd = """rmdir /S /Q "%s" """ % AbsPath
    else:
        cmd = """rm -rf "%s" """ % AbsPath

    os.system( cmd )
    return not ( os.path.exists( AbsPath ) )

def movefile(filename1, filename2):
    if not os.path.exists(os.path.dirname(filename2)):
        os.makedirs(os.path.dirname(filename2))
    shutil.move( filename1, os.path.dirname(filename2) )
    if os.path.isfile (filename2): return True
    return False

def svnList(path, reporter):
    list = ExecProg('svn list ' + path, reporter)
    if list == -1:
        print('Erro ao ler o caminho: ' + path)
        return []
    return list