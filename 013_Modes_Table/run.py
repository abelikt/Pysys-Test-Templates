import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

# See
# https://pysys-test.github.io/pysys-test/UserGuide.html#running-tests-in-multiple-modes

# run
#  pysys.py run -v DEBUG --mode ALL

class PySysTest(BaseTest):
    def setup(self):#, testObj):
        self.log.info("Setup")
        self.addCleanupFunction(self.mycleanup)

        self.log.info(self.mode)

        parameters = self.mode.split('_')
        assert(len(parameters) == 4)
        self.log.info(parameters)

    def execute(self):
        self.log.info("Execute")

    def validate(self):
        self.log.info("Validate")
        self.addOutcome(PASSED)

    def mycleanup(self):
        self.log.info("Cleanup")
