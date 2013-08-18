# -*- coding: utf-8 -*-

import unittest

from nive.helper import FormatConfTestFailure
from nive.helper import LoadConfiguration


class TestConf(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_conf(self):
        configuration = LoadConfiguration("nive_tmpl_element_json:configuration.json")
        r=configuration.test()
        if not r:
            return
        print FormatConfTestFailure(r)
        self.assert_(False, "Configuration Error")

