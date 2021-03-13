import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def execute(self):

        process = self.startProcess(
            command="/usr/bin/date",
            arguments=[],
            stdouterr="date",
        )
        self.assertGrep("date.out", "2021", contains=True)

        self.assertGrep("date.out", "Nope", contains=False)
