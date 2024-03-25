# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.datasets_dataset_id_wmts.get import QueryDataSetWmts
from agrimetrics_python_sdk.apis.tags.wmts_api_raw import WMTSApiRaw


class WMTSApi(
    QueryDataSetWmts,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WMTSApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WMTSApiRaw(api_client)
