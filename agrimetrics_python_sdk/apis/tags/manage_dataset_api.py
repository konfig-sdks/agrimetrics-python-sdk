# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.datasets_dataset_id_layers.post import IngestFileNewLayer
from agrimetrics_python_sdk.apis.tags.manage_dataset_api_raw import ManageDatasetApiRaw


class ManageDatasetApi(
    IngestFileNewLayer,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ManageDatasetApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ManageDatasetApiRaw(api_client)
