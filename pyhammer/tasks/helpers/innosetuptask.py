from pyhammer.tasks.helpers.commandtask import CommandTask

class InnoSetupTask( CommandTask ):
    def __init__( self, scriptPath, outDir ):
        CommandTask().__init__( 'iscc.exe %s /o"%s"' % (scriptPath, outDir) )
