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
from agrimetrics_python_sdk.paths.templates import get
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestTemplates(ApiTestMixin, unittest.TestCase):
    """
    Templates unit test stubs
        List all templates you have permission to view.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
