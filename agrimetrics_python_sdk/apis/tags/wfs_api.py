# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.datasets_dataset_id_wfs.head import QueryDataOpenGis
from agrimetrics_python_sdk.paths.datasets_dataset_id_wfs.post import QueryDataOpenGis0
from agrimetrics_python_sdk.paths.datasets_dataset_id_wfs.get import QueryDataWithOpenGis
from agrimetrics_python_sdk.apis.tags.wfs_api_raw import WFSApiRaw


class WFSApi(
    QueryDataOpenGis,
    QueryDataOpenGis0,
    QueryDataWithOpenGis,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WFSApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WFSApiRaw(api_client)
