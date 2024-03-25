# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from agrimetrics_python_sdk.pydantic.billable import Billable

class ServiceDefinition(BaseModel):
    dataset_id: str = Field(alias='datasetId')

    layer_name: str = Field(alias='layerName')

    service: Literal["WCS", "WFS"] = Field(alias='service')

    w_f_s: Literal["Y", "N"] = Field(alias='WFS')

    w_c_s: Literal["Y", "N"] = Field(alias='WCS')

    w_m_s: Literal["Y", "N"] = Field(alias='WMS')

    w_m_t_s: Literal["Y", "N"] = Field(alias='WMTS')

    o_g_c_api_features: Literal["Y", "N"] = Field(alias='OGCApiFeatures')

    o_g_c_api_tiles: Literal["Y", "N"] = Field(alias='OGCApiTiles')

    temporal: typing.Optional[bool] = Field(None, alias='temporal')

    datastore: typing.Optional[str] = Field(None, alias='datastore')

    geoserver_host_name: typing.Optional[str] = Field(None, alias='geoserverHostName')

    geometry_field: typing.Optional[str] = Field(None, alias='geometryField')

    billable: typing.Optional[Billable] = Field(None, alias='billable')

    default_e_p_s_g_code: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultEPSGCode')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
