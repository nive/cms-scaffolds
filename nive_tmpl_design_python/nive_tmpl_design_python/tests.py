# -*- coding: utf-8 -*-

import time
import unittest

from nive.helper import FormatConfTestFailure

import nive_tmpl_design_python


class TestConf(unittest.TestCase):

    def test_conf1(self):
        r=nive_tmpl_design_python.configuration.test()
        if not r:
            return
        print FormatConfTestFailure(r)
        self.assert_(False, "Configuration Error")
