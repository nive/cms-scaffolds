# -*- coding: utf-8 -*-

import unittest

from nive.helper import FormatConfTestFailure

import nive_tmpl_element_python


class TestConf(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_conf(self):
        r=nive_tmpl_element_python.configuration.test()
        if not r:
            return
        print FormatConfTestFailure(r)
        self.assert_(False, "Configuration Error")

