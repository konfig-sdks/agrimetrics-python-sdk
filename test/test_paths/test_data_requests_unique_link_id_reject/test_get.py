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
from agrimetrics_python_sdk.paths.data_requests_unique_link_id_reject import get
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataRequestsUniqueLinkIdReject(ApiTestMixin, unittest.TestCase):
    """
    DataRequestsUniqueLinkIdReject unit test stubs
        reject data access
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
