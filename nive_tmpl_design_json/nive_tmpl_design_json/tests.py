# -*- coding: utf-8 -*-

import time
import unittest

from nive.helper import FormatConfTestFailure
from nive.helper import LoadConfiguration


class TestConf(unittest.TestCase):

    def test_conf1(self):
        configuration = LoadConfiguration("nive_tmpl_design_json:configuration.json")
        r=configuration.test()
        if not r:
            return
        print FormatConfTestFailure(r)
        self.assert_(False, "Configuration Error")
