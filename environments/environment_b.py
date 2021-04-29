import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

class EnvironmentB(BaseTest):

    def setup(self):
        self.log.info("EnvironmentB Setup")
        self.addCleanupFunction(self.mycleanup_env_b)

    def execute(self):
        self.log.info("EnvironmentB Execute")

    def validate(self):
        self.log.info("EnvironmentB Validate")
        self.addOutcome(PASSED)

    def mycleanup_env_b(self):
        self.log.info("EnvironmentB Cleanup")

