"""
Type annotations for kinesis service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_kinesis/type_defs/)

Usage::

    ```python
    from mypy_boto3_kinesis.type_defs import AddTagsToStreamInputRequestTypeDef

    data: AddTagsToStreamInputRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.eventstream import EventStream
from botocore.response import StreamingBody

from .literals import (
    ConsumerStatusType,
    EncryptionTypeType,
    MetricsNameType,
    ShardFilterTypeType,
    ShardIteratorTypeType,
    StreamModeType,
    StreamStatusType,
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
    "AddTagsToStreamInputRequestTypeDef",
    "BlobTypeDef",
    "HashKeyRangeTypeDef",
    "ConsumerDescriptionTypeDef",
    "ConsumerTypeDef",
    "StreamModeDetailsTypeDef",
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    "DeleteResourcePolicyInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DeregisterStreamConsumerInputRequestTypeDef",
    "ResponseMetadataTypeDef",
    "DescribeStreamConsumerInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeStreamSummaryInputRequestTypeDef",
    "DisableEnhancedMonitoringInputRequestTypeDef",
    "EnableEnhancedMonitoringInputRequestTypeDef",
    "EnhancedMetricsTypeDef",
    "GetRecordsInputRequestTypeDef",
    "RecordTypeDef",
    "GetResourcePolicyInputRequestTypeDef",
    "TimestampTypeDef",
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    "InternalFailureExceptionTypeDef",
    "KMSAccessDeniedExceptionTypeDef",
    "KMSDisabledExceptionTypeDef",
    "KMSInvalidStateExceptionTypeDef",
    "KMSNotFoundExceptionTypeDef",
    "KMSOptInRequiredTypeDef",
    "KMSThrottlingExceptionTypeDef",
    "ListStreamsInputRequestTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "TagTypeDef",
    "MergeShardsInputRequestTypeDef",
    "PutRecordsResultEntryTypeDef",
    "PutResourcePolicyInputRequestTypeDef",
    "RegisterStreamConsumerInputRequestTypeDef",
    "RemoveTagsFromStreamInputRequestTypeDef",
    "ResourceInUseExceptionTypeDef",
    "ResourceNotFoundExceptionTypeDef",
    "SequenceNumberRangeTypeDef",
    "SplitShardInputRequestTypeDef",
    "StartStreamEncryptionInputRequestTypeDef",
    "StopStreamEncryptionInputRequestTypeDef",
    "UpdateShardCountInputRequestTypeDef",
    "PutRecordInputRequestTypeDef",
    "PutRecordsRequestEntryTypeDef",
    "ChildShardTypeDef",
    "CreateStreamInputRequestTypeDef",
    "StreamSummaryTypeDef",
    "UpdateStreamModeInputRequestTypeDef",
    "DescribeLimitsOutputTypeDef",
    "DescribeStreamConsumerOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EnhancedMonitoringOutputTypeDef",
    "GetResourcePolicyOutputTypeDef",
    "GetShardIteratorOutputTypeDef",
    "ListStreamConsumersOutputTypeDef",
    "PutRecordOutputTypeDef",
    "RegisterStreamConsumerOutputTypeDef",
    "UpdateShardCountOutputTypeDef",
    "DescribeStreamInputDescribeStreamPaginateTypeDef",
    "ListStreamsInputListStreamsPaginateTypeDef",
    "DescribeStreamInputStreamExistsWaitTypeDef",
    "DescribeStreamInputStreamNotExistsWaitTypeDef",
    "StreamDescriptionSummaryTypeDef",
    "GetShardIteratorInputRequestTypeDef",
    "ListStreamConsumersInputListStreamConsumersPaginateTypeDef",
    "ListStreamConsumersInputRequestTypeDef",
    "ShardFilterTypeDef",
    "StartingPositionTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "PutRecordsOutputTypeDef",
    "ShardTypeDef",
    "PutRecordsInputRequestTypeDef",
    "GetRecordsOutputTypeDef",
    "SubscribeToShardEventTypeDef",
    "ListStreamsOutputTypeDef",
    "DescribeStreamSummaryOutputTypeDef",
    "ListShardsInputListShardsPaginateTypeDef",
    "ListShardsInputRequestTypeDef",
    "SubscribeToShardInputRequestTypeDef",
    "ListShardsOutputTypeDef",
    "StreamDescriptionTypeDef",
    "SubscribeToShardEventStreamTypeDef",
    "DescribeStreamOutputTypeDef",
    "SubscribeToShardOutputTypeDef",
)

AddTagsToStreamInputRequestTypeDef = TypedDict(
    "AddTagsToStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
HashKeyRangeTypeDef = TypedDict(
    "HashKeyRangeTypeDef",
    {
        "StartingHashKey": str,
        "EndingHashKey": str,
    },
)
ConsumerDescriptionTypeDef = TypedDict(
    "ConsumerDescriptionTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
        "StreamARN": str,
    },
)
ConsumerTypeDef = TypedDict(
    "ConsumerTypeDef",
    {
        "ConsumerName": str,
        "ConsumerARN": str,
        "ConsumerStatus": ConsumerStatusType,
        "ConsumerCreationTimestamp": datetime,
    },
)
StreamModeDetailsTypeDef = TypedDict(
    "StreamModeDetailsTypeDef",
    {
        "StreamMode": StreamModeType,
    },
)
DecreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "DecreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
DeleteResourcePolicyInputRequestTypeDef = TypedDict(
    "DeleteResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
DeleteStreamInputRequestTypeDef = TypedDict(
    "DeleteStreamInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "EnforceConsumerDeletion": NotRequired[bool],
        "StreamARN": NotRequired[str],
    },
)
DeregisterStreamConsumerInputRequestTypeDef = TypedDict(
    "DeregisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": NotRequired[str],
        "ConsumerName": NotRequired[str],
        "ConsumerARN": NotRequired[str],
    },
)
ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
        "HostId": NotRequired[str],
    },
)
DescribeStreamConsumerInputRequestTypeDef = TypedDict(
    "DescribeStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": NotRequired[str],
        "ConsumerName": NotRequired[str],
        "ConsumerARN": NotRequired[str],
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
DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "Limit": NotRequired[int],
        "ExclusiveStartShardId": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeStreamSummaryInputRequestTypeDef = TypedDict(
    "DescribeStreamSummaryInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
DisableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "DisableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": Sequence[MetricsNameType],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
EnableEnhancedMonitoringInputRequestTypeDef = TypedDict(
    "EnableEnhancedMonitoringInputRequestTypeDef",
    {
        "ShardLevelMetrics": Sequence[MetricsNameType],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
EnhancedMetricsTypeDef = TypedDict(
    "EnhancedMetricsTypeDef",
    {
        "ShardLevelMetrics": NotRequired[List[MetricsNameType]],
    },
)
GetRecordsInputRequestTypeDef = TypedDict(
    "GetRecordsInputRequestTypeDef",
    {
        "ShardIterator": str,
        "Limit": NotRequired[int],
        "StreamARN": NotRequired[str],
    },
)
RecordTypeDef = TypedDict(
    "RecordTypeDef",
    {
        "SequenceNumber": str,
        "Data": bytes,
        "PartitionKey": str,
        "ApproximateArrivalTimestamp": NotRequired[datetime],
        "EncryptionType": NotRequired[EncryptionTypeType],
    },
)
GetResourcePolicyInputRequestTypeDef = TypedDict(
    "GetResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
TimestampTypeDef = Union[datetime, str]
IncreaseStreamRetentionPeriodInputRequestTypeDef = TypedDict(
    "IncreaseStreamRetentionPeriodInputRequestTypeDef",
    {
        "RetentionPeriodHours": int,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
InternalFailureExceptionTypeDef = TypedDict(
    "InternalFailureExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSAccessDeniedExceptionTypeDef = TypedDict(
    "KMSAccessDeniedExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSDisabledExceptionTypeDef = TypedDict(
    "KMSDisabledExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSInvalidStateExceptionTypeDef = TypedDict(
    "KMSInvalidStateExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSNotFoundExceptionTypeDef = TypedDict(
    "KMSNotFoundExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSOptInRequiredTypeDef = TypedDict(
    "KMSOptInRequiredTypeDef",
    {
        "message": NotRequired[str],
    },
)
KMSThrottlingExceptionTypeDef = TypedDict(
    "KMSThrottlingExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "Limit": NotRequired[int],
        "ExclusiveStartStreamName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "ExclusiveStartTagKey": NotRequired[str],
        "Limit": NotRequired[int],
        "StreamARN": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": NotRequired[str],
    },
)
MergeShardsInputRequestTypeDef = TypedDict(
    "MergeShardsInputRequestTypeDef",
    {
        "ShardToMerge": str,
        "AdjacentShardToMerge": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
PutRecordsResultEntryTypeDef = TypedDict(
    "PutRecordsResultEntryTypeDef",
    {
        "SequenceNumber": NotRequired[str],
        "ShardId": NotRequired[str],
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
    },
)
PutResourcePolicyInputRequestTypeDef = TypedDict(
    "PutResourcePolicyInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Policy": str,
    },
)
RegisterStreamConsumerInputRequestTypeDef = TypedDict(
    "RegisterStreamConsumerInputRequestTypeDef",
    {
        "StreamARN": str,
        "ConsumerName": str,
    },
)
RemoveTagsFromStreamInputRequestTypeDef = TypedDict(
    "RemoveTagsFromStreamInputRequestTypeDef",
    {
        "TagKeys": Sequence[str],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
ResourceInUseExceptionTypeDef = TypedDict(
    "ResourceInUseExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
ResourceNotFoundExceptionTypeDef = TypedDict(
    "ResourceNotFoundExceptionTypeDef",
    {
        "message": NotRequired[str],
    },
)
SequenceNumberRangeTypeDef = TypedDict(
    "SequenceNumberRangeTypeDef",
    {
        "StartingSequenceNumber": str,
        "EndingSequenceNumber": NotRequired[str],
    },
)
SplitShardInputRequestTypeDef = TypedDict(
    "SplitShardInputRequestTypeDef",
    {
        "ShardToSplit": str,
        "NewStartingHashKey": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
StartStreamEncryptionInputRequestTypeDef = TypedDict(
    "StartStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
StopStreamEncryptionInputRequestTypeDef = TypedDict(
    "StopStreamEncryptionInputRequestTypeDef",
    {
        "EncryptionType": EncryptionTypeType,
        "KeyId": str,
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
UpdateShardCountInputRequestTypeDef = TypedDict(
    "UpdateShardCountInputRequestTypeDef",
    {
        "TargetShardCount": int,
        "ScalingType": Literal["UNIFORM_SCALING"],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
PutRecordInputRequestTypeDef = TypedDict(
    "PutRecordInputRequestTypeDef",
    {
        "Data": BlobTypeDef,
        "PartitionKey": str,
        "StreamName": NotRequired[str],
        "ExplicitHashKey": NotRequired[str],
        "SequenceNumberForOrdering": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
PutRecordsRequestEntryTypeDef = TypedDict(
    "PutRecordsRequestEntryTypeDef",
    {
        "Data": BlobTypeDef,
        "PartitionKey": str,
        "ExplicitHashKey": NotRequired[str],
    },
)
ChildShardTypeDef = TypedDict(
    "ChildShardTypeDef",
    {
        "ShardId": str,
        "ParentShards": List[str],
        "HashKeyRange": HashKeyRangeTypeDef,
    },
)
CreateStreamInputRequestTypeDef = TypedDict(
    "CreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "ShardCount": NotRequired[int],
        "StreamModeDetails": NotRequired[StreamModeDetailsTypeDef],
    },
)
StreamSummaryTypeDef = TypedDict(
    "StreamSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "StreamModeDetails": NotRequired[StreamModeDetailsTypeDef],
        "StreamCreationTimestamp": NotRequired[datetime],
    },
)
UpdateStreamModeInputRequestTypeDef = TypedDict(
    "UpdateStreamModeInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamModeDetails": StreamModeDetailsTypeDef,
    },
)
DescribeLimitsOutputTypeDef = TypedDict(
    "DescribeLimitsOutputTypeDef",
    {
        "ShardLimit": int,
        "OpenShardCount": int,
        "OnDemandStreamCount": int,
        "OnDemandStreamCountLimit": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStreamConsumerOutputTypeDef = TypedDict(
    "DescribeStreamConsumerOutputTypeDef",
    {
        "ConsumerDescription": ConsumerDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EnhancedMonitoringOutputTypeDef = TypedDict(
    "EnhancedMonitoringOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardLevelMetrics": List[MetricsNameType],
        "DesiredShardLevelMetrics": List[MetricsNameType],
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetResourcePolicyOutputTypeDef = TypedDict(
    "GetResourcePolicyOutputTypeDef",
    {
        "Policy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetShardIteratorOutputTypeDef = TypedDict(
    "GetShardIteratorOutputTypeDef",
    {
        "ShardIterator": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStreamConsumersOutputTypeDef = TypedDict(
    "ListStreamConsumersOutputTypeDef",
    {
        "Consumers": List[ConsumerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
PutRecordOutputTypeDef = TypedDict(
    "PutRecordOutputTypeDef",
    {
        "ShardId": str,
        "SequenceNumber": str,
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterStreamConsumerOutputTypeDef = TypedDict(
    "RegisterStreamConsumerOutputTypeDef",
    {
        "Consumer": ConsumerTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateShardCountOutputTypeDef = TypedDict(
    "UpdateShardCountOutputTypeDef",
    {
        "StreamName": str,
        "CurrentShardCount": int,
        "TargetShardCount": int,
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStreamInputDescribeStreamPaginateTypeDef = TypedDict(
    "DescribeStreamInputDescribeStreamPaginateTypeDef",
    {
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStreamsInputListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsInputListStreamsPaginateTypeDef",
    {
        "ExclusiveStartStreamName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStreamInputStreamExistsWaitTypeDef = TypedDict(
    "DescribeStreamInputStreamExistsWaitTypeDef",
    {
        "StreamName": NotRequired[str],
        "Limit": NotRequired[int],
        "ExclusiveStartShardId": NotRequired[str],
        "StreamARN": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStreamInputStreamNotExistsWaitTypeDef = TypedDict(
    "DescribeStreamInputStreamNotExistsWaitTypeDef",
    {
        "StreamName": NotRequired[str],
        "Limit": NotRequired[int],
        "ExclusiveStartShardId": NotRequired[str],
        "StreamARN": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
StreamDescriptionSummaryTypeDef = TypedDict(
    "StreamDescriptionSummaryTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[EnhancedMetricsTypeDef],
        "OpenShardCount": int,
        "StreamModeDetails": NotRequired[StreamModeDetailsTypeDef],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KeyId": NotRequired[str],
        "ConsumerCount": NotRequired[int],
    },
)
GetShardIteratorInputRequestTypeDef = TypedDict(
    "GetShardIteratorInputRequestTypeDef",
    {
        "ShardId": str,
        "ShardIteratorType": ShardIteratorTypeType,
        "StreamName": NotRequired[str],
        "StartingSequenceNumber": NotRequired[str],
        "Timestamp": NotRequired[TimestampTypeDef],
        "StreamARN": NotRequired[str],
    },
)
ListStreamConsumersInputListStreamConsumersPaginateTypeDef = TypedDict(
    "ListStreamConsumersInputListStreamConsumersPaginateTypeDef",
    {
        "StreamARN": str,
        "StreamCreationTimestamp": NotRequired[TimestampTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStreamConsumersInputRequestTypeDef = TypedDict(
    "ListStreamConsumersInputRequestTypeDef",
    {
        "StreamARN": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StreamCreationTimestamp": NotRequired[TimestampTypeDef],
    },
)
ShardFilterTypeDef = TypedDict(
    "ShardFilterTypeDef",
    {
        "Type": ShardFilterTypeType,
        "ShardId": NotRequired[str],
        "Timestamp": NotRequired[TimestampTypeDef],
    },
)
StartingPositionTypeDef = TypedDict(
    "StartingPositionTypeDef",
    {
        "Type": ShardIteratorTypeType,
        "SequenceNumber": NotRequired[str],
        "Timestamp": NotRequired[TimestampTypeDef],
    },
)
ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "Tags": List[TagTypeDef],
        "HasMoreTags": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutRecordsOutputTypeDef = TypedDict(
    "PutRecordsOutputTypeDef",
    {
        "FailedRecordCount": int,
        "Records": List[PutRecordsResultEntryTypeDef],
        "EncryptionType": EncryptionTypeType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ShardTypeDef = TypedDict(
    "ShardTypeDef",
    {
        "ShardId": str,
        "HashKeyRange": HashKeyRangeTypeDef,
        "SequenceNumberRange": SequenceNumberRangeTypeDef,
        "ParentShardId": NotRequired[str],
        "AdjacentParentShardId": NotRequired[str],
    },
)
PutRecordsInputRequestTypeDef = TypedDict(
    "PutRecordsInputRequestTypeDef",
    {
        "Records": Sequence[PutRecordsRequestEntryTypeDef],
        "StreamName": NotRequired[str],
        "StreamARN": NotRequired[str],
    },
)
GetRecordsOutputTypeDef = TypedDict(
    "GetRecordsOutputTypeDef",
    {
        "Records": List[RecordTypeDef],
        "NextShardIterator": str,
        "MillisBehindLatest": int,
        "ChildShards": List[ChildShardTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribeToShardEventTypeDef = TypedDict(
    "SubscribeToShardEventTypeDef",
    {
        "Records": List[RecordTypeDef],
        "ContinuationSequenceNumber": str,
        "MillisBehindLatest": int,
        "ChildShards": NotRequired[List[ChildShardTypeDef]],
    },
)
ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamNames": List[str],
        "HasMoreStreams": bool,
        "StreamSummaries": List[StreamSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStreamSummaryOutputTypeDef = TypedDict(
    "DescribeStreamSummaryOutputTypeDef",
    {
        "StreamDescriptionSummary": StreamDescriptionSummaryTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListShardsInputListShardsPaginateTypeDef = TypedDict(
    "ListShardsInputListShardsPaginateTypeDef",
    {
        "StreamName": NotRequired[str],
        "ExclusiveStartShardId": NotRequired[str],
        "StreamCreationTimestamp": NotRequired[TimestampTypeDef],
        "ShardFilter": NotRequired[ShardFilterTypeDef],
        "StreamARN": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListShardsInputRequestTypeDef = TypedDict(
    "ListShardsInputRequestTypeDef",
    {
        "StreamName": NotRequired[str],
        "NextToken": NotRequired[str],
        "ExclusiveStartShardId": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StreamCreationTimestamp": NotRequired[TimestampTypeDef],
        "ShardFilter": NotRequired[ShardFilterTypeDef],
        "StreamARN": NotRequired[str],
    },
)
SubscribeToShardInputRequestTypeDef = TypedDict(
    "SubscribeToShardInputRequestTypeDef",
    {
        "ConsumerARN": str,
        "ShardId": str,
        "StartingPosition": StartingPositionTypeDef,
    },
)
ListShardsOutputTypeDef = TypedDict(
    "ListShardsOutputTypeDef",
    {
        "Shards": List[ShardTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
StreamDescriptionTypeDef = TypedDict(
    "StreamDescriptionTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "StreamStatus": StreamStatusType,
        "Shards": List[ShardTypeDef],
        "HasMoreShards": bool,
        "RetentionPeriodHours": int,
        "StreamCreationTimestamp": datetime,
        "EnhancedMonitoring": List[EnhancedMetricsTypeDef],
        "StreamModeDetails": NotRequired[StreamModeDetailsTypeDef],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KeyId": NotRequired[str],
    },
)
SubscribeToShardEventStreamTypeDef = TypedDict(
    "SubscribeToShardEventStreamTypeDef",
    {
        "SubscribeToShardEvent": SubscribeToShardEventTypeDef,
        "ResourceNotFoundException": NotRequired[ResourceNotFoundExceptionTypeDef],
        "ResourceInUseException": NotRequired[ResourceInUseExceptionTypeDef],
        "KMSDisabledException": NotRequired[KMSDisabledExceptionTypeDef],
        "KMSInvalidStateException": NotRequired[KMSInvalidStateExceptionTypeDef],
        "KMSAccessDeniedException": NotRequired[KMSAccessDeniedExceptionTypeDef],
        "KMSNotFoundException": NotRequired[KMSNotFoundExceptionTypeDef],
        "KMSOptInRequired": NotRequired[KMSOptInRequiredTypeDef],
        "KMSThrottlingException": NotRequired[KMSThrottlingExceptionTypeDef],
        "InternalFailureException": NotRequired[InternalFailureExceptionTypeDef],
    },
)
DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamDescription": StreamDescriptionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SubscribeToShardOutputTypeDef = TypedDict(
    "SubscribeToShardOutputTypeDef",
    {
        "EventStream": "EventStream[SubscribeToShardEventStreamTypeDef]",
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
