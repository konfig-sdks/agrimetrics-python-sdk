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


class ServiceDefinitionResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "layerId",
            "WFS",
            "WCS",
            "service",
            "OGCApiTiles",
            "datasetId",
            "layerName",
            "WMS",
            "OGCApiFeatures",
            "WMTS",
        }
        
        class properties:
            layerId = schemas.StrSchema
            datasetId = schemas.StrSchema
            layerName = schemas.StrSchema
            
            
            class service(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def WCS(cls):
                    return cls("WCS")
                
                @schemas.classproperty
                def WFS(cls):
                    return cls("WFS")
            
            
            class WMS(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            
            
            class WMTS(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            
            
            class WFS(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            
            
            class WCS(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            
            
            class OGCApiFeatures(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            
            
            class OGCApiTiles(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def Y(cls):
                    return cls("Y")
                
                @schemas.classproperty
                def N(cls):
                    return cls("N")
            temporal = schemas.BoolSchema
            datastore = schemas.StrSchema
            geoserverHostName = schemas.StrSchema
            geometryField = schemas.StrSchema
        
            @staticmethod
            def billable() -> typing.Type['Billable']:
                return Billable
            defaultEPSGCode = schemas.NumberSchema
            __annotations__ = {
                "layerId": layerId,
                "datasetId": datasetId,
                "layerName": layerName,
                "service": service,
                "WMS": WMS,
                "WMTS": WMTS,
                "WFS": WFS,
                "WCS": WCS,
                "OGCApiFeatures": OGCApiFeatures,
                "OGCApiTiles": OGCApiTiles,
                "temporal": temporal,
                "datastore": datastore,
                "geoserverHostName": geoserverHostName,
                "geometryField": geometryField,
                "billable": billable,
                "defaultEPSGCode": defaultEPSGCode,
            }
    
    layerId: MetaOapg.properties.layerId
    WFS: MetaOapg.properties.WFS
    WCS: MetaOapg.properties.WCS
    service: MetaOapg.properties.service
    OGCApiTiles: MetaOapg.properties.OGCApiTiles
    datasetId: MetaOapg.properties.datasetId
    layerName: MetaOapg.properties.layerName
    WMS: MetaOapg.properties.WMS
    OGCApiFeatures: MetaOapg.properties.OGCApiFeatures
    WMTS: MetaOapg.properties.WMTS
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layerId"]) -> MetaOapg.properties.layerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datasetId"]) -> MetaOapg.properties.datasetId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["layerName"]) -> MetaOapg.properties.layerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WMS"]) -> MetaOapg.properties.WMS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WMTS"]) -> MetaOapg.properties.WMTS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WFS"]) -> MetaOapg.properties.WFS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["WCS"]) -> MetaOapg.properties.WCS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OGCApiFeatures"]) -> MetaOapg.properties.OGCApiFeatures: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["OGCApiTiles"]) -> MetaOapg.properties.OGCApiTiles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["temporal"]) -> MetaOapg.properties.temporal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datastore"]) -> MetaOapg.properties.datastore: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geoserverHostName"]) -> MetaOapg.properties.geoserverHostName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geometryField"]) -> MetaOapg.properties.geometryField: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["billable"]) -> 'Billable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultEPSGCode"]) -> MetaOapg.properties.defaultEPSGCode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["layerId", "datasetId", "layerName", "service", "WMS", "WMTS", "WFS", "WCS", "OGCApiFeatures", "OGCApiTiles", "temporal", "datastore", "geoserverHostName", "geometryField", "billable", "defaultEPSGCode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layerId"]) -> MetaOapg.properties.layerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datasetId"]) -> MetaOapg.properties.datasetId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["layerName"]) -> MetaOapg.properties.layerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["service"]) -> MetaOapg.properties.service: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WMS"]) -> MetaOapg.properties.WMS: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WMTS"]) -> MetaOapg.properties.WMTS: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WFS"]) -> MetaOapg.properties.WFS: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["WCS"]) -> MetaOapg.properties.WCS: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OGCApiFeatures"]) -> MetaOapg.properties.OGCApiFeatures: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["OGCApiTiles"]) -> MetaOapg.properties.OGCApiTiles: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["temporal"]) -> typing.Union[MetaOapg.properties.temporal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datastore"]) -> typing.Union[MetaOapg.properties.datastore, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geoserverHostName"]) -> typing.Union[MetaOapg.properties.geoserverHostName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geometryField"]) -> typing.Union[MetaOapg.properties.geometryField, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["billable"]) -> typing.Union['Billable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultEPSGCode"]) -> typing.Union[MetaOapg.properties.defaultEPSGCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["layerId", "datasetId", "layerName", "service", "WMS", "WMTS", "WFS", "WCS", "OGCApiFeatures", "OGCApiTiles", "temporal", "datastore", "geoserverHostName", "geometryField", "billable", "defaultEPSGCode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        layerId: typing.Union[MetaOapg.properties.layerId, str, ],
        WFS: typing.Union[MetaOapg.properties.WFS, str, ],
        WCS: typing.Union[MetaOapg.properties.WCS, str, ],
        service: typing.Union[MetaOapg.properties.service, str, ],
        OGCApiTiles: typing.Union[MetaOapg.properties.OGCApiTiles, str, ],
        datasetId: typing.Union[MetaOapg.properties.datasetId, str, ],
        layerName: typing.Union[MetaOapg.properties.layerName, str, ],
        WMS: typing.Union[MetaOapg.properties.WMS, str, ],
        OGCApiFeatures: typing.Union[MetaOapg.properties.OGCApiFeatures, str, ],
        WMTS: typing.Union[MetaOapg.properties.WMTS, str, ],
        temporal: typing.Union[MetaOapg.properties.temporal, bool, schemas.Unset] = schemas.unset,
        datastore: typing.Union[MetaOapg.properties.datastore, str, schemas.Unset] = schemas.unset,
        geoserverHostName: typing.Union[MetaOapg.properties.geoserverHostName, str, schemas.Unset] = schemas.unset,
        geometryField: typing.Union[MetaOapg.properties.geometryField, str, schemas.Unset] = schemas.unset,
        billable: typing.Union['Billable', schemas.Unset] = schemas.unset,
        defaultEPSGCode: typing.Union[MetaOapg.properties.defaultEPSGCode, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServiceDefinitionResponse':
        return super().__new__(
            cls,
            *args,
            layerId=layerId,
            WFS=WFS,
            WCS=WCS,
            service=service,
            OGCApiTiles=OGCApiTiles,
            datasetId=datasetId,
            layerName=layerName,
            WMS=WMS,
            OGCApiFeatures=OGCApiFeatures,
            WMTS=WMTS,
            temporal=temporal,
            datastore=datastore,
            geoserverHostName=geoserverHostName,
            geometryField=geometryField,
            billable=billable,
            defaultEPSGCode=defaultEPSGCode,
            _configuration=_configuration,
            **kwargs,
        )

from agrimetrics_python_sdk.model.billable import Billable
