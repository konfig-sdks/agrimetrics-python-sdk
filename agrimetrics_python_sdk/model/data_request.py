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


class DataRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "projectManagerEmail",
            "requestedFormat",
            "projectManagerName",
            "datasetName",
            "datasetId",
            "projectName",
        }
        
        class properties:
            projectName = schemas.StrSchema
            projectManagerName = schemas.StrSchema
            projectManagerEmail = schemas.StrSchema
            datasetId = schemas.UUIDSchema
            datasetName = schemas.StrSchema
            
            
            class requestedFormat(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "application/geo+json": "APPLICATION_GEOJSON",
                        "application/gml+xml; version=3.2": "APPLICATION_GMLXML_VERSION3_2",
                        "application/vnd.google-earth.kml+xml": "APPLICATION_VND_GOOGLEEARTH_KMLXML",
                        "application/zipped-shapefile": "APPLICATION_ZIPPEDSHAPEFILE",
                        "application/x.gdb+zip": "APPLICATION_X_GDBZIP",
                        "application/x.mid-mif+zip": "APPLICATION_X_MIDMIFZIP",
                        "application/x.tab+zip": "APPLICATION_X_TABZIP",
                        "application/dxf": "APPLICATION_DXF",
                        "image/tiff": "IMAGE_TIFF",
                    }
                
                @schemas.classproperty
                def APPLICATION_GEOJSON(cls):
                    return cls("application/geo+json")
                
                @schemas.classproperty
                def APPLICATION_GMLXML_VERSION3_2(cls):
                    return cls("application/gml+xml; version=3.2")
                
                @schemas.classproperty
                def APPLICATION_VND_GOOGLEEARTH_KMLXML(cls):
                    return cls("application/vnd.google-earth.kml+xml")
                
                @schemas.classproperty
                def APPLICATION_ZIPPEDSHAPEFILE(cls):
                    return cls("application/zipped-shapefile")
                
                @schemas.classproperty
                def APPLICATION_X_GDBZIP(cls):
                    return cls("application/x.gdb+zip")
                
                @schemas.classproperty
                def APPLICATION_X_MIDMIFZIP(cls):
                    return cls("application/x.mid-mif+zip")
                
                @schemas.classproperty
                def APPLICATION_X_TABZIP(cls):
                    return cls("application/x.tab+zip")
                
                @schemas.classproperty
                def APPLICATION_DXF(cls):
                    return cls("application/dxf")
                
                @schemas.classproperty
                def IMAGE_TIFF(cls):
                    return cls("image/tiff")
            geoJsonAOI = schemas.StrSchema
            shapefileAOI = schemas.BinarySchema
            __annotations__ = {
                "projectName": projectName,
                "projectManagerName": projectManagerName,
                "projectManagerEmail": projectManagerEmail,
                "datasetId": datasetId,
                "datasetName": datasetName,
                "requestedFormat": requestedFormat,
                "geoJsonAOI": geoJsonAOI,
                "shapefileAOI": shapefileAOI,
            }
    
    projectManagerEmail: MetaOapg.properties.projectManagerEmail
    requestedFormat: MetaOapg.properties.requestedFormat
    projectManagerName: MetaOapg.properties.projectManagerName
    datasetName: MetaOapg.properties.datasetName
    datasetId: MetaOapg.properties.datasetId
    projectName: MetaOapg.properties.projectName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectName"]) -> MetaOapg.properties.projectName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectManagerName"]) -> MetaOapg.properties.projectManagerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["projectManagerEmail"]) -> MetaOapg.properties.projectManagerEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetId"]) -> MetaOapg.properties.datasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetName"]) -> MetaOapg.properties.datasetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestedFormat"]) -> MetaOapg.properties.requestedFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geoJsonAOI"]) -> MetaOapg.properties.geoJsonAOI: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shapefileAOI"]) -> MetaOapg.properties.shapefileAOI: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["projectName", "projectManagerName", "projectManagerEmail", "datasetId", "datasetName", "requestedFormat", "geoJsonAOI", "shapefileAOI", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectName"]) -> MetaOapg.properties.projectName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectManagerName"]) -> MetaOapg.properties.projectManagerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["projectManagerEmail"]) -> MetaOapg.properties.projectManagerEmail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetId"]) -> MetaOapg.properties.datasetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetName"]) -> MetaOapg.properties.datasetName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestedFormat"]) -> MetaOapg.properties.requestedFormat: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geoJsonAOI"]) -> typing.Union[MetaOapg.properties.geoJsonAOI, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shapefileAOI"]) -> typing.Union[MetaOapg.properties.shapefileAOI, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["projectName", "projectManagerName", "projectManagerEmail", "datasetId", "datasetName", "requestedFormat", "geoJsonAOI", "shapefileAOI", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        projectManagerEmail: typing.Union[MetaOapg.properties.projectManagerEmail, str, ],
        requestedFormat: typing.Union[MetaOapg.properties.requestedFormat, str, ],
        projectManagerName: typing.Union[MetaOapg.properties.projectManagerName, str, ],
        datasetName: typing.Union[MetaOapg.properties.datasetName, str, ],
        datasetId: typing.Union[MetaOapg.properties.datasetId, str, uuid.UUID, ],
        projectName: typing.Union[MetaOapg.properties.projectName, str, ],
        geoJsonAOI: typing.Union[MetaOapg.properties.geoJsonAOI, str, schemas.Unset] = schemas.unset,
        shapefileAOI: typing.Union[MetaOapg.properties.shapefileAOI, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataRequest':
        return super().__new__(
            cls,
            *args,
            projectManagerEmail=projectManagerEmail,
            requestedFormat=requestedFormat,
            projectManagerName=projectManagerName,
            datasetName=datasetName,
            datasetId=datasetId,
            projectName=projectName,
            geoJsonAOI=geoJsonAOI,
            shapefileAOI=shapefileAOI,
            _configuration=_configuration,
            **kwargs,
        )
