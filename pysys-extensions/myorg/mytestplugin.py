import sys
import logging

import pysys


class MyTestPlugin(object):

    myPluginProperty = 999

    def setup(self, testObj):
        self.owner = self.testObj = testObj
        self.log = logging.getLogger("pysys.myorg.MyTestPlugin")
        self.log.info(
            "MyTestPlugin.setup called; myPluginProperty=%r", self.myPluginProperty
        )
        self.log.info("")
        testObj.addCleanupFunction(self.__myPluginCleanup)

    def __myPluginCleanup(self):
        self.log.info("MyTestPlugin.cleanup called")

    def getStuff(self):
        return "Stuff"

    # This is convenient for allowing access to the owner's methods and fields as if they were on self; e.g. "self.assertGrep"
    def __getattr__(self, name):
        return getattr(self.owner, name)
