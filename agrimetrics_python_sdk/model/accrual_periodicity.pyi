# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from agrimetrics_python_sdk import schemas  # noqa: F401


class AccrualPeriodicity(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Accrual periodicity options
    """
    
    @schemas.classproperty
    def HOURLY(cls):
        return cls("Hourly")
    
    @schemas.classproperty
    def DAILY(cls):
        return cls("Daily")
    
    @schemas.classproperty
    def THREE_TIMES_A_WEEK(cls):
        return cls("Three times a week")
    
    @schemas.classproperty
    def SEMIWEEKLY(cls):
        return cls("Semiweekly")
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("Weekly")
    
    @schemas.classproperty
    def THREE_TIMES_A_MONTH(cls):
        return cls("Three times a month")
    
    @schemas.classproperty
    def BIWEEKLY(cls):
        return cls("Biweekly")
    
    @schemas.classproperty
    def SEMIMONTHLY(cls):
        return cls("Semimonthly")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("Monthly")
    
    @schemas.classproperty
    def BIMONTHLY(cls):
        return cls("Bimonthly")
    
    @schemas.classproperty
    def QUARTERLY(cls):
        return cls("Quarterly")
    
    @schemas.classproperty
    def THREE_TIMES_A_YEAR(cls):
        return cls("Three times a year")
    
    @schemas.classproperty
    def SEMIANNUAL(cls):
        return cls("Semiannual")
    
    @schemas.classproperty
    def ANNUAL(cls):
        return cls("Annual")
    
    @schemas.classproperty
    def BIENNIAL(cls):
        return cls("Biennial")
    
    @schemas.classproperty
    def TRIENNIAL(cls):
        return cls("Triennial")
    
    @schemas.classproperty
    def CONTINUOUS(cls):
        return cls("Continuous")
    
    @schemas.classproperty
    def IRREGULAR(cls):
        return cls("Irregular")
    
    @schemas.classproperty
    def CONTINUAL(cls):
        return cls("continual")
    
    @schemas.classproperty
    def DAILY(cls):
        return cls("daily")
    
    @schemas.classproperty
    def WEEKLY(cls):
        return cls("weekly")
    
    @schemas.classproperty
    def FORTNIGHTLY(cls):
        return cls("fortnightly")
    
    @schemas.classproperty
    def MONTHLY(cls):
        return cls("monthly")
    
    @schemas.classproperty
    def QUARTERLY(cls):
        return cls("quarterly")
    
    @schemas.classproperty
    def BIANNUALLY(cls):
        return cls("biannually")
    
    @schemas.classproperty
    def ANNUALLY(cls):
        return cls("annually")
    
    @schemas.classproperty
    def AS_NEEDED(cls):
        return cls("asNeeded")
    
    @schemas.classproperty
    def IRREGULAR(cls):
        return cls("irregular")
    
    @schemas.classproperty
    def NOT_PLANNED(cls):
        return cls("notPlanned")
    
    @schemas.classproperty
    def UNKNOWN(cls):
        return cls("unknown")
