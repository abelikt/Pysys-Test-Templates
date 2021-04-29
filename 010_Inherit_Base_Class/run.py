import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

# https://pysys-test.github.io/pysys-test/UserGuide.html
#Alternatively, you can create a trivial BaseTest subclass that instantiates plugins in code (rather than XML) which would allow # code completion (if your editor of choice supports this) but still provide the benefits of the modular composition approach.

class EnvironmentA(BaseTest):

    def setup(self):
        self.log.info("EnvironmentA Setup")
        self.addCleanupFunction(self.mycleanup_env_a)

    def execute(self):
        self.log.info("EnvironmentA Execute")

    def validate(self):
        self.log.info("EnvironmentA Validate")
        self.addOutcome(PASSED)


    def mycleanup_env_a(self):
        """Select a different name here to avoid that it is overriden in subclasses
        """
        self.log.info("EnvironmentA Cleanup")


class PySysTest(EnvironmentA):

    def setup(self):
        super().setup()
        self.log.info("Setup Test")
        self.addCleanupFunction(self.mycleanup)

    def execute(self):
        super().execute()
        self.log.info("Execute Test")

    def validate(self):
        super().validate()
        self.log.info("Validate Test")
        self.addOutcome(PASSED)

    def mycleanup(self):
        # Don't call the parent cleanup
        # super().mycleanup()
        self.log.info("Cleanup Test")
