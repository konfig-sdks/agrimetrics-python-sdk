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
from agrimetrics_python_sdk.paths.data_sets_data_set_id_file_dataset import post
from agrimetrics_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestDataSetsDataSetIdFileDataset(ApiTestMixin, unittest.TestCase):
    """
    DataSetsDataSetIdFileDataset unit test stubs
        Create and attach file dataset
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
