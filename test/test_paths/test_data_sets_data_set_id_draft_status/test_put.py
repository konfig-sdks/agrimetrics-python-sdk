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
from agrimetrics_python_sdk.paths.data_sets_data_set_id_draft_status import put
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataSetsDataSetIdDraftStatus(ApiTestMixin, unittest.TestCase):
    """
    DataSetsDataSetIdDraftStatus unit test stubs
        Set the draft status for the data set catalog entry.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
