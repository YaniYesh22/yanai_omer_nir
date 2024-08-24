"""
Type annotations for xray service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_xray.client import XRayClient

    session = Session()
    client: XRayClient = session.client("xray")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import EncryptionTypeType, InsightStateType, TimeRangeTypeType
from .paginator import (
    BatchGetTracesPaginator,
    GetGroupsPaginator,
    GetSamplingRulesPaginator,
    GetSamplingStatisticSummariesPaginator,
    GetServiceGraphPaginator,
    GetTimeSeriesServiceStatisticsPaginator,
    GetTraceGraphPaginator,
    GetTraceSummariesPaginator,
    ListResourcePoliciesPaginator,
    ListTagsForResourcePaginator,
)
from .type_defs import (
    BatchGetTracesResultTypeDef,
    CreateGroupResultTypeDef,
    CreateSamplingRuleResultTypeDef,
    DeleteSamplingRuleResultTypeDef,
    GetEncryptionConfigResultTypeDef,
    GetGroupResultTypeDef,
    GetGroupsResultTypeDef,
    GetInsightEventsResultTypeDef,
    GetInsightImpactGraphResultTypeDef,
    GetInsightResultTypeDef,
    GetInsightSummariesResultTypeDef,
    GetSamplingRulesResultTypeDef,
    GetSamplingStatisticSummariesResultTypeDef,
    GetSamplingTargetsResultTypeDef,
    GetServiceGraphResultTypeDef,
    GetTimeSeriesServiceStatisticsResultTypeDef,
    GetTraceGraphResultTypeDef,
    GetTraceSummariesResultTypeDef,
    InsightsConfigurationTypeDef,
    ListResourcePoliciesResultTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutEncryptionConfigResultTypeDef,
    PutResourcePolicyResultTypeDef,
    PutTraceSegmentsResultTypeDef,
    SamplingRuleTypeDef,
    SamplingRuleUpdateTypeDef,
    SamplingStatisticsDocumentTypeDef,
    SamplingStrategyTypeDef,
    TagTypeDef,
    TelemetryRecordTypeDef,
    TimestampTypeDef,
    UpdateGroupResultTypeDef,
    UpdateSamplingRuleResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("XRayClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    InvalidPolicyRevisionIdException: Type[BotocoreClientError]
    InvalidRequestException: Type[BotocoreClientError]
    LockoutPreventionException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PolicyCountLimitExceededException: Type[BotocoreClientError]
    PolicySizeLimitExceededException: Type[BotocoreClientError]
    ResourceNotFoundException: Type[BotocoreClientError]
    RuleLimitExceededException: Type[BotocoreClientError]
    ThrottledException: Type[BotocoreClientError]
    TooManyTagsException: Type[BotocoreClientError]


class XRayClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        XRayClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#exceptions)
        """

    def batch_get_traces(
        self, *, TraceIds: Sequence[str], NextToken: str = ...
    ) -> BatchGetTracesResultTypeDef:
        """
        Retrieves a list of traces specified by ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.batch_get_traces)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#batch_get_traces)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#close)
        """

    def create_group(
        self,
        *,
        GroupName: str,
        FilterExpression: str = ...,
        InsightsConfiguration: InsightsConfigurationTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateGroupResultTypeDef:
        """
        Creates a group resource with a name and a filter expression.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.create_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#create_group)
        """

    def create_sampling_rule(
        self, *, SamplingRule: SamplingRuleTypeDef, Tags: Sequence[TagTypeDef] = ...
    ) -> CreateSamplingRuleResultTypeDef:
        """
        Creates a rule to control sampling behavior for instrumented applications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.create_sampling_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#create_sampling_rule)
        """

    def delete_group(self, *, GroupName: str = ..., GroupARN: str = ...) -> Dict[str, Any]:
        """
        Deletes a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.delete_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#delete_group)
        """

    def delete_resource_policy(
        self, *, PolicyName: str, PolicyRevisionId: str = ...
    ) -> Dict[str, Any]:
        """
        Deletes a resource policy from the target Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#delete_resource_policy)
        """

    def delete_sampling_rule(
        self, *, RuleName: str = ..., RuleARN: str = ...
    ) -> DeleteSamplingRuleResultTypeDef:
        """
        Deletes a sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.delete_sampling_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#delete_sampling_rule)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#generate_presigned_url)
        """

    def get_encryption_config(self) -> GetEncryptionConfigResultTypeDef:
        """
        Retrieves the current encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_encryption_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_encryption_config)
        """

    def get_group(self, *, GroupName: str = ..., GroupARN: str = ...) -> GetGroupResultTypeDef:
        """
        Retrieves group resource details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_group)
        """

    def get_groups(self, *, NextToken: str = ...) -> GetGroupsResultTypeDef:
        """
        Retrieves all active group details.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_groups)
        """

    def get_insight(self, *, InsightId: str) -> GetInsightResultTypeDef:
        """
        Retrieves the summary information of an insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_insight)
        """

    def get_insight_events(
        self, *, InsightId: str, MaxResults: int = ..., NextToken: str = ...
    ) -> GetInsightEventsResultTypeDef:
        """
        X-Ray reevaluates insights periodically until they're resolved, and records
        each intermediate state as an
        event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_events)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_insight_events)
        """

    def get_insight_impact_graph(
        self,
        *,
        InsightId: str,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        NextToken: str = ...
    ) -> GetInsightImpactGraphResultTypeDef:
        """
        Retrieves a service graph structure filtered by the specified insight.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_impact_graph)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_insight_impact_graph)
        """

    def get_insight_summaries(
        self,
        *,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        States: Sequence[InsightStateType] = ...,
        GroupARN: str = ...,
        GroupName: str = ...,
        MaxResults: int = ...,
        NextToken: str = ...
    ) -> GetInsightSummariesResultTypeDef:
        """
        Retrieves the summaries of all insights in the specified group matching the
        provided filter
        values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_insight_summaries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_insight_summaries)
        """

    def get_sampling_rules(self, *, NextToken: str = ...) -> GetSamplingRulesResultTypeDef:
        """
        Retrieves all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_rules)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_sampling_rules)
        """

    def get_sampling_statistic_summaries(
        self, *, NextToken: str = ...
    ) -> GetSamplingStatisticSummariesResultTypeDef:
        """
        Retrieves information about recent sampling results for all sampling rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_statistic_summaries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_sampling_statistic_summaries)
        """

    def get_sampling_targets(
        self, *, SamplingStatisticsDocuments: Sequence[SamplingStatisticsDocumentTypeDef]
    ) -> GetSamplingTargetsResultTypeDef:
        """
        Requests a sampling quota for rules that the service is using to sample
        requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_sampling_targets)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_sampling_targets)
        """

    def get_service_graph(
        self,
        *,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        GroupName: str = ...,
        GroupARN: str = ...,
        NextToken: str = ...
    ) -> GetServiceGraphResultTypeDef:
        """
        Retrieves a document that describes services that process incoming requests,
        and downstream services that they call as a
        result.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_service_graph)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_service_graph)
        """

    def get_time_series_service_statistics(
        self,
        *,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        GroupName: str = ...,
        GroupARN: str = ...,
        EntitySelectorExpression: str = ...,
        Period: int = ...,
        ForecastStatistics: bool = ...,
        NextToken: str = ...
    ) -> GetTimeSeriesServiceStatisticsResultTypeDef:
        """
        Get an aggregation of service statistics defined by a specific time range.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_time_series_service_statistics)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_time_series_service_statistics)
        """

    def get_trace_graph(
        self, *, TraceIds: Sequence[str], NextToken: str = ...
    ) -> GetTraceGraphResultTypeDef:
        """
        Retrieves a service graph for one or more specific trace IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_trace_graph)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_trace_graph)
        """

    def get_trace_summaries(
        self,
        *,
        StartTime: TimestampTypeDef,
        EndTime: TimestampTypeDef,
        TimeRangeType: TimeRangeTypeType = ...,
        Sampling: bool = ...,
        SamplingStrategy: SamplingStrategyTypeDef = ...,
        FilterExpression: str = ...,
        NextToken: str = ...
    ) -> GetTraceSummariesResultTypeDef:
        """
        Retrieves IDs and annotations for traces available for a specified time frame
        using an optional
        filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_trace_summaries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_trace_summaries)
        """

    def list_resource_policies(self, *, NextToken: str = ...) -> ListResourcePoliciesResultTypeDef:
        """
        Returns the list of resource policies in the target Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.list_resource_policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#list_resource_policies)
        """

    def list_tags_for_resource(
        self, *, ResourceARN: str, NextToken: str = ...
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Returns a list of tags that are applied to the specified Amazon Web Services
        X-Ray group or sampling
        rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#list_tags_for_resource)
        """

    def put_encryption_config(
        self, *, Type: EncryptionTypeType, KeyId: str = ...
    ) -> PutEncryptionConfigResultTypeDef:
        """
        Updates the encryption configuration for X-Ray data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_encryption_config)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#put_encryption_config)
        """

    def put_resource_policy(
        self,
        *,
        PolicyName: str,
        PolicyDocument: str,
        PolicyRevisionId: str = ...,
        BypassPolicyLockoutCheck: bool = ...
    ) -> PutResourcePolicyResultTypeDef:
        """
        Sets the resource policy to grant one or more Amazon Web Services services and
        accounts permissions to access
        X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#put_resource_policy)
        """

    def put_telemetry_records(
        self,
        *,
        TelemetryRecords: Sequence[TelemetryRecordTypeDef],
        EC2InstanceId: str = ...,
        Hostname: str = ...,
        ResourceARN: str = ...
    ) -> Dict[str, Any]:
        """
        Used by the Amazon Web Services X-Ray daemon to upload telemetry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_telemetry_records)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#put_telemetry_records)
        """

    def put_trace_segments(
        self, *, TraceSegmentDocuments: Sequence[str]
    ) -> PutTraceSegmentsResultTypeDef:
        """
        Uploads segment documents to Amazon Web Services X-Ray.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.put_trace_segments)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#put_trace_segments)
        """

    def tag_resource(self, *, ResourceARN: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Applies tags to an existing Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#tag_resource)
        """

    def untag_resource(self, *, ResourceARN: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes tags from an Amazon Web Services X-Ray group or sampling rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#untag_resource)
        """

    def update_group(
        self,
        *,
        GroupName: str = ...,
        GroupARN: str = ...,
        FilterExpression: str = ...,
        InsightsConfiguration: InsightsConfigurationTypeDef = ...
    ) -> UpdateGroupResultTypeDef:
        """
        Updates a group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.update_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#update_group)
        """

    def update_sampling_rule(
        self, *, SamplingRuleUpdate: SamplingRuleUpdateTypeDef
    ) -> UpdateSamplingRuleResultTypeDef:
        """
        Modifies a sampling rule's configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.update_sampling_rule)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#update_sampling_rule)
        """

    @overload
    def get_paginator(self, operation_name: Literal["batch_get_traces"]) -> BatchGetTracesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_groups"]) -> GetGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_rules"]
    ) -> GetSamplingRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_sampling_statistic_summaries"]
    ) -> GetSamplingStatisticSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_service_graph"]
    ) -> GetServiceGraphPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_time_series_service_statistics"]
    ) -> GetTimeSeriesServiceStatisticsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["get_trace_graph"]) -> GetTraceGraphPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_trace_summaries"]
    ) -> GetTraceSummariesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_resource_policies"]
    ) -> ListResourcePoliciesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_tags_for_resource"]
    ) -> ListTagsForResourcePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/xray.html#XRay.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_xray/client/#get_paginator)
        """
