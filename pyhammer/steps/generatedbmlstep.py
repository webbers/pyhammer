import os
from pyhammer.steps.abstractstep import AbstractStep
from pyhammer.utils import ExecProg

sqlMetalPath = os.path.join( os.path.dirname( __file__ ), "../../res/tools/sqlMetal/SqlMetal.exe" )

#---------------------------------------------------------------------
class GenerateDbmlStep(AbstractStep):
    """SqlMetal Step"""

    def __init__( self, server, database, user, password, namespace, context, outputFile ):
        AbstractStep.__init__( self, "Generate Dbml" )
        self.server = server
        self.database = database
        self.user = user
        self.password = password
        self.namespace = namespace
        self.context = context
        self.outputFile = outputFile

    def do( self ):
        self.reporter.message("generating dbml file in %s" % (self.outputFile))
        commandLine = '/pluralize /server:' + self.server + ' /database:' + self.database + ' /user:' + self.user + ' /password:' + self.password + ' /dbml:"' + self.outputFile + '" /namespace:' + self.namespace + ' /context:' + self.context
        return ExecProg( '"' + sqlMetalPath + '" ' + commandLine, self.reporter ) == 0