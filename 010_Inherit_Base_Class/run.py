import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

# https://pysys-test.github.io/pysys-test/UserGuide.html
#Alternatively, you can create a trivial BaseTest subclass that instantiates plugins in code (rather than XML) which would allow # code completion (if your editor of choice supports this) but still provide the benefits of the modular composition approach.

class EnvironmentA(BaseTest):

    def setup(self):
        self.log.info("EnvironmentA Setup")
        self.addCleanupFunction(self.mycleanup)

    def execute(self):
        self.log.info("EnvironmentA Execute")

    def validate(self):
        self.log.info("EnvironmentA Validate")
        self.addOutcome(PASSED)

    def mycleanup(self):
        self.log.info("EnvironmentA Cleanup")


class PySysTest(EnvironmentA):

    def setup(self):
        super().setup()
        self.log.info("Setup")
        self.addCleanupFunction(self.mycleanup)

    def execute(self):
        super().execute()
        self.log.info("Execute")

    def validate(self):
        super().validate()
        self.log.info("Validate")
        self.addOutcome(PASSED)

    def mycleanup(self):
        super().mycleanup()
        self.log.info("Cleanup")
