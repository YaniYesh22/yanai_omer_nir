"""
Type annotations for stepfunctions service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/type_defs/)

Usage::

    ```python
    from mypy_boto3_stepfunctions.type_defs import ActivityFailedEventDetailsTypeDef

    data: ActivityFailedEventDetailsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    EncryptionTypeType,
    ExecutionRedriveFilterType,
    ExecutionRedriveStatusType,
    ExecutionStatusType,
    HistoryEventTypeType,
    IncludedDataType,
    InspectionLevelType,
    LogLevelType,
    MapRunStatusType,
    StateMachineStatusType,
    StateMachineTypeType,
    SyncExecutionStatusType,
    TestExecutionStatusType,
    ValidateStateMachineDefinitionResultCodeType,
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
    "ActivityFailedEventDetailsTypeDef",
    "ActivityListItemTypeDef",
    "ActivityScheduleFailedEventDetailsTypeDef",
    "HistoryEventExecutionDataDetailsTypeDef",
    "ActivityStartedEventDetailsTypeDef",
    "ActivityTimedOutEventDetailsTypeDef",
    "BillingDetailsTypeDef",
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    "CloudWatchLogsLogGroupTypeDef",
    "EncryptionConfigurationTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "RoutingConfigurationListItemTypeDef",
    "TracingConfigurationTypeDef",
    "DeleteActivityInputRequestTypeDef",
    "DeleteStateMachineAliasInputRequestTypeDef",
    "DeleteStateMachineInputRequestTypeDef",
    "DeleteStateMachineVersionInputRequestTypeDef",
    "DescribeActivityInputRequestTypeDef",
    "DescribeExecutionInputRequestTypeDef",
    "DescribeMapRunInputRequestTypeDef",
    "MapRunExecutionCountsTypeDef",
    "MapRunItemCountsTypeDef",
    "DescribeStateMachineAliasInputRequestTypeDef",
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    "DescribeStateMachineInputRequestTypeDef",
    "ExecutionAbortedEventDetailsTypeDef",
    "ExecutionFailedEventDetailsTypeDef",
    "ExecutionListItemTypeDef",
    "ExecutionRedrivenEventDetailsTypeDef",
    "ExecutionTimedOutEventDetailsTypeDef",
    "GetActivityTaskInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetExecutionHistoryInputRequestTypeDef",
    "LambdaFunctionFailedEventDetailsTypeDef",
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    "MapIterationEventDetailsTypeDef",
    "MapRunFailedEventDetailsTypeDef",
    "MapRunRedrivenEventDetailsTypeDef",
    "MapRunStartedEventDetailsTypeDef",
    "MapStateStartedEventDetailsTypeDef",
    "TaskFailedEventDetailsTypeDef",
    "TaskStartFailedEventDetailsTypeDef",
    "TaskStartedEventDetailsTypeDef",
    "TaskSubmitFailedEventDetailsTypeDef",
    "TaskTimedOutEventDetailsTypeDef",
    "InspectionDataRequestTypeDef",
    "InspectionDataResponseTypeDef",
    "TaskCredentialsTypeDef",
    "ListActivitiesInputRequestTypeDef",
    "ListExecutionsInputRequestTypeDef",
    "ListMapRunsInputRequestTypeDef",
    "MapRunListItemTypeDef",
    "ListStateMachineAliasesInputRequestTypeDef",
    "StateMachineAliasListItemTypeDef",
    "ListStateMachineVersionsInputRequestTypeDef",
    "StateMachineVersionListItemTypeDef",
    "ListStateMachinesInputRequestTypeDef",
    "StateMachineListItemTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "PublishStateMachineVersionInputRequestTypeDef",
    "RedriveExecutionInputRequestTypeDef",
    "SendTaskFailureInputRequestTypeDef",
    "SendTaskHeartbeatInputRequestTypeDef",
    "SendTaskSuccessInputRequestTypeDef",
    "StartExecutionInputRequestTypeDef",
    "StartSyncExecutionInputRequestTypeDef",
    "StopExecutionInputRequestTypeDef",
    "TestStateInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UpdateMapRunInputRequestTypeDef",
    "ValidateStateMachineDefinitionDiagnosticTypeDef",
    "ValidateStateMachineDefinitionInputRequestTypeDef",
    "ActivityScheduledEventDetailsTypeDef",
    "ActivitySucceededEventDetailsTypeDef",
    "ExecutionStartedEventDetailsTypeDef",
    "ExecutionSucceededEventDetailsTypeDef",
    "LambdaFunctionSucceededEventDetailsTypeDef",
    "StateEnteredEventDetailsTypeDef",
    "StateExitedEventDetailsTypeDef",
    "TaskSubmittedEventDetailsTypeDef",
    "TaskSucceededEventDetailsTypeDef",
    "LogDestinationTypeDef",
    "CreateActivityInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateActivityOutputTypeDef",
    "CreateStateMachineAliasOutputTypeDef",
    "CreateStateMachineOutputTypeDef",
    "DescribeActivityOutputTypeDef",
    "DescribeExecutionOutputTypeDef",
    "GetActivityTaskOutputTypeDef",
    "ListActivitiesOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "PublishStateMachineVersionOutputTypeDef",
    "RedriveExecutionOutputTypeDef",
    "StartExecutionOutputTypeDef",
    "StartSyncExecutionOutputTypeDef",
    "StopExecutionOutputTypeDef",
    "UpdateStateMachineAliasOutputTypeDef",
    "UpdateStateMachineOutputTypeDef",
    "CreateStateMachineAliasInputRequestTypeDef",
    "DescribeStateMachineAliasOutputTypeDef",
    "UpdateStateMachineAliasInputRequestTypeDef",
    "DescribeMapRunOutputTypeDef",
    "ListExecutionsOutputTypeDef",
    "GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef",
    "ListActivitiesInputListActivitiesPaginateTypeDef",
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    "ListMapRunsInputListMapRunsPaginateTypeDef",
    "ListStateMachinesInputListStateMachinesPaginateTypeDef",
    "InspectionDataTypeDef",
    "LambdaFunctionScheduledEventDetailsTypeDef",
    "TaskScheduledEventDetailsTypeDef",
    "ListMapRunsOutputTypeDef",
    "ListStateMachineAliasesOutputTypeDef",
    "ListStateMachineVersionsOutputTypeDef",
    "ListStateMachinesOutputTypeDef",
    "ValidateStateMachineDefinitionOutputTypeDef",
    "LoggingConfigurationOutputTypeDef",
    "LoggingConfigurationTypeDef",
    "TestStateOutputTypeDef",
    "HistoryEventTypeDef",
    "DescribeStateMachineForExecutionOutputTypeDef",
    "DescribeStateMachineOutputTypeDef",
    "CreateStateMachineInputRequestTypeDef",
    "LoggingConfigurationUnionTypeDef",
    "UpdateStateMachineInputRequestTypeDef",
    "GetExecutionHistoryOutputTypeDef",
)

ActivityFailedEventDetailsTypeDef = TypedDict(
    "ActivityFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
ActivityListItemTypeDef = TypedDict(
    "ActivityListItemTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
    },
)
ActivityScheduleFailedEventDetailsTypeDef = TypedDict(
    "ActivityScheduleFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
HistoryEventExecutionDataDetailsTypeDef = TypedDict(
    "HistoryEventExecutionDataDetailsTypeDef",
    {
        "truncated": NotRequired[bool],
    },
)
ActivityStartedEventDetailsTypeDef = TypedDict(
    "ActivityStartedEventDetailsTypeDef",
    {
        "workerName": NotRequired[str],
    },
)
ActivityTimedOutEventDetailsTypeDef = TypedDict(
    "ActivityTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
BillingDetailsTypeDef = TypedDict(
    "BillingDetailsTypeDef",
    {
        "billedMemoryUsedInMB": NotRequired[int],
        "billedDurationInMilliseconds": NotRequired[int],
    },
)
CloudWatchEventsExecutionDataDetailsTypeDef = TypedDict(
    "CloudWatchEventsExecutionDataDetailsTypeDef",
    {
        "included": NotRequired[bool],
    },
)
CloudWatchLogsLogGroupTypeDef = TypedDict(
    "CloudWatchLogsLogGroupTypeDef",
    {
        "logGroupArn": NotRequired[str],
    },
)
EncryptionConfigurationTypeDef = TypedDict(
    "EncryptionConfigurationTypeDef",
    {
        "type": EncryptionTypeType,
        "kmsKeyId": NotRequired[str],
        "kmsDataKeyReusePeriodSeconds": NotRequired[int],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "key": NotRequired[str],
        "value": NotRequired[str],
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
RoutingConfigurationListItemTypeDef = TypedDict(
    "RoutingConfigurationListItemTypeDef",
    {
        "stateMachineVersionArn": str,
        "weight": int,
    },
)
TracingConfigurationTypeDef = TypedDict(
    "TracingConfigurationTypeDef",
    {
        "enabled": NotRequired[bool],
    },
)
DeleteActivityInputRequestTypeDef = TypedDict(
    "DeleteActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)
DeleteStateMachineAliasInputRequestTypeDef = TypedDict(
    "DeleteStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)
DeleteStateMachineInputRequestTypeDef = TypedDict(
    "DeleteStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
    },
)
DeleteStateMachineVersionInputRequestTypeDef = TypedDict(
    "DeleteStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineVersionArn": str,
    },
)
DescribeActivityInputRequestTypeDef = TypedDict(
    "DescribeActivityInputRequestTypeDef",
    {
        "activityArn": str,
    },
)
DescribeExecutionInputRequestTypeDef = TypedDict(
    "DescribeExecutionInputRequestTypeDef",
    {
        "executionArn": str,
        "includedData": NotRequired[IncludedDataType],
    },
)
DescribeMapRunInputRequestTypeDef = TypedDict(
    "DescribeMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
    },
)
MapRunExecutionCountsTypeDef = TypedDict(
    "MapRunExecutionCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
        "failuresNotRedrivable": NotRequired[int],
        "pendingRedrive": NotRequired[int],
    },
)
MapRunItemCountsTypeDef = TypedDict(
    "MapRunItemCountsTypeDef",
    {
        "pending": int,
        "running": int,
        "succeeded": int,
        "failed": int,
        "timedOut": int,
        "aborted": int,
        "total": int,
        "resultsWritten": int,
        "failuresNotRedrivable": NotRequired[int],
        "pendingRedrive": NotRequired[int],
    },
)
DescribeStateMachineAliasInputRequestTypeDef = TypedDict(
    "DescribeStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
    },
)
DescribeStateMachineForExecutionInputRequestTypeDef = TypedDict(
    "DescribeStateMachineForExecutionInputRequestTypeDef",
    {
        "executionArn": str,
        "includedData": NotRequired[IncludedDataType],
    },
)
DescribeStateMachineInputRequestTypeDef = TypedDict(
    "DescribeStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "includedData": NotRequired[IncludedDataType],
    },
)
ExecutionAbortedEventDetailsTypeDef = TypedDict(
    "ExecutionAbortedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
ExecutionFailedEventDetailsTypeDef = TypedDict(
    "ExecutionFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
ExecutionListItemTypeDef = TypedDict(
    "ExecutionListItemTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": NotRequired[datetime],
        "mapRunArn": NotRequired[str],
        "itemCount": NotRequired[int],
        "stateMachineVersionArn": NotRequired[str],
        "stateMachineAliasArn": NotRequired[str],
        "redriveCount": NotRequired[int],
        "redriveDate": NotRequired[datetime],
    },
)
ExecutionRedrivenEventDetailsTypeDef = TypedDict(
    "ExecutionRedrivenEventDetailsTypeDef",
    {
        "redriveCount": NotRequired[int],
    },
)
ExecutionTimedOutEventDetailsTypeDef = TypedDict(
    "ExecutionTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
GetActivityTaskInputRequestTypeDef = TypedDict(
    "GetActivityTaskInputRequestTypeDef",
    {
        "activityArn": str,
        "workerName": NotRequired[str],
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
GetExecutionHistoryInputRequestTypeDef = TypedDict(
    "GetExecutionHistoryInputRequestTypeDef",
    {
        "executionArn": str,
        "maxResults": NotRequired[int],
        "reverseOrder": NotRequired[bool],
        "nextToken": NotRequired[str],
        "includeExecutionData": NotRequired[bool],
    },
)
LambdaFunctionFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
LambdaFunctionScheduleFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduleFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
LambdaFunctionStartFailedEventDetailsTypeDef = TypedDict(
    "LambdaFunctionStartFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
LambdaFunctionTimedOutEventDetailsTypeDef = TypedDict(
    "LambdaFunctionTimedOutEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
MapIterationEventDetailsTypeDef = TypedDict(
    "MapIterationEventDetailsTypeDef",
    {
        "name": NotRequired[str],
        "index": NotRequired[int],
    },
)
MapRunFailedEventDetailsTypeDef = TypedDict(
    "MapRunFailedEventDetailsTypeDef",
    {
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
MapRunRedrivenEventDetailsTypeDef = TypedDict(
    "MapRunRedrivenEventDetailsTypeDef",
    {
        "mapRunArn": NotRequired[str],
        "redriveCount": NotRequired[int],
    },
)
MapRunStartedEventDetailsTypeDef = TypedDict(
    "MapRunStartedEventDetailsTypeDef",
    {
        "mapRunArn": NotRequired[str],
    },
)
MapStateStartedEventDetailsTypeDef = TypedDict(
    "MapStateStartedEventDetailsTypeDef",
    {
        "length": NotRequired[int],
    },
)
TaskFailedEventDetailsTypeDef = TypedDict(
    "TaskFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
TaskStartFailedEventDetailsTypeDef = TypedDict(
    "TaskStartFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
TaskStartedEventDetailsTypeDef = TypedDict(
    "TaskStartedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
    },
)
TaskSubmitFailedEventDetailsTypeDef = TypedDict(
    "TaskSubmitFailedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
TaskTimedOutEventDetailsTypeDef = TypedDict(
    "TaskTimedOutEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
InspectionDataRequestTypeDef = TypedDict(
    "InspectionDataRequestTypeDef",
    {
        "protocol": NotRequired[str],
        "method": NotRequired[str],
        "url": NotRequired[str],
        "headers": NotRequired[str],
        "body": NotRequired[str],
    },
)
InspectionDataResponseTypeDef = TypedDict(
    "InspectionDataResponseTypeDef",
    {
        "protocol": NotRequired[str],
        "statusCode": NotRequired[str],
        "statusMessage": NotRequired[str],
        "headers": NotRequired[str],
        "body": NotRequired[str],
    },
)
TaskCredentialsTypeDef = TypedDict(
    "TaskCredentialsTypeDef",
    {
        "roleArn": NotRequired[str],
    },
)
ListActivitiesInputRequestTypeDef = TypedDict(
    "ListActivitiesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListExecutionsInputRequestTypeDef = TypedDict(
    "ListExecutionsInputRequestTypeDef",
    {
        "stateMachineArn": NotRequired[str],
        "statusFilter": NotRequired[ExecutionStatusType],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "mapRunArn": NotRequired[str],
        "redriveFilter": NotRequired[ExecutionRedriveFilterType],
    },
)
ListMapRunsInputRequestTypeDef = TypedDict(
    "ListMapRunsInputRequestTypeDef",
    {
        "executionArn": str,
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
MapRunListItemTypeDef = TypedDict(
    "MapRunListItemTypeDef",
    {
        "executionArn": str,
        "mapRunArn": str,
        "stateMachineArn": str,
        "startDate": datetime,
        "stopDate": NotRequired[datetime],
    },
)
ListStateMachineAliasesInputRequestTypeDef = TypedDict(
    "ListStateMachineAliasesInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StateMachineAliasListItemTypeDef = TypedDict(
    "StateMachineAliasListItemTypeDef",
    {
        "stateMachineAliasArn": str,
        "creationDate": datetime,
    },
)
ListStateMachineVersionsInputRequestTypeDef = TypedDict(
    "ListStateMachineVersionsInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "nextToken": NotRequired[str],
        "maxResults": NotRequired[int],
    },
)
StateMachineVersionListItemTypeDef = TypedDict(
    "StateMachineVersionListItemTypeDef",
    {
        "stateMachineVersionArn": str,
        "creationDate": datetime,
    },
)
ListStateMachinesInputRequestTypeDef = TypedDict(
    "ListStateMachinesInputRequestTypeDef",
    {
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
StateMachineListItemTypeDef = TypedDict(
    "StateMachineListItemTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
    },
)
ListTagsForResourceInputRequestTypeDef = TypedDict(
    "ListTagsForResourceInputRequestTypeDef",
    {
        "resourceArn": str,
    },
)
PublishStateMachineVersionInputRequestTypeDef = TypedDict(
    "PublishStateMachineVersionInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "revisionId": NotRequired[str],
        "description": NotRequired[str],
    },
)
RedriveExecutionInputRequestTypeDef = TypedDict(
    "RedriveExecutionInputRequestTypeDef",
    {
        "executionArn": str,
        "clientToken": NotRequired[str],
    },
)
SendTaskFailureInputRequestTypeDef = TypedDict(
    "SendTaskFailureInputRequestTypeDef",
    {
        "taskToken": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
SendTaskHeartbeatInputRequestTypeDef = TypedDict(
    "SendTaskHeartbeatInputRequestTypeDef",
    {
        "taskToken": str,
    },
)
SendTaskSuccessInputRequestTypeDef = TypedDict(
    "SendTaskSuccessInputRequestTypeDef",
    {
        "taskToken": str,
        "output": str,
    },
)
StartExecutionInputRequestTypeDef = TypedDict(
    "StartExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
    },
)
StartSyncExecutionInputRequestTypeDef = TypedDict(
    "StartSyncExecutionInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "name": NotRequired[str],
        "input": NotRequired[str],
        "traceHeader": NotRequired[str],
        "includedData": NotRequired[IncludedDataType],
    },
)
StopExecutionInputRequestTypeDef = TypedDict(
    "StopExecutionInputRequestTypeDef",
    {
        "executionArn": str,
        "error": NotRequired[str],
        "cause": NotRequired[str],
    },
)
TestStateInputRequestTypeDef = TypedDict(
    "TestStateInputRequestTypeDef",
    {
        "definition": str,
        "roleArn": str,
        "input": NotRequired[str],
        "inspectionLevel": NotRequired[InspectionLevelType],
        "revealSecrets": NotRequired[bool],
    },
)
UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UpdateMapRunInputRequestTypeDef = TypedDict(
    "UpdateMapRunInputRequestTypeDef",
    {
        "mapRunArn": str,
        "maxConcurrency": NotRequired[int],
        "toleratedFailurePercentage": NotRequired[float],
        "toleratedFailureCount": NotRequired[int],
    },
)
ValidateStateMachineDefinitionDiagnosticTypeDef = TypedDict(
    "ValidateStateMachineDefinitionDiagnosticTypeDef",
    {
        "severity": Literal["ERROR"],
        "code": str,
        "message": str,
        "location": NotRequired[str],
    },
)
ValidateStateMachineDefinitionInputRequestTypeDef = TypedDict(
    "ValidateStateMachineDefinitionInputRequestTypeDef",
    {
        "definition": str,
        "type": NotRequired[StateMachineTypeType],
    },
)
ActivityScheduledEventDetailsTypeDef = TypedDict(
    "ActivityScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "timeoutInSeconds": NotRequired[int],
        "heartbeatInSeconds": NotRequired[int],
    },
)
ActivitySucceededEventDetailsTypeDef = TypedDict(
    "ActivitySucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
ExecutionStartedEventDetailsTypeDef = TypedDict(
    "ExecutionStartedEventDetailsTypeDef",
    {
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "roleArn": NotRequired[str],
        "stateMachineAliasArn": NotRequired[str],
        "stateMachineVersionArn": NotRequired[str],
    },
)
ExecutionSucceededEventDetailsTypeDef = TypedDict(
    "ExecutionSucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
LambdaFunctionSucceededEventDetailsTypeDef = TypedDict(
    "LambdaFunctionSucceededEventDetailsTypeDef",
    {
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
StateEnteredEventDetailsTypeDef = TypedDict(
    "StateEnteredEventDetailsTypeDef",
    {
        "name": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
StateExitedEventDetailsTypeDef = TypedDict(
    "StateExitedEventDetailsTypeDef",
    {
        "name": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
TaskSubmittedEventDetailsTypeDef = TypedDict(
    "TaskSubmittedEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
TaskSucceededEventDetailsTypeDef = TypedDict(
    "TaskSucceededEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "output": NotRequired[str],
        "outputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
    },
)
LogDestinationTypeDef = TypedDict(
    "LogDestinationTypeDef",
    {
        "cloudWatchLogsLogGroup": NotRequired[CloudWatchLogsLogGroupTypeDef],
    },
)
CreateActivityInputRequestTypeDef = TypedDict(
    "CreateActivityInputRequestTypeDef",
    {
        "name": str,
        "tags": NotRequired[Sequence[TagTypeDef]],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Sequence[TagTypeDef],
    },
)
CreateActivityOutputTypeDef = TypedDict(
    "CreateActivityOutputTypeDef",
    {
        "activityArn": str,
        "creationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStateMachineAliasOutputTypeDef = TypedDict(
    "CreateStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
        "creationDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStateMachineOutputTypeDef = TypedDict(
    "CreateStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "creationDate": datetime,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeActivityOutputTypeDef = TypedDict(
    "DescribeActivityOutputTypeDef",
    {
        "activityArn": str,
        "name": str,
        "creationDate": datetime,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeExecutionOutputTypeDef = TypedDict(
    "DescribeExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "status": ExecutionStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "output": str,
        "outputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "traceHeader": str,
        "mapRunArn": str,
        "error": str,
        "cause": str,
        "stateMachineVersionArn": str,
        "stateMachineAliasArn": str,
        "redriveCount": int,
        "redriveDate": datetime,
        "redriveStatus": ExecutionRedriveStatusType,
        "redriveStatusReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetActivityTaskOutputTypeDef = TypedDict(
    "GetActivityTaskOutputTypeDef",
    {
        "taskToken": str,
        "input": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListActivitiesOutputTypeDef = TypedDict(
    "ListActivitiesOutputTypeDef",
    {
        "activities": List[ActivityListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishStateMachineVersionOutputTypeDef = TypedDict(
    "PublishStateMachineVersionOutputTypeDef",
    {
        "creationDate": datetime,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RedriveExecutionOutputTypeDef = TypedDict(
    "RedriveExecutionOutputTypeDef",
    {
        "redriveDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartExecutionOutputTypeDef = TypedDict(
    "StartExecutionOutputTypeDef",
    {
        "executionArn": str,
        "startDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSyncExecutionOutputTypeDef = TypedDict(
    "StartSyncExecutionOutputTypeDef",
    {
        "executionArn": str,
        "stateMachineArn": str,
        "name": str,
        "startDate": datetime,
        "stopDate": datetime,
        "status": SyncExecutionStatusType,
        "error": str,
        "cause": str,
        "input": str,
        "inputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "output": str,
        "outputDetails": CloudWatchEventsExecutionDataDetailsTypeDef,
        "traceHeader": str,
        "billingDetails": BillingDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StopExecutionOutputTypeDef = TypedDict(
    "StopExecutionOutputTypeDef",
    {
        "stopDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStateMachineAliasOutputTypeDef = TypedDict(
    "UpdateStateMachineAliasOutputTypeDef",
    {
        "updateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStateMachineOutputTypeDef = TypedDict(
    "UpdateStateMachineOutputTypeDef",
    {
        "updateDate": datetime,
        "revisionId": str,
        "stateMachineVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStateMachineAliasInputRequestTypeDef = TypedDict(
    "CreateStateMachineAliasInputRequestTypeDef",
    {
        "name": str,
        "routingConfiguration": Sequence[RoutingConfigurationListItemTypeDef],
        "description": NotRequired[str],
    },
)
DescribeStateMachineAliasOutputTypeDef = TypedDict(
    "DescribeStateMachineAliasOutputTypeDef",
    {
        "stateMachineAliasArn": str,
        "name": str,
        "description": str,
        "routingConfiguration": List[RoutingConfigurationListItemTypeDef],
        "creationDate": datetime,
        "updateDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStateMachineAliasInputRequestTypeDef = TypedDict(
    "UpdateStateMachineAliasInputRequestTypeDef",
    {
        "stateMachineAliasArn": str,
        "description": NotRequired[str],
        "routingConfiguration": NotRequired[Sequence[RoutingConfigurationListItemTypeDef]],
    },
)
DescribeMapRunOutputTypeDef = TypedDict(
    "DescribeMapRunOutputTypeDef",
    {
        "mapRunArn": str,
        "executionArn": str,
        "status": MapRunStatusType,
        "startDate": datetime,
        "stopDate": datetime,
        "maxConcurrency": int,
        "toleratedFailurePercentage": float,
        "toleratedFailureCount": int,
        "itemCounts": MapRunItemCountsTypeDef,
        "executionCounts": MapRunExecutionCountsTypeDef,
        "redriveCount": int,
        "redriveDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExecutionsOutputTypeDef = TypedDict(
    "ListExecutionsOutputTypeDef",
    {
        "executions": List[ExecutionListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef = TypedDict(
    "GetExecutionHistoryInputGetExecutionHistoryPaginateTypeDef",
    {
        "executionArn": str,
        "reverseOrder": NotRequired[bool],
        "includeExecutionData": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListActivitiesInputListActivitiesPaginateTypeDef = TypedDict(
    "ListActivitiesInputListActivitiesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExecutionsInputListExecutionsPaginateTypeDef = TypedDict(
    "ListExecutionsInputListExecutionsPaginateTypeDef",
    {
        "stateMachineArn": NotRequired[str],
        "statusFilter": NotRequired[ExecutionStatusType],
        "mapRunArn": NotRequired[str],
        "redriveFilter": NotRequired[ExecutionRedriveFilterType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMapRunsInputListMapRunsPaginateTypeDef = TypedDict(
    "ListMapRunsInputListMapRunsPaginateTypeDef",
    {
        "executionArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStateMachinesInputListStateMachinesPaginateTypeDef = TypedDict(
    "ListStateMachinesInputListStateMachinesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
InspectionDataTypeDef = TypedDict(
    "InspectionDataTypeDef",
    {
        "input": NotRequired[str],
        "afterInputPath": NotRequired[str],
        "afterParameters": NotRequired[str],
        "result": NotRequired[str],
        "afterResultSelector": NotRequired[str],
        "afterResultPath": NotRequired[str],
        "request": NotRequired[InspectionDataRequestTypeDef],
        "response": NotRequired[InspectionDataResponseTypeDef],
    },
)
LambdaFunctionScheduledEventDetailsTypeDef = TypedDict(
    "LambdaFunctionScheduledEventDetailsTypeDef",
    {
        "resource": str,
        "input": NotRequired[str],
        "inputDetails": NotRequired[HistoryEventExecutionDataDetailsTypeDef],
        "timeoutInSeconds": NotRequired[int],
        "taskCredentials": NotRequired[TaskCredentialsTypeDef],
    },
)
TaskScheduledEventDetailsTypeDef = TypedDict(
    "TaskScheduledEventDetailsTypeDef",
    {
        "resourceType": str,
        "resource": str,
        "region": str,
        "parameters": str,
        "timeoutInSeconds": NotRequired[int],
        "heartbeatInSeconds": NotRequired[int],
        "taskCredentials": NotRequired[TaskCredentialsTypeDef],
    },
)
ListMapRunsOutputTypeDef = TypedDict(
    "ListMapRunsOutputTypeDef",
    {
        "mapRuns": List[MapRunListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStateMachineAliasesOutputTypeDef = TypedDict(
    "ListStateMachineAliasesOutputTypeDef",
    {
        "stateMachineAliases": List[StateMachineAliasListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStateMachineVersionsOutputTypeDef = TypedDict(
    "ListStateMachineVersionsOutputTypeDef",
    {
        "stateMachineVersions": List[StateMachineVersionListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStateMachinesOutputTypeDef = TypedDict(
    "ListStateMachinesOutputTypeDef",
    {
        "stateMachines": List[StateMachineListItemTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ValidateStateMachineDefinitionOutputTypeDef = TypedDict(
    "ValidateStateMachineDefinitionOutputTypeDef",
    {
        "result": ValidateStateMachineDefinitionResultCodeType,
        "diagnostics": List[ValidateStateMachineDefinitionDiagnosticTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
LoggingConfigurationOutputTypeDef = TypedDict(
    "LoggingConfigurationOutputTypeDef",
    {
        "level": NotRequired[LogLevelType],
        "includeExecutionData": NotRequired[bool],
        "destinations": NotRequired[List[LogDestinationTypeDef]],
    },
)
LoggingConfigurationTypeDef = TypedDict(
    "LoggingConfigurationTypeDef",
    {
        "level": NotRequired[LogLevelType],
        "includeExecutionData": NotRequired[bool],
        "destinations": NotRequired[Sequence[LogDestinationTypeDef]],
    },
)
TestStateOutputTypeDef = TypedDict(
    "TestStateOutputTypeDef",
    {
        "output": str,
        "error": str,
        "cause": str,
        "inspectionData": InspectionDataTypeDef,
        "nextState": str,
        "status": TestExecutionStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
HistoryEventTypeDef = TypedDict(
    "HistoryEventTypeDef",
    {
        "timestamp": datetime,
        "type": HistoryEventTypeType,
        "id": int,
        "previousEventId": NotRequired[int],
        "activityFailedEventDetails": NotRequired[ActivityFailedEventDetailsTypeDef],
        "activityScheduleFailedEventDetails": NotRequired[
            ActivityScheduleFailedEventDetailsTypeDef
        ],
        "activityScheduledEventDetails": NotRequired[ActivityScheduledEventDetailsTypeDef],
        "activityStartedEventDetails": NotRequired[ActivityStartedEventDetailsTypeDef],
        "activitySucceededEventDetails": NotRequired[ActivitySucceededEventDetailsTypeDef],
        "activityTimedOutEventDetails": NotRequired[ActivityTimedOutEventDetailsTypeDef],
        "taskFailedEventDetails": NotRequired[TaskFailedEventDetailsTypeDef],
        "taskScheduledEventDetails": NotRequired[TaskScheduledEventDetailsTypeDef],
        "taskStartFailedEventDetails": NotRequired[TaskStartFailedEventDetailsTypeDef],
        "taskStartedEventDetails": NotRequired[TaskStartedEventDetailsTypeDef],
        "taskSubmitFailedEventDetails": NotRequired[TaskSubmitFailedEventDetailsTypeDef],
        "taskSubmittedEventDetails": NotRequired[TaskSubmittedEventDetailsTypeDef],
        "taskSucceededEventDetails": NotRequired[TaskSucceededEventDetailsTypeDef],
        "taskTimedOutEventDetails": NotRequired[TaskTimedOutEventDetailsTypeDef],
        "executionFailedEventDetails": NotRequired[ExecutionFailedEventDetailsTypeDef],
        "executionStartedEventDetails": NotRequired[ExecutionStartedEventDetailsTypeDef],
        "executionSucceededEventDetails": NotRequired[ExecutionSucceededEventDetailsTypeDef],
        "executionAbortedEventDetails": NotRequired[ExecutionAbortedEventDetailsTypeDef],
        "executionTimedOutEventDetails": NotRequired[ExecutionTimedOutEventDetailsTypeDef],
        "executionRedrivenEventDetails": NotRequired[ExecutionRedrivenEventDetailsTypeDef],
        "mapStateStartedEventDetails": NotRequired[MapStateStartedEventDetailsTypeDef],
        "mapIterationStartedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationSucceededEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationFailedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "mapIterationAbortedEventDetails": NotRequired[MapIterationEventDetailsTypeDef],
        "lambdaFunctionFailedEventDetails": NotRequired[LambdaFunctionFailedEventDetailsTypeDef],
        "lambdaFunctionScheduleFailedEventDetails": NotRequired[
            LambdaFunctionScheduleFailedEventDetailsTypeDef
        ],
        "lambdaFunctionScheduledEventDetails": NotRequired[
            LambdaFunctionScheduledEventDetailsTypeDef
        ],
        "lambdaFunctionStartFailedEventDetails": NotRequired[
            LambdaFunctionStartFailedEventDetailsTypeDef
        ],
        "lambdaFunctionSucceededEventDetails": NotRequired[
            LambdaFunctionSucceededEventDetailsTypeDef
        ],
        "lambdaFunctionTimedOutEventDetails": NotRequired[
            LambdaFunctionTimedOutEventDetailsTypeDef
        ],
        "stateEnteredEventDetails": NotRequired[StateEnteredEventDetailsTypeDef],
        "stateExitedEventDetails": NotRequired[StateExitedEventDetailsTypeDef],
        "mapRunStartedEventDetails": NotRequired[MapRunStartedEventDetailsTypeDef],
        "mapRunFailedEventDetails": NotRequired[MapRunFailedEventDetailsTypeDef],
        "mapRunRedrivenEventDetails": NotRequired[MapRunRedrivenEventDetailsTypeDef],
    },
)
DescribeStateMachineForExecutionOutputTypeDef = TypedDict(
    "DescribeStateMachineForExecutionOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "definition": str,
        "roleArn": str,
        "updateDate": datetime,
        "loggingConfiguration": LoggingConfigurationOutputTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "mapRunArn": str,
        "label": str,
        "revisionId": str,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStateMachineOutputTypeDef = TypedDict(
    "DescribeStateMachineOutputTypeDef",
    {
        "stateMachineArn": str,
        "name": str,
        "status": StateMachineStatusType,
        "definition": str,
        "roleArn": str,
        "type": StateMachineTypeType,
        "creationDate": datetime,
        "loggingConfiguration": LoggingConfigurationOutputTypeDef,
        "tracingConfiguration": TracingConfigurationTypeDef,
        "label": str,
        "revisionId": str,
        "description": str,
        "encryptionConfiguration": EncryptionConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStateMachineInputRequestTypeDef = TypedDict(
    "CreateStateMachineInputRequestTypeDef",
    {
        "name": str,
        "definition": str,
        "roleArn": str,
        "type": NotRequired[StateMachineTypeType],
        "loggingConfiguration": NotRequired[LoggingConfigurationTypeDef],
        "tags": NotRequired[Sequence[TagTypeDef]],
        "tracingConfiguration": NotRequired[TracingConfigurationTypeDef],
        "publish": NotRequired[bool],
        "versionDescription": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
LoggingConfigurationUnionTypeDef = Union[
    LoggingConfigurationTypeDef, LoggingConfigurationOutputTypeDef
]
UpdateStateMachineInputRequestTypeDef = TypedDict(
    "UpdateStateMachineInputRequestTypeDef",
    {
        "stateMachineArn": str,
        "definition": NotRequired[str],
        "roleArn": NotRequired[str],
        "loggingConfiguration": NotRequired[LoggingConfigurationTypeDef],
        "tracingConfiguration": NotRequired[TracingConfigurationTypeDef],
        "publish": NotRequired[bool],
        "versionDescription": NotRequired[str],
        "encryptionConfiguration": NotRequired[EncryptionConfigurationTypeDef],
    },
)
GetExecutionHistoryOutputTypeDef = TypedDict(
    "GetExecutionHistoryOutputTypeDef",
    {
        "events": List[HistoryEventTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
