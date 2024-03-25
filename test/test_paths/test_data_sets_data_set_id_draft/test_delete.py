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
from agrimetrics_python_sdk.paths.data_sets_data_set_id_draft import delete
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataSetsDataSetIdDraft(ApiTestMixin, unittest.TestCase):
    """
    DataSetsDataSetIdDraft unit test stubs
        Discards the draft changes on a data set catalog entry.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200
    response_body = ''


if __name__ == '__main__':
    unittest.main()
