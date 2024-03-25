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

from agrimetrics_python_sdk.type.batch_identity_input_entitlements import BatchIdentityInputEntitlements
from agrimetrics_python_sdk.type.data_set_patch import DataSetPatch
from agrimetrics_python_sdk.type.entitlements import Entitlements
from agrimetrics_python_sdk.type.exchange import Exchange

class RequiredDataSetTemplateMetadata(TypedDict):
    name: str

class OptionalDataSetTemplateMetadata(TypedDict, total=False):
    description: str

    dataSet: DataSetPatch

    entitlements: BatchIdentityInputEntitlements

    creatorEntitlements: Entitlements

    exchange: Exchange

class DataSetTemplateMetadata(RequiredDataSetTemplateMetadata, OptionalDataSetTemplateMetadata):
    pass
