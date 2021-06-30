import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

# See
# https://pysys-test.github.io/pysys-test/UserGuide.html#running-tests-in-multiple-modes


# Code intended for a Plugin:
#class MyTestPlugin(object):
    #def setup(self, testObj):
        ## Unpack and validate mode
        #testObj.databaseMode, testObj.browserMode = testObj.mode.split('_')
        #assert testObj.browserMode in ['Chrome', 'Firefox'], testObj.browserMode
        #
        ## This is a convenient pattern for specifying the method or class
        ## constructor to call for each mode, and to get an exception if an
        ## invalid mode is specified
        #dbHelperFactory = {
        #        'MockDatabase': MockDB,
        #        'MyDatabase2.0': lambda: self.startMyDatabase('2.0')
        #}[testObj.databaseMode]
        #
        ## Call the supplied method to start/configure the database
        #testObj.db = dbHelperFactory()


class PySysTest(BaseTest):
    def setup(self):#, testObj):
        self.log.info("Setup")
        self.addCleanupFunction(self.mycleanup)

        self.log.info(self.mode)

        # Port the code from the Plugin to the test:

        databaseMode, browserMode = self.mode.split('_')
        assert browserMode in ['Chrome', 'Firefox']

        self.log.info( 'databaseMode : ' + str( databaseMode))
        self.log.info( 'browserMode: ' + str( browserMode))

        dbHelperFactory = {
                'MockDatabase': lambda: self.log.info('MockDB'),
                'MyDatabase2.0': lambda: self.log.info('self.startMyDatabase(\'2.0\')')
        }[databaseMode]

        # Call the supplied method to start/configure the database
        db = dbHelperFactory()

        self.log.info(db)





    def execute(self):
        self.log.info("Execute")

    def validate(self):
        self.log.info("Validate")
        self.addOutcome(PASSED)

    def mycleanup(self):
        self.log.info("Cleanup")
