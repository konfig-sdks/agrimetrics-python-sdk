# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.datasets_dataset_id_wmts_rest_layer_name_style_tile_matrix_set_tile_matrix_tile_row_tile_col.get import QueryTileMatrixSet
from agrimetrics_python_sdk.paths.datasets_dataset_id_wmts_rest_layer_name_style_tilejson_image_format.get import QueryTilejsonImageFormat
from agrimetrics_python_sdk.paths.datasets_dataset_id_wmts_rest_layer_name_style_tile_matrix_set_tile_matrix_tile_row_tile_col_j_i.get import ServiceQuery
from agrimetrics_python_sdk.apis.tags.wmtsrest_api_raw import WMTSRESTApiRaw


class WMTSRESTApi(
    QueryTileMatrixSet,
    QueryTilejsonImageFormat,
    ServiceQuery,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WMTSRESTApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WMTSRESTApiRaw(api_client)