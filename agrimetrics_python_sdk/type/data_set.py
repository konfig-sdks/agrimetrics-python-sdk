# coding: utf-8

"""
    Catalog API

    This API lists data sets available on Agrimetrics platform.

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from agrimetrics_python_sdk.type.accrual_periodicity import AccrualPeriodicity
from agrimetrics_python_sdk.type.basic_data_set_info import BasicDataSetInfo
from agrimetrics_python_sdk.type.category_value import CategoryValue
from agrimetrics_python_sdk.type.contact import Contact
from agrimetrics_python_sdk.type.data_format import DataFormat
from agrimetrics_python_sdk.type.data_set_alternative_titles import DataSetAlternativeTitles
from agrimetrics_python_sdk.type.data_set_concepts import DataSetConcepts
from agrimetrics_python_sdk.type.data_set_data_set import DataSetDataSet
from agrimetrics_python_sdk.type.data_set_derived_from import DataSetDerivedFrom
from agrimetrics_python_sdk.type.data_set_distributions import DataSetDistributions
from agrimetrics_python_sdk.type.data_set_entitlements_by_identity import DataSetEntitlementsByIdentity
from agrimetrics_python_sdk.type.data_set_keywords import DataSetKeywords
from agrimetrics_python_sdk.type.data_set_sample_data import DataSetSampleData
from agrimetrics_python_sdk.type.data_set_services import DataSetServices
from agrimetrics_python_sdk.type.data_set_tags import DataSetTags
from agrimetrics_python_sdk.type.draft_status import DraftStatus
from agrimetrics_python_sdk.type.entitlement import Entitlement
from agrimetrics_python_sdk.type.entry_type import EntryType
from agrimetrics_python_sdk.type.exchange import Exchange
from agrimetrics_python_sdk.type.geospatial_extent import GeospatialExtent
from agrimetrics_python_sdk.type.image_representation import ImageRepresentation
from agrimetrics_python_sdk.type.licence import Licence
from agrimetrics_python_sdk.type.public_contact import PublicContact
from agrimetrics_python_sdk.type.published_status import PublishedStatus
from agrimetrics_python_sdk.type.resource import Resource
from agrimetrics_python_sdk.type.spatial_coverage import SpatialCoverage
from agrimetrics_python_sdk.type.taxonomy_keywords import TaxonomyKeywords
from agrimetrics_python_sdk.type.topic import Topic
from agrimetrics_python_sdk.type.workflow_keywords import WorkflowKeywords

class RequiredDataSet(TypedDict):
    # Title for the data set.
    title: str

    # Description of the data set.
    description: str

    entryType: EntryType

class OptionalDataSet(TypedDict, total=False):
    tags: DataSetTags

    # Summary of the data set.
    summary: str

    # The ID of a dataset in the catalog
    id: str

    exchange: Exchange

    alternativeTitles: DataSetAlternativeTitles

    # Scoring URI of the model.
    scoringURI: str

    # Endpoint key for the model.
    endpointKey: str

    # Whether the current user is the owner of this data set.
    isOwner: bool

    # The ID of the publisher.
    publisher: str

    # Data set creation timestamp.
    createdAt: typing.Union[int, float]

    # Data set publication timestamp.
    published: typing.Union[int, float]

    # Metadata last-modification timestmap.
    metadataModified: typing.Union[int, float]

    # Other data sets using this data set.
    usedBy: typing.List[BasicDataSetInfo]

    derivedFrom: DataSetDerivedFrom

    # Entitlements for the current user.
    entitlements: typing.List[Entitlement]

    entitlementsByIdentity: DataSetEntitlementsByIdentity

    # Creator of the data set.
    creator: str

    # Free text description about the reliability of this dataset.
    dataReliability: str

    # WARNING: This property is deprecated
    # License of the data set.
    license: str

    licence: Licence

    # WARNING: This property is deprecated
    # DEPRECATED. This has been replaced with the resources attribute. Reference URI of the data set.
    landingPage: str

    # Links containing more information on the data set
    resources: typing.List[Resource]

    # Format of the data set
    dataFormats: typing.List[DataFormat]

    # Pricing description of the data set.
    pricingDescription: str

    spatialCoverage: SpatialCoverage

    # The resolution of data set in meters.
    spatialResolution: typing.Union[int, float]

    geospatialExtent: GeospatialExtent

    # The time frame this data set covers.
    temporalCoverage: str

    # The sampling time period of the data set.
    temporalResolution: str

    accrualPeriodicity: AccrualPeriodicity

    distributions: DataSetDistributions

    # The date when the data set was issued.
    issued: str

    # An timestamp of when the data in this dataset was last updated
    modified: typing.Union[int, float]

    # WARNING: This property is deprecated
    keywords: DataSetKeywords

    # List of topics on this data set
    topics: typing.List[Topic]

    # List of workflow keywords on this data set
    workflowKeywords: typing.List[WorkflowKeywords]

    # List of keywords based on specific taxonomies
    taxonomyKeywords: typing.List[TaxonomyKeywords]

    category: CategoryValue

    # Whether or not this data set should be displayed in the index.
    visibility: str

    concepts: DataSetConcepts

    dataSet: DataSetDataSet

    services: DataSetServices

    sampleData: DataSetSampleData

    image: ImageRepresentation

    # URL to the specification of the coordinate system used in the data
    coordinateReferenceSystemId: str

    # Type of the geospatial data
    spatialRepresentationType: str

    # Information about the creation and quality assurance process of the dataset
    lineage: str

    # Information about which template was used to create the dataset record
    fromTemplate: str

    # List of contacts for this data set
    contacts: typing.List[Contact]

    metadataContact: Contact

    publicContact: PublicContact

    # Approval for access status number
    approvalForAccessNumber: typing.Union[int, float]

    # Approval for access status value
    approvalForAccessStatus: str

    # Language used on the data set
    language: str

    # Character set used on the data set
    characterSet: str

    # Hierarchy level of the data set
    hierarchyLevel: str

    # Language used on the metadata
    metadataLanguage: str

    # Character set used on the metadata
    metadataCharacterSet: str

    metadataStandardName: str

    metadataStandardVersion: str

    draftStatus: DraftStatus

    # Any notes added during review of the data set
    draftNotes: str

    publishedStatus: PublishedStatus

class DataSet(RequiredDataSet, OptionalDataSet):
    pass
