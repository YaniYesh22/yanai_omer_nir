"""
Type annotations for schemas service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/type_defs/)

Usage::

    ```python
    from mypy_boto3_schemas.type_defs import CreateDiscovererRequestRequestTypeDef

    data: CreateDiscovererRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from botocore.response import StreamingBody

from .literals import CodeGenerationStatusType, DiscovererStateType, TypeType

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "CreateDiscovererRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateRegistryRequestRequestTypeDef",
    "CreateSchemaRequestRequestTypeDef",
    "DeleteDiscovererRequestRequestTypeDef",
    "DeleteRegistryRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSchemaRequestRequestTypeDef",
    "DeleteSchemaVersionRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeCodeBindingRequestRequestTypeDef",
    "DescribeDiscovererRequestRequestTypeDef",
    "DescribeRegistryRequestRequestTypeDef",
    "DescribeSchemaRequestRequestTypeDef",
    "DiscovererSummaryTypeDef",
    "ExportSchemaRequestRequestTypeDef",
    "GetCodeBindingSourceRequestRequestTypeDef",
    "GetDiscoveredSchemaRequestRequestTypeDef",
    "GetResourcePolicyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "ListDiscoverersRequestRequestTypeDef",
    "ListRegistriesRequestRequestTypeDef",
    "RegistrySummaryTypeDef",
    "ListSchemaVersionsRequestRequestTypeDef",
    "SchemaVersionSummaryTypeDef",
    "ListSchemasRequestRequestTypeDef",
    "SchemaSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutCodeBindingRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "SearchSchemaVersionSummaryTypeDef",
    "SearchSchemasRequestRequestTypeDef",
    "StartDiscovererRequestRequestTypeDef",
    "StopDiscovererRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UpdateDiscovererRequestRequestTypeDef",
    "UpdateRegistryRequestRequestTypeDef",
    "UpdateSchemaRequestRequestTypeDef",
    "CreateDiscovererResponseTypeDef",
    "CreateRegistryResponseTypeDef",
    "CreateSchemaResponseTypeDef",
    "DescribeCodeBindingResponseTypeDef",
    "DescribeDiscovererResponseTypeDef",
    "DescribeRegistryResponseTypeDef",
    "DescribeSchemaResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportSchemaResponseTypeDef",
    "GetCodeBindingSourceResponseTypeDef",
    "GetDiscoveredSchemaResponseTypeDef",
    "GetResourcePolicyResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutCodeBindingResponseTypeDef",
    "PutResourcePolicyResponseTypeDef",
    "StartDiscovererResponseTypeDef",
    "StopDiscovererResponseTypeDef",
    "UpdateDiscovererResponseTypeDef",
    "UpdateRegistryResponseTypeDef",
    "UpdateSchemaResponseTypeDef",
    "DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef",
    "ListDiscoverersResponseTypeDef",
    "ListDiscoverersRequestListDiscoverersPaginateTypeDef",
    "ListRegistriesRequestListRegistriesPaginateTypeDef",
    "ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef",
    "ListSchemasRequestListSchemasPaginateTypeDef",
    "SearchSchemasRequestSearchSchemasPaginateTypeDef",
    "ListRegistriesResponseTypeDef",
    "ListSchemaVersionsResponseTypeDef",
    "ListSchemasResponseTypeDef",
    "SearchSchemaSummaryTypeDef",
    "SearchSchemasResponseTypeDef",
)

CreateDiscovererRequestRequestTypeDef = TypedDict(
    "CreateDiscovererRequestRequestTypeDef",
    {
        "SourceArn": str,
        "Description": NotRequired[str],
        "CrossAccount": NotRequired[bool],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)
CreateRegistryRequestRequestTypeDef = TypedDict(
    "CreateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
CreateSchemaRequestRequestTypeDef = TypedDict(
    "CreateSchemaRequestRequestTypeDef",
    {
        "Content": str,
        "RegistryName": str,
        "SchemaName": str,
        "Type": TypeType,
        "Description": NotRequired[str],
        "Tags": NotRequired[Mapping[str, str]],
    },
)
DeleteDiscovererRequestRequestTypeDef = TypedDict(
    "DeleteDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
DeleteRegistryRequestRequestTypeDef = TypedDict(
    "DeleteRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": NotRequired[str],
    },
)
DeleteSchemaRequestRequestTypeDef = TypedDict(
    "DeleteSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
    },
)
DeleteSchemaVersionRequestRequestTypeDef = TypedDict(
    "DeleteSchemaVersionRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeCodeBindingRequestRequestTypeDef = TypedDict(
    "DescribeCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)
DescribeDiscovererRequestRequestTypeDef = TypedDict(
    "DescribeDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
DescribeRegistryRequestRequestTypeDef = TypedDict(
    "DescribeRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
    },
)
DescribeSchemaRequestRequestTypeDef = TypedDict(
    "DescribeSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)
DiscovererSummaryTypeDef = TypedDict(
    "DiscovererSummaryTypeDef",
    {
        "DiscovererArn": NotRequired[str],
        "DiscovererId": NotRequired[str],
        "SourceArn": NotRequired[str],
        "State": NotRequired[DiscovererStateType],
        "CrossAccount": NotRequired[bool],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ExportSchemaRequestRequestTypeDef = TypedDict(
    "ExportSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Type": str,
        "SchemaVersion": NotRequired[str],
    },
)
GetCodeBindingSourceRequestRequestTypeDef = TypedDict(
    "GetCodeBindingSourceRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)
GetDiscoveredSchemaRequestRequestTypeDef = TypedDict(
    "GetDiscoveredSchemaRequestRequestTypeDef",
    {
        "Events": Sequence[str],
        "Type": TypeType,
    },
)
GetResourcePolicyRequestRequestTypeDef = TypedDict(
    "GetResourcePolicyRequestRequestTypeDef",
    {
        "RegistryName": NotRequired[str],
    },
)
PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": NotRequired[int],
        "PageSize": NotRequired[int],
        "StartingToken": NotRequired[str],
    },
)
ListDiscoverersRequestRequestTypeDef = TypedDict(
    "ListDiscoverersRequestRequestTypeDef",
    {
        "DiscovererIdPrefix": NotRequired[str],
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "SourceArnPrefix": NotRequired[str],
    },
)
ListRegistriesRequestRequestTypeDef = TypedDict(
    "ListRegistriesRequestRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "RegistryNamePrefix": NotRequired[str],
        "Scope": NotRequired[str],
    },
)
RegistrySummaryTypeDef = TypedDict(
    "RegistrySummaryTypeDef",
    {
        "RegistryArn": NotRequired[str],
        "RegistryName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
    },
)
ListSchemaVersionsRequestRequestTypeDef = TypedDict(
    "ListSchemaVersionsRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
SchemaVersionSummaryTypeDef = TypedDict(
    "SchemaVersionSummaryTypeDef",
    {
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)
ListSchemasRequestRequestTypeDef = TypedDict(
    "ListSchemasRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
        "SchemaNamePrefix": NotRequired[str],
    },
)
SchemaSummaryTypeDef = TypedDict(
    "SchemaSummaryTypeDef",
    {
        "LastModified": NotRequired[datetime],
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "Tags": NotRequired[Dict[str, str]],
        "VersionCount": NotRequired[int],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)
PutCodeBindingRequestRequestTypeDef = TypedDict(
    "PutCodeBindingRequestRequestTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "Policy": str,
        "RegistryName": NotRequired[str],
        "RevisionId": NotRequired[str],
    },
)
SearchSchemaVersionSummaryTypeDef = TypedDict(
    "SearchSchemaVersionSummaryTypeDef",
    {
        "CreatedDate": NotRequired[datetime],
        "SchemaVersion": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)
SearchSchemasRequestRequestTypeDef = TypedDict(
    "SearchSchemasRequestRequestTypeDef",
    {
        "Keywords": str,
        "RegistryName": str,
        "Limit": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
StartDiscovererRequestRequestTypeDef = TypedDict(
    "StartDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
StopDiscovererRequestRequestTypeDef = TypedDict(
    "StopDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)
UpdateDiscovererRequestRequestTypeDef = TypedDict(
    "UpdateDiscovererRequestRequestTypeDef",
    {
        "DiscovererId": str,
        "Description": NotRequired[str],
        "CrossAccount": NotRequired[bool],
    },
)
UpdateRegistryRequestRequestTypeDef = TypedDict(
    "UpdateRegistryRequestRequestTypeDef",
    {
        "RegistryName": str,
        "Description": NotRequired[str],
    },
)
UpdateSchemaRequestRequestTypeDef = TypedDict(
    "UpdateSchemaRequestRequestTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "ClientTokenId": NotRequired[str],
        "Content": NotRequired[str],
        "Description": NotRequired[str],
        "Type": NotRequired[TypeType],
    },
)
CreateDiscovererResponseTypeDef = TypedDict(
    "CreateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateRegistryResponseTypeDef = TypedDict(
    "CreateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSchemaResponseTypeDef = TypedDict(
    "CreateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCodeBindingResponseTypeDef = TypedDict(
    "DescribeCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeDiscovererResponseTypeDef = TypedDict(
    "DescribeDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeRegistryResponseTypeDef = TypedDict(
    "DescribeRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeSchemaResponseTypeDef = TypedDict(
    "DescribeSchemaResponseTypeDef",
    {
        "Content": str,
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportSchemaResponseTypeDef = TypedDict(
    "ExportSchemaResponseTypeDef",
    {
        "Content": str,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Type": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCodeBindingSourceResponseTypeDef = TypedDict(
    "GetCodeBindingSourceResponseTypeDef",
    {
        "Body": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetDiscoveredSchemaResponseTypeDef = TypedDict(
    "GetDiscoveredSchemaResponseTypeDef",
    {
        "Content": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyResponseTypeDef = TypedDict(
    "GetResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutCodeBindingResponseTypeDef = TypedDict(
    "PutCodeBindingResponseTypeDef",
    {
        "CreationDate": datetime,
        "LastModified": datetime,
        "SchemaVersion": str,
        "Status": CodeGenerationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResponseTypeDef = TypedDict(
    "PutResourcePolicyResponseTypeDef",
    {
        "Policy": str,
        "RevisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartDiscovererResponseTypeDef = TypedDict(
    "StartDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopDiscovererResponseTypeDef = TypedDict(
    "StopDiscovererResponseTypeDef",
    {
        "DiscovererId": str,
        "State": DiscovererStateType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateDiscovererResponseTypeDef = TypedDict(
    "UpdateDiscovererResponseTypeDef",
    {
        "Description": str,
        "DiscovererArn": str,
        "DiscovererId": str,
        "SourceArn": str,
        "State": DiscovererStateType,
        "CrossAccount": bool,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRegistryResponseTypeDef = TypedDict(
    "UpdateRegistryResponseTypeDef",
    {
        "Description": str,
        "RegistryArn": str,
        "RegistryName": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSchemaResponseTypeDef = TypedDict(
    "UpdateSchemaResponseTypeDef",
    {
        "Description": str,
        "LastModified": datetime,
        "SchemaArn": str,
        "SchemaName": str,
        "SchemaVersion": str,
        "Tags": Dict[str, str],
        "Type": str,
        "VersionCreatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef = TypedDict(
    "DescribeCodeBindingRequestCodeBindingExistsWaitTypeDef",
    {
        "Language": str,
        "RegistryName": str,
        "SchemaName": str,
        "SchemaVersion": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
ListDiscoverersResponseTypeDef = TypedDict(
    "ListDiscoverersResponseTypeDef",
    {
        "Discoverers": List[DiscovererSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListDiscoverersRequestListDiscoverersPaginateTypeDef = TypedDict(
    "ListDiscoverersRequestListDiscoverersPaginateTypeDef",
    {
        "DiscovererIdPrefix": NotRequired[str],
        "SourceArnPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegistriesRequestListRegistriesPaginateTypeDef = TypedDict(
    "ListRegistriesRequestListRegistriesPaginateTypeDef",
    {
        "RegistryNamePrefix": NotRequired[str],
        "Scope": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef = TypedDict(
    "ListSchemaVersionsRequestListSchemaVersionsPaginateTypeDef",
    {
        "RegistryName": str,
        "SchemaName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSchemasRequestListSchemasPaginateTypeDef = TypedDict(
    "ListSchemasRequestListSchemasPaginateTypeDef",
    {
        "RegistryName": str,
        "SchemaNamePrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SearchSchemasRequestSearchSchemasPaginateTypeDef = TypedDict(
    "SearchSchemasRequestSearchSchemasPaginateTypeDef",
    {
        "Keywords": str,
        "RegistryName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRegistriesResponseTypeDef = TypedDict(
    "ListRegistriesResponseTypeDef",
    {
        "NextToken": str,
        "Registries": List[RegistrySummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchemaVersionsResponseTypeDef = TypedDict(
    "ListSchemaVersionsResponseTypeDef",
    {
        "NextToken": str,
        "SchemaVersions": List[SchemaVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSchemasResponseTypeDef = TypedDict(
    "ListSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List[SchemaSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SearchSchemaSummaryTypeDef = TypedDict(
    "SearchSchemaSummaryTypeDef",
    {
        "RegistryName": NotRequired[str],
        "SchemaArn": NotRequired[str],
        "SchemaName": NotRequired[str],
        "SchemaVersions": NotRequired[List[SearchSchemaVersionSummaryTypeDef]],
    },
)
SearchSchemasResponseTypeDef = TypedDict(
    "SearchSchemasResponseTypeDef",
    {
        "NextToken": str,
        "Schemas": List[SearchSchemaSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
