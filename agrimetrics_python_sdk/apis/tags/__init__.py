# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from agrimetrics_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    DATASET = "Dataset"
    OGCAPI = "OGCAPI"
    OGC_API_TILES = "OGC API Tiles"
    ADMIN = "Admin"
    MANAGE_LAYER = "Manage Layer"
    DATA_REQUEST = "dataRequest"
    TEMPLATE = "Template"
    QUERY_LAYER = "Query Layer"
    SERVICE_DEFINITION = "Service Definition"
    WFS = "WFS"
    WMTS_REST = "WMTS REST"
    ACCESS_REQUEST = "AccessRequest"
    STATUS = "Status"
    WMS = "WMS"
    WCS = "WCS"
    ESRI = "ESRI"
    HARVEST = "Harvest"
    QUERY_DATASET = "Query Dataset"
    MANAGE_DATASET = "Manage Dataset"
    WMTS = "WMTS"
    IMPORT = "Import"
    SHAPEFILE = "Shapefile"
    AUTHENTICATION = "Authentication"
    GRAPH = "Graph"
    IMAGE = "Image"
