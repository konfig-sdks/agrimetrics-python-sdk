# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.linked_data_concepts.get import ListConcepts
from agrimetrics_python_sdk.apis.tags.graph_api_raw import GraphApiRaw


class GraphApi(
    ListConcepts,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: GraphApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = GraphApiRaw(api_client)
