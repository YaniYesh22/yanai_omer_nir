"""
Type annotations for stepfunctions service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_stepfunctions.client import SFNClient

    session = Session()
    client: SFNClient = session.client("stepfunctions")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import (
    ExecutionRedriveFilterType,
    ExecutionStatusType,
    IncludedDataType,
    InspectionLevelType,
    StateMachineTypeType,
)
from .paginator import (
    GetExecutionHistoryPaginator,
    ListActivitiesPaginator,
    ListExecutionsPaginator,
    ListMapRunsPaginator,
    ListStateMachinesPaginator,
)
from .type_defs import (
    CreateActivityOutputTypeDef,
    CreateStateMachineAliasOutputTypeDef,
    CreateStateMachineOutputTypeDef,
    DescribeActivityOutputTypeDef,
    DescribeExecutionOutputTypeDef,
    DescribeMapRunOutputTypeDef,
    DescribeStateMachineAliasOutputTypeDef,
    DescribeStateMachineForExecutionOutputTypeDef,
    DescribeStateMachineOutputTypeDef,
    EncryptionConfigurationTypeDef,
    GetActivityTaskOutputTypeDef,
    GetExecutionHistoryOutputTypeDef,
    ListActivitiesOutputTypeDef,
    ListExecutionsOutputTypeDef,
    ListMapRunsOutputTypeDef,
    ListStateMachineAliasesOutputTypeDef,
    ListStateMachinesOutputTypeDef,
    ListStateMachineVersionsOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    LoggingConfigurationUnionTypeDef,
    PublishStateMachineVersionOutputTypeDef,
    RedriveExecutionOutputTypeDef,
    RoutingConfigurationListItemTypeDef,
    StartExecutionOutputTypeDef,
    StartSyncExecutionOutputTypeDef,
    StopExecutionOutputTypeDef,
    TagTypeDef,
    TestStateOutputTypeDef,
    TracingConfigurationTypeDef,
    UpdateStateMachineAliasOutputTypeDef,
    UpdateStateMachineOutputTypeDef,
    ValidateStateMachineDefinitionOutputTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("SFNClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ActivityAlreadyExists: Type[BotocoreClientError]
    ActivityDoesNotExist: Type[BotocoreClientError]
    ActivityLimitExceeded: Type[BotocoreClientError]
    ActivityWorkerLimitExceeded: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ExecutionAlreadyExists: Type[BotocoreClientError]
    ExecutionDoesNotExist: Type[BotocoreClientError]
    ExecutionLimitExceeded: Type[BotocoreClientError]
    ExecutionNotRedrivable: Type[BotocoreClientError]
    InvalidArn: Type[BotocoreClientError]
    InvalidDefinition: Type[BotocoreClientError]
    InvalidEncryptionConfiguration: Type[BotocoreClientError]
    InvalidExecutionInput: Type[BotocoreClientError]
    InvalidLoggingConfiguration: Type[BotocoreClientError]
    InvalidName: Type[BotocoreClientError]
    InvalidOutput: Type[BotocoreClientError]
    InvalidToken: Type[BotocoreClientError]
    InvalidTracingConfiguration: Type[BotocoreClientError]
    KmsAccessDeniedException: Type[BotocoreClientError]
    KmsInvalidStateException: Type[BotocoreClientError]
    KmsThrottlingException: Type[BotocoreClientError]
    MissingRequiredParameter: Type[BotocoreClientError]
    ResourceNotFound: Type[BotocoreClientError]
    ServiceQuotaExceededException: Type[BotocoreClientError]
    StateMachineAlreadyExists: Type[BotocoreClientError]
    StateMachineDeleting: Type[BotocoreClientError]
    StateMachineDoesNotExist: Type[BotocoreClientError]
    StateMachineLimitExceeded: Type[BotocoreClientError]
    StateMachineTypeNotSupported: Type[BotocoreClientError]
    TaskDoesNotExist: Type[BotocoreClientError]
    TaskTimedOut: Type[BotocoreClientError]
    TooManyTags: Type[BotocoreClientError]
    ValidationException: Type[BotocoreClientError]


class SFNClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SFNClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#close)
        """

    def create_activity(
        self,
        *,
        name: str,
        tags: Sequence[TagTypeDef] = ...,
        encryptionConfiguration: EncryptionConfigurationTypeDef = ...,
    ) -> CreateActivityOutputTypeDef:
        """
        Creates an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.create_activity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_activity)
        """

    def create_state_machine(
        self,
        *,
        name: str,
        definition: str,
        roleArn: str,
        type: StateMachineTypeType = ...,
        loggingConfiguration: LoggingConfigurationUnionTypeDef = ...,
        tags: Sequence[TagTypeDef] = ...,
        tracingConfiguration: TracingConfigurationTypeDef = ...,
        publish: bool = ...,
        versionDescription: str = ...,
        encryptionConfiguration: EncryptionConfigurationTypeDef = ...,
    ) -> CreateStateMachineOutputTypeDef:
        """
        Creates a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.create_state_machine)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_state_machine)
        """

    def create_state_machine_alias(
        self,
        *,
        name: str,
        routingConfiguration: Sequence[RoutingConfigurationListItemTypeDef],
        description: str = ...,
    ) -> CreateStateMachineAliasOutputTypeDef:
        """
        Creates an
        [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html)
        for a state machine that points to one or two
        [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html)
        of the same state
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.create_state_machine_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#create_state_machine_alias)
        """

    def delete_activity(self, *, activityArn: str) -> Dict[str, Any]:
        """
        Deletes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_activity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_activity)
        """

    def delete_state_machine(self, *, stateMachineArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_state_machine)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine)
        """

    def delete_state_machine_alias(self, *, stateMachineAliasArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine
        [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_state_machine_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine_alias)
        """

    def delete_state_machine_version(self, *, stateMachineVersionArn: str) -> Dict[str, Any]:
        """
        Deletes a state machine
        [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.delete_state_machine_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#delete_state_machine_version)
        """

    def describe_activity(self, *, activityArn: str) -> DescribeActivityOutputTypeDef:
        """
        Describes an activity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_activity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_activity)
        """

    def describe_execution(
        self, *, executionArn: str, includedData: IncludedDataType = ...
    ) -> DescribeExecutionOutputTypeDef:
        """
        Provides information about a state machine execution, such as the state machine
        associated with the execution, the execution input and output, and relevant
        execution
        metadata.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_execution)
        """

    def describe_map_run(self, *, mapRunArn: str) -> DescribeMapRunOutputTypeDef:
        """
        Provides information about a Map Run's configuration, progress, and results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_map_run)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_map_run)
        """

    def describe_state_machine(
        self, *, stateMachineArn: str, includedData: IncludedDataType = ...
    ) -> DescribeStateMachineOutputTypeDef:
        """
        Provides information about a state machine's definition, its IAM role Amazon
        Resource Name (ARN), and
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine)
        """

    def describe_state_machine_alias(
        self, *, stateMachineAliasArn: str
    ) -> DescribeStateMachineAliasOutputTypeDef:
        """
        Returns details about a state machine
        [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine_alias)
        """

    def describe_state_machine_for_execution(
        self, *, executionArn: str, includedData: IncludedDataType = ...
    ) -> DescribeStateMachineForExecutionOutputTypeDef:
        """
        Provides information about a state machine's definition, its execution role
        ARN, and
        configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.describe_state_machine_for_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#describe_state_machine_for_execution)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#generate_presigned_url)
        """

    def get_activity_task(
        self, *, activityArn: str, workerName: str = ...
    ) -> GetActivityTaskOutputTypeDef:
        """
        Used by workers to retrieve a task (with the specified activity ARN) which has
        been scheduled for execution by a running state
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_activity_task)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_activity_task)
        """

    def get_execution_history(
        self,
        *,
        executionArn: str,
        maxResults: int = ...,
        reverseOrder: bool = ...,
        nextToken: str = ...,
        includeExecutionData: bool = ...,
    ) -> GetExecutionHistoryOutputTypeDef:
        """
        Returns the history of the specified execution as a list of events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_execution_history)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_execution_history)
        """

    def list_activities(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListActivitiesOutputTypeDef:
        """
        Lists the existing activities.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_activities)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_activities)
        """

    def list_executions(
        self,
        *,
        stateMachineArn: str = ...,
        statusFilter: ExecutionStatusType = ...,
        maxResults: int = ...,
        nextToken: str = ...,
        mapRunArn: str = ...,
        redriveFilter: ExecutionRedriveFilterType = ...,
    ) -> ListExecutionsOutputTypeDef:
        """
        Lists all executions of a state machine or a Map Run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_executions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_executions)
        """

    def list_map_runs(
        self, *, executionArn: str, maxResults: int = ..., nextToken: str = ...
    ) -> ListMapRunsOutputTypeDef:
        """
        Lists all Map Runs that were started by a given state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_map_runs)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_map_runs)
        """

    def list_state_machine_aliases(
        self, *, stateMachineArn: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListStateMachineAliasesOutputTypeDef:
        """
        Lists
        [aliases](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html)
        for a specified state machine
        ARN.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_state_machine_aliases)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machine_aliases)
        """

    def list_state_machine_versions(
        self, *, stateMachineArn: str, nextToken: str = ..., maxResults: int = ...
    ) -> ListStateMachineVersionsOutputTypeDef:
        """
        Lists
        [versions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html)
        for the specified state machine Amazon Resource Name
        (ARN).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_state_machine_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machine_versions)
        """

    def list_state_machines(
        self, *, maxResults: int = ..., nextToken: str = ...
    ) -> ListStateMachinesOutputTypeDef:
        """
        Lists the existing state machines.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_state_machines)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_state_machines)
        """

    def list_tags_for_resource(self, *, resourceArn: str) -> ListTagsForResourceOutputTypeDef:
        """
        List tags for a given resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#list_tags_for_resource)
        """

    def publish_state_machine_version(
        self, *, stateMachineArn: str, revisionId: str = ..., description: str = ...
    ) -> PublishStateMachineVersionOutputTypeDef:
        """
        Creates a
        [version](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-version.html)
        from the current revision of a state
        machine.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.publish_state_machine_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#publish_state_machine_version)
        """

    def redrive_execution(
        self, *, executionArn: str, clientToken: str = ...
    ) -> RedriveExecutionOutputTypeDef:
        """
        Restarts unsuccessful executions of Standard workflows that didn't complete
        successfully in the last 14
        days.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.redrive_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#redrive_execution)
        """

    def send_task_failure(
        self, *, taskToken: str, error: str = ..., cause: str = ...
    ) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the
        [callback](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token)
        pattern, and optionally Task states using the `job run
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#con...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_failure)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_failure)
        """

    def send_task_heartbeat(self, *, taskToken: str) -> Dict[str, Any]:
        """
        Used by activity workers and Task states using the
        [callback](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token)
        pattern, and optionally Task states using the `job run
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_heartbeat)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_heartbeat)
        """

    def send_task_success(self, *, taskToken: str, output: str) -> Dict[str, Any]:
        """
        Used by activity workers, Task states using the
        [callback](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#connect-wait-token)
        pattern, and optionally Task states using the `job run
        <https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html#con...`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.send_task_success)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#send_task_success)
        """

    def start_execution(
        self, *, stateMachineArn: str, name: str = ..., input: str = ..., traceHeader: str = ...
    ) -> StartExecutionOutputTypeDef:
        """
        Starts a state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.start_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#start_execution)
        """

    def start_sync_execution(
        self,
        *,
        stateMachineArn: str,
        name: str = ...,
        input: str = ...,
        traceHeader: str = ...,
        includedData: IncludedDataType = ...,
    ) -> StartSyncExecutionOutputTypeDef:
        """
        Starts a Synchronous Express state machine execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.start_sync_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#start_sync_execution)
        """

    def stop_execution(
        self, *, executionArn: str, error: str = ..., cause: str = ...
    ) -> StopExecutionOutputTypeDef:
        """
        Stops an execution.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.stop_execution)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#stop_execution)
        """

    def tag_resource(self, *, resourceArn: str, tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Add a tag to a Step Functions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#tag_resource)
        """

    def test_state(
        self,
        *,
        definition: str,
        roleArn: str,
        input: str = ...,
        inspectionLevel: InspectionLevelType = ...,
        revealSecrets: bool = ...,
    ) -> TestStateOutputTypeDef:
        """
        Accepts the definition of a single state and executes it.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.test_state)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#test_state)
        """

    def untag_resource(self, *, resourceArn: str, tagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Remove a tag from a Step Functions resource See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/states-2016-11-23/UntagResource).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#untag_resource)
        """

    def update_map_run(
        self,
        *,
        mapRunArn: str,
        maxConcurrency: int = ...,
        toleratedFailurePercentage: float = ...,
        toleratedFailureCount: int = ...,
    ) -> Dict[str, Any]:
        """
        Updates an in-progress Map Run's configuration to include changes to the
        settings that control maximum concurrency and Map Run
        failure.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.update_map_run)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_map_run)
        """

    def update_state_machine(
        self,
        *,
        stateMachineArn: str,
        definition: str = ...,
        roleArn: str = ...,
        loggingConfiguration: LoggingConfigurationUnionTypeDef = ...,
        tracingConfiguration: TracingConfigurationTypeDef = ...,
        publish: bool = ...,
        versionDescription: str = ...,
        encryptionConfiguration: EncryptionConfigurationTypeDef = ...,
    ) -> UpdateStateMachineOutputTypeDef:
        """
        Updates an existing state machine by modifying its `definition`, `roleArn`,
        `loggingConfiguration`, or
        `EncryptionConfiguration`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.update_state_machine)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_state_machine)
        """

    def update_state_machine_alias(
        self,
        *,
        stateMachineAliasArn: str,
        description: str = ...,
        routingConfiguration: Sequence[RoutingConfigurationListItemTypeDef] = ...,
    ) -> UpdateStateMachineAliasOutputTypeDef:
        """
        Updates the configuration of an existing state machine
        [alias](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-state-machine-alias.html)
        by modifying its `description` or
        `routingConfiguration`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.update_state_machine_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#update_state_machine_alias)
        """

    def validate_state_machine_definition(
        self, *, definition: str, type: StateMachineTypeType = ...
    ) -> ValidateStateMachineDefinitionOutputTypeDef:
        """
        Validates the syntax of a state machine definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.validate_state_machine_definition)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#validate_state_machine_definition)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_execution_history"]
    ) -> GetExecutionHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_activities"]) -> ListActivitiesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_executions"]) -> ListExecutionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_map_runs"]) -> ListMapRunsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_state_machines"]
    ) -> ListStateMachinesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/stepfunctions.html#SFN.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_stepfunctions/client/#get_paginator)
        """
