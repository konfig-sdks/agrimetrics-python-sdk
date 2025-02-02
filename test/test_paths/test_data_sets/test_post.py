# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import agrimetrics_python_sdk
from agrimetrics_python_sdk.paths.data_sets import post
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataSets(ApiTestMixin, unittest.TestCase):
    """
    DataSets unit test stubs
        Create a single data set catalog entry.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 201




if __name__ == '__main__':
    unittest.main()
