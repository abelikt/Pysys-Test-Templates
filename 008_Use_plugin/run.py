import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def setup(self):
        self.log.info("Setup")
        self.addCleanupFunction(self.cleanup)

    def execute(self):
        self.log.info("Execute")
        v = self.runner.therunnerplugin.getPythonVersion()
        self.log.info(v)

    def validate(self):
        self.log.info("Validate")
        self.addOutcome(PASSED)

    def cleanup(self):
        self.log.info("Cleanup")
