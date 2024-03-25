<div align="center">

[![Visit Agrimetrics](./header.png)](https://agrimetrics.co.uk)

# Agrimetrics<a id="agrimetrics"></a>

This API lists data sets available on Agrimetrics platform.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`agrimetrics.access_request.create_new_request`](#agrimetricsaccess_requestcreate_new_request)
  * [`agrimetrics.access_request.delete_request_by_id`](#agrimetricsaccess_requestdelete_request_by_id)
  * [`agrimetrics.access_request.list`](#agrimetricsaccess_requestlist)
  * [`agrimetrics.admin.create_new_definition`](#agrimetricsadmincreate_new_definition)
  * [`agrimetrics.admin.delete_by_id`](#agrimetricsadmindelete_by_id)
  * [`agrimetrics.admin.delete_layer`](#agrimetricsadmindelete_layer)
  * [`agrimetrics.admin.get_by_layer_id`](#agrimetricsadminget_by_layer_id)
  * [`agrimetrics.admin.ingest_file`](#agrimetricsadminingest_file)
  * [`agrimetrics.admin.ingest_file_new_layer`](#agrimetricsadminingest_file_new_layer)
  * [`agrimetrics.admin.remove_file`](#agrimetricsadminremove_file)
  * [`agrimetrics.admin.update_existing_definition`](#agrimetricsadminupdate_existing_definition)
  * [`agrimetrics.authentication.get_jwt`](#agrimetricsauthenticationget_jwt)
  * [`agrimetrics.dataset.create_file_dataset`](#agrimetricsdatasetcreate_file_dataset)
  * [`agrimetrics.dataset.create_single_catalog_entry`](#agrimetricsdatasetcreate_single_catalog_entry)
  * [`agrimetrics.dataset.delete_single_data_set`](#agrimetricsdatasetdelete_single_data_set)
  * [`agrimetrics.dataset.discard_draft_changes`](#agrimetricsdatasetdiscard_draft_changes)
  * [`agrimetrics.dataset.get_draft_changes`](#agrimetricsdatasetget_draft_changes)
  * [`agrimetrics.dataset.get_entitlements`](#agrimetricsdatasetget_entitlements)
  * [`agrimetrics.dataset.get_file_dataset_id`](#agrimetricsdatasetget_file_dataset_id)
  * [`agrimetrics.dataset.get_non_spatial_data_for_group`](#agrimetricsdatasetget_non_spatial_data_for_group)
  * [`agrimetrics.dataset.get_single_catalog_entry`](#agrimetricsdatasetget_single_catalog_entry)
  * [`agrimetrics.dataset.get_validation_report`](#agrimetricsdatasetget_validation_report)
  * [`agrimetrics.dataset.get_validation_report_0`](#agrimetricsdatasetget_validation_report_0)
  * [`agrimetrics.dataset.list_all_data_sets`](#agrimetricsdatasetlist_all_data_sets)
  * [`agrimetrics.dataset.list_valid_categories`](#agrimetricsdatasetlist_valid_categories)
  * [`agrimetrics.dataset.list_valid_tags`](#agrimetricsdatasetlist_valid_tags)
  * [`agrimetrics.dataset.set_entitlements`](#agrimetricsdatasetset_entitlements)
  * [`agrimetrics.dataset.set_image`](#agrimetricsdatasetset_image)
  * [`agrimetrics.dataset.update_single_catalog_entry`](#agrimetricsdatasetupdate_single_catalog_entry)
  * [`agrimetrics.dataset.update_single_entry`](#agrimetricsdatasetupdate_single_entry)
  * [`agrimetrics.esri.rest_service_query`](#agrimetricsesrirest_service_query)
  * [`agrimetrics.esri.rest_service_query_0`](#agrimetricsesrirest_service_query_0)
  * [`agrimetrics.graph.list_concepts`](#agrimetricsgraphlist_concepts)
  * [`agrimetrics.harvest.xml_data_on_group`](#agrimetricsharvestxml_data_on_group)
  * [`agrimetrics.harvest.xml_data_on_group_post`](#agrimetricsharvestxml_data_on_group_post)
  * [`agrimetrics.image.get_raw_image`](#agrimetricsimageget_raw_image)
  * [`agrimetrics.import.data_sets`](#agrimetricsimportdata_sets)
  * [`agrimetrics.manage_dataset.ingest_file_new_layer`](#agrimetricsmanage_datasetingest_file_new_layer)
  * [`agrimetrics.manage_layer.add_geo_tiff`](#agrimetricsmanage_layeradd_geo_tiff)
  * [`agrimetrics.manage_layer.auto_generate_style`](#agrimetricsmanage_layerauto_generate_style)
  * [`agrimetrics.manage_layer.delete_layer`](#agrimetricsmanage_layerdelete_layer)
  * [`agrimetrics.manage_layer.get_style`](#agrimetricsmanage_layerget_style)
  * [`agrimetrics.manage_layer.ingest_file`](#agrimetricsmanage_layeringest_file)
  * [`agrimetrics.manage_layer.remove_file`](#agrimetricsmanage_layerremove_file)
  * [`agrimetrics.manage_layer.remove_style`](#agrimetricsmanage_layerremove_style)
  * [`agrimetrics.manage_layer.set_style`](#agrimetricsmanage_layerset_style)
  * [`agrimetrics.ogc_api_tiles.get_conformance`](#agrimetricsogc_api_tilesget_conformance)
  * [`agrimetrics.ogc_api_tiles.get_query_tiles_collection`](#agrimetricsogc_api_tilesget_query_tiles_collection)
  * [`agrimetrics.ogc_api_tiles.get_tiles_collection`](#agrimetricsogc_api_tilesget_tiles_collection)
  * [`agrimetrics.ogc_api_tiles.query_collection_by_id`](#agrimetricsogc_api_tilesquery_collection_by_id)
  * [`agrimetrics.ogc_api_tiles.query_collection_queryables`](#agrimetricsogc_api_tilesquery_collection_queryables)
  * [`agrimetrics.ogc_api_tiles.query_collections`](#agrimetricsogc_api_tilesquery_collections)
  * [`agrimetrics.ogc_api_tiles.query_tile_matrix_sets`](#agrimetricsogc_api_tilesquery_tile_matrix_sets)
  * [`agrimetrics.ogc_api_tiles.query_tile_matrix_sets_0`](#agrimetricsogc_api_tilesquery_tile_matrix_sets_0)
  * [`agrimetrics.ogc_api_tiles.query_tiles_v1`](#agrimetricsogc_api_tilesquery_tiles_v1)
  * [`agrimetrics.ogcapi.features_query`](#agrimetricsogcapifeatures_query)
  * [`agrimetrics.ogcapi.features_query_0`](#agrimetricsogcapifeatures_query_0)
  * [`agrimetrics.ogcapi.features_query_conformance`](#agrimetricsogcapifeatures_query_conformance)
  * [`agrimetrics.ogcapi.features_query_ogc`](#agrimetricsogcapifeatures_query_ogc)
  * [`agrimetrics.ogcapi.features_queryables`](#agrimetricsogcapifeatures_queryables)
  * [`agrimetrics.ogcapi.get_style_for_css_file`](#agrimetricsogcapiget_style_for_css_file)
  * [`agrimetrics.ogcapi.get_swagger_file`](#agrimetricsogcapiget_swagger_file)
  * [`agrimetrics.ogcapi.query_features_collection`](#agrimetricsogcapiquery_features_collection)
  * [`agrimetrics.ogcapi.query_features_collection_items`](#agrimetricsogcapiquery_features_collection_items)
  * [`agrimetrics.ogcapi.query_features_function`](#agrimetricsogcapiquery_features_function)
  * [`agrimetrics.ogcapi.query_features_openapi`](#agrimetricsogcapiquery_features_openapi)
  * [`agrimetrics.query_dataset.list_layers_within_dataset`](#agrimetricsquery_datasetlist_layers_within_dataset)
  * [`agrimetrics.query_layer.calculate_cost`](#agrimetricsquery_layercalculate_cost)
  * [`agrimetrics.query_layer.calculate_statistics_within_geometry`](#agrimetricsquery_layercalculate_statistics_within_geometry)
  * [`agrimetrics.query_layer.cut_shape_boundary_and_retrieve`](#agrimetricsquery_layercut_shape_boundary_and_retrieve)
  * [`agrimetrics.query_layer.metadata`](#agrimetricsquery_layermetadata)
  * [`agrimetrics.query_layer.search_geometry`](#agrimetricsquery_layersearch_geometry)
  * [`agrimetrics.service_definition.create_new_definition`](#agrimetricsservice_definitioncreate_new_definition)
  * [`agrimetrics.service_definition.delete_by_id`](#agrimetricsservice_definitiondelete_by_id)
  * [`agrimetrics.service_definition.get_by_layer_id`](#agrimetricsservice_definitionget_by_layer_id)
  * [`agrimetrics.service_definition.update_existing_definition`](#agrimetricsservice_definitionupdate_existing_definition)
  * [`agrimetrics.shapefile.convert_to_geo_json`](#agrimetricsshapefileconvert_to_geo_json)
  * [`agrimetrics.status.get_catalog_api_status`](#agrimetricsstatusget_catalog_api_status)
  * [`agrimetrics.status.set_draft_status`](#agrimetricsstatusset_draft_status)
  * [`agrimetrics.template.create_catalog_entry`](#agrimetricstemplatecreate_catalog_entry)
  * [`agrimetrics.template.delete_specific_template`](#agrimetricstemplatedelete_specific_template)
  * [`agrimetrics.template.get_specific_template`](#agrimetricstemplateget_specific_template)
  * [`agrimetrics.template.list_permissions_to_view`](#agrimetricstemplatelist_permissions_to_view)
  * [`agrimetrics.template.update_template_item`](#agrimetricstemplateupdate_template_item)
  * [`agrimetrics.template.update_template_item_0`](#agrimetricstemplateupdate_template_item_0)
  * [`agrimetrics.wcs.query_data`](#agrimetricswcsquery_data)
  * [`agrimetrics.wcs.query_data_0`](#agrimetricswcsquery_data_0)
  * [`agrimetrics.wfs.query_data_open_gis`](#agrimetricswfsquery_data_open_gis)
  * [`agrimetrics.wfs.query_data_open_gis_0`](#agrimetricswfsquery_data_open_gis_0)
  * [`agrimetrics.wfs.query_data_with_open_gis`](#agrimetricswfsquery_data_with_open_gis)
  * [`agrimetrics.wms.query_layer_with_open_gis`](#agrimetricswmsquery_layer_with_open_gis)
  * [`agrimetrics.wms.query_with_open_gis`](#agrimetricswmsquery_with_open_gis)
  * [`agrimetrics.wmts.query_data_set_wmts`](#agrimetricswmtsquery_data_set_wmts)
  * [`agrimetrics.wmts_rest.query_tile_matrix_set`](#agrimetricswmts_restquery_tile_matrix_set)
  * [`agrimetrics.wmts_rest.query_tilejson_image_format`](#agrimetricswmts_restquery_tilejson_image_format)
  * [`agrimetrics.wmts_rest.service_query`](#agrimetricswmts_restservice_query)
  * [`agrimetrics.data_request.create_single_access_request`](#agrimetricsdata_requestcreate_single_access_request)
  * [`agrimetrics.data_request.get_geo_json_geometry`](#agrimetricsdata_requestget_geo_json_geometry)
  * [`agrimetrics.data_request.get_requested_data`](#agrimetricsdata_requestget_requested_data)
  * [`agrimetrics.data_request.get_results`](#agrimetricsdata_requestget_results)
  * [`agrimetrics.data_request.grant_user_access`](#agrimetricsdata_requestgrant_user_access)
  * [`agrimetrics.data_request.list_user_access_requests`](#agrimetricsdata_requestlist_user_access_requests)
  * [`agrimetrics.data_request.reject_user_access`](#agrimetricsdata_requestreject_user_access)
  * [`agrimetrics.data_request.update_request`](#agrimetricsdata_requestupdate_request)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Agrimetrics&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from agrimetrics_python_sdk import Agrimetrics, ApiException

agrimetrics = Agrimetrics(
)

try:
    agrimetrics.access_request.create_new_request(
        data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
        requesting_entity_id="string_example",
        request_message="string_example",
        requester_name="string_example",
        requester_email="string_example",
    )
except ApiException as e:
    print("Exception when calling AccessRequestApi.create_new_request: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from agrimetrics_python_sdk import Agrimetrics, ApiException

agrimetrics = Agrimetrics(
)

async def main():
    try:
        await agrimetrics.access_request.acreate_new_request(
            data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
            requesting_entity_id="string_example",
            request_message="string_example",
            requester_name="string_example",
            requester_email="string_example",
        )
    except ApiException as e:
        print("Exception when calling AccessRequestApi.create_new_request: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from agrimetrics_python_sdk import Agrimetrics, ApiException

agrimetrics = Agrimetrics(
)

try:
    create_new_request_response = agrimetrics.access_request.raw.create_new_request(
        data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
        requesting_entity_id="string_example",
        request_message="string_example",
        requester_name="string_example",
        requester_email="string_example",
    )
    pprint(create_new_request_response.headers)
    pprint(create_new_request_response.status)
    pprint(create_new_request_response.round_trip_time)
except ApiException as e:
    print("Exception when calling AccessRequestApi.create_new_request: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `agrimetrics.access_request.create_new_request`<a id="agrimetricsaccess_requestcreate_new_request"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.access_request.create_new_request(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    requesting_entity_id="string_example",
    request_message="string_example",
    requester_name="string_example",
    requester_email="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

The ID of a dataset in the catalog

##### requesting_entity_id: `str`<a id="requesting_entity_id-str"></a>

ID for the entity which is requesting access.

##### request_message: `str`<a id="request_message-str"></a>

Free text message provided by the user when requesting access.

##### requester_name: `str`<a id="requester_name-str"></a>

Name of the user who requested access.

##### requester_email: `str`<a id="requester_email-str"></a>

Contact email address for the user who requested access.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AccessRequestCreateNewRequestRequest`](./agrimetrics_python_sdk/type/access_request_create_new_request_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.access_request.delete_request_by_id`<a id="agrimetricsaccess_requestdelete_request_by_id"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.access_request.delete_request_by_id(
    request_id="requestId_example",
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    accepted=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

##### accepted: `bool`<a id="accepted-bool"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-requests/{requestId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.access_request.list`<a id="agrimetricsaccess_requestlist"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.access_request.list(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    requesting_entity_id="string_example",
    entity_id=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

##### requesting_entity_id: `str`<a id="requesting_entity_id-str"></a>

##### entity_id: List[`str`]<a id="entity_id-liststr"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/access-requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.create_new_definition`<a id="agrimetricsadmincreate_new_definition"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Create new service definition within a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_definition_response = agrimetrics.admin.create_new_definition(
    dataset_id="a420450f-ef42-4fc9-a137-69456bdad016",
    layer_name="Geospatial Layer",
    service="WCS",
    wfs="Y",
    wcs="Y",
    wms="Y",
    wmts="Y",
    ogc_api_features="Y",
    ogc_api_tiles="Y",
    temporal=True,
    datastore="Datastore Name",
    geoserver_host_name="geoserver-test.agrimetrics.co.uk",
    geometry_field="geom",
    billable={
        "billing_data_type": "billing_data_type_example",
        "billing_credit_type": "billing_credit_type_example",
        "billing_credit_cost": 3.14,
    },
    default_epsg_code=4326,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### layer_name: `str`<a id="layer_name-str"></a>

##### service: `str`<a id="service-str"></a>

##### wfs: `str`<a id="wfs-str"></a>

##### wcs: `str`<a id="wcs-str"></a>

##### wms: `str`<a id="wms-str"></a>

##### wmts: `str`<a id="wmts-str"></a>

##### ogc_api_features: `str`<a id="ogc_api_features-str"></a>

##### ogc_api_tiles: `str`<a id="ogc_api_tiles-str"></a>

##### temporal: `bool`<a id="temporal-bool"></a>

##### datastore: `str`<a id="datastore-str"></a>

##### geoserver_host_name: `str`<a id="geoserver_host_name-str"></a>

##### geometry_field: `str`<a id="geometry_field-str"></a>

##### billable: [`Billable`](./agrimetrics_python_sdk/type/billable.py)<a id="billable-billableagrimetrics_python_sdktypebillablepy"></a>


##### default_epsg_code: `Union[int, float]`<a id="default_epsg_code-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServiceDefinition`](./agrimetrics_python_sdk/type/service_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.delete_by_id`<a id="agrimetricsadmindelete_by_id"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Delete service definition given layer ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.admin.delete_by_id(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.delete_layer`<a id="agrimetricsadmindelete_layer"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Delete the datastore and layer relating to a zip file on a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.admin.delete_layer(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.get_by_layer_id`<a id="agrimetricsadminget_by_layer_id"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Get the service definition for a given layer ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_layer_id_response = agrimetrics.admin.get_by_layer_id(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.ingest_file`<a id="agrimetricsadminingest_file"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Ingest a file that has been uploaded to a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.admin.ingest_file(
    file_id="https://api.agrimetrics.co.uk/file-management/data-sets/5e74c298-515d-408d-8926-974abc696092/files/samplehabitats.zip",
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    file_name="samplehabitats.zip",
    datetime="20130310T180000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### file_name: `str`<a id="file_name-str"></a>

##### datetime: [`ISO8601Datetime`](./agrimetrics_python_sdk/type/iso8601_datetime.py)<a id="datetime-iso8601datetimeagrimetrics_python_sdktypeiso8601_datetimepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageLayerIngestFileRequest`](./agrimetrics_python_sdk/type/manage_layer_ingest_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/ingest` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.ingest_file_new_layer`<a id="agrimetricsadminingest_file_new_layer"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Ingest a file that has been uploaded to the catalog to create a new layer.
See [supported ingest formats](doc:supported-ingest-formats) for supported formats.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ingest_file_new_layer_response = agrimetrics.admin.ingest_file_new_layer(
    file_uri="https://api.agrimetrics.co.uk/file-management/data-sets/5e74c298-515d-408d-8926-974abc696092/files/samplehabitats.zip",
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_uri: `str`<a id="file_uri-str"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageDatasetIngestFileNewLayerRequest`](./agrimetrics_python_sdk/type/manage_dataset_ingest_file_new_layer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NewLayers`](./agrimetrics_python_sdk/pydantic/new_layers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/layers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.remove_file`<a id="agrimetricsadminremove_file"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Remove a file from a layer. When you are deleting a file from a layer, the layer may remain if any other files were ingested onto the same layer. If removing a raster file, provide the fileName query parameter; if removing a vector file, provide the fileUri.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.admin.remove_file(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    file_uri="https://api-test.agrimetrics.co.uk/file-management/data-sets/11111111-2222-3333-4444-55555555555/files/example.zip",
    filename="example.tif",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### file_uri: `str`<a id="file_uri-str"></a>

##### filename: `str`<a id="filename-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/files` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.admin.update_existing_definition`<a id="agrimetricsadminupdate_existing_definition"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Update an existing service definition with billing and coordinates reference system metadata.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_definition_response = agrimetrics.admin.update_existing_definition(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    billable={
        "billing_data_type": "billing_data_type_example",
        "billing_credit_type": "billing_credit_type_example",
        "billing_credit_cost": 3.14,
    },
    default_epsg_code=4326,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### billable: [`Billable`](./agrimetrics_python_sdk/type/billable.py)<a id="billable-billableagrimetrics_python_sdktypebillablepy"></a>


##### default_epsg_code: `Union[int, float]`<a id="default_epsg_code-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServiceDefinitionUpdateExistingDefinitionRequest`](./agrimetrics_python_sdk/type/service_definition_update_existing_definition_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.authentication.get_jwt`<a id="agrimetricsauthenticationget_jwt"></a>

Retrieve an Agrimetrics JWT to be used as additional authentication on specified endpoints

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_jwt_response = agrimetrics.authentication.get_jwt(
    username="string_example",
    password="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### username: `str`<a id="username-str"></a>

Agrimetrics Catalog username

##### password: `str`<a id="password-str"></a>

Agrimetrics Catalog password

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`AuthenticationGetJwtRequest`](./agrimetrics_python_sdk/type/authentication_get_jwt_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`AuthenticationGetJwtResponse`](./agrimetrics_python_sdk/pydantic/authentication_get_jwt_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/authenticate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.create_file_dataset`<a id="agrimetricsdatasetcreate_file_dataset"></a>

Create and attach file dataset. If the file dataset already exists, this will not do anything. Note this should usually be automatically created when creating a catalogue entry.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_file_dataset_response = agrimetrics.dataset.create_file_dataset(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetCreateFileDatasetResponse`](./agrimetrics_python_sdk/pydantic/dataset_create_file_dataset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/fileDataset` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.create_single_catalog_entry`<a id="agrimetricsdatasetcreate_single_catalog_entry"></a>

Creates a single catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_single_catalog_entry_response = agrimetrics.dataset.create_single_catalog_entry(
    body=None,
    tags=[
        "string_example"
    ],
    summary="string_example",
    title="string_example",
    description="string_example",
    id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    entry_type="model",
    exchange="agrimetrics",
    alternative_titles=[
        "string_example"
    ],
    scoring_uri="string_example",
    endpoint_key="string_example",
    is_owner=True,
    publisher="string_example",
    created_at=3.14,
    published=3.14,
    metadata_modified=3.14,
    used_by=[
        {
            "title": "title_example",
            "id": "97130f06-6242-463f-bf19-0dd6f5a58cfb",
            "entry_type": "model",
        }
    ],
    derived_from=[
        None
    ],
    entitlements=[
        "string_example"
    ],
    entitlements_by_identity={
        "key": [
            "string_example"
        ],
    },
    creator="string_example",
    data_reliability="string_example",
    license="string_example",
    licence={
        "text": "text_example",
    },
    landing_page="string_example",
    resources=[
        {
            "url": "url_example",
        }
    ],
    data_formats=[
        {
            "data_format": "data_format_example",
        }
    ],
    pricing_description="string_example",
    spatial_coverage="United Kingdom",
    spatial_resolution=3.14,
    geospatial_extent={
        "north_bound_latitude": 3.14,
        "east_bound_longitude": 3.14,
        "south_bound_latitude": 3.14,
        "west_bound_longitude": 3.14,
    },
    temporal_coverage="0480-02-18-0015-18-22",
    temporal_resolution="P1Y",
    accrual_periodicity="Hourly",
    distributions=[
        {
        }
    ],
    issued="0480-02-18",
    modified=3.14,
    keywords=[
        "string_example"
    ],
    topics=[
        "string_example"
    ],
    workflow_keywords=[
        "string_example"
    ],
    taxonomy_keywords=[
        {
            "value_uri": "http://www.eionet.europa.eu/gemet/concept/4118",
            "value_label": "hydrology",
            "source_uri": "http://inspire.ec.europa.eu/theme",
            "source_label": "GEMET - INSPIRE themes, version 1.0",
        }
    ],
    items="free",
    visibility="visible",
    concepts=[
        "string_example"
    ],
    data_set={
        "type": "file",
    },
    services=[
        {
        }
    ],
    sample_data={
    },
    image={
    },
    coordinate_reference_system_id="string_example",
    spatial_representation_type="string_example",
    lineage="string_example",
    from_template="string_example",
    contacts=[
        {
            "organisation_name": "organisation_name_example",
            "role": "resourceProvider",
        }
    ],
    metadata_contact={
        "organisation_name": "organisation_name_example",
        "role": "resourceProvider",
    },
    public_contact={
        "organisation_name": "organisation_name_example",
        "role": "pointOfContact",
    },
    approval_for_access_number=3.14,
    approval_for_access_status="AfA (Information Requests only)",
    language="string_example",
    character_set="string_example",
    hierarchy_level="string_example",
    metadata_language="string_example",
    metadata_character_set="string_example",
    metadata_standard_name="string_example",
    metadata_standard_version="string_example",
    draft_status="submitted",
    draft_notes="string_example",
    published_status="published",
    template_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### tags: [`DataSetTags`](./agrimetrics_python_sdk/type/data_set_tags.py)<a id="tags-datasettagsagrimetrics_python_sdktypedata_set_tagspy"></a>

##### summary: `str`<a id="summary-str"></a>

Summary of the data set.

##### title: `str`<a id="title-str"></a>

Title for the data set.

##### description: `str`<a id="description-str"></a>

Description of the data set.

##### id: `str`<a id="id-str"></a>

The ID of a dataset in the catalog

##### entry_type: [`EntryType`](./agrimetrics_python_sdk/type/entry_type.py)<a id="entry_type-entrytypeagrimetrics_python_sdktypeentry_typepy"></a>

##### exchange: [`Exchange`](./agrimetrics_python_sdk/type/exchange.py)<a id="exchange-exchangeagrimetrics_python_sdktypeexchangepy"></a>

##### alternative_titles: [`DataSetAlternativeTitles`](./agrimetrics_python_sdk/type/data_set_alternative_titles.py)<a id="alternative_titles-datasetalternativetitlesagrimetrics_python_sdktypedata_set_alternative_titlespy"></a>

##### scoring_uri: `str`<a id="scoring_uri-str"></a>

Scoring URI of the model.

##### endpoint_key: `str`<a id="endpoint_key-str"></a>

Endpoint key for the model.

##### is_owner: `bool`<a id="is_owner-bool"></a>

Whether the current user is the owner of this data set.

##### publisher: `str`<a id="publisher-str"></a>

The ID of the publisher.

##### created_at: `Union[int, float]`<a id="created_at-unionint-float"></a>

Data set creation timestamp.

##### published: `Union[int, float]`<a id="published-unionint-float"></a>

Data set publication timestamp.

##### metadata_modified: `Union[int, float]`<a id="metadata_modified-unionint-float"></a>

Metadata last-modification timestmap.

##### used_by: List[`BasicDataSetInfo`]<a id="used_by-listbasicdatasetinfo"></a>

Other data sets using this data set.

##### derived_from: [`DataSetDerivedFrom`](./agrimetrics_python_sdk/type/data_set_derived_from.py)<a id="derived_from-datasetderivedfromagrimetrics_python_sdktypedata_set_derived_frompy"></a>

##### entitlements: List[[`Entitlement`](./agrimetrics_python_sdk/type/entitlement.py)]<a id="entitlements-listentitlementagrimetrics_python_sdktypeentitlementpy"></a>

Entitlements for the current user.

##### entitlements_by_identity: [`DataSetEntitlementsByIdentity`](./agrimetrics_python_sdk/type/data_set_entitlements_by_identity.py)<a id="entitlements_by_identity-datasetentitlementsbyidentityagrimetrics_python_sdktypedata_set_entitlements_by_identitypy"></a>

##### creator: `str`<a id="creator-str"></a>

Creator of the data set.

##### data_reliability: `str`<a id="data_reliability-str"></a>

Free text description about the reliability of this dataset.

##### license: `str`<a id="license-str"></a>

License of the data set.

##### licence: [`Licence`](./agrimetrics_python_sdk/type/licence.py)<a id="licence-licenceagrimetrics_python_sdktypelicencepy"></a>


##### landing_page: `str`<a id="landing_page-str"></a>

DEPRECATED. This has been replaced with the resources attribute. Reference URI of the data set.

##### resources: List[`Resource`]<a id="resources-listresource"></a>

Links containing more information on the data set

##### data_formats: List[`DataFormat`]<a id="data_formats-listdataformat"></a>

Format of the data set

##### pricing_description: `str`<a id="pricing_description-str"></a>

Pricing description of the data set.

##### spatial_coverage: [`SpatialCoverage`](./agrimetrics_python_sdk/type/spatial_coverage.py)<a id="spatial_coverage-spatialcoverageagrimetrics_python_sdktypespatial_coveragepy"></a>

##### spatial_resolution: `Union[int, float]`<a id="spatial_resolution-unionint-float"></a>

The resolution of data set in meters.

##### geospatial_extent: [`GeospatialExtent`](./agrimetrics_python_sdk/type/geospatial_extent.py)<a id="geospatial_extent-geospatialextentagrimetrics_python_sdktypegeospatial_extentpy"></a>


##### temporal_coverage: `str`<a id="temporal_coverage-str"></a>

The time frame this data set covers.

##### temporal_resolution: `str`<a id="temporal_resolution-str"></a>

The sampling time period of the data set.

##### accrual_periodicity: [`AccrualPeriodicity`](./agrimetrics_python_sdk/type/accrual_periodicity.py)<a id="accrual_periodicity-accrualperiodicityagrimetrics_python_sdktypeaccrual_periodicitypy"></a>

##### distributions: [`DataSetDistributions`](./agrimetrics_python_sdk/type/data_set_distributions.py)<a id="distributions-datasetdistributionsagrimetrics_python_sdktypedata_set_distributionspy"></a>

##### issued: `str`<a id="issued-str"></a>

The date when the data set was issued.

##### modified: `Union[int, float]`<a id="modified-unionint-float"></a>

An timestamp of when the data in this dataset was last updated

##### keywords: [`DataSetKeywords`](./agrimetrics_python_sdk/type/data_set_keywords.py)<a id="keywords-datasetkeywordsagrimetrics_python_sdktypedata_set_keywordspy"></a>

##### topics: List[[`Topic`](./agrimetrics_python_sdk/type/topic.py)]<a id="topics-listtopicagrimetrics_python_sdktypetopicpy"></a>

List of topics on this data set

##### workflow_keywords: List[[`WorkflowKeywords`](./agrimetrics_python_sdk/type/workflow_keywords.py)]<a id="workflow_keywords-listworkflowkeywordsagrimetrics_python_sdktypeworkflow_keywordspy"></a>

List of workflow keywords on this data set

##### taxonomy_keywords: List[`TaxonomyKeywords`]<a id="taxonomy_keywords-listtaxonomykeywords"></a>

List of keywords based on specific taxonomies

##### items: [`CategoryValue`](./agrimetrics_python_sdk/type/category_value.py)<a id="items-categoryvalueagrimetrics_python_sdktypecategory_valuepy"></a>

##### visibility: `str`<a id="visibility-str"></a>

Whether or not this data set should be displayed in the index.

##### concepts: [`DataSetConcepts`](./agrimetrics_python_sdk/type/data_set_concepts.py)<a id="concepts-datasetconceptsagrimetrics_python_sdktypedata_set_conceptspy"></a>

##### data_set: [`DataSetDataSet`](./agrimetrics_python_sdk/type/data_set_data_set.py)<a id="data_set-datasetdatasetagrimetrics_python_sdktypedata_set_data_setpy"></a>


##### services: [`DataSetServices`](./agrimetrics_python_sdk/type/data_set_services.py)<a id="services-datasetservicesagrimetrics_python_sdktypedata_set_servicespy"></a>

##### sample_data: [`DataSetSampleData`](./agrimetrics_python_sdk/type/data_set_sample_data.py)<a id="sample_data-datasetsampledataagrimetrics_python_sdktypedata_set_sample_datapy"></a>


##### image: [`ImageRepresentation`](./agrimetrics_python_sdk/type/image_representation.py)<a id="image-imagerepresentationagrimetrics_python_sdktypeimage_representationpy"></a>


##### coordinate_reference_system_id: `str`<a id="coordinate_reference_system_id-str"></a>

URL to the specification of the coordinate system used in the data

##### spatial_representation_type: `str`<a id="spatial_representation_type-str"></a>

Type of the geospatial data

##### lineage: `str`<a id="lineage-str"></a>

Information about the creation and quality assurance process of the dataset

##### from_template: `str`<a id="from_template-str"></a>

Information about which template was used to create the dataset record

##### contacts: List[`Contact`]<a id="contacts-listcontact"></a>

List of contacts for this data set

##### metadata_contact: [`Contact`](./agrimetrics_python_sdk/type/contact.py)<a id="metadata_contact-contactagrimetrics_python_sdktypecontactpy"></a>


##### public_contact: [`PublicContact`](./agrimetrics_python_sdk/type/public_contact.py)<a id="public_contact-publiccontactagrimetrics_python_sdktypepublic_contactpy"></a>


##### approval_for_access_number: `Union[int, float]`<a id="approval_for_access_number-unionint-float"></a>

Approval for access status number

##### approval_for_access_status: `str`<a id="approval_for_access_status-str"></a>

Approval for access status value

##### language: `str`<a id="language-str"></a>

Language used on the data set

##### character_set: `str`<a id="character_set-str"></a>

Character set used on the data set

##### hierarchy_level: `str`<a id="hierarchy_level-str"></a>

Hierarchy level of the data set

##### metadata_language: `str`<a id="metadata_language-str"></a>

Language used on the metadata

##### metadata_character_set: `str`<a id="metadata_character_set-str"></a>

Character set used on the metadata

##### metadata_standard_name: `str`<a id="metadata_standard_name-str"></a>

##### metadata_standard_version: `str`<a id="metadata_standard_version-str"></a>

##### draft_status: [`DraftStatus`](./agrimetrics_python_sdk/type/draft_status.py)<a id="draft_status-draftstatusagrimetrics_python_sdktypedraft_statuspy"></a>

##### draft_notes: `str`<a id="draft_notes-str"></a>

Any notes added during review of the data set

##### published_status: [`PublishedStatus`](./agrimetrics_python_sdk/type/published_status.py)<a id="published_status-publishedstatusagrimetrics_python_sdktypepublished_statuspy"></a>

##### template_id: `str`<a id="template_id-str"></a>

The ID of a template in the catalog

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatasetCreateSingleCatalogEntryRequest`](./agrimetrics_python_sdk/type/dataset_create_single_catalog_entry_request.py)
The data set to create.

#### 🔄 Return<a id="🔄-return"></a>

[`EntryUpdateResponse`](./agrimetrics_python_sdk/pydantic/entry_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.delete_single_data_set`<a id="agrimetricsdatasetdelete_single_data_set"></a>

Delete a single Data Set

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_single_data_set_response = agrimetrics.dataset.delete_single_data_set(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetDeleteSingleDataSetResponse`](./agrimetrics_python_sdk/pydantic/dataset_delete_single_data_set_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.discard_draft_changes`<a id="agrimetricsdatasetdiscard_draft_changes"></a>

Discards the draft changes on a data set catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.dataset.discard_draft_changes(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/draft` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_draft_changes`<a id="agrimetricsdatasetget_draft_changes"></a>

Get the draft changes on a data set catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_draft_changes_response = agrimetrics.dataset.get_draft_changes(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DataSet`](./agrimetrics_python_sdk/pydantic/data_set.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/draft` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_entitlements`<a id="agrimetricsdatasetget_entitlements"></a>

Gets the entitlements on a data set.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_entitlements_response = agrimetrics.dataset.get_entitlements(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetGetEntitlementsResponse`](./agrimetrics_python_sdk/pydantic/dataset_get_entitlements_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/access` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_file_dataset_id`<a id="agrimetricsdatasetget_file_dataset_id"></a>

Get file dataset id from dataset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_file_dataset_id_response = agrimetrics.dataset.get_file_dataset_id(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetGetFileDatasetIdResponse`](./agrimetrics_python_sdk/pydantic/dataset_get_file_dataset_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/fileDataset` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_non_spatial_data_for_group`<a id="agrimetricsdatasetget_non_spatial_data_for_group"></a>

Get the DCAT metadata for the given group. This will retrieve metadata for all the non spatial datasets in the public domain.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_non_spatial_data_for_group_response = agrimetrics.dataset.get_non_spatial_data_for_group(
    group="apha",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group: [`GroupCode`](./agrimetrics_python_sdk/type/.py)<a id="group-groupcodeagrimetrics_python_sdktypepy"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/harvest/{group}/dcat` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_single_catalog_entry`<a id="agrimetricsdatasetget_single_catalog_entry"></a>

Get a single data set catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_single_catalog_entry_response = agrimetrics.dataset.get_single_catalog_entry(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DataSet`](./agrimetrics_python_sdk/pydantic/data_set.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_validation_report`<a id="agrimetricsdatasetget_validation_report"></a>

Get the schematron validation report using the data sets validation profile. Throws an error if there is no validation profile

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_validation_report_response = agrimetrics.dataset.get_validation_report(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetGetValidationReportResponse`](./agrimetrics_python_sdk/pydantic/dataset_get_validation_report_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/validationReport` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.get_validation_report_0`<a id="agrimetricsdatasetget_validation_report_0"></a>

Get the schematron validation report using the data sets validation profile. Throws an error if there is no validation profile

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_validation_report_0_response = agrimetrics.dataset.get_validation_report_0(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetGetValidationReport200Response`](./agrimetrics_python_sdk/pydantic/dataset_get_validation_report200_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/draft/validationReport` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.list_all_data_sets`<a id="agrimetricsdatasetlist_all_data_sets"></a>

List all data sets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_all_data_sets_response = agrimetrics.dataset.list_all_data_sets(
    ids=[
        "string_example"
    ],
    creator=[
        "string_example"
    ],
    keywords=[
        "string_example"
    ],
    tags=[
        "string_example"
    ],
    tag_relationship="narrower",
    category=[
        "string_example"
    ],
    spatial_coverage=[
        "string_example"
    ],
    text="Weather",
    extended_text="Soil",
    identities=[
        "string_example"
    ],
    only_featured=True,
    show_editable=True,
    show_hidden=True,
    page_num=1,
    page_size=1,
    offset=0,
    search_type="title",
    limit=1,
    legacy_concepts=True,
    sort="title",
    exchange="agrimetrics",
    metadata_standard_name=[
        "string_example"
    ],
    draft_status=[
        "string_example"
    ],
    published_status=[
        None
    ],
    licence=[
        "string_example"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### ids: List[`str`]<a id="ids-liststr"></a>

List of data set ids

##### creator: List[`str`]<a id="creator-liststr"></a>

The creator of the data set.

##### keywords: List[`str`]<a id="keywords-liststr"></a>

Tags describing the data set. keywords is deprecated - use tags instead

##### tags: List[`str`]<a id="tags-liststr"></a>

Tags describing the data set.

##### tag_relationship: [`Relationship`](./agrimetrics_python_sdk/type/.py)<a id="tag_relationship-relationshipagrimetrics_python_sdktypepy"></a>

Note - This feature will no longer be available as we are in the process of moving to a different backend and will soon be removed. If provided, include data sets that have been tagged with concepts that are related to the values provided in the `tags` parameter. If not provided, only include data sets tagged with exact matches.

##### category: List[[`CategoryValue`](./agrimetrics_python_sdk/type/category_value.py)]<a id="category-listcategoryvalueagrimetrics_python_sdktypecategory_valuepy"></a>

Indicates the type of data

##### spatial_coverage: List[[`SpatialCoverage`](./agrimetrics_python_sdk/type/spatial_coverage.py)]<a id="spatial_coverage-listspatialcoverageagrimetrics_python_sdktypespatial_coveragepy"></a>

The region the data is applicable to.

##### text: `str`<a id="text-str"></a>

Note - Use extendedText. This field has been deprecated. Free text search for data sets.

##### extended_text: `str`<a id="extended_text-str"></a>

Free text search for data sets matching title; summary; description; tags; concepts; and source.

##### identities: List[`str`]<a id="identities-liststr"></a>

Only show datasets accessible by these identities. Can be 'PUBLIC', a user ID or an organisation ID.

##### only_featured: `bool`<a id="only_featured-bool"></a>

Defines whether to return only featured data sets

##### show_editable: `bool`<a id="show_editable-bool"></a>

Defines whether my editable data sets should be shown.

##### show_hidden: `bool`<a id="show_hidden-bool"></a>

Defines whether hidden data sets should be shown.

##### page_num: `int`<a id="page_num-int"></a>

Set the page number. Should not be specified in conjunction with offset or limit.

##### page_size: `int`<a id="page_size-int"></a>

Set the page size. Should not be specified in conjunction with offset or limit.

##### offset: `int`<a id="offset-int"></a>

Set the pagination offset. Should not be specified in conjunction with pageNum or pageSize.

##### search_type: `str`<a id="search_type-str"></a>

Choose whether to search across all metadata on a data set, or just the title.

##### limit: `int`<a id="limit-int"></a>

Set the pagination limit. Should not be specified in conjunction with pageNum or pageSize.

##### legacy_concepts: `bool`<a id="legacy_concepts-bool"></a>

Note - This feature will no longer be available once we move to a different backend. \"Format response to convert any new concepts to legacy concepts\"

##### sort: `str`<a id="sort-str"></a>

Criterion by which to order the results

##### exchange: [`Exchange`](./agrimetrics_python_sdk/type/.py)<a id="exchange-exchangeagrimetrics_python_sdktypepy"></a>

The private data exchange for which to retrieve records

##### metadata_standard_name: List[`str`]<a id="metadata_standard_name-liststr"></a>

##### draft_status: List[[`DraftStatus`](./agrimetrics_python_sdk/type/draft_status.py)]<a id="draft_status-listdraftstatusagrimetrics_python_sdktypedraft_statuspy"></a>

##### published_status: List[`Union[PublishedStatus, str]`]<a id="published_status-listunionpublishedstatus-str"></a>

##### licence: List[`str`]<a id="licence-liststr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DataSets`](./agrimetrics_python_sdk/pydantic/data_sets.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.list_valid_categories`<a id="agrimetricsdatasetlist_valid_categories"></a>

List all the valid categories of datasets.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_valid_categories_response = agrimetrics.dataset.list_valid_categories()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Categories`](./agrimetrics_python_sdk/pydantic/categories.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/categories` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.list_valid_tags`<a id="agrimetricsdatasetlist_valid_tags"></a>

List all the valid tags that can be set on a data set.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_valid_tags_response = agrimetrics.dataset.list_valid_tags()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetListValidTagsResponse`](./agrimetrics_python_sdk/pydantic/dataset_list_valid_tags_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tags` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.set_entitlements`<a id="agrimetricsdatasetset_entitlements"></a>

Set the entitlements and on a data set for all identities.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_entitlements_response = agrimetrics.dataset.set_entitlements(
    entitlements=[
        {
            "identity": {
                "type": "user",
            },
            "entitlements": {
                "catalog": {
                },
                "is_admin": True,
            },
        }
    ],
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### entitlements: [`BatchIdentityInputEntitlements`](./agrimetrics_python_sdk/type/batch_identity_input_entitlements.py)<a id="entitlements-batchidentityinputentitlementsagrimetrics_python_sdktypebatch_identity_input_entitlementspy"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DatasetSetEntitlementsRequest`](./agrimetrics_python_sdk/type/dataset_set_entitlements_request.py)
The access to update.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/access` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.set_image`<a id="agrimetricsdatasetset_image"></a>

Set the image for a data set. Can either be an image upload a plain text string representing the unsplash image id.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.dataset.set_image(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/image` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.update_single_catalog_entry`<a id="agrimetricsdatasetupdate_single_catalog_entry"></a>

Updates a single catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_single_catalog_entry_response = agrimetrics.dataset.update_single_catalog_entry(
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    tags=[
        "string_example"
    ],
    summary="string_example",
    title="string_example",
    description="string_example",
    alternative_titles=[
        "string_example"
    ],
    scoring_uri="string_example",
    endpoint_key="string_example",
    derived_from=[
        None
    ],
    creator="string_example",
    data_reliability="string_example",
    license="string_example",
    licence={
        "text": "text_example",
    },
    resources=[
        {
            "url": "url_example",
        }
    ],
    data_formats=[
        {
            "data_format": "data_format_example",
        }
    ],
    spatial_coverage="United Kingdom",
    spatial_resolution=3.14,
    geospatial_extent={
        "north_bound_latitude": 3.14,
        "east_bound_longitude": 3.14,
        "south_bound_latitude": 3.14,
        "west_bound_longitude": 3.14,
    },
    temporal_coverage="0480-02-18-0015-18-22",
    temporal_extent={
        "begin": "begin_example",
    },
    temporal_resolution="P1Y",
    topics=[
        "string_example"
    ],
    workflow_keywords=[
        "string_example"
    ],
    taxonomy_keywords=[
        {
            "value_uri": "http://www.eionet.europa.eu/gemet/concept/4118",
            "value_label": "hydrology",
            "source_uri": "http://inspire.ec.europa.eu/theme",
            "source_label": "GEMET - INSPIRE themes, version 1.0",
        }
    ],
    accrual_periodicity="Hourly",
    issued="0480-02-18",
    created_at=3.14,
    published=3.14,
    published_status="published",
    modified=3.14,
    items="free",
    visibility="visible",
    pricing_description="string_example",
    distributions=[
        {
        }
    ],
    approval_for_access_number=3.14,
    approval_for_access_status="AfA (Information Requests only)",
    contacts=[
        {
            "organisation_name": "organisation_name_example",
            "role": "resourceProvider",
        }
    ],
    metadata_contact={
        "organisation_name": "organisation_name_example",
        "role": "resourceProvider",
    },
    lineage="string_example",
    language="string_example",
    character_set="string_example",
    hierarchy_level="string_example",
    metadata_language="string_example",
    metadata_character_set="string_example",
    metadata_standard_name="string_example",
    metadata_standard_version="string_example",
    coordinate_reference_system_id="string_example",
    spatial_representation_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

##### tags: [`DataSetPatchTags`](./agrimetrics_python_sdk/type/data_set_patch_tags.py)<a id="tags-datasetpatchtagsagrimetrics_python_sdktypedata_set_patch_tagspy"></a>

##### summary: `str`<a id="summary-str"></a>

Summary of the data set.

##### title: `str`<a id="title-str"></a>

Title for the data set.

##### description: `str`<a id="description-str"></a>

Description of the data set.

##### alternative_titles: [`DataSetPatchAlternativeTitles`](./agrimetrics_python_sdk/type/data_set_patch_alternative_titles.py)<a id="alternative_titles-datasetpatchalternativetitlesagrimetrics_python_sdktypedata_set_patch_alternative_titlespy"></a>

##### scoring_uri: `str`<a id="scoring_uri-str"></a>

ScoringURI for the model.

##### endpoint_key: `str`<a id="endpoint_key-str"></a>

Endpoint key for the model.

##### derived_from: [`DataSetPatchDerivedFrom`](./agrimetrics_python_sdk/type/data_set_patch_derived_from.py)<a id="derived_from-datasetpatchderivedfromagrimetrics_python_sdktypedata_set_patch_derived_frompy"></a>

##### creator: `Optional[str]`<a id="creator-optionalstr"></a>

Creator of the data set.

##### data_reliability: `Optional[str]`<a id="data_reliability-optionalstr"></a>

Free text description about the reliability of this dataset.

##### license: `Optional[str]`<a id="license-optionalstr"></a>

License of the data set.

##### licence: [`DataSetPatchLicence`](./agrimetrics_python_sdk/type/data_set_patch_licence.py)<a id="licence-datasetpatchlicenceagrimetrics_python_sdktypedata_set_patch_licencepy"></a>


##### resources: List[`Resource`]<a id="resources-listresource"></a>

Links containing more information on the data set

##### data_formats: List[`DataFormat`]<a id="data_formats-listdataformat"></a>

Format of the data set

##### spatial_coverage: `Optional[str]`<a id="spatial_coverage-optionalstr"></a>

The geo spatial coverage of the data set.

##### spatial_resolution: `Optional[Union[int, float]]`<a id="spatial_resolution-optionalunionint-float"></a>

The resolution of data set in meters.

##### geospatial_extent: [`DataSetPatchGeospatialExtent`](./agrimetrics_python_sdk/type/data_set_patch_geospatial_extent.py)<a id="geospatial_extent-datasetpatchgeospatialextentagrimetrics_python_sdktypedata_set_patch_geospatial_extentpy"></a>


##### temporal_coverage: `Optional[str]`<a id="temporal_coverage-optionalstr"></a>

The time frame this data set covers.

##### temporal_extent: [`DataSetPatchTemporalExtent`](./agrimetrics_python_sdk/type/data_set_patch_temporal_extent.py)<a id="temporal_extent-datasetpatchtemporalextentagrimetrics_python_sdktypedata_set_patch_temporal_extentpy"></a>


##### temporal_resolution: `Optional[str]`<a id="temporal_resolution-optionalstr"></a>

The sampling time period of the data set.

##### topics: List[[`Topic`](./agrimetrics_python_sdk/type/topic.py)]<a id="topics-listtopicagrimetrics_python_sdktypetopicpy"></a>

##### workflow_keywords: List[[`WorkflowKeywords`](./agrimetrics_python_sdk/type/workflow_keywords.py)]<a id="workflow_keywords-listworkflowkeywordsagrimetrics_python_sdktypeworkflow_keywordspy"></a>

List of workflow keywords on this data set

##### taxonomy_keywords: List[`TaxonomyKeywords`]<a id="taxonomy_keywords-listtaxonomykeywords"></a>

List of keywords based on specific taxonomies

##### accrual_periodicity: `Optional[str]`<a id="accrual_periodicity-optionalstr"></a>

The frequency at which data set is published.

##### issued: `Optional[str]`<a id="issued-optionalstr"></a>

The date when the data set was issued.

##### created_at: `Optional[Union[int, float]]`<a id="created_at-optionalunionint-float"></a>

Data set creation timestamp.

##### published: `Optional[Union[int, float]]`<a id="published-optionalunionint-float"></a>

Data set publication timestamp.

##### published_status: [`PublishedStatus`](./agrimetrics_python_sdk/type/published_status.py)<a id="published_status-publishedstatusagrimetrics_python_sdktypepublished_statuspy"></a>

##### modified: `Optional[Union[int, float]]`<a id="modified-optionalunionint-float"></a>

An timestamp of when the data in this dataset was last updated

##### items: [`CategoryValue`](./agrimetrics_python_sdk/type/category_value.py)<a id="items-categoryvalueagrimetrics_python_sdktypecategory_valuepy"></a>

##### visibility: `str`<a id="visibility-str"></a>

Whether or not this data set should be displayed in the index.

##### pricing_description: `str`<a id="pricing_description-str"></a>

Pricing description of the data set.

##### distributions: [`DataSetPatchDistributions`](./agrimetrics_python_sdk/type/data_set_patch_distributions.py)<a id="distributions-datasetpatchdistributionsagrimetrics_python_sdktypedata_set_patch_distributionspy"></a>

##### approval_for_access_number: `Optional[Union[int, float]]`<a id="approval_for_access_number-optionalunionint-float"></a>

Approval for access status number

##### approval_for_access_status: `Optional[str]`<a id="approval_for_access_status-optionalstr"></a>

Approval for access status value

##### contacts: List[`Contact`]<a id="contacts-listcontact"></a>

List of contacts for this data set

##### metadata_contact: [`DataSetPatchMetadataContact`](./agrimetrics_python_sdk/type/data_set_patch_metadata_contact.py)<a id="metadata_contact-datasetpatchmetadatacontactagrimetrics_python_sdktypedata_set_patch_metadata_contactpy"></a>


##### lineage: `Optional[str]`<a id="lineage-optionalstr"></a>

Information about the creation and quality assurance process of the dataset

##### language: `Optional[str]`<a id="language-optionalstr"></a>

Language used on the data set

##### character_set: `Optional[str]`<a id="character_set-optionalstr"></a>

Character set used on the data set

##### hierarchy_level: `Optional[str]`<a id="hierarchy_level-optionalstr"></a>

Hierarchy level of the data set

##### metadata_language: `Optional[str]`<a id="metadata_language-optionalstr"></a>

Language used on the metadata

##### metadata_character_set: `Optional[str]`<a id="metadata_character_set-optionalstr"></a>

Character set used on the metadata

##### metadata_standard_name: `Optional[str]`<a id="metadata_standard_name-optionalstr"></a>

##### metadata_standard_version: `Optional[str]`<a id="metadata_standard_version-optionalstr"></a>

##### coordinate_reference_system_id: `Optional[str]`<a id="coordinate_reference_system_id-optionalstr"></a>

URL to the specification of the coordinate system used in the data

##### spatial_representation_type: `Optional[str]`<a id="spatial_representation_type-optionalstr"></a>

Type of the geospatial data

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataSetPatch`](./agrimetrics_python_sdk/type/data_set_patch.py)
The updated data set information.

#### 🔄 Return<a id="🔄-return"></a>

[`DataSet`](./agrimetrics_python_sdk/pydantic/data_set.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.dataset.update_single_entry`<a id="agrimetricsdatasetupdate_single_entry"></a>

Updates a single catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_single_entry_response = agrimetrics.dataset.update_single_entry(
    title="string_example",
    description="string_example",
    entry_type="model",
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    tags=[
        "string_example"
    ],
    summary="string_example",
    id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    exchange="agrimetrics",
    alternative_titles=[
        "string_example"
    ],
    scoring_uri="string_example",
    endpoint_key="string_example",
    is_owner=True,
    publisher="string_example",
    created_at=3.14,
    published=3.14,
    metadata_modified=3.14,
    used_by=[
        {
            "title": "title_example",
            "id": "97130f06-6242-463f-bf19-0dd6f5a58cfb",
            "entry_type": "model",
        }
    ],
    derived_from=[
        None
    ],
    entitlements=[
        "string_example"
    ],
    entitlements_by_identity={
        "key": [
            "string_example"
        ],
    },
    creator="string_example",
    data_reliability="string_example",
    license="string_example",
    licence={
        "text": "text_example",
    },
    landing_page="string_example",
    resources=[
        {
            "url": "url_example",
        }
    ],
    data_formats=[
        {
            "data_format": "data_format_example",
        }
    ],
    pricing_description="string_example",
    spatial_coverage="United Kingdom",
    spatial_resolution=3.14,
    geospatial_extent={
        "north_bound_latitude": 3.14,
        "east_bound_longitude": 3.14,
        "south_bound_latitude": 3.14,
        "west_bound_longitude": 3.14,
    },
    temporal_coverage="0480-02-18-0015-18-22",
    temporal_resolution="P1Y",
    accrual_periodicity="Hourly",
    distributions=[
        {
        }
    ],
    issued="0480-02-18",
    modified=3.14,
    keywords=[
        "string_example"
    ],
    topics=[
        "string_example"
    ],
    workflow_keywords=[
        "string_example"
    ],
    taxonomy_keywords=[
        {
            "value_uri": "http://www.eionet.europa.eu/gemet/concept/4118",
            "value_label": "hydrology",
            "source_uri": "http://inspire.ec.europa.eu/theme",
            "source_label": "GEMET - INSPIRE themes, version 1.0",
        }
    ],
    items="free",
    visibility="visible",
    concepts=[
        "string_example"
    ],
    data_set={
        "type": "file",
    },
    services=[
        {
        }
    ],
    sample_data={
    },
    image={
    },
    coordinate_reference_system_id="string_example",
    spatial_representation_type="string_example",
    lineage="string_example",
    from_template="string_example",
    contacts=[
        {
            "organisation_name": "organisation_name_example",
            "role": "resourceProvider",
        }
    ],
    metadata_contact={
        "organisation_name": "organisation_name_example",
        "role": "resourceProvider",
    },
    public_contact={
        "organisation_name": "organisation_name_example",
        "role": "pointOfContact",
    },
    approval_for_access_number=3.14,
    approval_for_access_status="AfA (Information Requests only)",
    language="string_example",
    character_set="string_example",
    hierarchy_level="string_example",
    metadata_language="string_example",
    metadata_character_set="string_example",
    metadata_standard_name="string_example",
    metadata_standard_version="string_example",
    draft_status="submitted",
    draft_notes="string_example",
    published_status="published",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### title: `str`<a id="title-str"></a>

Title for the data set.

##### description: `str`<a id="description-str"></a>

Description of the data set.

##### entry_type: [`EntryType`](./agrimetrics_python_sdk/type/entry_type.py)<a id="entry_type-entrytypeagrimetrics_python_sdktypeentry_typepy"></a>

##### data_set_id: `str`<a id="data_set_id-str"></a>

##### tags: [`DataSetTags`](./agrimetrics_python_sdk/type/data_set_tags.py)<a id="tags-datasettagsagrimetrics_python_sdktypedata_set_tagspy"></a>

##### summary: `str`<a id="summary-str"></a>

Summary of the data set.

##### id: `str`<a id="id-str"></a>

The ID of a dataset in the catalog

##### exchange: [`Exchange`](./agrimetrics_python_sdk/type/exchange.py)<a id="exchange-exchangeagrimetrics_python_sdktypeexchangepy"></a>

##### alternative_titles: [`DataSetAlternativeTitles`](./agrimetrics_python_sdk/type/data_set_alternative_titles.py)<a id="alternative_titles-datasetalternativetitlesagrimetrics_python_sdktypedata_set_alternative_titlespy"></a>

##### scoring_uri: `str`<a id="scoring_uri-str"></a>

Scoring URI of the model.

##### endpoint_key: `str`<a id="endpoint_key-str"></a>

Endpoint key for the model.

##### is_owner: `bool`<a id="is_owner-bool"></a>

Whether the current user is the owner of this data set.

##### publisher: `str`<a id="publisher-str"></a>

The ID of the publisher.

##### created_at: `Union[int, float]`<a id="created_at-unionint-float"></a>

Data set creation timestamp.

##### published: `Union[int, float]`<a id="published-unionint-float"></a>

Data set publication timestamp.

##### metadata_modified: `Union[int, float]`<a id="metadata_modified-unionint-float"></a>

Metadata last-modification timestmap.

##### used_by: List[`BasicDataSetInfo`]<a id="used_by-listbasicdatasetinfo"></a>

Other data sets using this data set.

##### derived_from: [`DataSetDerivedFrom`](./agrimetrics_python_sdk/type/data_set_derived_from.py)<a id="derived_from-datasetderivedfromagrimetrics_python_sdktypedata_set_derived_frompy"></a>

##### entitlements: List[[`Entitlement`](./agrimetrics_python_sdk/type/entitlement.py)]<a id="entitlements-listentitlementagrimetrics_python_sdktypeentitlementpy"></a>

Entitlements for the current user.

##### entitlements_by_identity: [`DataSetEntitlementsByIdentity`](./agrimetrics_python_sdk/type/data_set_entitlements_by_identity.py)<a id="entitlements_by_identity-datasetentitlementsbyidentityagrimetrics_python_sdktypedata_set_entitlements_by_identitypy"></a>

##### creator: `str`<a id="creator-str"></a>

Creator of the data set.

##### data_reliability: `str`<a id="data_reliability-str"></a>

Free text description about the reliability of this dataset.

##### license: `str`<a id="license-str"></a>

License of the data set.

##### licence: [`Licence`](./agrimetrics_python_sdk/type/licence.py)<a id="licence-licenceagrimetrics_python_sdktypelicencepy"></a>


##### landing_page: `str`<a id="landing_page-str"></a>

DEPRECATED. This has been replaced with the resources attribute. Reference URI of the data set.

##### resources: List[`Resource`]<a id="resources-listresource"></a>

Links containing more information on the data set

##### data_formats: List[`DataFormat`]<a id="data_formats-listdataformat"></a>

Format of the data set

##### pricing_description: `str`<a id="pricing_description-str"></a>

Pricing description of the data set.

##### spatial_coverage: [`SpatialCoverage`](./agrimetrics_python_sdk/type/spatial_coverage.py)<a id="spatial_coverage-spatialcoverageagrimetrics_python_sdktypespatial_coveragepy"></a>

##### spatial_resolution: `Union[int, float]`<a id="spatial_resolution-unionint-float"></a>

The resolution of data set in meters.

##### geospatial_extent: [`GeospatialExtent`](./agrimetrics_python_sdk/type/geospatial_extent.py)<a id="geospatial_extent-geospatialextentagrimetrics_python_sdktypegeospatial_extentpy"></a>


##### temporal_coverage: `str`<a id="temporal_coverage-str"></a>

The time frame this data set covers.

##### temporal_resolution: `str`<a id="temporal_resolution-str"></a>

The sampling time period of the data set.

##### accrual_periodicity: [`AccrualPeriodicity`](./agrimetrics_python_sdk/type/accrual_periodicity.py)<a id="accrual_periodicity-accrualperiodicityagrimetrics_python_sdktypeaccrual_periodicitypy"></a>

##### distributions: [`DataSetDistributions`](./agrimetrics_python_sdk/type/data_set_distributions.py)<a id="distributions-datasetdistributionsagrimetrics_python_sdktypedata_set_distributionspy"></a>

##### issued: `str`<a id="issued-str"></a>

The date when the data set was issued.

##### modified: `Union[int, float]`<a id="modified-unionint-float"></a>

An timestamp of when the data in this dataset was last updated

##### keywords: [`DataSetKeywords`](./agrimetrics_python_sdk/type/data_set_keywords.py)<a id="keywords-datasetkeywordsagrimetrics_python_sdktypedata_set_keywordspy"></a>

##### topics: List[[`Topic`](./agrimetrics_python_sdk/type/topic.py)]<a id="topics-listtopicagrimetrics_python_sdktypetopicpy"></a>

List of topics on this data set

##### workflow_keywords: List[[`WorkflowKeywords`](./agrimetrics_python_sdk/type/workflow_keywords.py)]<a id="workflow_keywords-listworkflowkeywordsagrimetrics_python_sdktypeworkflow_keywordspy"></a>

List of workflow keywords on this data set

##### taxonomy_keywords: List[`TaxonomyKeywords`]<a id="taxonomy_keywords-listtaxonomykeywords"></a>

List of keywords based on specific taxonomies

##### items: [`CategoryValue`](./agrimetrics_python_sdk/type/category_value.py)<a id="items-categoryvalueagrimetrics_python_sdktypecategory_valuepy"></a>

##### visibility: `str`<a id="visibility-str"></a>

Whether or not this data set should be displayed in the index.

##### concepts: [`DataSetConcepts`](./agrimetrics_python_sdk/type/data_set_concepts.py)<a id="concepts-datasetconceptsagrimetrics_python_sdktypedata_set_conceptspy"></a>

##### data_set: [`DataSetDataSet`](./agrimetrics_python_sdk/type/data_set_data_set.py)<a id="data_set-datasetdatasetagrimetrics_python_sdktypedata_set_data_setpy"></a>


##### services: [`DataSetServices`](./agrimetrics_python_sdk/type/data_set_services.py)<a id="services-datasetservicesagrimetrics_python_sdktypedata_set_servicespy"></a>

##### sample_data: [`DataSetSampleData`](./agrimetrics_python_sdk/type/data_set_sample_data.py)<a id="sample_data-datasetsampledataagrimetrics_python_sdktypedata_set_sample_datapy"></a>


##### image: [`ImageRepresentation`](./agrimetrics_python_sdk/type/image_representation.py)<a id="image-imagerepresentationagrimetrics_python_sdktypeimage_representationpy"></a>


##### coordinate_reference_system_id: `str`<a id="coordinate_reference_system_id-str"></a>

URL to the specification of the coordinate system used in the data

##### spatial_representation_type: `str`<a id="spatial_representation_type-str"></a>

Type of the geospatial data

##### lineage: `str`<a id="lineage-str"></a>

Information about the creation and quality assurance process of the dataset

##### from_template: `str`<a id="from_template-str"></a>

Information about which template was used to create the dataset record

##### contacts: List[`Contact`]<a id="contacts-listcontact"></a>

List of contacts for this data set

##### metadata_contact: [`Contact`](./agrimetrics_python_sdk/type/contact.py)<a id="metadata_contact-contactagrimetrics_python_sdktypecontactpy"></a>


##### public_contact: [`PublicContact`](./agrimetrics_python_sdk/type/public_contact.py)<a id="public_contact-publiccontactagrimetrics_python_sdktypepublic_contactpy"></a>


##### approval_for_access_number: `Union[int, float]`<a id="approval_for_access_number-unionint-float"></a>

Approval for access status number

##### approval_for_access_status: `str`<a id="approval_for_access_status-str"></a>

Approval for access status value

##### language: `str`<a id="language-str"></a>

Language used on the data set

##### character_set: `str`<a id="character_set-str"></a>

Character set used on the data set

##### hierarchy_level: `str`<a id="hierarchy_level-str"></a>

Hierarchy level of the data set

##### metadata_language: `str`<a id="metadata_language-str"></a>

Language used on the metadata

##### metadata_character_set: `str`<a id="metadata_character_set-str"></a>

Character set used on the metadata

##### metadata_standard_name: `str`<a id="metadata_standard_name-str"></a>

##### metadata_standard_version: `str`<a id="metadata_standard_version-str"></a>

##### draft_status: [`DraftStatus`](./agrimetrics_python_sdk/type/draft_status.py)<a id="draft_status-draftstatusagrimetrics_python_sdktypedraft_statuspy"></a>

##### draft_notes: `str`<a id="draft_notes-str"></a>

Any notes added during review of the data set

##### published_status: [`PublishedStatus`](./agrimetrics_python_sdk/type/published_status.py)<a id="published_status-publishedstatusagrimetrics_python_sdktypepublished_statuspy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataSet`](./agrimetrics_python_sdk/type/data_set.py)
The updated data set information.

#### 🔄 Return<a id="🔄-return"></a>

[`DataSet`](./agrimetrics_python_sdk/pydantic/data_set.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.esri.rest_service_query`<a id="agrimetricsesrirest_service_query"></a>

Query the given dataset using ESRI Rest Services


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rest_service_query_response = agrimetrics.esri.rest_service_query(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    param_one="paramOne_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### param_one: `str`<a id="param_one-str"></a>

Additional path element

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest/services/{datasetId}/{paramOne}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.esri.rest_service_query_0`<a id="agrimetricsesrirest_service_query_0"></a>

Query the given dataset using ESRI Rest Services


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
rest_service_query_0_response = agrimetrics.esri.rest_service_query_0(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    param_one="paramOne_example",
    param_two="paramTwo_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### param_one: `str`<a id="param_one-str"></a>

Additional path element

##### param_two: `str`<a id="param_two-str"></a>

Additional path element

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/rest/services/{datasetId}/{paramOne}/{paramTwo}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.graph.list_concepts`<a id="agrimetricsgraphlist_concepts"></a>

List All Concepts Available in Agrimetrics Ontology Graph.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.graph.list_concepts()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/linked-data/concepts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.harvest.xml_data_on_group`<a id="agrimetricsharvestxml_data_on_group"></a>

Harvest xml data on the given group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
xml_data_on_group_response = agrimetrics.harvest.xml_data_on_group(
    group="apha",
    service="CSW",
    request="GetRecords",
    version="string_example",
    start_position=1,
    max_records=10,
    id=[
        "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
    ],
    output_schema="http://www.isotc211.org/2005/gmd",
    elementsetname="full",
    output_format="application/xml",
    type_names="gmd:MD_Metadata",
    result_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group: [`GroupCode`](./agrimetrics_python_sdk/type/.py)<a id="group-groupcodeagrimetrics_python_sdktypepy"></a>

##### service: `str`<a id="service-str"></a>

##### request: `str`<a id="request-str"></a>

##### version: `str`<a id="version-str"></a>

##### start_position: `Union[int, float]`<a id="start_position-unionint-float"></a>

##### max_records: `Union[int, float]`<a id="max_records-unionint-float"></a>

##### id: List[`str`]<a id="id-liststr"></a>

##### output_schema: `str`<a id="output_schema-str"></a>

##### elementsetname: `str`<a id="elementsetname-str"></a>

##### output_format: `str`<a id="output_format-str"></a>

##### type_names: `str`<a id="type_names-str"></a>

##### result_type: `str`<a id="result_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/harvest/{group}/csw` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.harvest.xml_data_on_group_post`<a id="agrimetricsharvestxml_data_on_group_post"></a>

Harvest xml data on the given group

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
xml_data_on_group_post_response = agrimetrics.harvest.xml_data_on_group_post(
    group="apha",
    service="CSW",
    request="GetRecords",
    version="string_example",
    start_position=1,
    max_records=10,
    id=[
        "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
    ],
    output_schema="http://www.isotc211.org/2005/gmd",
    elementsetname="full",
    output_format="application/xml",
    type_names="gmd:MD_Metadata",
    result_type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### group: [`GroupCode`](./agrimetrics_python_sdk/type/.py)<a id="group-groupcodeagrimetrics_python_sdktypepy"></a>

##### service: `str`<a id="service-str"></a>

##### request: `str`<a id="request-str"></a>

##### version: `str`<a id="version-str"></a>

##### start_position: `Union[int, float]`<a id="start_position-unionint-float"></a>

##### max_records: `Union[int, float]`<a id="max_records-unionint-float"></a>

##### id: List[`str`]<a id="id-liststr"></a>

##### output_schema: `str`<a id="output_schema-str"></a>

##### elementsetname: `str`<a id="elementsetname-str"></a>

##### output_format: `str`<a id="output_format-str"></a>

##### type_names: `str`<a id="type_names-str"></a>

##### result_type: `str`<a id="result_type-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/harvest/{group}/csw` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.image.get_raw_image`<a id="agrimetricsimageget_raw_image"></a>

Get an image referenced on a data set. This will always return the raw image data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.image.get_raw_image(
    image_type="custom",
    image_id="imageId_example",
    thumbnail="false",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### image_type: `str`<a id="image_type-str"></a>

##### image_id: `str`<a id="image_id-str"></a>

##### thumbnail: `str`<a id="thumbnail-str"></a>

Whether to provide a thumbnail image. If set to true and no thumbnail exists, the full image will be returned

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/images/{imageType}/{imageId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.import.data_sets`<a id="agrimetricsimportdata_sets"></a>



#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.import.data_sets(
    body=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`IO`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/import` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_dataset.ingest_file_new_layer`<a id="agrimetricsmanage_datasetingest_file_new_layer"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Ingest a file that has been uploaded to the catalog to create a new layer.
See [supported ingest formats](doc:supported-ingest-formats) for supported formats.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
ingest_file_new_layer_response = agrimetrics.manage_dataset.ingest_file_new_layer(
    file_uri="https://api.agrimetrics.co.uk/file-management/data-sets/5e74c298-515d-408d-8926-974abc696092/files/samplehabitats.zip",
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_uri: `str`<a id="file_uri-str"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageDatasetIngestFileNewLayerRequest`](./agrimetrics_python_sdk/type/manage_dataset_ingest_file_new_layer_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`NewLayers`](./agrimetrics_python_sdk/pydantic/new_layers.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/layers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.add_geo_tiff`<a id="agrimetricsmanage_layeradd_geo_tiff"></a>

> :warning: **The maximum file size accepted for this endpoint to work is 200 MiB.**

This endpoint will add a GeoTIFF to an existing GeoTIFF layer.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
add_geo_tiff_response = agrimetrics.manage_layer.add_geo_tiff(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    datetime="20130310T180000Z",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### datetime: [`ISO8601Datetime`](./agrimetrics_python_sdk/type/iso8601_datetime.py)<a id="datetime-iso8601datetimeagrimetrics_python_sdktypeiso8601_datetimepy"></a>

##### file: `IO`<a id="file-io"></a>

The file to upload.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageLayerAddGeoTiffRequest`](./agrimetrics_python_sdk/type/manage_layer_add_geo_tiff_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ManageLayerAddGeoTiffResponse`](./agrimetrics_python_sdk/pydantic/manage_layer_add_geo_tiff_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.auto_generate_style`<a id="agrimetricsmanage_layerauto_generate_style"></a>

Generate a new style and apply it to the given layer.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
auto_generate_style_response = agrimetrics.manage_layer.auto_generate_style(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    key="LU_CODE",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### key: `str`<a id="key-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`RestError`](./agrimetrics_python_sdk/pydantic/rest_error.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/style` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.delete_layer`<a id="agrimetricsmanage_layerdelete_layer"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Delete the datastore and layer relating to a zip file on a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.manage_layer.delete_layer(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.get_style`<a id="agrimetricsmanage_layerget_style"></a>

Get the SLD style that has been applied to a layer.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.manage_layer.get_style(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/style` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.ingest_file`<a id="agrimetricsmanage_layeringest_file"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Ingest a file that has been uploaded to a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.manage_layer.ingest_file(
    file_id="https://api.agrimetrics.co.uk/file-management/data-sets/5e74c298-515d-408d-8926-974abc696092/files/samplehabitats.zip",
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    file_name="samplehabitats.zip",
    datetime="20130310T180000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### file_id: `str`<a id="file_id-str"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### file_name: `str`<a id="file_name-str"></a>

##### datetime: [`ISO8601Datetime`](./agrimetrics_python_sdk/type/iso8601_datetime.py)<a id="datetime-iso8601datetimeagrimetrics_python_sdktypeiso8601_datetimepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageLayerIngestFileRequest`](./agrimetrics_python_sdk/type/manage_layer_ingest_file_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/ingest` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.remove_file`<a id="agrimetricsmanage_layerremove_file"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Remove a file from a layer. When you are deleting a file from a layer, the layer may remain if any other files were ingested onto the same layer. If removing a raster file, provide the fileName query parameter; if removing a vector file, provide the fileUri.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.manage_layer.remove_file(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    file_uri="https://api-test.agrimetrics.co.uk/file-management/data-sets/11111111-2222-3333-4444-55555555555/files/example.zip",
    filename="example.tif",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### file_uri: `str`<a id="file_uri-str"></a>

##### filename: `str`<a id="filename-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/files` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.remove_style`<a id="agrimetricsmanage_layerremove_style"></a>

Delete an SLD style that has been applied to a layer.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.manage_layer.remove_style(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/style` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.manage_layer.set_style`<a id="agrimetricsmanage_layerset_style"></a>

Apply a new style to the given layer. The style must be provided as an SLD file (1.0.0 and 1.1.0 supported).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_style_response = agrimetrics.manage_layer.set_style(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    file=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### file: `IO`<a id="file-io"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ManageLayerSetStyleRequest`](./agrimetrics_python_sdk/type/manage_layer_set_style_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/style` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.get_conformance`<a id="agrimetricsogc_api_tilesget_conformance"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_conformance_response = agrimetrics.ogc_api_tiles.get_conformance(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/conformance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.get_query_tiles_collection`<a id="agrimetricsogc_api_tilesget_query_tiles_collection"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_query_tiles_collection_response = agrimetrics.ogc_api_tiles.get_query_tiles_collection(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
    tile_matrix_set_id="tileMatrixSetId_example",
    tile_matrix="tileMatrix_example",
    tile_row=1,
    tile_col=1,
    f="f_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

##### tile_matrix_set_id: `str`<a id="tile_matrix_set_id-str"></a>

##### tile_matrix: `str`<a id="tile_matrix-str"></a>

##### tile_row: `int`<a id="tile_row-int"></a>

##### tile_col: `int`<a id="tile_col-int"></a>

##### f: `str`<a id="f-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/map/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.get_tiles_collection`<a id="agrimetricsogc_api_tilesget_tiles_collection"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_tiles_collection_response = agrimetrics.ogc_api_tiles.get_tiles_collection(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
    tile_matrix_set_id="tileMatrixSetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

##### tile_matrix_set_id: `str`<a id="tile_matrix_set_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/tiles/{tileMatrixSetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_collection_by_id`<a id="agrimetricsogc_api_tilesquery_collection_by_id"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_collection_by_id_response = agrimetrics.ogc_api_tiles.query_collection_by_id(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_collection_queryables`<a id="agrimetricsogc_api_tilesquery_collection_queryables"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_collection_queryables_response = agrimetrics.ogc_api_tiles.query_collection_queryables(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/queryables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_collections`<a id="agrimetricsogc_api_tilesquery_collections"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_collections_response = agrimetrics.ogc_api_tiles.query_collections(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_tile_matrix_sets`<a id="agrimetricsogc_api_tilesquery_tile_matrix_sets"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tile_matrix_sets_response = agrimetrics.ogc_api_tiles.query_tile_matrix_sets(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/tileMatrixSets` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_tile_matrix_sets_0`<a id="agrimetricsogc_api_tilesquery_tile_matrix_sets_0"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tile_matrix_sets_0_response = agrimetrics.ogc_api_tiles.query_tile_matrix_sets_0(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    tile_matrix_set_id="tileMatrixSetId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### tile_matrix_set_id: `str`<a id="tile_matrix_set_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1/tileMatrixSets/{tileMatrixSetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogc_api_tiles.query_tiles_v1`<a id="agrimetricsogc_api_tilesquery_tiles_v1"></a>

Query the given data set with OGC API Tiles standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tiles_v1_response = agrimetrics.ogc_api_tiles.query_tiles_v1(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/tiles/v1` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.features_query`<a id="agrimetricsogcapifeatures_query"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
features_query_response = agrimetrics.ogcapi.features_query(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.features_query_0`<a id="agrimetricsogcapifeatures_query_0"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
features_query_0_response = agrimetrics.ogcapi.features_query_0(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
    feature_id="featureId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

##### feature_id: `str`<a id="feature_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/items/{featureId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.features_query_conformance`<a id="agrimetricsogcapifeatures_query_conformance"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
features_query_conformance_response = agrimetrics.ogcapi.features_query_conformance(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/conformance` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.features_query_ogc`<a id="agrimetricsogcapifeatures_query_ogc"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
features_query_ogc_response = agrimetrics.ogcapi.features_query_ogc(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.features_queryables`<a id="agrimetricsogcapifeatures_queryables"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
features_queryables_response = agrimetrics.ogcapi.features_queryables(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/queryables` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.get_style_for_css_file`<a id="agrimetricsogcapiget_style_for_css_file"></a>

Get CSS files

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.ogcapi.get_style_for_css_file(
    css_file="cssFile_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### css_file: `str`<a id="css_file-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/apicss/{cssFile}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.get_swagger_file`<a id="agrimetricsogcapiget_swagger_file"></a>

Get swagger files

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.ogcapi.get_swagger_file(
    swagger_file="swaggerFile_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### swagger_file: `str`<a id="swagger_file-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/swagger-ui/{swaggerFile}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.query_features_collection`<a id="agrimetricsogcapiquery_features_collection"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_features_collection_response = agrimetrics.ogcapi.query_features_collection(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/collections` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.query_features_collection_items`<a id="agrimetricsogcapiquery_features_collection_items"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_features_collection_items_response = agrimetrics.ogcapi.query_features_collection_items(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    collection_id="collectionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### collection_id: `str`<a id="collection_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/items` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.query_features_function`<a id="agrimetricsogcapiquery_features_function"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_features_function_response = agrimetrics.ogcapi.query_features_function(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/functions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.ogcapi.query_features_openapi`<a id="agrimetricsogcapiquery_features_openapi"></a>

Query the given data set with the OGC-API Featuresinterface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_features_openapi_response = agrimetrics.ogcapi.query_features_openapi(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/ogc/features/v1/openapi` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_dataset.list_layers_within_dataset`<a id="agrimetricsquery_datasetlist_layers_within_dataset"></a>

Get the list of layers contained in a geospatial data set.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_layers_within_dataset_response = agrimetrics.query_dataset.list_layers_within_dataset(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

This parameter corresponds to the Agrimetrics Catalogue dataset ID.

#### 🔄 Return<a id="🔄-return"></a>

[`QueryDatasetListLayersWithinDatasetResponse`](./agrimetrics_python_sdk/pydantic/query_dataset_list_layers_within_dataset_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_layer.calculate_cost`<a id="agrimetricsquery_layercalculate_cost"></a>

Find out the cost of searching a specific geometry within a layer.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_cost_response = agrimetrics.query_layer.calculate_cost(
    body=None,
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    geometry={
        "type": "Point",
        "coordinates": [-91.85, 15.52],
    },
    time="2017-01-01T00:00:00.000Z",
    distance=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### geometry: [`GeoJSONPoint`](./agrimetrics_python_sdk/type/geo_json_point.py)<a id="geometry-geojsonpointagrimetrics_python_sdktypegeo_json_pointpy"></a>


##### time: `datetime`<a id="time-datetime"></a>

##### distance: `int`<a id="distance-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QueryLayerCalculateCostRequest`](./agrimetrics_python_sdk/type/query_layer_calculate_cost_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`CostSummary`](./agrimetrics_python_sdk/pydantic/cost_summary.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/search/cost` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_layer.calculate_statistics_within_geometry`<a id="agrimetricsquery_layercalculate_statistics_within_geometry"></a>

> :warning: Search geometries are currently limited to areas up to 500 square km.

Calculates basic statistics of the raster layer within the specified geometry (and optionally time).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
calculate_statistics_within_geometry_response = agrimetrics.query_layer.calculate_statistics_within_geometry(
    geometry=None,
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    time="2017-01-01T00:00:00.000Z",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### geometry: `GeneralGeometry`<a id="geometry-generalgeometry"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### time: `datetime`<a id="time-datetime"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QueryLayerCalculateStatisticsWithinGeometryRequest`](./agrimetrics_python_sdk/type/query_layer_calculate_statistics_within_geometry_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Statistics`](./agrimetrics_python_sdk/pydantic/statistics.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/search/statistics` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_layer.cut_shape_boundary_and_retrieve`<a id="agrimetricsquery_layercut_shape_boundary_and_retrieve"></a>

Cut one or more layers to a shape boundary and retrieve the features as multiple layers in a single downloadable file

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
cut_shape_boundary_and_retrieve_response = agrimetrics.query_layer.cut_shape_boundary_and_retrieve(
    layer=[
        "97130f06-6242-463f-bf19-0dd6f5a58cfb"
    ],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer: List[`str`]<a id="layer-liststr"></a>

A layer to query

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/query` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_layer.metadata`<a id="agrimetricsquery_layermetadata"></a>

Get the metadata for a given layer, including the geospatial extent.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
metadata_response = agrimetrics.query_layer.metadata(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`QueryLayerMetadataResponse`](./agrimetrics_python_sdk/pydantic/query_layer_metadata_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.query_layer.search_geometry`<a id="agrimetricsquery_layersearch_geometry"></a>

> :warning: Search geometries are currently limited to areas up to 500 square km.

Search a specific geometry within a layer. You can optionally specify a time range and/or choose the format of the response (file type, or json).


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
search_geometry_response = agrimetrics.query_layer.search_geometry(
    body=None,
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    geometry={
        "type": "Point",
        "coordinates": [-91.85, 15.52],
    },
    time="2017-01-01T00:00:00.000Z",
    output_format="shape-zip",
    distance=10,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### geometry: [`GeoJSONPoint`](./agrimetrics_python_sdk/type/geo_json_point.py)<a id="geometry-geojsonpointagrimetrics_python_sdktypegeo_json_pointpy"></a>


##### time: `datetime`<a id="time-datetime"></a>

##### output_format: [`OutputFormats`](./agrimetrics_python_sdk/type/output_formats.py)<a id="output_format-outputformatsagrimetrics_python_sdktypeoutput_formatspy"></a>

##### distance: `int`<a id="distance-int"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`QueryLayerSearchGeometryRequest`](./agrimetrics_python_sdk/type/query_layer_search_geometry_request.py)
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/layers/{layerId}/search` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.service_definition.create_new_definition`<a id="agrimetricsservice_definitioncreate_new_definition"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Create new service definition within a data set.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_definition_response = agrimetrics.service_definition.create_new_definition(
    dataset_id="a420450f-ef42-4fc9-a137-69456bdad016",
    layer_name="Geospatial Layer",
    service="WCS",
    wfs="Y",
    wcs="Y",
    wms="Y",
    wmts="Y",
    ogc_api_features="Y",
    ogc_api_tiles="Y",
    temporal=True,
    datastore="Datastore Name",
    geoserver_host_name="geoserver-test.agrimetrics.co.uk",
    geometry_field="geom",
    billable={
        "billing_data_type": "billing_data_type_example",
        "billing_credit_type": "billing_credit_type_example",
        "billing_credit_cost": 3.14,
    },
    default_epsg_code=4326,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### layer_name: `str`<a id="layer_name-str"></a>

##### service: `str`<a id="service-str"></a>

##### wfs: `str`<a id="wfs-str"></a>

##### wcs: `str`<a id="wcs-str"></a>

##### wms: `str`<a id="wms-str"></a>

##### wmts: `str`<a id="wmts-str"></a>

##### ogc_api_features: `str`<a id="ogc_api_features-str"></a>

##### ogc_api_tiles: `str`<a id="ogc_api_tiles-str"></a>

##### temporal: `bool`<a id="temporal-bool"></a>

##### datastore: `str`<a id="datastore-str"></a>

##### geoserver_host_name: `str`<a id="geoserver_host_name-str"></a>

##### geometry_field: `str`<a id="geometry_field-str"></a>

##### billable: [`Billable`](./agrimetrics_python_sdk/type/billable.py)<a id="billable-billableagrimetrics_python_sdktypebillablepy"></a>


##### default_epsg_code: `Union[int, float]`<a id="default_epsg_code-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServiceDefinition`](./agrimetrics_python_sdk/type/service_definition.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.service_definition.delete_by_id`<a id="agrimetricsservice_definitiondelete_by_id"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Delete service definition given layer ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.service_definition.delete_by_id(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.service_definition.get_by_layer_id`<a id="agrimetricsservice_definitionget_by_layer_id"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Get the service definition for a given layer ID


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_layer_id_response = agrimetrics.service_definition.get_by_layer_id(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.service_definition.update_existing_definition`<a id="agrimetricsservice_definitionupdate_existing_definition"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Update an existing service definition with billing and coordinates reference system metadata.


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_existing_definition_response = agrimetrics.service_definition.update_existing_definition(
    layer_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    billable={
        "billing_data_type": "billing_data_type_example",
        "billing_credit_type": "billing_credit_type_example",
        "billing_credit_cost": 3.14,
    },
    default_epsg_code=4326,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### layer_id: `str`<a id="layer_id-str"></a>

##### billable: [`Billable`](./agrimetrics_python_sdk/type/billable.py)<a id="billable-billableagrimetrics_python_sdktypebillablepy"></a>


##### default_epsg_code: `Union[int, float]`<a id="default_epsg_code-unionint-float"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ServiceDefinitionUpdateExistingDefinitionRequest`](./agrimetrics_python_sdk/type/service_definition_update_existing_definition_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ServiceDefinitionResponse`](./agrimetrics_python_sdk/pydantic/service_definition_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/serviceDefinition/{layerId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.shapefile.convert_to_geo_json`<a id="agrimetricsshapefileconvert_to_geo_json"></a>

> :warning: **This is an Agrimetrics internal operation. It relies on information which is not exposed externally.**

Receive a shapefile and return GeoJson for explore page


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
convert_to_geo_json_response = agrimetrics.shapefile.convert_to_geo_json(
    body=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`IO`
#### 🔄 Return<a id="🔄-return"></a>

[`GeoJSONPolygon`](./agrimetrics_python_sdk/pydantic/geo_json_polygon.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/shapefile` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.status.get_catalog_api_status`<a id="agrimetricsstatusget_catalog_api_status"></a>

Get status of catalog API.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_catalog_api_status_response = agrimetrics.status.get_catalog_api_status()
```

#### 🔄 Return<a id="🔄-return"></a>

[`StatusGetCatalogApiStatusResponse`](./agrimetrics_python_sdk/pydantic/status_get_catalog_api_status_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/status` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.status.set_draft_status`<a id="agrimetricsstatusset_draft_status"></a>

Set the draft status for the data set catalog entry.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
set_draft_status_response = agrimetrics.status.set_draft_status(
    status=None,
    data_set_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    notes="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### status: Union[[`DraftStatus`](./agrimetrics_python_sdk/type/draft_status.py), `Optional[str]`]<a id="status-uniondraftstatusagrimetrics_python_sdktypedraft_statuspy-optionalstr"></a>


##### data_set_id: `str`<a id="data_set_id-str"></a>

##### notes: `str`<a id="notes-str"></a>

Any notes added during review of the data set

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`StatusSetDraftStatusRequest`](./agrimetrics_python_sdk/type/status_set_draft_status_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EntryUpdateResponse`](./agrimetrics_python_sdk/pydantic/entry_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-sets/{dataSetId}/draft-status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.create_catalog_entry`<a id="agrimetricstemplatecreate_catalog_entry"></a>

Creates a single template that can be used to create similar catalogue entries.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_catalog_entry_response = agrimetrics.template.create_catalog_entry(
    name="string_example",
    description="string_example",
    data_set={
        "spatial_coverage": "United Kingdom",
        "temporal_resolution": "P1Y",
        "accrual_periodicity": "Hourly",
        "published_status": "published",
        "category": "free",
        "visibility": "visible",
        "approval_for_access_status": "AfA (Information Requests only)",
    },
    entitlements=[
        {
            "identity": {
                "type": "user",
            },
            "entitlements": {
                "catalog": {
                },
                "is_admin": True,
            },
        }
    ],
    creator_entitlements={
        "catalog": {
        },
        "is_admin": True,
    },
    exchange="agrimetrics",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### description: `str`<a id="description-str"></a>

##### data_set: [`DataSetPatch`](./agrimetrics_python_sdk/type/data_set_patch.py)<a id="data_set-datasetpatchagrimetrics_python_sdktypedata_set_patchpy"></a>


##### entitlements: [`BatchIdentityInputEntitlements`](./agrimetrics_python_sdk/type/batch_identity_input_entitlements.py)<a id="entitlements-batchidentityinputentitlementsagrimetrics_python_sdktypebatch_identity_input_entitlementspy"></a>

##### creator_entitlements: [`Entitlements`](./agrimetrics_python_sdk/type/entitlements.py)<a id="creator_entitlements-entitlementsagrimetrics_python_sdktypeentitlementspy"></a>


##### exchange: [`Exchange`](./agrimetrics_python_sdk/type/exchange.py)<a id="exchange-exchangeagrimetrics_python_sdktypeexchangepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataSetTemplateMetadata`](./agrimetrics_python_sdk/type/data_set_template_metadata.py)
The data set to create.

#### 🔄 Return<a id="🔄-return"></a>

[`EntryUpdateResponse`](./agrimetrics_python_sdk/pydantic/entry_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.delete_specific_template`<a id="agrimetricstemplatedelete_specific_template"></a>

Delete a specific template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
delete_specific_template_response = agrimetrics.template.delete_specific_template(
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`EntryUpdateResponse`](./agrimetrics_python_sdk/pydantic/entry_update_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{templateId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.get_specific_template`<a id="agrimetricstemplateget_specific_template"></a>

Get a specific template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_specific_template_response = agrimetrics.template.get_specific_template(
    template_id="templateId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DataSetTemplateEntity`](./agrimetrics_python_sdk/pydantic/data_set_template_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{templateId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.list_permissions_to_view`<a id="agrimetricstemplatelist_permissions_to_view"></a>

List all templates you have permission to view.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_permissions_to_view_response = agrimetrics.template.list_permissions_to_view()
```

#### 🔄 Return<a id="🔄-return"></a>

[`TemplateListPermissionsToViewResponse`](./agrimetrics_python_sdk/pydantic/template_list_permissions_to_view_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.update_template_item`<a id="agrimetricstemplateupdate_template_item"></a>

Update a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_template_item_response = agrimetrics.template.update_template_item(
    name="string_example",
    template_id="templateId_example",
    description="string_example",
    data_set={
        "spatial_coverage": "United Kingdom",
        "temporal_resolution": "P1Y",
        "accrual_periodicity": "Hourly",
        "published_status": "published",
        "category": "free",
        "visibility": "visible",
        "approval_for_access_status": "AfA (Information Requests only)",
    },
    entitlements=[
        {
            "identity": {
                "type": "user",
            },
            "entitlements": {
                "catalog": {
                },
                "is_admin": True,
            },
        }
    ],
    creator_entitlements={
        "catalog": {
        },
        "is_admin": True,
    },
    exchange="agrimetrics",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### data_set: [`DataSetPatch`](./agrimetrics_python_sdk/type/data_set_patch.py)<a id="data_set-datasetpatchagrimetrics_python_sdktypedata_set_patchpy"></a>


##### entitlements: [`BatchIdentityInputEntitlements`](./agrimetrics_python_sdk/type/batch_identity_input_entitlements.py)<a id="entitlements-batchidentityinputentitlementsagrimetrics_python_sdktypebatch_identity_input_entitlementspy"></a>

##### creator_entitlements: [`Entitlements`](./agrimetrics_python_sdk/type/entitlements.py)<a id="creator_entitlements-entitlementsagrimetrics_python_sdktypeentitlementspy"></a>


##### exchange: [`Exchange`](./agrimetrics_python_sdk/type/exchange.py)<a id="exchange-exchangeagrimetrics_python_sdktypeexchangepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataSetTemplateMetadata`](./agrimetrics_python_sdk/type/data_set_template_metadata.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataSetTemplateEntity`](./agrimetrics_python_sdk/pydantic/data_set_template_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{templateId}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.template.update_template_item_0`<a id="agrimetricstemplateupdate_template_item_0"></a>

Update a template

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_template_item_0_response = agrimetrics.template.update_template_item_0(
    template_id="templateId_example",
    description="string_example",
    name="string_example",
    data_set={
        "spatial_coverage": "United Kingdom",
        "temporal_resolution": "P1Y",
        "accrual_periodicity": "Hourly",
        "published_status": "published",
        "category": "free",
        "visibility": "visible",
        "approval_for_access_status": "AfA (Information Requests only)",
    },
    entitlements=[
        {
            "identity": {
                "type": "user",
            },
            "entitlements": {
                "catalog": {
                },
                "is_admin": True,
            },
        }
    ],
    creator_entitlements={
        "catalog": {
        },
        "is_admin": True,
    },
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### template_id: `str`<a id="template_id-str"></a>

##### description: `str`<a id="description-str"></a>

##### name: `str`<a id="name-str"></a>

##### data_set: [`DataSetPatch`](./agrimetrics_python_sdk/type/data_set_patch.py)<a id="data_set-datasetpatchagrimetrics_python_sdktypedata_set_patchpy"></a>


##### entitlements: [`BatchIdentityInputEntitlements`](./agrimetrics_python_sdk/type/batch_identity_input_entitlements.py)<a id="entitlements-batchidentityinputentitlementsagrimetrics_python_sdktypebatch_identity_input_entitlementspy"></a>

##### creator_entitlements: [`Entitlements`](./agrimetrics_python_sdk/type/entitlements.py)<a id="creator_entitlements-entitlementsagrimetrics_python_sdktypeentitlementspy"></a>


#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataSetTemplatePatchMetadata`](./agrimetrics_python_sdk/type/data_set_template_patch_metadata.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataSetTemplateEntity`](./agrimetrics_python_sdk/pydantic/data_set_template_entity.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/templates/{templateId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wcs.query_data`<a id="agrimetricswcsquery_data"></a>

Query the given data set with the OpenGIS® Web Coverage Serice interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_response = agrimetrics.wcs.query_data(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wcs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wcs.query_data_0`<a id="agrimetricswcsquery_data_0"></a>

Query the given data set with the OpenGIS® Web Coverage Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_0_response = agrimetrics.wcs.query_data_0(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wcs` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wfs.query_data_open_gis`<a id="agrimetricswfsquery_data_open_gis"></a>

Query the given data set with the OpenGIS® Web Feature Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_open_gis_response = agrimetrics.wfs.query_data_open_gis(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wfs` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wfs.query_data_open_gis_0`<a id="agrimetricswfsquery_data_open_gis_0"></a>

Query the given data set with the OpenGIS® Web Feature Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_open_gis_0_response = agrimetrics.wfs.query_data_open_gis_0(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

`Dict[str, Union[bool, date, datetime, dict, float, int, list, str, None]]`
#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wfs` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wfs.query_data_with_open_gis`<a id="agrimetricswfsquery_data_with_open_gis"></a>

Query the given data set with the OpenGIS® Web Feature Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_with_open_gis_response = agrimetrics.wfs.query_data_with_open_gis(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wfs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wms.query_layer_with_open_gis`<a id="agrimetricswmsquery_layer_with_open_gis"></a>

Query the given layer with the OpenGIS® Web Map Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_layer_with_open_gis_response = agrimetrics.wms.query_layer_with_open_gis(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wms` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wms.query_with_open_gis`<a id="agrimetricswmsquery_with_open_gis"></a>

Query the given data set with the OpenGIS® Web Map Service interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_with_open_gis_response = agrimetrics.wms.query_with_open_gis(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wms` `head`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wmts.query_data_set_wmts`<a id="agrimetricswmtsquery_data_set_wmts"></a>

Query the given data set with the OpenGIS® Web Map Tile Serice interface standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_data_set_wmts_response = agrimetrics.wmts.query_data_set_wmts(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wmts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wmts_rest.query_tile_matrix_set`<a id="agrimetricswmts_restquery_tile_matrix_set"></a>

Query the given data set with theWMTS standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tile_matrix_set_response = agrimetrics.wmts_rest.query_tile_matrix_set(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    layer_name="layerName_example",
    style="style_example",
    tile_matrix_set="TileMatrixSet_example",
    tile_matrix="TileMatrix_example",
    tile_row=0,
    tile_col=0,
    format="format_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### layer_name: `str`<a id="layer_name-str"></a>

##### style: `str`<a id="style-str"></a>

##### tile_matrix_set: `str`<a id="tile_matrix_set-str"></a>

##### tile_matrix: `str`<a id="tile_matrix-str"></a>

##### tile_row: `int`<a id="tile_row-int"></a>

##### tile_col: `int`<a id="tile_col-int"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wmts/rest/{layerName}/{style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wmts_rest.query_tilejson_image_format`<a id="agrimetricswmts_restquery_tilejson_image_format"></a>

Query the given data set with theWMTS standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
query_tilejson_image_format_response = agrimetrics.wmts_rest.query_tilejson_image_format(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    layer_name="layerName_example",
    style="style_example",
    image_format="imageFormat_example",
    format="format_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### layer_name: `str`<a id="layer_name-str"></a>

##### style: `str`<a id="style-str"></a>

##### image_format: `str`<a id="image_format-str"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wmts/rest/{layerName}/{style}/tilejson/{imageFormat}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.wmts_rest.service_query`<a id="agrimetricswmts_restservice_query"></a>

Query the given data set with theWMTS standard


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
service_query_response = agrimetrics.wmts_rest.service_query(
    dataset_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    layer_name="layerName_example",
    style="style_example",
    tile_matrix_set="TileMatrixSet_example",
    tile_matrix="TileMatrix_example",
    tile_row=0,
    tile_col=0,
    j=1,
    i=1,
    format="format_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_id: `str`<a id="dataset_id-str"></a>

##### layer_name: `str`<a id="layer_name-str"></a>

##### style: `str`<a id="style-str"></a>

##### tile_matrix_set: `str`<a id="tile_matrix_set-str"></a>

##### tile_matrix: `str`<a id="tile_matrix-str"></a>

##### tile_row: `int`<a id="tile_row-int"></a>

##### tile_col: `int`<a id="tile_col-int"></a>

##### j: `int`<a id="j-int"></a>

##### i: `int`<a id="i-int"></a>

##### format: `str`<a id="format-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/datasets/{datasetId}/wmts/rest/{layerName}/{style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}/{J}/{I}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.create_single_access_request`<a id="agrimetricsdata_requestcreate_single_access_request"></a>

Create a single access request for an authenticated user

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_single_access_request_response = agrimetrics.data_request.create_single_access_request(
    project_name="string_example",
    project_manager_name="string_example",
    project_manager_email="string_example",
    dataset_id="046b6c7f-0b8a-43b9-b35d-6489e6daee91",
    dataset_name="string_example",
    requested_format="application/geo+json",
    geo_json_aoi="string_example",
    shapefile_aoi=open('/path/to/file', 'rb'),
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### project_name: `str`<a id="project_name-str"></a>

The name of the project the data is for

##### project_manager_name: `str`<a id="project_manager_name-str"></a>

The name of the project manager who can approve the request

##### project_manager_email: `str`<a id="project_manager_email-str"></a>

The email address of the project manager who can approve the request

##### dataset_id: `str`<a id="dataset_id-str"></a>

The ID of the dataset that the data request relates to

##### dataset_name: `str`<a id="dataset_name-str"></a>

The name of the dataset that the data request relates to

##### requested_format: `str`<a id="requested_format-str"></a>

The format the user would like the data to be provided in

##### geo_json_aoi: `str`<a id="geo_json_aoi-str"></a>

The area of interest that the user is requesting access to as a stringified GeoJSON

##### shapefile_aoi: `IO`<a id="shapefile_aoi-io"></a>

The area of interest that the user is requesting access to as a zipped shapefile

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataRequest`](./agrimetrics_python_sdk/type/data_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataRequestCreateSingleAccessRequestResponse`](./agrimetrics_python_sdk/pydantic/data_request_create_single_access_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.get_geo_json_geometry`<a id="agrimetricsdata_requestget_geo_json_geometry"></a>

Returns the geometry of the data request as GeoJSON

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_geo_json_geometry_response = agrimetrics.data_request.get_geo_json_geometry(
    unique_link_id="uniqueLinkId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_link_id: `str`<a id="unique_link_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`GeoJSONPolygon`](./agrimetrics_python_sdk/pydantic/geo_json_polygon.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{uniqueLinkId}/geometry` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.get_requested_data`<a id="agrimetricsdata_requestget_requested_data"></a>

Returns the users requested data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_requested_data_response = agrimetrics.data_request.get_requested_data(
    request_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DataRequestDetails`](./agrimetrics_python_sdk/pydantic/data_request_details.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{requestId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.get_results`<a id="agrimetricsdata_requestget_results"></a>

Once a data access request has been approved, this endpoint returns the data requested.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_results_response = agrimetrics.data_request.get_results(
    request_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{requestId}/download` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.grant_user_access`<a id="agrimetricsdata_requestgrant_user_access"></a>

Grants access to a user on a given data request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.data_request.grant_user_access(
    unique_link_id="uniqueLinkId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_link_id: `str`<a id="unique_link_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{uniqueLinkId}/approve` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.list_user_access_requests`<a id="agrimetricsdata_requestlist_user_access_requests"></a>

Query the given users data access requests


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_user_access_requests_response = agrimetrics.data_request.list_user_access_requests()
```

#### 🔄 Return<a id="🔄-return"></a>

[`DataRequestResponse`](./agrimetrics_python_sdk/pydantic/data_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.reject_user_access`<a id="agrimetricsdata_requestreject_user_access"></a>

Rejects access to a user on a given data request

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
agrimetrics.data_request.reject_user_access(
    unique_link_id="uniqueLinkId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### unique_link_id: `str`<a id="unique_link_id-str"></a>

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{uniqueLinkId}/reject` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `agrimetrics.data_request.update_request`<a id="agrimetricsdata_requestupdate_request"></a>

Allows updating of the given data request |
- For example: cancelling the request


#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_request_response = agrimetrics.data_request.update_request(
    request_id="97130f06-6242-463f-bf19-0dd6f5a58cfb",
    status="cancelled",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### request_id: `str`<a id="request_id-str"></a>

##### status: `str`<a id="status-str"></a>

The status of the data request

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`DataRequestUpdateRequestRequest`](./agrimetrics_python_sdk/type/data_request_update_request_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DataRequestUpdateRequestResponse`](./agrimetrics_python_sdk/pydantic/data_request_update_request_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/data-requests/{requestId}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
