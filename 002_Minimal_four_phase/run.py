import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def setup(self):
        self.log.info("Setup")
        self.addCleanupFunction(self.mycleanup)

    def execute(self):
        self.log.info("Execute")

    def validate(self):
        self.log.info("Validate")
        self.addOutcome(PASSED)

    def mycleanup(self):
        self.log.info("Cleanup")
