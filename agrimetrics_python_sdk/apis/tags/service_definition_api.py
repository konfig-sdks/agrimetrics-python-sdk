# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from agrimetrics_python_sdk.paths.service_definition.post import CreateNewDefinition
from agrimetrics_python_sdk.paths.service_definition_layer_id.delete import DeleteById
from agrimetrics_python_sdk.paths.service_definition_layer_id.get import GetByLayerId
from agrimetrics_python_sdk.paths.service_definition_layer_id.patch import UpdateExistingDefinition
from agrimetrics_python_sdk.apis.tags.service_definition_api_raw import ServiceDefinitionApiRaw


class ServiceDefinitionApi(
    CreateNewDefinition,
    DeleteById,
    GetByLayerId,
    UpdateExistingDefinition,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ServiceDefinitionApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ServiceDefinitionApiRaw(api_client)