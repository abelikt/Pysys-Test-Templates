import pysys
from pysys.constants import *
from pysys.basetest import BaseTest


class PySysTest(BaseTest):
    def execute(self):
        self.assertThat("True")
        self.assertThat("True == value", value=True)
        self.assertThat("value == expected", expected=True, value=True)
        self.assertThat("value == expected", expected="melon", value="melon")

        user = "myuser"
        self.assertThat("actualUser == expected", expected="myuser", actualUser=user)

        self.assertThat("user is not None", user=user)
