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


class Contact(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "organisationName",
            "role",
        }
        
        class properties:
            organisationName = schemas.StrSchema
            
            
            class role(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "resourceProvider": "RESOURCE_PROVIDER",
                        "custodian": "CUSTODIAN",
                        "owner": "OWNER",
                        "user": "USER",
                        "distributor": "DISTRIBUTOR",
                        "originator": "ORIGINATOR",
                        "pointOfContact": "POINT_OF_CONTACT",
                        "principalInvestigator": "PRINCIPAL_INVESTIGATOR",
                        "processor": "PROCESSOR",
                        "publisher": "PUBLISHER",
                        "author": "AUTHOR",
                    }
                
                @schemas.classproperty
                def RESOURCE_PROVIDER(cls):
                    return cls("resourceProvider")
                
                @schemas.classproperty
                def CUSTODIAN(cls):
                    return cls("custodian")
                
                @schemas.classproperty
                def OWNER(cls):
                    return cls("owner")
                
                @schemas.classproperty
                def USER(cls):
                    return cls("user")
                
                @schemas.classproperty
                def DISTRIBUTOR(cls):
                    return cls("distributor")
                
                @schemas.classproperty
                def ORIGINATOR(cls):
                    return cls("originator")
                
                @schemas.classproperty
                def POINT_OF_CONTACT(cls):
                    return cls("pointOfContact")
                
                @schemas.classproperty
                def PRINCIPAL_INVESTIGATOR(cls):
                    return cls("principalInvestigator")
                
                @schemas.classproperty
                def PROCESSOR(cls):
                    return cls("processor")
                
                @schemas.classproperty
                def PUBLISHER(cls):
                    return cls("publisher")
                
                @schemas.classproperty
                def AUTHOR(cls):
                    return cls("author")
            individualName = schemas.StrSchema
            positionName = schemas.StrSchema
            emailAddress = schemas.StrSchema
            __annotations__ = {
                "organisationName": organisationName,
                "role": role,
                "individualName": individualName,
                "positionName": positionName,
                "emailAddress": emailAddress,
            }
    
    organisationName: MetaOapg.properties.organisationName
    role: MetaOapg.properties.role
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["organisationName"]) -> MetaOapg.properties.organisationName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["individualName"]) -> MetaOapg.properties.individualName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positionName"]) -> MetaOapg.properties.positionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailAddress"]) -> MetaOapg.properties.emailAddress: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["organisationName", "role", "individualName", "positionName", "emailAddress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["organisationName"]) -> MetaOapg.properties.organisationName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["role"]) -> MetaOapg.properties.role: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["individualName"]) -> typing.Union[MetaOapg.properties.individualName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positionName"]) -> typing.Union[MetaOapg.properties.positionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailAddress"]) -> typing.Union[MetaOapg.properties.emailAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["organisationName", "role", "individualName", "positionName", "emailAddress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        organisationName: typing.Union[MetaOapg.properties.organisationName, str, ],
        role: typing.Union[MetaOapg.properties.role, str, ],
        individualName: typing.Union[MetaOapg.properties.individualName, str, schemas.Unset] = schemas.unset,
        positionName: typing.Union[MetaOapg.properties.positionName, str, schemas.Unset] = schemas.unset,
        emailAddress: typing.Union[MetaOapg.properties.emailAddress, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contact':
        return super().__new__(
            cls,
            *args,
            organisationName=organisationName,
            role=role,
            individualName=individualName,
            positionName=positionName,
            emailAddress=emailAddress,
            _configuration=_configuration,
            **kwargs,
        )
