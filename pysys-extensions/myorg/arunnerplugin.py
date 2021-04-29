import sys
import os
import json
import logging

import pysys

# Some parts are taken from the PySys sample cookbook
# https://github.com/pysys-test/sample-cookbook


class ARunnerPlugin(object):
    def setup(self, runner):
        self.owner = self.runner = runner
        self.log = logging.getLogger("pysys.myorg.ARunnerPlugin")
        self.log.info("Setup Plugin ARunnerPlugin up and doing stuff")
        self.owner.mkdir(self.owner.output)
        runner.addCleanupFunction(self.__myPluginCleanup)

    def getPythonVersion(self):
        self.owner.startProcess(
            sys.executable, arguments=["--version"], stdouterr="ARunnerPlugin"
        )
        return self.owner.waitForGrep("ARunnerPlugin.out", "(?P<output>.+)")[
            "output"
        ].strip()

    def __myPluginCleanup(self):
        self.log.info("MyRunnerPlugin cleanup called")
