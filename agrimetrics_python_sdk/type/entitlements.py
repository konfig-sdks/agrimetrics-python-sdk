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

from agrimetrics_python_sdk.type.entitlements_catalog import EntitlementsCatalog
from agrimetrics_python_sdk.type.entitlements_data_set import EntitlementsDataSet

class RequiredEntitlements(TypedDict):
    catalog: EntitlementsCatalog

    isAdmin: bool

class OptionalEntitlements(TypedDict, total=False):
    dataSet: EntitlementsDataSet

class Entitlements(RequiredEntitlements, OptionalEntitlements):
    pass
