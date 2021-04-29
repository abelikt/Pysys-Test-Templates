import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def execute(self):

        process = self.startProcess(
            # The complete path is mandatory (Error 71) !!!
            command="/usr/bin/ls",
            arguments=["-lah"],
            # stdouterr = 'lsoutput',
        )
        self.addOutcome(PASSED)
