# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.layers_layer_id.patch import AddGeoTiff
from agrimetrics_python_sdk.paths.layers_layer_id_style.post import AutoGenerateStyle
from agrimetrics_python_sdk.paths.layers_layer_id.delete import DeleteLayer
from agrimetrics_python_sdk.paths.layers_layer_id_style.get import GetStyle
from agrimetrics_python_sdk.paths.layers_layer_id_ingest.post import IngestFile
from agrimetrics_python_sdk.paths.layers_layer_id_files.delete import RemoveFile
from agrimetrics_python_sdk.paths.layers_layer_id_style.delete import RemoveStyle
from agrimetrics_python_sdk.paths.layers_layer_id_style.put import SetStyle
from agrimetrics_python_sdk.apis.tags.manage_layer_api_raw import ManageLayerApiRaw


class ManageLayerApi(
    AddGeoTiff,
    AutoGenerateStyle,
    DeleteLayer,
    GetStyle,
    IngestFile,
    RemoveFile,
    RemoveStyle,
    SetStyle,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ManageLayerApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ManageLayerApiRaw(api_client)
