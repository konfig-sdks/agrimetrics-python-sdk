# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.status.get import GetCatalogApiStatusRaw
from agrimetrics_python_sdk.paths.data_sets_data_set_id_draft_status.put import SetDraftStatusRaw


class StatusApiRaw(
    GetCatalogApiStatusRaw,
    SetDraftStatusRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
