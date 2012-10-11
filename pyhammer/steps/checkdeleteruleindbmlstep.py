import re
from pyhammer.steps.abstractstep import AbstractStep

class CheckDeleteRuleInDbmlStep( AbstractStep ):
    def __init__( self, dbml ):
        AbstractStep.__init__( self, "Check Delete Rule In Dbml" )
        self.__dbml = dbml

    def build( self ):
        f = open( self.__dbml, 'r' )
        content = f.read()
        f.close()
        matches = re.findall('DeleteRule=\"CASCADE\"', content )
        if( len(matches) ):
            self.reporter.failure( str(len(matches)) + " DeleteRule=\"CASCADE\" no dbml" )
            return 0
        return 1