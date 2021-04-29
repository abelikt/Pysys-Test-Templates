import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def execute(self):

        # https://pysys-test.github.io/pysys-test/BaseTest.html#test-configuration

        self.log.info("self.input " + self.input)
        self.log.info("self.output " + self.output)
        self.log.info("self.reference " + self.reference)
        self.log.info("self.mode " + str(self.mode))
        # and more ...

        self.assertTrue(True)
