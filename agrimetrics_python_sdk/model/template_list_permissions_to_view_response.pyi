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


class TemplateListPermissionsToViewResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "templates",
        }
        
        class properties:
            
            
            class templates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DataSetTemplateEntity']:
                        return DataSetTemplateEntity
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DataSetTemplateEntity'], typing.List['DataSetTemplateEntity']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'templates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DataSetTemplateEntity':
                    return super().__getitem__(i)
            __annotations__ = {
                "templates": templates,
            }
    
    templates: MetaOapg.properties.templates
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["templates"]) -> MetaOapg.properties.templates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["templates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["templates"]) -> MetaOapg.properties.templates: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["templates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        templates: typing.Union[MetaOapg.properties.templates, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TemplateListPermissionsToViewResponse':
        return super().__new__(
            cls,
            *args,
            templates=templates,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.data_set_template_entity import DataSetTemplateEntity