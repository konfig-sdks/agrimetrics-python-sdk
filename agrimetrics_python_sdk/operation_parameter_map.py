operation_parameter_map = {
    '/access-requests-POST': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
            {
                'name': 'requestingEntityId'
            },
            {
                'name': 'requestMessage'
            },
            {
                'name': 'requesterName'
            },
            {
                'name': 'requesterEmail'
            },
        ]
    },
    '/access-requests/{requestId}-DELETE': {
        'parameters': [
            {
                'name': 'requestId'
            },
            {
                'name': 'dataSetId'
            },
            {
                'name': 'accepted'
            },
        ]
    },
    '/access-requests-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
            {
                'name': 'requestingEntityId'
            },
            {
                'name': 'entityId'
            },
        ]
    },
    '/serviceDefinition-POST': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'layerName'
            },
            {
                'name': 'service'
            },
            {
                'name': 'WFS'
            },
            {
                'name': 'WCS'
            },
            {
                'name': 'WMS'
            },
            {
                'name': 'WMTS'
            },
            {
                'name': 'OGCApiFeatures'
            },
            {
                'name': 'OGCApiTiles'
            },
            {
                'name': 'temporal'
            },
            {
                'name': 'datastore'
            },
            {
                'name': 'geoserverHostName'
            },
            {
                'name': 'geometryField'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'defaultEPSGCode'
            },
        ]
    },
    '/serviceDefinition/{layerId}-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/serviceDefinition/{layerId}-GET': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}/ingest-POST': {
        'parameters': [
            {
                'name': 'fileId'
            },
            {
                'name': 'layerId'
            },
            {
                'name': 'fileName'
            },
            {
                'name': 'datetime'
            },
        ]
    },
    '/datasets/{datasetId}/layers-POST': {
        'parameters': [
            {
                'name': 'fileUri'
            },
            {
                'name': 'datasetId'
            },
        ]
    },
    '/layers/{layerId}/files-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'fileUri'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/serviceDefinition/{layerId}-PATCH': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'defaultEPSGCode'
            },
        ]
    },
    '/authenticate-POST': {
        'parameters': [
            {
                'name': 'username'
            },
            {
                'name': 'password'
            },
        ]
    },
    '/data-sets/{dataSetId}/fileDataset-POST': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets-POST': {
        'parameters': [
            {
                'name': 'tags'
            },
            {
                'name': 'summary'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'id'
            },
            {
                'name': 'entryType'
            },
            {
                'name': 'exchange'
            },
            {
                'name': 'alternativeTitles'
            },
            {
                'name': 'scoringURI'
            },
            {
                'name': 'endpointKey'
            },
            {
                'name': 'isOwner'
            },
            {
                'name': 'publisher'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'published'
            },
            {
                'name': 'metadataModified'
            },
            {
                'name': 'usedBy'
            },
            {
                'name': 'derivedFrom'
            },
            {
                'name': 'entitlements'
            },
            {
                'name': 'entitlementsByIdentity'
            },
            {
                'name': 'creator'
            },
            {
                'name': 'dataReliability'
            },
            {
                'name': 'license'
            },
            {
                'name': 'licence'
            },
            {
                'name': 'landingPage'
            },
            {
                'name': 'resources'
            },
            {
                'name': 'dataFormats'
            },
            {
                'name': 'pricingDescription'
            },
            {
                'name': 'spatialCoverage'
            },
            {
                'name': 'spatialResolution'
            },
            {
                'name': 'geospatialExtent'
            },
            {
                'name': 'temporalCoverage'
            },
            {
                'name': 'temporalResolution'
            },
            {
                'name': 'accrualPeriodicity'
            },
            {
                'name': 'distributions'
            },
            {
                'name': 'issued'
            },
            {
                'name': 'modified'
            },
            {
                'name': 'keywords'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'workflowKeywords'
            },
            {
                'name': 'taxonomyKeywords'
            },
            {
                'name': 'items'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'concepts'
            },
            {
                'name': 'dataSet'
            },
            {
                'name': 'services'
            },
            {
                'name': 'sampleData'
            },
            {
                'name': 'image'
            },
            {
                'name': 'coordinateReferenceSystemId'
            },
            {
                'name': 'spatialRepresentationType'
            },
            {
                'name': 'lineage'
            },
            {
                'name': 'fromTemplate'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'metadataContact'
            },
            {
                'name': 'publicContact'
            },
            {
                'name': 'approvalForAccessNumber'
            },
            {
                'name': 'approvalForAccessStatus'
            },
            {
                'name': 'language'
            },
            {
                'name': 'characterSet'
            },
            {
                'name': 'hierarchyLevel'
            },
            {
                'name': 'metadataLanguage'
            },
            {
                'name': 'metadataCharacterSet'
            },
            {
                'name': 'metadataStandardName'
            },
            {
                'name': 'metadataStandardVersion'
            },
            {
                'name': 'draftStatus'
            },
            {
                'name': 'draftNotes'
            },
            {
                'name': 'publishedStatus'
            },
            {
                'name': 'templateId'
            },
        ]
    },
    '/data-sets/{dataSetId}-DELETE': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/draft-DELETE': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/draft-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/access-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/fileDataset-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/harvest/{group}/dcat-GET': {
        'parameters': [
            {
                'name': 'group'
            },
        ]
    },
    '/data-sets/{dataSetId}-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/validationReport-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/draft/validationReport-GET': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets-GET': {
        'parameters': [
            {
                'name': 'ids'
            },
            {
                'name': 'creator'
            },
            {
                'name': 'keywords'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'tagRelationship'
            },
            {
                'name': 'category'
            },
            {
                'name': 'spatialCoverage'
            },
            {
                'name': 'text'
            },
            {
                'name': 'extendedText'
            },
            {
                'name': 'identities'
            },
            {
                'name': 'onlyFeatured'
            },
            {
                'name': 'showEditable'
            },
            {
                'name': 'showHidden'
            },
            {
                'name': 'pageNum'
            },
            {
                'name': 'pageSize'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'searchType'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'legacyConcepts'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'exchange'
            },
            {
                'name': 'metadataStandardName'
            },
            {
                'name': 'draftStatus'
            },
            {
                'name': 'publishedStatus'
            },
            {
                'name': 'licence'
            },
        ]
    },
    '/categories-GET': {
        'parameters': [
        ]
    },
    '/tags-GET': {
        'parameters': [
        ]
    },
    '/data-sets/{dataSetId}/access-PATCH': {
        'parameters': [
            {
                'name': 'entitlements'
            },
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}/image-PUT': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
        ]
    },
    '/data-sets/{dataSetId}-PATCH': {
        'parameters': [
            {
                'name': 'dataSetId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'summary'
            },
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'alternativeTitles'
            },
            {
                'name': 'scoringURI'
            },
            {
                'name': 'endpointKey'
            },
            {
                'name': 'derivedFrom'
            },
            {
                'name': 'creator'
            },
            {
                'name': 'dataReliability'
            },
            {
                'name': 'license'
            },
            {
                'name': 'licence'
            },
            {
                'name': 'resources'
            },
            {
                'name': 'dataFormats'
            },
            {
                'name': 'spatialCoverage'
            },
            {
                'name': 'spatialResolution'
            },
            {
                'name': 'geospatialExtent'
            },
            {
                'name': 'temporalCoverage'
            },
            {
                'name': 'temporalExtent'
            },
            {
                'name': 'temporalResolution'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'workflowKeywords'
            },
            {
                'name': 'taxonomyKeywords'
            },
            {
                'name': 'accrualPeriodicity'
            },
            {
                'name': 'issued'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'published'
            },
            {
                'name': 'publishedStatus'
            },
            {
                'name': 'modified'
            },
            {
                'name': 'items'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'pricingDescription'
            },
            {
                'name': 'distributions'
            },
            {
                'name': 'approvalForAccessNumber'
            },
            {
                'name': 'approvalForAccessStatus'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'metadataContact'
            },
            {
                'name': 'lineage'
            },
            {
                'name': 'language'
            },
            {
                'name': 'characterSet'
            },
            {
                'name': 'hierarchyLevel'
            },
            {
                'name': 'metadataLanguage'
            },
            {
                'name': 'metadataCharacterSet'
            },
            {
                'name': 'metadataStandardName'
            },
            {
                'name': 'metadataStandardVersion'
            },
            {
                'name': 'coordinateReferenceSystemId'
            },
            {
                'name': 'spatialRepresentationType'
            },
        ]
    },
    '/data-sets/{dataSetId}-PUT': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'description'
            },
            {
                'name': 'entryType'
            },
            {
                'name': 'dataSetId'
            },
            {
                'name': 'tags'
            },
            {
                'name': 'summary'
            },
            {
                'name': 'id'
            },
            {
                'name': 'exchange'
            },
            {
                'name': 'alternativeTitles'
            },
            {
                'name': 'scoringURI'
            },
            {
                'name': 'endpointKey'
            },
            {
                'name': 'isOwner'
            },
            {
                'name': 'publisher'
            },
            {
                'name': 'createdAt'
            },
            {
                'name': 'published'
            },
            {
                'name': 'metadataModified'
            },
            {
                'name': 'usedBy'
            },
            {
                'name': 'derivedFrom'
            },
            {
                'name': 'entitlements'
            },
            {
                'name': 'entitlementsByIdentity'
            },
            {
                'name': 'creator'
            },
            {
                'name': 'dataReliability'
            },
            {
                'name': 'license'
            },
            {
                'name': 'licence'
            },
            {
                'name': 'landingPage'
            },
            {
                'name': 'resources'
            },
            {
                'name': 'dataFormats'
            },
            {
                'name': 'pricingDescription'
            },
            {
                'name': 'spatialCoverage'
            },
            {
                'name': 'spatialResolution'
            },
            {
                'name': 'geospatialExtent'
            },
            {
                'name': 'temporalCoverage'
            },
            {
                'name': 'temporalResolution'
            },
            {
                'name': 'accrualPeriodicity'
            },
            {
                'name': 'distributions'
            },
            {
                'name': 'issued'
            },
            {
                'name': 'modified'
            },
            {
                'name': 'keywords'
            },
            {
                'name': 'topics'
            },
            {
                'name': 'workflowKeywords'
            },
            {
                'name': 'taxonomyKeywords'
            },
            {
                'name': 'items'
            },
            {
                'name': 'visibility'
            },
            {
                'name': 'concepts'
            },
            {
                'name': 'dataSet'
            },
            {
                'name': 'services'
            },
            {
                'name': 'sampleData'
            },
            {
                'name': 'image'
            },
            {
                'name': 'coordinateReferenceSystemId'
            },
            {
                'name': 'spatialRepresentationType'
            },
            {
                'name': 'lineage'
            },
            {
                'name': 'fromTemplate'
            },
            {
                'name': 'contacts'
            },
            {
                'name': 'metadataContact'
            },
            {
                'name': 'publicContact'
            },
            {
                'name': 'approvalForAccessNumber'
            },
            {
                'name': 'approvalForAccessStatus'
            },
            {
                'name': 'language'
            },
            {
                'name': 'characterSet'
            },
            {
                'name': 'hierarchyLevel'
            },
            {
                'name': 'metadataLanguage'
            },
            {
                'name': 'metadataCharacterSet'
            },
            {
                'name': 'metadataStandardName'
            },
            {
                'name': 'metadataStandardVersion'
            },
            {
                'name': 'draftStatus'
            },
            {
                'name': 'draftNotes'
            },
            {
                'name': 'publishedStatus'
            },
        ]
    },
    '/rest/services/{datasetId}/{paramOne}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'paramOne'
            },
        ]
    },
    '/rest/services/{datasetId}/{paramOne}/{paramTwo}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'paramOne'
            },
            {
                'name': 'paramTwo'
            },
        ]
    },
    '/linked-data/concepts-GET': {
        'parameters': [
        ]
    },
    '/harvest/{group}/csw-GET': {
        'parameters': [
            {
                'name': 'group'
            },
            {
                'name': 'service'
            },
            {
                'name': 'request'
            },
            {
                'name': 'version'
            },
            {
                'name': 'startPosition'
            },
            {
                'name': 'maxRecords'
            },
            {
                'name': 'id'
            },
            {
                'name': 'outputSchema'
            },
            {
                'name': 'elementsetname'
            },
            {
                'name': 'outputFormat'
            },
            {
                'name': 'typeNames'
            },
            {
                'name': 'resultType'
            },
        ]
    },
    '/harvest/{group}/csw-POST': {
        'parameters': [
            {
                'name': 'group'
            },
            {
                'name': 'service'
            },
            {
                'name': 'request'
            },
            {
                'name': 'version'
            },
            {
                'name': 'startPosition'
            },
            {
                'name': 'maxRecords'
            },
            {
                'name': 'id'
            },
            {
                'name': 'outputSchema'
            },
            {
                'name': 'elementsetname'
            },
            {
                'name': 'outputFormat'
            },
            {
                'name': 'typeNames'
            },
            {
                'name': 'resultType'
            },
        ]
    },
    '/images/{imageType}/{imageId}-GET': {
        'parameters': [
            {
                'name': 'imageType'
            },
            {
                'name': 'imageId'
            },
            {
                'name': 'thumbnail'
            },
        ]
    },
    '/import-POST': {
        'parameters': [
        ]
    },
    '/datasets/{datasetId}/layers-POST': {
        'parameters': [
            {
                'name': 'fileUri'
            },
            {
                'name': 'datasetId'
            },
        ]
    },
    '/layers/{layerId}-PATCH': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'datetime'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/layers/{layerId}/style-POST': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'key'
            },
        ]
    },
    '/layers/{layerId}-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}/style-GET': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}/ingest-POST': {
        'parameters': [
            {
                'name': 'fileId'
            },
            {
                'name': 'layerId'
            },
            {
                'name': 'fileName'
            },
            {
                'name': 'datetime'
            },
        ]
    },
    '/layers/{layerId}/files-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'fileUri'
            },
            {
                'name': 'filename'
            },
        ]
    },
    '/layers/{layerId}/style-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}/style-PUT': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/conformance-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/map/tiles/{tileMatrixSetId}/{tileMatrix}/{tileRow}/{tileCol}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'tileMatrixSetId'
            },
            {
                'name': 'tileMatrix'
            },
            {
                'name': 'tileRow'
            },
            {
                'name': 'tileCol'
            },
            {
                'name': 'f'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/tiles/{tileMatrixSetId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'tileMatrixSetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/collections/{collectionId}/queryables-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/collections-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/tileMatrixSets-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1/tileMatrixSets/{tileMatrixSetId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'tileMatrixSetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/tiles/v1-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/items/{featureId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
            {
                'name': 'featureId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/conformance-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/queryables-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/datasets/apicss/{cssFile}-GET': {
        'parameters': [
            {
                'name': 'cssFile'
            },
        ]
    },
    '/datasets/swagger-ui/{swaggerFile}-GET': {
        'parameters': [
            {
                'name': 'swaggerFile'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/collections-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/collections/{collectionId}/items-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'collectionId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/functions-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/ogc/features/v1/openapi-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/layers/{layerId}/search/cost-POST': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'geometry'
            },
            {
                'name': 'time'
            },
            {
                'name': 'distance'
            },
        ]
    },
    '/layers/{layerId}/search/statistics-POST': {
        'parameters': [
            {
                'name': 'geometry'
            },
            {
                'name': 'layerId'
            },
            {
                'name': 'time'
            },
        ]
    },
    '/query-POST': {
        'parameters': [
            {
                'name': 'layer'
            },
        ]
    },
    '/layers/{layerId}-GET': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/layers/{layerId}/search-POST': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'geometry'
            },
            {
                'name': 'time'
            },
            {
                'name': 'outputFormat'
            },
            {
                'name': 'distance'
            },
        ]
    },
    '/serviceDefinition-POST': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'layerName'
            },
            {
                'name': 'service'
            },
            {
                'name': 'WFS'
            },
            {
                'name': 'WCS'
            },
            {
                'name': 'WMS'
            },
            {
                'name': 'WMTS'
            },
            {
                'name': 'OGCApiFeatures'
            },
            {
                'name': 'OGCApiTiles'
            },
            {
                'name': 'temporal'
            },
            {
                'name': 'datastore'
            },
            {
                'name': 'geoserverHostName'
            },
            {
                'name': 'geometryField'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'defaultEPSGCode'
            },
        ]
    },
    '/serviceDefinition/{layerId}-DELETE': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/serviceDefinition/{layerId}-GET': {
        'parameters': [
            {
                'name': 'layerId'
            },
        ]
    },
    '/serviceDefinition/{layerId}-PATCH': {
        'parameters': [
            {
                'name': 'layerId'
            },
            {
                'name': 'billable'
            },
            {
                'name': 'defaultEPSGCode'
            },
        ]
    },
    '/shapefile-POST': {
        'parameters': [
        ]
    },
    '/status-GET': {
        'parameters': [
        ]
    },
    '/data-sets/{dataSetId}/draft-status-PUT': {
        'parameters': [
            {
                'name': 'status'
            },
            {
                'name': 'dataSetId'
            },
            {
                'name': 'notes'
            },
        ]
    },
    '/templates-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'dataSet'
            },
            {
                'name': 'entitlements'
            },
            {
                'name': 'creatorEntitlements'
            },
            {
                'name': 'exchange'
            },
        ]
    },
    '/templates/{templateId}-DELETE': {
        'parameters': [
            {
                'name': 'templateId'
            },
        ]
    },
    '/templates/{templateId}-GET': {
        'parameters': [
            {
                'name': 'templateId'
            },
        ]
    },
    '/templates-GET': {
        'parameters': [
        ]
    },
    '/templates/{templateId}-PUT': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'templateId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'dataSet'
            },
            {
                'name': 'entitlements'
            },
            {
                'name': 'creatorEntitlements'
            },
            {
                'name': 'exchange'
            },
        ]
    },
    '/templates/{templateId}-PATCH': {
        'parameters': [
            {
                'name': 'templateId'
            },
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'dataSet'
            },
            {
                'name': 'entitlements'
            },
            {
                'name': 'creatorEntitlements'
            },
        ]
    },
    '/datasets/{datasetId}/wcs-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wcs-HEAD': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wfs-HEAD': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wfs-POST': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wfs-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wms-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wms-HEAD': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wmts-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
        ]
    },
    '/datasets/{datasetId}/wmts/rest/{layerName}/{style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'layerName'
            },
            {
                'name': 'style'
            },
            {
                'name': 'TileMatrixSet'
            },
            {
                'name': 'TileMatrix'
            },
            {
                'name': 'TileRow'
            },
            {
                'name': 'TileCol'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/datasets/{datasetId}/wmts/rest/{layerName}/{style}/tilejson/{imageFormat}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'layerName'
            },
            {
                'name': 'style'
            },
            {
                'name': 'imageFormat'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/datasets/{datasetId}/wmts/rest/{layerName}/{style}/{TileMatrixSet}/{TileMatrix}/{TileRow}/{TileCol}/{J}/{I}-GET': {
        'parameters': [
            {
                'name': 'datasetId'
            },
            {
                'name': 'layerName'
            },
            {
                'name': 'style'
            },
            {
                'name': 'TileMatrixSet'
            },
            {
                'name': 'TileMatrix'
            },
            {
                'name': 'TileRow'
            },
            {
                'name': 'TileCol'
            },
            {
                'name': 'J'
            },
            {
                'name': 'I'
            },
            {
                'name': 'format'
            },
        ]
    },
    '/data-requests-POST': {
        'parameters': [
            {
                'name': 'projectName'
            },
            {
                'name': 'projectManagerName'
            },
            {
                'name': 'projectManagerEmail'
            },
            {
                'name': 'datasetId'
            },
            {
                'name': 'datasetName'
            },
            {
                'name': 'requestedFormat'
            },
            {
                'name': 'geoJsonAOI'
            },
            {
                'name': 'shapefileAOI'
            },
        ]
    },
    '/data-requests/{uniqueLinkId}/geometry-GET': {
        'parameters': [
            {
                'name': 'uniqueLinkId'
            },
        ]
    },
    '/data-requests/{requestId}-GET': {
        'parameters': [
            {
                'name': 'requestId'
            },
        ]
    },
    '/data-requests/{requestId}/download-GET': {
        'parameters': [
            {
                'name': 'requestId'
            },
        ]
    },
    '/data-requests/{uniqueLinkId}/approve-GET': {
        'parameters': [
            {
                'name': 'uniqueLinkId'
            },
        ]
    },
    '/data-requests-GET': {
        'parameters': [
        ]
    },
    '/data-requests/{uniqueLinkId}/reject-GET': {
        'parameters': [
            {
                'name': 'uniqueLinkId'
            },
        ]
    },
    '/data-requests/{requestId}-PATCH': {
        'parameters': [
            {
                'name': 'requestId'
            },
            {
                'name': 'status'
            },
        ]
    },
};