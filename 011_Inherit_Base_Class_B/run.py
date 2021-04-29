import pysys
from pysys.constants import *
from pysys.basetest import BaseTest

import sys

sys.path.append('environments')
from environment_b import EnvironmentB

# https://pysys-test.github.io/pysys-test/UserGuide.html
#Alternatively, you can create a trivial BaseTest subclass that instantiates plugins in code (rather than XML) which would allow # code completion (if your editor of choice supports this) but still provide the benefits of the modular composition approach.

class PySysTest(EnvironmentB):

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
        self.log.info("Cleanup Test")
