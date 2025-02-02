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

from agrimetrics_python_sdk.pydantic.entitlements_catalog import EntitlementsCatalog
from agrimetrics_python_sdk.pydantic.entitlements_data_set import EntitlementsDataSet

class Entitlements(BaseModel):
    catalog: EntitlementsCatalog = Field(alias='catalog')

    is_admin: bool = Field(alias='isAdmin')

    data_set: typing.Optional[EntitlementsDataSet] = Field(None, alias='dataSet')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
