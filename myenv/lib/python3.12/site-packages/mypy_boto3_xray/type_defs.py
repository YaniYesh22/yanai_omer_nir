"""
Type annotations for xray service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/type_defs/)

Usage::

    ```python
    from mypy_boto3_xray.type_defs import AliasTypeDef

    data: AliasTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence, Union

from .literals import (
    EncryptionStatusType,
    EncryptionTypeType,
    InsightStateType,
    SamplingStrategyNameType,
    TimeRangeTypeType,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict


__all__ = (
    "AliasTypeDef",
    "AnnotationValueTypeDef",
    "ServiceIdTypeDef",
    "AvailabilityZoneDetailTypeDef",
    "BackendConnectionErrorsTypeDef",
    "PaginatorConfigTypeDef",
    "BatchGetTracesRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "InsightsConfigurationTypeDef",
    "TagTypeDef",
    "SamplingRuleTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteResourcePolicyRequestRequestTypeDef",
    "DeleteSamplingRuleRequestRequestTypeDef",
    "ErrorStatisticsTypeDef",
    "FaultStatisticsTypeDef",
    "HistogramEntryTypeDef",
    "EncryptionConfigTypeDef",
    "RootCauseExceptionTypeDef",
    "ForecastStatisticsTypeDef",
    "GetGroupRequestRequestTypeDef",
    "GetGroupsRequestRequestTypeDef",
    "GetInsightEventsRequestRequestTypeDef",
    "TimestampTypeDef",
    "GetInsightRequestRequestTypeDef",
    "GetSamplingRulesRequestRequestTypeDef",
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    "SamplingStatisticSummaryTypeDef",
    "SamplingTargetDocumentTypeDef",
    "UnprocessedStatisticsTypeDef",
    "GetTraceGraphRequestRequestTypeDef",
    "SamplingStrategyTypeDef",
    "HttpTypeDef",
    "RequestImpactStatisticsTypeDef",
    "InsightImpactGraphEdgeTypeDef",
    "InstanceIdDetailTypeDef",
    "ListResourcePoliciesRequestRequestTypeDef",
    "ResourcePolicyTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "PutEncryptionConfigRequestRequestTypeDef",
    "PutResourcePolicyRequestRequestTypeDef",
    "PutTraceSegmentsRequestRequestTypeDef",
    "UnprocessedTraceSegmentTypeDef",
    "ResourceARNDetailTypeDef",
    "ResponseTimeRootCauseEntityTypeDef",
    "SamplingRulePaginatorTypeDef",
    "SamplingRuleUpdateTypeDef",
    "SegmentTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AnomalousServiceTypeDef",
    "TraceUserTypeDef",
    "ValueWithServiceIdsTypeDef",
    "BatchGetTracesRequestBatchGetTracesPaginateTypeDef",
    "GetGroupsRequestGetGroupsPaginateTypeDef",
    "GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef",
    "GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef",
    "GetTraceGraphRequestGetTraceGraphPaginateTypeDef",
    "ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef",
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    "GroupSummaryTypeDef",
    "GroupTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateSamplingRuleRequestRequestTypeDef",
    "SamplingRuleRecordTypeDef",
    "EdgeStatisticsTypeDef",
    "ServiceStatisticsTypeDef",
    "GetEncryptionConfigResultTypeDef",
    "PutEncryptionConfigResultTypeDef",
    "ErrorRootCauseEntityTypeDef",
    "FaultRootCauseEntityTypeDef",
    "GetInsightImpactGraphRequestRequestTypeDef",
    "GetInsightSummariesRequestRequestTypeDef",
    "GetServiceGraphRequestGetServiceGraphPaginateTypeDef",
    "GetServiceGraphRequestRequestTypeDef",
    "GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef",
    "GetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    "SamplingStatisticsDocumentTypeDef",
    "TelemetryRecordTypeDef",
    "GetSamplingStatisticSummariesResultTypeDef",
    "GetSamplingTargetsResultTypeDef",
    "GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef",
    "GetTraceSummariesRequestRequestTypeDef",
    "InsightImpactGraphServiceTypeDef",
    "ListResourcePoliciesResultTypeDef",
    "PutResourcePolicyResultTypeDef",
    "PutTraceSegmentsResultTypeDef",
    "ResponseTimeRootCauseServiceTypeDef",
    "SamplingRuleRecordPaginatorTypeDef",
    "UpdateSamplingRuleRequestRequestTypeDef",
    "TraceTypeDef",
    "InsightEventTypeDef",
    "InsightSummaryTypeDef",
    "InsightTypeDef",
    "GetGroupsResultTypeDef",
    "CreateGroupResultTypeDef",
    "GetGroupResultTypeDef",
    "UpdateGroupResultTypeDef",
    "CreateSamplingRuleResultTypeDef",
    "DeleteSamplingRuleResultTypeDef",
    "GetSamplingRulesResultTypeDef",
    "UpdateSamplingRuleResultTypeDef",
    "EdgeTypeDef",
    "TimeSeriesServiceStatisticsTypeDef",
    "ErrorRootCauseServiceTypeDef",
    "FaultRootCauseServiceTypeDef",
    "GetSamplingTargetsRequestRequestTypeDef",
    "PutTelemetryRecordsRequestRequestTypeDef",
    "GetInsightImpactGraphResultTypeDef",
    "ResponseTimeRootCauseTypeDef",
    "GetSamplingRulesResultPaginatorTypeDef",
    "BatchGetTracesResultTypeDef",
    "GetInsightEventsResultTypeDef",
    "GetInsightSummariesResultTypeDef",
    "GetInsightResultTypeDef",
    "ServiceTypeDef",
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    "ErrorRootCauseTypeDef",
    "FaultRootCauseTypeDef",
    "GetServiceGraphResultTypeDef",
    "GetTraceGraphResultTypeDef",
    "TraceSummaryTypeDef",
    "GetTraceSummariesResultTypeDef",
)

AliasTypeDef = TypedDict(
    "AliasTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
    },
)
AnnotationValueTypeDef = TypedDict(
    "AnnotationValueTypeDef",
    {
        "NumberValue": NotRequired[float],
        "BooleanValue": NotRequired[bool],
        "StringValue": NotRequired[str],
    },
)
ServiceIdTypeDef = TypedDict(
    "ServiceIdTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
    },
)
AvailabilityZoneDetailTypeDef = TypedDict(
    "AvailabilityZoneDetailTypeDef",
    {
        "Name": NotRequired[str],
    },
)
BackendConnectionErrorsTypeDef = TypedDict(
    "BackendConnectionErrorsTypeDef",
    {
        "TimeoutCount": NotRequired[int],
        "ConnectionRefusedCount": NotRequired[int],
        "HTTPCode4XXCount": NotRequired[int],
        "HTTPCode5XXCount": NotRequired[int],
        "UnknownHostCount": NotRequired[int],
        "OtherCount": NotRequired[int],
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
BatchGetTracesRequestRequestTypeDef = TypedDict(
    "BatchGetTracesRequestRequestTypeDef",
    {
        "TraceIds": Sequence[str],
        "NextToken": NotRequired[str],
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
InsightsConfigurationTypeDef = TypedDict(
    "InsightsConfigurationTypeDef",
    {
        "InsightsEnabled": NotRequired[bool],
        "NotificationsEnabled": NotRequired[bool],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
SamplingRuleTypeDef = TypedDict(
    "SamplingRuleTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
    },
)
DeleteResourcePolicyRequestRequestTypeDef = TypedDict(
    "DeleteResourcePolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyRevisionId": NotRequired[str],
    },
)
DeleteSamplingRuleRequestRequestTypeDef = TypedDict(
    "DeleteSamplingRuleRequestRequestTypeDef",
    {
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
    },
)
ErrorStatisticsTypeDef = TypedDict(
    "ErrorStatisticsTypeDef",
    {
        "ThrottleCount": NotRequired[int],
        "OtherCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)
FaultStatisticsTypeDef = TypedDict(
    "FaultStatisticsTypeDef",
    {
        "OtherCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)
HistogramEntryTypeDef = TypedDict(
    "HistogramEntryTypeDef",
    {
        "Value": NotRequired[float],
        "Count": NotRequired[int],
    },
)
EncryptionConfigTypeDef = TypedDict(
    "EncryptionConfigTypeDef",
    {
        "KeyId": NotRequired[str],
        "Status": NotRequired[EncryptionStatusType],
        "Type": NotRequired[EncryptionTypeType],
    },
)
RootCauseExceptionTypeDef = TypedDict(
    "RootCauseExceptionTypeDef",
    {
        "Name": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ForecastStatisticsTypeDef = TypedDict(
    "ForecastStatisticsTypeDef",
    {
        "FaultCountHigh": NotRequired[int],
        "FaultCountLow": NotRequired[int],
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
    },
)
GetGroupsRequestRequestTypeDef = TypedDict(
    "GetGroupsRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
GetInsightEventsRequestRequestTypeDef = TypedDict(
    "GetInsightEventsRequestRequestTypeDef",
    {
        "InsightId": str,
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
TimestampTypeDef = Union[datetime, str]
GetInsightRequestRequestTypeDef = TypedDict(
    "GetInsightRequestRequestTypeDef",
    {
        "InsightId": str,
    },
)
GetSamplingRulesRequestRequestTypeDef = TypedDict(
    "GetSamplingRulesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
GetSamplingStatisticSummariesRequestRequestTypeDef = TypedDict(
    "GetSamplingStatisticSummariesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
SamplingStatisticSummaryTypeDef = TypedDict(
    "SamplingStatisticSummaryTypeDef",
    {
        "RuleName": NotRequired[str],
        "Timestamp": NotRequired[datetime],
        "RequestCount": NotRequired[int],
        "BorrowCount": NotRequired[int],
        "SampledCount": NotRequired[int],
    },
)
SamplingTargetDocumentTypeDef = TypedDict(
    "SamplingTargetDocumentTypeDef",
    {
        "RuleName": NotRequired[str],
        "FixedRate": NotRequired[float],
        "ReservoirQuota": NotRequired[int],
        "ReservoirQuotaTTL": NotRequired[datetime],
        "Interval": NotRequired[int],
    },
)
UnprocessedStatisticsTypeDef = TypedDict(
    "UnprocessedStatisticsTypeDef",
    {
        "RuleName": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)
GetTraceGraphRequestRequestTypeDef = TypedDict(
    "GetTraceGraphRequestRequestTypeDef",
    {
        "TraceIds": Sequence[str],
        "NextToken": NotRequired[str],
    },
)
SamplingStrategyTypeDef = TypedDict(
    "SamplingStrategyTypeDef",
    {
        "Name": NotRequired[SamplingStrategyNameType],
        "Value": NotRequired[float],
    },
)
HttpTypeDef = TypedDict(
    "HttpTypeDef",
    {
        "HttpURL": NotRequired[str],
        "HttpStatus": NotRequired[int],
        "HttpMethod": NotRequired[str],
        "UserAgent": NotRequired[str],
        "ClientIp": NotRequired[str],
    },
)
RequestImpactStatisticsTypeDef = TypedDict(
    "RequestImpactStatisticsTypeDef",
    {
        "FaultCount": NotRequired[int],
        "OkCount": NotRequired[int],
        "TotalCount": NotRequired[int],
    },
)
InsightImpactGraphEdgeTypeDef = TypedDict(
    "InsightImpactGraphEdgeTypeDef",
    {
        "ReferenceId": NotRequired[int],
    },
)
InstanceIdDetailTypeDef = TypedDict(
    "InstanceIdDetailTypeDef",
    {
        "Id": NotRequired[str],
    },
)
ListResourcePoliciesRequestRequestTypeDef = TypedDict(
    "ListResourcePoliciesRequestRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ResourcePolicyTypeDef = TypedDict(
    "ResourcePolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyDocument": NotRequired[str],
        "PolicyRevisionId": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "NextToken": NotRequired[str],
    },
)
PutEncryptionConfigRequestRequestTypeDef = TypedDict(
    "PutEncryptionConfigRequestRequestTypeDef",
    {
        "Type": EncryptionTypeType,
        "KeyId": NotRequired[str],
    },
)
PutResourcePolicyRequestRequestTypeDef = TypedDict(
    "PutResourcePolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
        "PolicyRevisionId": NotRequired[str],
        "BypassPolicyLockoutCheck": NotRequired[bool],
    },
)
PutTraceSegmentsRequestRequestTypeDef = TypedDict(
    "PutTraceSegmentsRequestRequestTypeDef",
    {
        "TraceSegmentDocuments": Sequence[str],
    },
)
UnprocessedTraceSegmentTypeDef = TypedDict(
    "UnprocessedTraceSegmentTypeDef",
    {
        "Id": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "Message": NotRequired[str],
    },
)
ResourceARNDetailTypeDef = TypedDict(
    "ResourceARNDetailTypeDef",
    {
        "ARN": NotRequired[str],
    },
)
ResponseTimeRootCauseEntityTypeDef = TypedDict(
    "ResponseTimeRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Coverage": NotRequired[float],
        "Remote": NotRequired[bool],
    },
)
SamplingRulePaginatorTypeDef = TypedDict(
    "SamplingRulePaginatorTypeDef",
    {
        "ResourceARN": str,
        "Priority": int,
        "FixedRate": float,
        "ReservoirSize": int,
        "ServiceName": str,
        "ServiceType": str,
        "Host": str,
        "HTTPMethod": str,
        "URLPath": str,
        "Version": int,
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "Attributes": NotRequired[Dict[str, str]],
    },
)
SamplingRuleUpdateTypeDef = TypedDict(
    "SamplingRuleUpdateTypeDef",
    {
        "RuleName": NotRequired[str],
        "RuleARN": NotRequired[str],
        "ResourceARN": NotRequired[str],
        "Priority": NotRequired[int],
        "FixedRate": NotRequired[float],
        "ReservoirSize": NotRequired[int],
        "Host": NotRequired[str],
        "ServiceName": NotRequired[str],
        "ServiceType": NotRequired[str],
        "HTTPMethod": NotRequired[str],
        "URLPath": NotRequired[str],
        "Attributes": NotRequired[Mapping[str, str]],
    },
)
SegmentTypeDef = TypedDict(
    "SegmentTypeDef",
    {
        "Id": NotRequired[str],
        "Document": NotRequired[str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": Sequence[str],
    },
)
AnomalousServiceTypeDef = TypedDict(
    "AnomalousServiceTypeDef",
    {
        "ServiceId": NotRequired[ServiceIdTypeDef],
    },
)
TraceUserTypeDef = TypedDict(
    "TraceUserTypeDef",
    {
        "UserName": NotRequired[str],
        "ServiceIds": NotRequired[List[ServiceIdTypeDef]],
    },
)
ValueWithServiceIdsTypeDef = TypedDict(
    "ValueWithServiceIdsTypeDef",
    {
        "AnnotationValue": NotRequired[AnnotationValueTypeDef],
        "ServiceIds": NotRequired[List[ServiceIdTypeDef]],
    },
)
BatchGetTracesRequestBatchGetTracesPaginateTypeDef = TypedDict(
    "BatchGetTracesRequestBatchGetTracesPaginateTypeDef",
    {
        "TraceIds": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetGroupsRequestGetGroupsPaginateTypeDef = TypedDict(
    "GetGroupsRequestGetGroupsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef = TypedDict(
    "GetSamplingRulesRequestGetSamplingRulesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef = TypedDict(
    "GetSamplingStatisticSummariesRequestGetSamplingStatisticSummariesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTraceGraphRequestGetTraceGraphPaginateTypeDef = TypedDict(
    "GetTraceGraphRequestGetTraceGraphPaginateTypeDef",
    {
        "TraceIds": Sequence[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef = TypedDict(
    "ListResourcePoliciesRequestListResourcePoliciesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTagsForResourceRequestListTagsForResourcePaginateTypeDef = TypedDict(
    "ListTagsForResourceRequestListTagsForResourcePaginateTypeDef",
    {
        "ResourceARN": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GroupSummaryTypeDef = TypedDict(
    "GroupSummaryTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired[InsightsConfigurationTypeDef],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired[InsightsConfigurationTypeDef],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired[InsightsConfigurationTypeDef],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "FilterExpression": NotRequired[str],
        "InsightsConfiguration": NotRequired[InsightsConfigurationTypeDef],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)
CreateSamplingRuleRequestRequestTypeDef = TypedDict(
    "CreateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRule": SamplingRuleTypeDef,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
SamplingRuleRecordTypeDef = TypedDict(
    "SamplingRuleRecordTypeDef",
    {
        "SamplingRule": NotRequired[SamplingRuleTypeDef],
        "CreatedAt": NotRequired[datetime],
        "ModifiedAt": NotRequired[datetime],
    },
)
EdgeStatisticsTypeDef = TypedDict(
    "EdgeStatisticsTypeDef",
    {
        "OkCount": NotRequired[int],
        "ErrorStatistics": NotRequired[ErrorStatisticsTypeDef],
        "FaultStatistics": NotRequired[FaultStatisticsTypeDef],
        "TotalCount": NotRequired[int],
        "TotalResponseTime": NotRequired[float],
    },
)
ServiceStatisticsTypeDef = TypedDict(
    "ServiceStatisticsTypeDef",
    {
        "OkCount": NotRequired[int],
        "ErrorStatistics": NotRequired[ErrorStatisticsTypeDef],
        "FaultStatistics": NotRequired[FaultStatisticsTypeDef],
        "TotalCount": NotRequired[int],
        "TotalResponseTime": NotRequired[float],
    },
)
GetEncryptionConfigResultTypeDef = TypedDict(
    "GetEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": EncryptionConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutEncryptionConfigResultTypeDef = TypedDict(
    "PutEncryptionConfigResultTypeDef",
    {
        "EncryptionConfig": EncryptionConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ErrorRootCauseEntityTypeDef = TypedDict(
    "ErrorRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Exceptions": NotRequired[List[RootCauseExceptionTypeDef]],
        "Remote": NotRequired[bool],
    },
)
FaultRootCauseEntityTypeDef = TypedDict(
    "FaultRootCauseEntityTypeDef",
    {
        "Name": NotRequired[str],
        "Exceptions": NotRequired[List[RootCauseExceptionTypeDef]],
        "Remote": NotRequired[bool],
    },
)
GetInsightImpactGraphRequestRequestTypeDef = TypedDict(
    "GetInsightImpactGraphRequestRequestTypeDef",
    {
        "InsightId": str,
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetInsightSummariesRequestRequestTypeDef = TypedDict(
    "GetInsightSummariesRequestRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "States": NotRequired[Sequence[InsightStateType]],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
GetServiceGraphRequestGetServiceGraphPaginateTypeDef = TypedDict(
    "GetServiceGraphRequestGetServiceGraphPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetServiceGraphRequestRequestTypeDef = TypedDict(
    "GetServiceGraphRequestRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsRequestGetTimeSeriesServiceStatisticsPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "EntitySelectorExpression": NotRequired[str],
        "Period": NotRequired[int],
        "ForecastStatistics": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTimeSeriesServiceStatisticsRequestRequestTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsRequestRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "GroupName": NotRequired[str],
        "GroupARN": NotRequired[str],
        "EntitySelectorExpression": NotRequired[str],
        "Period": NotRequired[int],
        "ForecastStatistics": NotRequired[bool],
        "NextToken": NotRequired[str],
    },
)
SamplingStatisticsDocumentTypeDef = TypedDict(
    "SamplingStatisticsDocumentTypeDef",
    {
        "RuleName": str,
        "ClientID": str,
        "Timestamp": TimestampTypeDef,
        "RequestCount": int,
        "SampledCount": int,
        "BorrowCount": NotRequired[int],
    },
)
TelemetryRecordTypeDef = TypedDict(
    "TelemetryRecordTypeDef",
    {
        "Timestamp": TimestampTypeDef,
        "SegmentsReceivedCount": NotRequired[int],
        "SegmentsSentCount": NotRequired[int],
        "SegmentsSpilloverCount": NotRequired[int],
        "SegmentsRejectedCount": NotRequired[int],
        "BackendConnectionErrors": NotRequired[BackendConnectionErrorsTypeDef],
    },
)
GetSamplingStatisticSummariesResultTypeDef = TypedDict(
    "GetSamplingStatisticSummariesResultTypeDef",
    {
        "SamplingStatisticSummaries": List[SamplingStatisticSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSamplingTargetsResultTypeDef = TypedDict(
    "GetSamplingTargetsResultTypeDef",
    {
        "SamplingTargetDocuments": List[SamplingTargetDocumentTypeDef],
        "LastRuleModification": datetime,
        "UnprocessedStatistics": List[UnprocessedStatisticsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef = TypedDict(
    "GetTraceSummariesRequestGetTraceSummariesPaginateTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "TimeRangeType": NotRequired[TimeRangeTypeType],
        "Sampling": NotRequired[bool],
        "SamplingStrategy": NotRequired[SamplingStrategyTypeDef],
        "FilterExpression": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetTraceSummariesRequestRequestTypeDef = TypedDict(
    "GetTraceSummariesRequestRequestTypeDef",
    {
        "StartTime": TimestampTypeDef,
        "EndTime": TimestampTypeDef,
        "TimeRangeType": NotRequired[TimeRangeTypeType],
        "Sampling": NotRequired[bool],
        "SamplingStrategy": NotRequired[SamplingStrategyTypeDef],
        "FilterExpression": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
InsightImpactGraphServiceTypeDef = TypedDict(
    "InsightImpactGraphServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Type": NotRequired[str],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "AccountId": NotRequired[str],
        "Edges": NotRequired[List[InsightImpactGraphEdgeTypeDef]],
    },
)
ListResourcePoliciesResultTypeDef = TypedDict(
    "ListResourcePoliciesResultTypeDef",
    {
        "ResourcePolicies": List[ResourcePolicyTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutResourcePolicyResultTypeDef = TypedDict(
    "PutResourcePolicyResultTypeDef",
    {
        "ResourcePolicy": ResourcePolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutTraceSegmentsResultTypeDef = TypedDict(
    "PutTraceSegmentsResultTypeDef",
    {
        "UnprocessedTraceSegments": List[UnprocessedTraceSegmentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseTimeRootCauseServiceTypeDef = TypedDict(
    "ResponseTimeRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[ResponseTimeRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)
SamplingRuleRecordPaginatorTypeDef = TypedDict(
    "SamplingRuleRecordPaginatorTypeDef",
    {
        "SamplingRule": NotRequired[SamplingRulePaginatorTypeDef],
        "CreatedAt": NotRequired[datetime],
        "ModifiedAt": NotRequired[datetime],
    },
)
UpdateSamplingRuleRequestRequestTypeDef = TypedDict(
    "UpdateSamplingRuleRequestRequestTypeDef",
    {
        "SamplingRuleUpdate": SamplingRuleUpdateTypeDef,
    },
)
TraceTypeDef = TypedDict(
    "TraceTypeDef",
    {
        "Id": NotRequired[str],
        "Duration": NotRequired[float],
        "LimitExceeded": NotRequired[bool],
        "Segments": NotRequired[List[SegmentTypeDef]],
    },
)
InsightEventTypeDef = TypedDict(
    "InsightEventTypeDef",
    {
        "Summary": NotRequired[str],
        "EventTime": NotRequired[datetime],
        "ClientRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "RootCauseServiceRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "TopAnomalousServices": NotRequired[List[AnomalousServiceTypeDef]],
    },
)
InsightSummaryTypeDef = TypedDict(
    "InsightSummaryTypeDef",
    {
        "InsightId": NotRequired[str],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "RootCauseServiceId": NotRequired[ServiceIdTypeDef],
        "Categories": NotRequired[List[Literal["FAULT"]]],
        "State": NotRequired[InsightStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Summary": NotRequired[str],
        "ClientRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "RootCauseServiceRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "TopAnomalousServices": NotRequired[List[AnomalousServiceTypeDef]],
        "LastUpdateTime": NotRequired[datetime],
    },
)
InsightTypeDef = TypedDict(
    "InsightTypeDef",
    {
        "InsightId": NotRequired[str],
        "GroupARN": NotRequired[str],
        "GroupName": NotRequired[str],
        "RootCauseServiceId": NotRequired[ServiceIdTypeDef],
        "Categories": NotRequired[List[Literal["FAULT"]]],
        "State": NotRequired[InsightStateType],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Summary": NotRequired[str],
        "ClientRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "RootCauseServiceRequestImpactStatistics": NotRequired[RequestImpactStatisticsTypeDef],
        "TopAnomalousServices": NotRequired[List[AnomalousServiceTypeDef]],
    },
)
GetGroupsResultTypeDef = TypedDict(
    "GetGroupsResultTypeDef",
    {
        "Groups": List[GroupSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupResultTypeDef = TypedDict(
    "CreateGroupResultTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResultTypeDef = TypedDict(
    "GetGroupResultTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGroupResultTypeDef = TypedDict(
    "UpdateGroupResultTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateSamplingRuleResultTypeDef = TypedDict(
    "CreateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": SamplingRuleRecordTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteSamplingRuleResultTypeDef = TypedDict(
    "DeleteSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": SamplingRuleRecordTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSamplingRulesResultTypeDef = TypedDict(
    "GetSamplingRulesResultTypeDef",
    {
        "SamplingRuleRecords": List[SamplingRuleRecordTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSamplingRuleResultTypeDef = TypedDict(
    "UpdateSamplingRuleResultTypeDef",
    {
        "SamplingRuleRecord": SamplingRuleRecordTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EdgeTypeDef = TypedDict(
    "EdgeTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "SummaryStatistics": NotRequired[EdgeStatisticsTypeDef],
        "ResponseTimeHistogram": NotRequired[List[HistogramEntryTypeDef]],
        "Aliases": NotRequired[List[AliasTypeDef]],
        "EdgeType": NotRequired[str],
        "ReceivedEventAgeHistogram": NotRequired[List[HistogramEntryTypeDef]],
    },
)
TimeSeriesServiceStatisticsTypeDef = TypedDict(
    "TimeSeriesServiceStatisticsTypeDef",
    {
        "Timestamp": NotRequired[datetime],
        "EdgeSummaryStatistics": NotRequired[EdgeStatisticsTypeDef],
        "ServiceSummaryStatistics": NotRequired[ServiceStatisticsTypeDef],
        "ServiceForecastStatistics": NotRequired[ForecastStatisticsTypeDef],
        "ResponseTimeHistogram": NotRequired[List[HistogramEntryTypeDef]],
    },
)
ErrorRootCauseServiceTypeDef = TypedDict(
    "ErrorRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[ErrorRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)
FaultRootCauseServiceTypeDef = TypedDict(
    "FaultRootCauseServiceTypeDef",
    {
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Type": NotRequired[str],
        "AccountId": NotRequired[str],
        "EntityPath": NotRequired[List[FaultRootCauseEntityTypeDef]],
        "Inferred": NotRequired[bool],
    },
)
GetSamplingTargetsRequestRequestTypeDef = TypedDict(
    "GetSamplingTargetsRequestRequestTypeDef",
    {
        "SamplingStatisticsDocuments": Sequence[SamplingStatisticsDocumentTypeDef],
    },
)
PutTelemetryRecordsRequestRequestTypeDef = TypedDict(
    "PutTelemetryRecordsRequestRequestTypeDef",
    {
        "TelemetryRecords": Sequence[TelemetryRecordTypeDef],
        "EC2InstanceId": NotRequired[str],
        "Hostname": NotRequired[str],
        "ResourceARN": NotRequired[str],
    },
)
GetInsightImpactGraphResultTypeDef = TypedDict(
    "GetInsightImpactGraphResultTypeDef",
    {
        "InsightId": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "ServiceGraphStartTime": datetime,
        "ServiceGraphEndTime": datetime,
        "Services": List[InsightImpactGraphServiceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResponseTimeRootCauseTypeDef = TypedDict(
    "ResponseTimeRootCauseTypeDef",
    {
        "Services": NotRequired[List[ResponseTimeRootCauseServiceTypeDef]],
        "ClientImpacting": NotRequired[bool],
    },
)
GetSamplingRulesResultPaginatorTypeDef = TypedDict(
    "GetSamplingRulesResultPaginatorTypeDef",
    {
        "SamplingRuleRecords": List[SamplingRuleRecordPaginatorTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchGetTracesResultTypeDef = TypedDict(
    "BatchGetTracesResultTypeDef",
    {
        "Traces": List[TraceTypeDef],
        "UnprocessedTraceIds": List[str],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightEventsResultTypeDef = TypedDict(
    "GetInsightEventsResultTypeDef",
    {
        "InsightEvents": List[InsightEventTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightSummariesResultTypeDef = TypedDict(
    "GetInsightSummariesResultTypeDef",
    {
        "InsightSummaries": List[InsightSummaryTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInsightResultTypeDef = TypedDict(
    "GetInsightResultTypeDef",
    {
        "Insight": InsightTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServiceTypeDef = TypedDict(
    "ServiceTypeDef",
    {
        "ReferenceId": NotRequired[int],
        "Name": NotRequired[str],
        "Names": NotRequired[List[str]],
        "Root": NotRequired[bool],
        "AccountId": NotRequired[str],
        "Type": NotRequired[str],
        "State": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "Edges": NotRequired[List[EdgeTypeDef]],
        "SummaryStatistics": NotRequired[ServiceStatisticsTypeDef],
        "DurationHistogram": NotRequired[List[HistogramEntryTypeDef]],
        "ResponseTimeHistogram": NotRequired[List[HistogramEntryTypeDef]],
    },
)
GetTimeSeriesServiceStatisticsResultTypeDef = TypedDict(
    "GetTimeSeriesServiceStatisticsResultTypeDef",
    {
        "TimeSeriesServiceStatistics": List[TimeSeriesServiceStatisticsTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ErrorRootCauseTypeDef = TypedDict(
    "ErrorRootCauseTypeDef",
    {
        "Services": NotRequired[List[ErrorRootCauseServiceTypeDef]],
        "ClientImpacting": NotRequired[bool],
    },
)
FaultRootCauseTypeDef = TypedDict(
    "FaultRootCauseTypeDef",
    {
        "Services": NotRequired[List[FaultRootCauseServiceTypeDef]],
        "ClientImpacting": NotRequired[bool],
    },
)
GetServiceGraphResultTypeDef = TypedDict(
    "GetServiceGraphResultTypeDef",
    {
        "StartTime": datetime,
        "EndTime": datetime,
        "Services": List[ServiceTypeDef],
        "ContainsOldGroupVersions": bool,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTraceGraphResultTypeDef = TypedDict(
    "GetTraceGraphResultTypeDef",
    {
        "Services": List[ServiceTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TraceSummaryTypeDef = TypedDict(
    "TraceSummaryTypeDef",
    {
        "Id": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "Duration": NotRequired[float],
        "ResponseTime": NotRequired[float],
        "HasFault": NotRequired[bool],
        "HasError": NotRequired[bool],
        "HasThrottle": NotRequired[bool],
        "IsPartial": NotRequired[bool],
        "Http": NotRequired[HttpTypeDef],
        "Annotations": NotRequired[Dict[str, List[ValueWithServiceIdsTypeDef]]],
        "Users": NotRequired[List[TraceUserTypeDef]],
        "ServiceIds": NotRequired[List[ServiceIdTypeDef]],
        "ResourceARNs": NotRequired[List[ResourceARNDetailTypeDef]],
        "InstanceIds": NotRequired[List[InstanceIdDetailTypeDef]],
        "AvailabilityZones": NotRequired[List[AvailabilityZoneDetailTypeDef]],
        "EntryPoint": NotRequired[ServiceIdTypeDef],
        "FaultRootCauses": NotRequired[List[FaultRootCauseTypeDef]],
        "ErrorRootCauses": NotRequired[List[ErrorRootCauseTypeDef]],
        "ResponseTimeRootCauses": NotRequired[List[ResponseTimeRootCauseTypeDef]],
        "Revision": NotRequired[int],
        "MatchedEventTime": NotRequired[datetime],
    },
)
GetTraceSummariesResultTypeDef = TypedDict(
    "GetTraceSummariesResultTypeDef",
    {
        "TraceSummaries": List[TraceSummaryTypeDef],
        "ApproximateTime": datetime,
        "TracesProcessedCount": int,
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
