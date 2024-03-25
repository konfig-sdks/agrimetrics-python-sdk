import typing_extensions

from agrimetrics_python_sdk.apis.tags import TagValues
from agrimetrics_python_sdk.apis.tags.dataset_api import DatasetApi
from agrimetrics_python_sdk.apis.tags.ogcapi_api import OGCAPIApi
from agrimetrics_python_sdk.apis.tags.ogcapi_tiles_api import OGCAPITilesApi
from agrimetrics_python_sdk.apis.tags.admin_api import AdminApi
from agrimetrics_python_sdk.apis.tags.manage_layer_api import ManageLayerApi
from agrimetrics_python_sdk.apis.tags.data_request_api import DataRequestApi
from agrimetrics_python_sdk.apis.tags.template_api import TemplateApi
from agrimetrics_python_sdk.apis.tags.query_layer_api import QueryLayerApi
from agrimetrics_python_sdk.apis.tags.service_definition_api import ServiceDefinitionApi
from agrimetrics_python_sdk.apis.tags.wfs_api import WFSApi
from agrimetrics_python_sdk.apis.tags.wmtsrest_api import WMTSRESTApi
from agrimetrics_python_sdk.apis.tags.access_request_api import AccessRequestApi
from agrimetrics_python_sdk.apis.tags.status_api import StatusApi
from agrimetrics_python_sdk.apis.tags.wms_api import WMSApi
from agrimetrics_python_sdk.apis.tags.wcs_api import WCSApi
from agrimetrics_python_sdk.apis.tags.esri_api import ESRIApi
from agrimetrics_python_sdk.apis.tags.harvest_api import HarvestApi
from agrimetrics_python_sdk.apis.tags.query_dataset_api import QueryDatasetApi
from agrimetrics_python_sdk.apis.tags.manage_dataset_api import ManageDatasetApi
from agrimetrics_python_sdk.apis.tags.wmts_api import WMTSApi
from agrimetrics_python_sdk.apis.tags.model_import_api import ModelImportApi
from agrimetrics_python_sdk.apis.tags.shapefile_api import ShapefileApi
from agrimetrics_python_sdk.apis.tags.authentication_api import AuthenticationApi
from agrimetrics_python_sdk.apis.tags.graph_api import GraphApi
from agrimetrics_python_sdk.apis.tags.image_api import ImageApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATASET: DatasetApi,
        TagValues.OGCAPI: OGCAPIApi,
        TagValues.OGC_API_TILES: OGCAPITilesApi,
        TagValues.ADMIN: AdminApi,
        TagValues.MANAGE_LAYER: ManageLayerApi,
        TagValues.DATA_REQUEST: DataRequestApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.QUERY_LAYER: QueryLayerApi,
        TagValues.SERVICE_DEFINITION: ServiceDefinitionApi,
        TagValues.WFS: WFSApi,
        TagValues.WMTS_REST: WMTSRESTApi,
        TagValues.ACCESS_REQUEST: AccessRequestApi,
        TagValues.STATUS: StatusApi,
        TagValues.WMS: WMSApi,
        TagValues.WCS: WCSApi,
        TagValues.ESRI: ESRIApi,
        TagValues.HARVEST: HarvestApi,
        TagValues.QUERY_DATASET: QueryDatasetApi,
        TagValues.MANAGE_DATASET: ManageDatasetApi,
        TagValues.WMTS: WMTSApi,
        TagValues.IMPORT: ModelImportApi,
        TagValues.SHAPEFILE: ShapefileApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.GRAPH: GraphApi,
        TagValues.IMAGE: ImageApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATASET: DatasetApi,
        TagValues.OGCAPI: OGCAPIApi,
        TagValues.OGC_API_TILES: OGCAPITilesApi,
        TagValues.ADMIN: AdminApi,
        TagValues.MANAGE_LAYER: ManageLayerApi,
        TagValues.DATA_REQUEST: DataRequestApi,
        TagValues.TEMPLATE: TemplateApi,
        TagValues.QUERY_LAYER: QueryLayerApi,
        TagValues.SERVICE_DEFINITION: ServiceDefinitionApi,
        TagValues.WFS: WFSApi,
        TagValues.WMTS_REST: WMTSRESTApi,
        TagValues.ACCESS_REQUEST: AccessRequestApi,
        TagValues.STATUS: StatusApi,
        TagValues.WMS: WMSApi,
        TagValues.WCS: WCSApi,
        TagValues.ESRI: ESRIApi,
        TagValues.HARVEST: HarvestApi,
        TagValues.QUERY_DATASET: QueryDatasetApi,
        TagValues.MANAGE_DATASET: ManageDatasetApi,
        TagValues.WMTS: WMTSApi,
        TagValues.IMPORT: ModelImportApi,
        TagValues.SHAPEFILE: ShapefileApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.GRAPH: GraphApi,
        TagValues.IMAGE: ImageApi,
    }
)
