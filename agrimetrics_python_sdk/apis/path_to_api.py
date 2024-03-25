import typing_extensions

from agrimetrics_python_sdk.paths import PathValues
from agrimetrics_python_sdk.apis.paths.authenticate import Authenticate
from agrimetrics_python_sdk.apis.paths.status import Status
from agrimetrics_python_sdk.apis.paths.query import Query
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id import DatasetsDatasetId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_layers import DatasetsDatasetIdLayers
from agrimetrics_python_sdk.apis.paths.shapefile import Shapefile
from agrimetrics_python_sdk.apis.paths.layers_layer_id import LayersLayerId
from agrimetrics_python_sdk.apis.paths.layers_layer_id_files import LayersLayerIdFiles
from agrimetrics_python_sdk.apis.paths.layers_layer_id_ingest import LayersLayerIdIngest
from agrimetrics_python_sdk.apis.paths.layers_layer_id_style import LayersLayerIdStyle
from agrimetrics_python_sdk.apis.paths.layers_layer_id_search import LayersLayerIdSearch
from agrimetrics_python_sdk.apis.paths.layers_layer_id_search_cost import LayersLayerIdSearchCost
from agrimetrics_python_sdk.apis.paths.layers_layer_id_search_statistics import LayersLayerIdSearchStatistics
from agrimetrics_python_sdk.apis.paths.service_definition import ServiceDefinition
from agrimetrics_python_sdk.apis.paths.service_definition_layer_id import ServiceDefinitionLayerId
from agrimetrics_python_sdk.apis.paths.data_requests import DataRequests
from agrimetrics_python_sdk.apis.paths.data_requests_request_id import DataRequestsRequestId
from agrimetrics_python_sdk.apis.paths.data_requests_unique_link_id_approve import DataRequestsUniqueLinkIdApprove
from agrimetrics_python_sdk.apis.paths.data_requests_unique_link_id_reject import DataRequestsUniqueLinkIdReject
from agrimetrics_python_sdk.apis.paths.data_requests_unique_link_id_geometry import DataRequestsUniqueLinkIdGeometry
from agrimetrics_python_sdk.apis.paths.data_requests_request_id_download import DataRequestsRequestIdDownload
from agrimetrics_python_sdk.apis.paths.datasets_swagger_ui_swagger_file import DatasetsSwaggerUiSwaggerFile
from agrimetrics_python_sdk.apis.paths.datasets_apicss_css_file import DatasetsApicssCssFile
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wms import DatasetsDatasetIdWms
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wmts import DatasetsDatasetIdWmts
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wfs import DatasetsDatasetIdWfs
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1 import DatasetsDatasetIdOgcFeaturesV1
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_openapi import DatasetsDatasetIdOgcFeaturesV1Openapi
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_conformance import DatasetsDatasetIdOgcFeaturesV1Conformance
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_functions import DatasetsDatasetIdOgcFeaturesV1Functions
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_collections import DatasetsDatasetIdOgcFeaturesV1Collections
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_collections_collection_id import DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_collections_collection_id_queryables import DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdQueryables
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_collections_collection_id_items import DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItems
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_features_v1_collections_collection_id_items_feature_id import DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItemsFeatureId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1 import DatasetsDatasetIdOgcTilesV1
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_conformance import DatasetsDatasetIdOgcTilesV1Conformance
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_collections import DatasetsDatasetIdOgcTilesV1Collections
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_collections_collection_id import DatasetsDatasetIdOgcTilesV1CollectionsCollectionId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_collections_collection_id_queryables import DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdQueryables
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_collections_collection_id_tiles_tile_matrix_set_id import DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdTilesTileMatrixSetId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_collections_collection_id_map_tiles_tile_matrix_set_id_tile_matrix_tile_row_tile_col import DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdMapTilesTileMatrixSetIdTileMatrixTileRowTileCol
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_tile_matrix_sets import DatasetsDatasetIdOgcTilesV1TileMatrixSets
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_ogc_tiles_v1_tile_matrix_sets_tile_matrix_set_id import DatasetsDatasetIdOgcTilesV1TileMatrixSetsTileMatrixSetId
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wmts_rest_layer_name_style_tilejson_image_format import DatasetsDatasetIdWmtsRestLayerNameStyleTilejsonImageFormat
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wmts_rest_layer_name_style_tile_matrix_set_tile_matrix_tile_row_tile_col import DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileCol
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wmts_rest_layer_name_style_tile_matrix_set_tile_matrix_tile_row_tile_col_j_i import DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileColJI
from agrimetrics_python_sdk.apis.paths.datasets_dataset_id_wcs import DatasetsDatasetIdWcs
from agrimetrics_python_sdk.apis.paths.rest_services_dataset_id_param_one import RestServicesDatasetIdParamOne
from agrimetrics_python_sdk.apis.paths.rest_services_dataset_id_param_one_param_two import RestServicesDatasetIdParamOneParamTwo
from agrimetrics_python_sdk.apis.paths.categories import Categories
from agrimetrics_python_sdk.apis.paths.tags import Tags
from agrimetrics_python_sdk.apis.paths.linked_data_concepts import LinkedDataConcepts
from agrimetrics_python_sdk.apis.paths.data_sets import DataSets
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id import DataSetsDataSetId
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_draft import DataSetsDataSetIdDraft
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_draft_status import DataSetsDataSetIdDraftStatus
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_file_dataset import DataSetsDataSetIdFileDataset
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_access import DataSetsDataSetIdAccess
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_validation_report import DataSetsDataSetIdValidationReport
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_draft_validation_report import DataSetsDataSetIdDraftValidationReport
from agrimetrics_python_sdk.apis.paths.images_image_type_image_id import ImagesImageTypeImageId
from agrimetrics_python_sdk.apis.paths.data_sets_data_set_id_image import DataSetsDataSetIdImage
from agrimetrics_python_sdk.apis.paths.access_requests import AccessRequests
from agrimetrics_python_sdk.apis.paths.access_requests_request_id import AccessRequestsRequestId
from agrimetrics_python_sdk.apis.paths._import import ModelImport
from agrimetrics_python_sdk.apis.paths.templates import Templates
from agrimetrics_python_sdk.apis.paths.templates_template_id import TemplatesTemplateId
from agrimetrics_python_sdk.apis.paths.harvest_group_csw import HarvestGroupCsw
from agrimetrics_python_sdk.apis.paths.harvest_group_dcat import HarvestGroupDcat

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTHENTICATE: Authenticate,
        PathValues.STATUS: Status,
        PathValues.QUERY: Query,
        PathValues.DATASETS_DATASET_ID: DatasetsDatasetId,
        PathValues.DATASETS_DATASET_ID_LAYERS: DatasetsDatasetIdLayers,
        PathValues.SHAPEFILE: Shapefile,
        PathValues.LAYERS_LAYER_ID: LayersLayerId,
        PathValues.LAYERS_LAYER_ID_FILES: LayersLayerIdFiles,
        PathValues.LAYERS_LAYER_ID_INGEST: LayersLayerIdIngest,
        PathValues.LAYERS_LAYER_ID_STYLE: LayersLayerIdStyle,
        PathValues.LAYERS_LAYER_ID_SEARCH: LayersLayerIdSearch,
        PathValues.LAYERS_LAYER_ID_SEARCH_COST: LayersLayerIdSearchCost,
        PathValues.LAYERS_LAYER_ID_SEARCH_STATISTICS: LayersLayerIdSearchStatistics,
        PathValues.SERVICE_DEFINITION: ServiceDefinition,
        PathValues.SERVICE_DEFINITION_LAYER_ID: ServiceDefinitionLayerId,
        PathValues.DATAREQUESTS: DataRequests,
        PathValues.DATAREQUESTS_REQUEST_ID: DataRequestsRequestId,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_APPROVE: DataRequestsUniqueLinkIdApprove,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_REJECT: DataRequestsUniqueLinkIdReject,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_GEOMETRY: DataRequestsUniqueLinkIdGeometry,
        PathValues.DATAREQUESTS_REQUEST_ID_DOWNLOAD: DataRequestsRequestIdDownload,
        PathValues.DATASETS_SWAGGERUI_SWAGGER_FILE: DatasetsSwaggerUiSwaggerFile,
        PathValues.DATASETS_APICSS_CSS_FILE: DatasetsApicssCssFile,
        PathValues.DATASETS_DATASET_ID_WMS: DatasetsDatasetIdWms,
        PathValues.DATASETS_DATASET_ID_WMTS: DatasetsDatasetIdWmts,
        PathValues.DATASETS_DATASET_ID_WFS: DatasetsDatasetIdWfs,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1: DatasetsDatasetIdOgcFeaturesV1,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_OPENAPI: DatasetsDatasetIdOgcFeaturesV1Openapi,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_CONFORMANCE: DatasetsDatasetIdOgcFeaturesV1Conformance,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_FUNCTIONS: DatasetsDatasetIdOgcFeaturesV1Functions,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS: DatasetsDatasetIdOgcFeaturesV1Collections,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionId,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_QUERYABLES: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdQueryables,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_ITEMS: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItems,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_ITEMS_FEATURE_ID: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItemsFeatureId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1: DatasetsDatasetIdOgcTilesV1,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_CONFORMANCE: DatasetsDatasetIdOgcTilesV1Conformance,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS: DatasetsDatasetIdOgcTilesV1Collections,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID: DatasetsDatasetIdOgcTilesV1CollectionsCollectionId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_QUERYABLES: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdQueryables,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_TILES_TILE_MATRIX_SET_ID: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdTilesTileMatrixSetId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_MAP_TILES_TILE_MATRIX_SET_ID_TILE_MATRIX_TILE_ROW_TILE_COL: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdMapTilesTileMatrixSetIdTileMatrixTileRowTileCol,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_TILE_MATRIX_SETS: DatasetsDatasetIdOgcTilesV1TileMatrixSets,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_TILE_MATRIX_SETS_TILE_MATRIX_SET_ID: DatasetsDatasetIdOgcTilesV1TileMatrixSetsTileMatrixSetId,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILEJSON_IMAGE_FORMAT: DatasetsDatasetIdWmtsRestLayerNameStyleTilejsonImageFormat,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILE_MATRIX_SET_TILE_MATRIX_TILE_ROW_TILE_COL: DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileCol,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILE_MATRIX_SET_TILE_MATRIX_TILE_ROW_TILE_COL_J_I: DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileColJI,
        PathValues.DATASETS_DATASET_ID_WCS: DatasetsDatasetIdWcs,
        PathValues.REST_SERVICES_DATASET_ID_PARAM_ONE: RestServicesDatasetIdParamOne,
        PathValues.REST_SERVICES_DATASET_ID_PARAM_ONE_PARAM_TWO: RestServicesDatasetIdParamOneParamTwo,
        PathValues.CATEGORIES: Categories,
        PathValues.TAGS: Tags,
        PathValues.LINKEDDATA_CONCEPTS: LinkedDataConcepts,
        PathValues.DATASETS: DataSets,
        PathValues.DATASETS_DATA_SET_ID: DataSetsDataSetId,
        PathValues.DATASETS_DATA_SET_ID_DRAFT: DataSetsDataSetIdDraft,
        PathValues.DATASETS_DATA_SET_ID_DRAFTSTATUS: DataSetsDataSetIdDraftStatus,
        PathValues.DATASETS_DATA_SET_ID_FILE_DATASET: DataSetsDataSetIdFileDataset,
        PathValues.DATASETS_DATA_SET_ID_ACCESS: DataSetsDataSetIdAccess,
        PathValues.DATASETS_DATA_SET_ID_VALIDATION_REPORT: DataSetsDataSetIdValidationReport,
        PathValues.DATASETS_DATA_SET_ID_DRAFT_VALIDATION_REPORT: DataSetsDataSetIdDraftValidationReport,
        PathValues.IMAGES_IMAGE_TYPE_IMAGE_ID: ImagesImageTypeImageId,
        PathValues.DATASETS_DATA_SET_ID_IMAGE: DataSetsDataSetIdImage,
        PathValues.ACCESSREQUESTS: AccessRequests,
        PathValues.ACCESSREQUESTS_REQUEST_ID: AccessRequestsRequestId,
        PathValues.IMPORT: ModelImport,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.HARVEST_GROUP_CSW: HarvestGroupCsw,
        PathValues.HARVEST_GROUP_DCAT: HarvestGroupDcat,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTHENTICATE: Authenticate,
        PathValues.STATUS: Status,
        PathValues.QUERY: Query,
        PathValues.DATASETS_DATASET_ID: DatasetsDatasetId,
        PathValues.DATASETS_DATASET_ID_LAYERS: DatasetsDatasetIdLayers,
        PathValues.SHAPEFILE: Shapefile,
        PathValues.LAYERS_LAYER_ID: LayersLayerId,
        PathValues.LAYERS_LAYER_ID_FILES: LayersLayerIdFiles,
        PathValues.LAYERS_LAYER_ID_INGEST: LayersLayerIdIngest,
        PathValues.LAYERS_LAYER_ID_STYLE: LayersLayerIdStyle,
        PathValues.LAYERS_LAYER_ID_SEARCH: LayersLayerIdSearch,
        PathValues.LAYERS_LAYER_ID_SEARCH_COST: LayersLayerIdSearchCost,
        PathValues.LAYERS_LAYER_ID_SEARCH_STATISTICS: LayersLayerIdSearchStatistics,
        PathValues.SERVICE_DEFINITION: ServiceDefinition,
        PathValues.SERVICE_DEFINITION_LAYER_ID: ServiceDefinitionLayerId,
        PathValues.DATAREQUESTS: DataRequests,
        PathValues.DATAREQUESTS_REQUEST_ID: DataRequestsRequestId,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_APPROVE: DataRequestsUniqueLinkIdApprove,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_REJECT: DataRequestsUniqueLinkIdReject,
        PathValues.DATAREQUESTS_UNIQUE_LINK_ID_GEOMETRY: DataRequestsUniqueLinkIdGeometry,
        PathValues.DATAREQUESTS_REQUEST_ID_DOWNLOAD: DataRequestsRequestIdDownload,
        PathValues.DATASETS_SWAGGERUI_SWAGGER_FILE: DatasetsSwaggerUiSwaggerFile,
        PathValues.DATASETS_APICSS_CSS_FILE: DatasetsApicssCssFile,
        PathValues.DATASETS_DATASET_ID_WMS: DatasetsDatasetIdWms,
        PathValues.DATASETS_DATASET_ID_WMTS: DatasetsDatasetIdWmts,
        PathValues.DATASETS_DATASET_ID_WFS: DatasetsDatasetIdWfs,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1: DatasetsDatasetIdOgcFeaturesV1,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_OPENAPI: DatasetsDatasetIdOgcFeaturesV1Openapi,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_CONFORMANCE: DatasetsDatasetIdOgcFeaturesV1Conformance,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_FUNCTIONS: DatasetsDatasetIdOgcFeaturesV1Functions,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS: DatasetsDatasetIdOgcFeaturesV1Collections,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionId,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_QUERYABLES: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdQueryables,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_ITEMS: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItems,
        PathValues.DATASETS_DATASET_ID_OGC_FEATURES_V1_COLLECTIONS_COLLECTION_ID_ITEMS_FEATURE_ID: DatasetsDatasetIdOgcFeaturesV1CollectionsCollectionIdItemsFeatureId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1: DatasetsDatasetIdOgcTilesV1,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_CONFORMANCE: DatasetsDatasetIdOgcTilesV1Conformance,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS: DatasetsDatasetIdOgcTilesV1Collections,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID: DatasetsDatasetIdOgcTilesV1CollectionsCollectionId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_QUERYABLES: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdQueryables,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_TILES_TILE_MATRIX_SET_ID: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdTilesTileMatrixSetId,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_COLLECTIONS_COLLECTION_ID_MAP_TILES_TILE_MATRIX_SET_ID_TILE_MATRIX_TILE_ROW_TILE_COL: DatasetsDatasetIdOgcTilesV1CollectionsCollectionIdMapTilesTileMatrixSetIdTileMatrixTileRowTileCol,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_TILE_MATRIX_SETS: DatasetsDatasetIdOgcTilesV1TileMatrixSets,
        PathValues.DATASETS_DATASET_ID_OGC_TILES_V1_TILE_MATRIX_SETS_TILE_MATRIX_SET_ID: DatasetsDatasetIdOgcTilesV1TileMatrixSetsTileMatrixSetId,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILEJSON_IMAGE_FORMAT: DatasetsDatasetIdWmtsRestLayerNameStyleTilejsonImageFormat,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILE_MATRIX_SET_TILE_MATRIX_TILE_ROW_TILE_COL: DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileCol,
        PathValues.DATASETS_DATASET_ID_WMTS_REST_LAYER_NAME_STYLE_TILE_MATRIX_SET_TILE_MATRIX_TILE_ROW_TILE_COL_J_I: DatasetsDatasetIdWmtsRestLayerNameStyleTileMatrixSetTileMatrixTileRowTileColJI,
        PathValues.DATASETS_DATASET_ID_WCS: DatasetsDatasetIdWcs,
        PathValues.REST_SERVICES_DATASET_ID_PARAM_ONE: RestServicesDatasetIdParamOne,
        PathValues.REST_SERVICES_DATASET_ID_PARAM_ONE_PARAM_TWO: RestServicesDatasetIdParamOneParamTwo,
        PathValues.CATEGORIES: Categories,
        PathValues.TAGS: Tags,
        PathValues.LINKEDDATA_CONCEPTS: LinkedDataConcepts,
        PathValues.DATASETS: DataSets,
        PathValues.DATASETS_DATA_SET_ID: DataSetsDataSetId,
        PathValues.DATASETS_DATA_SET_ID_DRAFT: DataSetsDataSetIdDraft,
        PathValues.DATASETS_DATA_SET_ID_DRAFTSTATUS: DataSetsDataSetIdDraftStatus,
        PathValues.DATASETS_DATA_SET_ID_FILE_DATASET: DataSetsDataSetIdFileDataset,
        PathValues.DATASETS_DATA_SET_ID_ACCESS: DataSetsDataSetIdAccess,
        PathValues.DATASETS_DATA_SET_ID_VALIDATION_REPORT: DataSetsDataSetIdValidationReport,
        PathValues.DATASETS_DATA_SET_ID_DRAFT_VALIDATION_REPORT: DataSetsDataSetIdDraftValidationReport,
        PathValues.IMAGES_IMAGE_TYPE_IMAGE_ID: ImagesImageTypeImageId,
        PathValues.DATASETS_DATA_SET_ID_IMAGE: DataSetsDataSetIdImage,
        PathValues.ACCESSREQUESTS: AccessRequests,
        PathValues.ACCESSREQUESTS_REQUEST_ID: AccessRequestsRequestId,
        PathValues.IMPORT: ModelImport,
        PathValues.TEMPLATES: Templates,
        PathValues.TEMPLATES_TEMPLATE_ID: TemplatesTemplateId,
        PathValues.HARVEST_GROUP_CSW: HarvestGroupCsw,
        PathValues.HARVEST_GROUP_DCAT: HarvestGroupDcat,
    }
)
