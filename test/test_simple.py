# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from agrimetrics_python_sdk import Agrimetrics

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        agrimetrics = Agrimetrics(
        
            access_token = 'YOUR_BEARER_TOKEN',
        
                        api_key_header = 'YOUR_API_KEY',
        
                        api_key_query = 'YOUR_API_KEY',
        
                        sec0 = 'YOUR_API_KEY',
        
                        x_user_header = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(agrimetrics)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()