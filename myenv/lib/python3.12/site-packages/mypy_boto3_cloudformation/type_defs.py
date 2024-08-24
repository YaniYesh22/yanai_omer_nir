"""
Type annotations for cloudformation service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_cloudformation/type_defs/)

Usage::

    ```python
    from mypy_boto3_cloudformation.type_defs import AccountGateResultTypeDef

    data: AccountGateResultTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Any, Dict, List, Mapping, Sequence, Union

from .literals import (
    AccountFilterTypeType,
    AccountGateStatusType,
    AttributeChangeTypeType,
    CallAsType,
    CapabilityType,
    CategoryType,
    ChangeActionType,
    ChangeSetHooksStatusType,
    ChangeSetStatusType,
    ChangeSetTypeType,
    ChangeSourceType,
    ConcurrencyModeType,
    DeletionModeType,
    DeprecatedStatusType,
    DetailedStatusType,
    DifferenceTypeType,
    EvaluationTypeType,
    ExecutionStatusType,
    GeneratedTemplateDeletionPolicyType,
    GeneratedTemplateResourceStatusType,
    GeneratedTemplateStatusType,
    GeneratedTemplateUpdateReplacePolicyType,
    HandlerErrorCodeType,
    HookFailureModeType,
    HookStatusType,
    IdentityProviderType,
    OnFailureType,
    OnStackFailureType,
    OperationStatusType,
    OrganizationStatusType,
    PermissionModelsType,
    PolicyActionType,
    ProvisioningTypeType,
    PublisherStatusType,
    RegionConcurrencyTypeType,
    RegistrationStatusType,
    RegistryTypeType,
    ReplacementType,
    RequiresRecreationType,
    ResourceAttributeType,
    ResourceScanStatusType,
    ResourceSignalStatusType,
    ResourceStatusType,
    StackDriftDetectionStatusType,
    StackDriftStatusType,
    StackInstanceDetailedStatusType,
    StackInstanceFilterNameType,
    StackInstanceStatusType,
    StackResourceDriftStatusType,
    StackSetDriftDetectionStatusType,
    StackSetDriftStatusType,
    StackSetOperationActionType,
    StackSetOperationResultStatusType,
    StackSetOperationStatusType,
    StackSetStatusType,
    StackStatusType,
    TemplateFormatType,
    TemplateStageType,
    ThirdPartyTypeType,
    TypeTestsStatusType,
    VersionBumpType,
    VisibilityType,
    WarningTypeType,
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
    "AccountGateResultTypeDef",
    "AccountLimitTypeDef",
    "LoggingConfigTypeDef",
    "ResponseMetadataTypeDef",
    "AutoDeploymentTypeDef",
    "TypeConfigurationIdentifierTypeDef",
    "TypeConfigurationDetailsTypeDef",
    "CancelUpdateStackInputRequestTypeDef",
    "CancelUpdateStackInputStackCancelUpdateTypeDef",
    "ChangeSetHookResourceTargetDetailsTypeDef",
    "ChangeSetSummaryTypeDef",
    "ContinueUpdateRollbackInputRequestTypeDef",
    "ParameterTypeDef",
    "ResourceToImportTypeDef",
    "TagTypeDef",
    "ResourceDefinitionTypeDef",
    "TemplateConfigurationTypeDef",
    "DeploymentTargetsTypeDef",
    "StackSetOperationPreferencesTypeDef",
    "ManagedExecutionTypeDef",
    "DeactivateTypeInputRequestTypeDef",
    "DeleteChangeSetInputRequestTypeDef",
    "DeleteGeneratedTemplateInputRequestTypeDef",
    "DeleteStackInputRequestTypeDef",
    "DeleteStackInputStackDeleteTypeDef",
    "DeleteStackSetInputRequestTypeDef",
    "DeploymentTargetsOutputTypeDef",
    "DeregisterTypeInputRequestTypeDef",
    "PaginatorConfigTypeDef",
    "DescribeAccountLimitsInputRequestTypeDef",
    "DescribeChangeSetHooksInputRequestTypeDef",
    "WaiterConfigTypeDef",
    "DescribeChangeSetInputRequestTypeDef",
    "DescribeGeneratedTemplateInputRequestTypeDef",
    "TemplateProgressTypeDef",
    "DescribeOrganizationsAccessInputRequestTypeDef",
    "DescribePublisherInputRequestTypeDef",
    "DescribeResourceScanInputRequestTypeDef",
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    "DescribeStackEventsInputRequestTypeDef",
    "StackEventTypeDef",
    "DescribeStackInstanceInputRequestTypeDef",
    "DescribeStackResourceDriftsInputRequestTypeDef",
    "DescribeStackResourceInputRequestTypeDef",
    "DescribeStackResourcesInputRequestTypeDef",
    "DescribeStackSetInputRequestTypeDef",
    "DescribeStackSetOperationInputRequestTypeDef",
    "DescribeStacksInputRequestTypeDef",
    "DescribeTypeInputRequestTypeDef",
    "RequiredActivatedTypeTypeDef",
    "DescribeTypeRegistrationInputRequestTypeDef",
    "DetectStackDriftInputRequestTypeDef",
    "DetectStackResourceDriftInputRequestTypeDef",
    "ExecuteChangeSetInputRequestTypeDef",
    "ExportTypeDef",
    "GetGeneratedTemplateInputRequestTypeDef",
    "GetStackPolicyInputRequestTypeDef",
    "GetTemplateInputRequestTypeDef",
    "TemplateSummaryConfigTypeDef",
    "ResourceIdentifierSummaryTypeDef",
    "WarningsTypeDef",
    "ListChangeSetsInputRequestTypeDef",
    "ListExportsInputRequestTypeDef",
    "ListGeneratedTemplatesInputRequestTypeDef",
    "TemplateSummaryTypeDef",
    "ListImportsInputRequestTypeDef",
    "ScannedResourceIdentifierTypeDef",
    "ScannedResourceTypeDef",
    "ListResourceScanResourcesInputRequestTypeDef",
    "ListResourceScansInputRequestTypeDef",
    "ResourceScanSummaryTypeDef",
    "ListStackInstanceResourceDriftsInputRequestTypeDef",
    "StackInstanceFilterTypeDef",
    "ListStackResourcesInputRequestTypeDef",
    "ListStackSetAutoDeploymentTargetsInputRequestTypeDef",
    "StackSetAutoDeploymentTargetSummaryTypeDef",
    "OperationResultFilterTypeDef",
    "ListStackSetOperationsInputRequestTypeDef",
    "ListStackSetsInputRequestTypeDef",
    "ListStacksInputRequestTypeDef",
    "ListTypeRegistrationsInputRequestTypeDef",
    "ListTypeVersionsInputRequestTypeDef",
    "TypeVersionSummaryTypeDef",
    "TypeFiltersTypeDef",
    "TypeSummaryTypeDef",
    "ModuleInfoTypeDef",
    "OutputTypeDef",
    "ParameterConstraintsTypeDef",
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    "PropertyDifferenceTypeDef",
    "PublishTypeInputRequestTypeDef",
    "RecordHandlerProgressInputRequestTypeDef",
    "RegisterPublisherInputRequestTypeDef",
    "ResourceTargetDefinitionTypeDef",
    "RollbackTriggerTypeDef",
    "RollbackStackInputRequestTypeDef",
    "SetStackPolicyInputRequestTypeDef",
    "SetTypeConfigurationInputRequestTypeDef",
    "SetTypeDefaultVersionInputRequestTypeDef",
    "SignalResourceInputRequestTypeDef",
    "StackDriftInformationSummaryTypeDef",
    "StackDriftInformationTypeDef",
    "StackInstanceComprehensiveStatusTypeDef",
    "StackResourceDriftInformationTypeDef",
    "StackResourceDriftInformationSummaryTypeDef",
    "StackSetDriftDetectionDetailsTypeDef",
    "StackSetOperationPreferencesExtraOutputTypeDef",
    "StackSetOperationPreferencesOutputTypeDef",
    "StackSetOperationStatusDetailsTypeDef",
    "StartResourceScanInputRequestTypeDef",
    "StopStackSetOperationInputRequestTypeDef",
    "TemplateParameterTypeDef",
    "TestTypeInputRequestTypeDef",
    "UpdateTerminationProtectionInputRequestTypeDef",
    "ValidateTemplateInputRequestTypeDef",
    "WarningPropertyTypeDef",
    "StackSetOperationResultSummaryTypeDef",
    "ActivateTypeInputRequestTypeDef",
    "RegisterTypeInputRequestTypeDef",
    "ActivateTypeOutputTypeDef",
    "CreateChangeSetOutputTypeDef",
    "CreateGeneratedTemplateOutputTypeDef",
    "CreateStackInstancesOutputTypeDef",
    "CreateStackOutputTypeDef",
    "CreateStackSetOutputTypeDef",
    "DeleteStackInstancesOutputTypeDef",
    "DescribeAccountLimitsOutputTypeDef",
    "DescribeOrganizationsAccessOutputTypeDef",
    "DescribePublisherOutputTypeDef",
    "DescribeResourceScanOutputTypeDef",
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    "DescribeTypeRegistrationOutputTypeDef",
    "DetectStackDriftOutputTypeDef",
    "DetectStackSetDriftOutputTypeDef",
    "EmptyResponseMetadataTypeDef",
    "EstimateTemplateCostOutputTypeDef",
    "GetGeneratedTemplateOutputTypeDef",
    "GetStackPolicyOutputTypeDef",
    "GetTemplateOutputTypeDef",
    "ImportStacksToStackSetOutputTypeDef",
    "ListImportsOutputTypeDef",
    "ListTypeRegistrationsOutputTypeDef",
    "ModuleInfoResponseTypeDef",
    "PublishTypeOutputTypeDef",
    "RegisterPublisherOutputTypeDef",
    "RegisterTypeOutputTypeDef",
    "RollbackStackOutputTypeDef",
    "SetTypeConfigurationOutputTypeDef",
    "StackDriftInformationResponseTypeDef",
    "StackResourceDriftInformationResponseTypeDef",
    "StackResourceDriftInformationSummaryResponseTypeDef",
    "StartResourceScanOutputTypeDef",
    "TestTypeOutputTypeDef",
    "UpdateGeneratedTemplateOutputTypeDef",
    "UpdateStackInstancesOutputTypeDef",
    "UpdateStackOutputTypeDef",
    "UpdateStackSetOutputTypeDef",
    "UpdateTerminationProtectionOutputTypeDef",
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    "ChangeSetHookTargetDetailsTypeDef",
    "ListChangeSetsOutputTypeDef",
    "EstimateTemplateCostInputRequestTypeDef",
    "CreateGeneratedTemplateInputRequestTypeDef",
    "UpdateGeneratedTemplateInputRequestTypeDef",
    "CreateStackInstancesInputRequestTypeDef",
    "DeleteStackInstancesInputRequestTypeDef",
    "DetectStackSetDriftInputRequestTypeDef",
    "ImportStacksToStackSetInputRequestTypeDef",
    "UpdateStackInstancesInputRequestTypeDef",
    "CreateStackSetInputRequestTypeDef",
    "StackSetSummaryTypeDef",
    "UpdateStackSetInputRequestTypeDef",
    "DeploymentTargetsUnionTypeDef",
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    "DescribeChangeSetInputDescribeChangeSetPaginateTypeDef",
    "DescribeStackEventsInputDescribeStackEventsPaginateTypeDef",
    "DescribeStacksInputDescribeStacksPaginateTypeDef",
    "ListChangeSetsInputListChangeSetsPaginateTypeDef",
    "ListExportsInputListExportsPaginateTypeDef",
    "ListGeneratedTemplatesInputListGeneratedTemplatesPaginateTypeDef",
    "ListImportsInputListImportsPaginateTypeDef",
    "ListResourceScanResourcesInputListResourceScanResourcesPaginateTypeDef",
    "ListResourceScansInputListResourceScansPaginateTypeDef",
    "ListStackResourcesInputListStackResourcesPaginateTypeDef",
    "ListStackSetOperationsInputListStackSetOperationsPaginateTypeDef",
    "ListStackSetsInputListStackSetsPaginateTypeDef",
    "ListStacksInputListStacksPaginateTypeDef",
    "DescribeChangeSetInputChangeSetCreateCompleteWaitTypeDef",
    "DescribeStacksInputStackCreateCompleteWaitTypeDef",
    "DescribeStacksInputStackDeleteCompleteWaitTypeDef",
    "DescribeStacksInputStackExistsWaitTypeDef",
    "DescribeStacksInputStackImportCompleteWaitTypeDef",
    "DescribeStacksInputStackRollbackCompleteWaitTypeDef",
    "DescribeStacksInputStackUpdateCompleteWaitTypeDef",
    "DescribeTypeRegistrationInputTypeRegistrationCompleteWaitTypeDef",
    "DescribeStackEventsOutputTypeDef",
    "DescribeTypeOutputTypeDef",
    "ListExportsOutputTypeDef",
    "GetTemplateSummaryInputRequestTypeDef",
    "ListGeneratedTemplatesOutputTypeDef",
    "ListResourceScanRelatedResourcesInputListResourceScanRelatedResourcesPaginateTypeDef",
    "ListResourceScanRelatedResourcesInputRequestTypeDef",
    "ListResourceScanRelatedResourcesOutputTypeDef",
    "ListResourceScanResourcesOutputTypeDef",
    "ListResourceScansOutputTypeDef",
    "ListStackInstancesInputListStackInstancesPaginateTypeDef",
    "ListStackInstancesInputRequestTypeDef",
    "ListStackSetAutoDeploymentTargetsOutputTypeDef",
    "ListStackSetOperationResultsInputListStackSetOperationResultsPaginateTypeDef",
    "ListStackSetOperationResultsInputRequestTypeDef",
    "ListTypeVersionsOutputTypeDef",
    "ListTypesInputListTypesPaginateTypeDef",
    "ListTypesInputRequestTypeDef",
    "ListTypesOutputTypeDef",
    "ParameterDeclarationTypeDef",
    "StackInstanceResourceDriftsSummaryTypeDef",
    "StackResourceDriftTypeDef",
    "ResourceChangeDetailTypeDef",
    "RollbackConfigurationExtraOutputTypeDef",
    "RollbackConfigurationOutputTypeDef",
    "RollbackConfigurationResponseTypeDef",
    "RollbackConfigurationTypeDef",
    "StackSummaryTypeDef",
    "StackInstanceSummaryTypeDef",
    "StackInstanceTypeDef",
    "StackResourceDetailTypeDef",
    "StackResourceTypeDef",
    "StackResourceSummaryTypeDef",
    "StackSetTypeDef",
    "StackSetOperationPreferencesUnionTypeDef",
    "StackSetOperationSummaryTypeDef",
    "StackSetOperationTypeDef",
    "ValidateTemplateOutputTypeDef",
    "WarningDetailTypeDef",
    "ListStackSetOperationResultsOutputTypeDef",
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    "ChangeSetHookTypeDef",
    "ListStackSetsOutputTypeDef",
    "GetTemplateSummaryOutputTypeDef",
    "ListStackInstanceResourceDriftsOutputTypeDef",
    "DescribeStackResourceDriftsOutputTypeDef",
    "DetectStackResourceDriftOutputTypeDef",
    "ResourceChangeTypeDef",
    "StackTypeDef",
    "CreateChangeSetInputRequestTypeDef",
    "CreateStackInputRequestTypeDef",
    "CreateStackInputServiceResourceCreateStackTypeDef",
    "RollbackConfigurationUnionTypeDef",
    "UpdateStackInputRequestTypeDef",
    "UpdateStackInputStackUpdateTypeDef",
    "ListStacksOutputTypeDef",
    "ListStackInstancesOutputTypeDef",
    "DescribeStackInstanceOutputTypeDef",
    "DescribeStackResourceOutputTypeDef",
    "DescribeStackResourcesOutputTypeDef",
    "ListStackResourcesOutputTypeDef",
    "DescribeStackSetOutputTypeDef",
    "ListStackSetOperationsOutputTypeDef",
    "DescribeStackSetOperationOutputTypeDef",
    "ResourceDetailTypeDef",
    "DescribeChangeSetHooksOutputTypeDef",
    "ChangeTypeDef",
    "DescribeStacksOutputTypeDef",
    "DescribeGeneratedTemplateOutputTypeDef",
    "DescribeChangeSetOutputTypeDef",
)

AccountGateResultTypeDef = TypedDict(
    "AccountGateResultTypeDef",
    {
        "Status": NotRequired[AccountGateStatusType],
        "StatusReason": NotRequired[str],
    },
)
AccountLimitTypeDef = TypedDict(
    "AccountLimitTypeDef",
    {
        "Name": NotRequired[str],
        "Value": NotRequired[int],
    },
)
LoggingConfigTypeDef = TypedDict(
    "LoggingConfigTypeDef",
    {
        "LogRoleArn": str,
        "LogGroupName": str,
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
AutoDeploymentTypeDef = TypedDict(
    "AutoDeploymentTypeDef",
    {
        "Enabled": NotRequired[bool],
        "RetainStacksOnAccountRemoval": NotRequired[bool],
    },
)
TypeConfigurationIdentifierTypeDef = TypedDict(
    "TypeConfigurationIdentifierTypeDef",
    {
        "TypeArn": NotRequired[str],
        "TypeConfigurationAlias": NotRequired[str],
        "TypeConfigurationArn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
    },
)
TypeConfigurationDetailsTypeDef = TypedDict(
    "TypeConfigurationDetailsTypeDef",
    {
        "Arn": NotRequired[str],
        "Alias": NotRequired[str],
        "Configuration": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "TypeArn": NotRequired[str],
        "TypeName": NotRequired[str],
        "IsDefaultConfiguration": NotRequired[bool],
    },
)
CancelUpdateStackInputRequestTypeDef = TypedDict(
    "CancelUpdateStackInputRequestTypeDef",
    {
        "StackName": str,
        "ClientRequestToken": NotRequired[str],
    },
)
CancelUpdateStackInputStackCancelUpdateTypeDef = TypedDict(
    "CancelUpdateStackInputStackCancelUpdateTypeDef",
    {
        "ClientRequestToken": NotRequired[str],
    },
)
ChangeSetHookResourceTargetDetailsTypeDef = TypedDict(
    "ChangeSetHookResourceTargetDetailsTypeDef",
    {
        "LogicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceAction": NotRequired[ChangeActionType],
    },
)
ChangeSetSummaryTypeDef = TypedDict(
    "ChangeSetSummaryTypeDef",
    {
        "StackId": NotRequired[str],
        "StackName": NotRequired[str],
        "ChangeSetId": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "ExecutionStatus": NotRequired[ExecutionStatusType],
        "Status": NotRequired[ChangeSetStatusType],
        "StatusReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "Description": NotRequired[str],
        "IncludeNestedStacks": NotRequired[bool],
        "ParentChangeSetId": NotRequired[str],
        "RootChangeSetId": NotRequired[str],
        "ImportExistingResources": NotRequired[bool],
    },
)
ContinueUpdateRollbackInputRequestTypeDef = TypedDict(
    "ContinueUpdateRollbackInputRequestTypeDef",
    {
        "StackName": str,
        "RoleARN": NotRequired[str],
        "ResourcesToSkip": NotRequired[Sequence[str]],
        "ClientRequestToken": NotRequired[str],
    },
)
ParameterTypeDef = TypedDict(
    "ParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "ParameterValue": NotRequired[str],
        "UsePreviousValue": NotRequired[bool],
        "ResolvedValue": NotRequired[str],
    },
)
ResourceToImportTypeDef = TypedDict(
    "ResourceToImportTypeDef",
    {
        "ResourceType": str,
        "LogicalResourceId": str,
        "ResourceIdentifier": Mapping[str, str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
ResourceDefinitionTypeDef = TypedDict(
    "ResourceDefinitionTypeDef",
    {
        "ResourceType": str,
        "ResourceIdentifier": Mapping[str, str],
        "LogicalResourceId": NotRequired[str],
    },
)
TemplateConfigurationTypeDef = TypedDict(
    "TemplateConfigurationTypeDef",
    {
        "DeletionPolicy": NotRequired[GeneratedTemplateDeletionPolicyType],
        "UpdateReplacePolicy": NotRequired[GeneratedTemplateUpdateReplacePolicyType],
    },
)
DeploymentTargetsTypeDef = TypedDict(
    "DeploymentTargetsTypeDef",
    {
        "Accounts": NotRequired[Sequence[str]],
        "AccountsUrl": NotRequired[str],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "AccountFilterType": NotRequired[AccountFilterTypeType],
    },
)
StackSetOperationPreferencesTypeDef = TypedDict(
    "StackSetOperationPreferencesTypeDef",
    {
        "RegionConcurrencyType": NotRequired[RegionConcurrencyTypeType],
        "RegionOrder": NotRequired[Sequence[str]],
        "FailureToleranceCount": NotRequired[int],
        "FailureTolerancePercentage": NotRequired[int],
        "MaxConcurrentCount": NotRequired[int],
        "MaxConcurrentPercentage": NotRequired[int],
        "ConcurrencyMode": NotRequired[ConcurrencyModeType],
    },
)
ManagedExecutionTypeDef = TypedDict(
    "ManagedExecutionTypeDef",
    {
        "Active": NotRequired[bool],
    },
)
DeactivateTypeInputRequestTypeDef = TypedDict(
    "DeactivateTypeInputRequestTypeDef",
    {
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
    },
)
DeleteChangeSetInputRequestTypeDef = TypedDict(
    "DeleteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
    },
)
DeleteGeneratedTemplateInputRequestTypeDef = TypedDict(
    "DeleteGeneratedTemplateInputRequestTypeDef",
    {
        "GeneratedTemplateName": str,
    },
)
DeleteStackInputRequestTypeDef = TypedDict(
    "DeleteStackInputRequestTypeDef",
    {
        "StackName": str,
        "RetainResources": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "DeletionMode": NotRequired[DeletionModeType],
    },
)
DeleteStackInputStackDeleteTypeDef = TypedDict(
    "DeleteStackInputStackDeleteTypeDef",
    {
        "RetainResources": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "DeletionMode": NotRequired[DeletionModeType],
    },
)
DeleteStackSetInputRequestTypeDef = TypedDict(
    "DeleteStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "CallAs": NotRequired[CallAsType],
    },
)
DeploymentTargetsOutputTypeDef = TypedDict(
    "DeploymentTargetsOutputTypeDef",
    {
        "Accounts": NotRequired[List[str]],
        "AccountsUrl": NotRequired[str],
        "OrganizationalUnitIds": NotRequired[List[str]],
        "AccountFilterType": NotRequired[AccountFilterTypeType],
    },
)
DeregisterTypeInputRequestTypeDef = TypedDict(
    "DeregisterTypeInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
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
DescribeAccountLimitsInputRequestTypeDef = TypedDict(
    "DescribeAccountLimitsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
DescribeChangeSetHooksInputRequestTypeDef = TypedDict(
    "DescribeChangeSetHooksInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "LogicalResourceId": NotRequired[str],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
DescribeChangeSetInputRequestTypeDef = TypedDict(
    "DescribeChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "IncludePropertyValues": NotRequired[bool],
    },
)
DescribeGeneratedTemplateInputRequestTypeDef = TypedDict(
    "DescribeGeneratedTemplateInputRequestTypeDef",
    {
        "GeneratedTemplateName": str,
    },
)
TemplateProgressTypeDef = TypedDict(
    "TemplateProgressTypeDef",
    {
        "ResourcesSucceeded": NotRequired[int],
        "ResourcesFailed": NotRequired[int],
        "ResourcesProcessing": NotRequired[int],
        "ResourcesPending": NotRequired[int],
    },
)
DescribeOrganizationsAccessInputRequestTypeDef = TypedDict(
    "DescribeOrganizationsAccessInputRequestTypeDef",
    {
        "CallAs": NotRequired[CallAsType],
    },
)
DescribePublisherInputRequestTypeDef = TypedDict(
    "DescribePublisherInputRequestTypeDef",
    {
        "PublisherId": NotRequired[str],
    },
)
DescribeResourceScanInputRequestTypeDef = TypedDict(
    "DescribeResourceScanInputRequestTypeDef",
    {
        "ResourceScanId": str,
    },
)
DescribeStackDriftDetectionStatusInputRequestTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusInputRequestTypeDef",
    {
        "StackDriftDetectionId": str,
    },
)
DescribeStackEventsInputRequestTypeDef = TypedDict(
    "DescribeStackEventsInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
StackEventTypeDef = TypedDict(
    "StackEventTypeDef",
    {
        "StackId": str,
        "EventId": str,
        "StackName": str,
        "Timestamp": datetime,
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "ResourceStatus": NotRequired[ResourceStatusType],
        "ResourceStatusReason": NotRequired[str],
        "ResourceProperties": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "HookType": NotRequired[str],
        "HookStatus": NotRequired[HookStatusType],
        "HookStatusReason": NotRequired[str],
        "HookInvocationPoint": NotRequired[Literal["PRE_PROVISION"]],
        "HookFailureMode": NotRequired[HookFailureModeType],
        "DetailedStatus": NotRequired[DetailedStatusType],
    },
)
DescribeStackInstanceInputRequestTypeDef = TypedDict(
    "DescribeStackInstanceInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
        "CallAs": NotRequired[CallAsType],
    },
)
DescribeStackResourceDriftsInputRequestTypeDef = TypedDict(
    "DescribeStackResourceDriftsInputRequestTypeDef",
    {
        "StackName": str,
        "StackResourceDriftStatusFilters": NotRequired[Sequence[StackResourceDriftStatusType]],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
DescribeStackResourceInputRequestTypeDef = TypedDict(
    "DescribeStackResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)
DescribeStackResourcesInputRequestTypeDef = TypedDict(
    "DescribeStackResourcesInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
    },
)
DescribeStackSetInputRequestTypeDef = TypedDict(
    "DescribeStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "CallAs": NotRequired[CallAsType],
    },
)
DescribeStackSetOperationInputRequestTypeDef = TypedDict(
    "DescribeStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "CallAs": NotRequired[CallAsType],
    },
)
DescribeStacksInputRequestTypeDef = TypedDict(
    "DescribeStacksInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
    },
)
DescribeTypeInputRequestTypeDef = TypedDict(
    "DescribeTypeInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "VersionId": NotRequired[str],
        "PublisherId": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)
RequiredActivatedTypeTypeDef = TypedDict(
    "RequiredActivatedTypeTypeDef",
    {
        "TypeNameAlias": NotRequired[str],
        "OriginalTypeName": NotRequired[str],
        "PublisherId": NotRequired[str],
        "SupportedMajorVersions": NotRequired[List[int]],
    },
)
DescribeTypeRegistrationInputRequestTypeDef = TypedDict(
    "DescribeTypeRegistrationInputRequestTypeDef",
    {
        "RegistrationToken": str,
    },
)
DetectStackDriftInputRequestTypeDef = TypedDict(
    "DetectStackDriftInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceIds": NotRequired[Sequence[str]],
    },
)
DetectStackResourceDriftInputRequestTypeDef = TypedDict(
    "DetectStackResourceDriftInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
    },
)
ExecuteChangeSetInputRequestTypeDef = TypedDict(
    "ExecuteChangeSetInputRequestTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
ExportTypeDef = TypedDict(
    "ExportTypeDef",
    {
        "ExportingStackId": NotRequired[str],
        "Name": NotRequired[str],
        "Value": NotRequired[str],
    },
)
GetGeneratedTemplateInputRequestTypeDef = TypedDict(
    "GetGeneratedTemplateInputRequestTypeDef",
    {
        "GeneratedTemplateName": str,
        "Format": NotRequired[TemplateFormatType],
    },
)
GetStackPolicyInputRequestTypeDef = TypedDict(
    "GetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
    },
)
GetTemplateInputRequestTypeDef = TypedDict(
    "GetTemplateInputRequestTypeDef",
    {
        "StackName": NotRequired[str],
        "ChangeSetName": NotRequired[str],
        "TemplateStage": NotRequired[TemplateStageType],
    },
)
TemplateSummaryConfigTypeDef = TypedDict(
    "TemplateSummaryConfigTypeDef",
    {
        "TreatUnrecognizedResourceTypesAsWarnings": NotRequired[bool],
    },
)
ResourceIdentifierSummaryTypeDef = TypedDict(
    "ResourceIdentifierSummaryTypeDef",
    {
        "ResourceType": NotRequired[str],
        "LogicalResourceIds": NotRequired[List[str]],
        "ResourceIdentifiers": NotRequired[List[str]],
    },
)
WarningsTypeDef = TypedDict(
    "WarningsTypeDef",
    {
        "UnrecognizedResourceTypes": NotRequired[List[str]],
    },
)
ListChangeSetsInputRequestTypeDef = TypedDict(
    "ListChangeSetsInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": NotRequired[str],
    },
)
ListExportsInputRequestTypeDef = TypedDict(
    "ListExportsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
    },
)
ListGeneratedTemplatesInputRequestTypeDef = TypedDict(
    "ListGeneratedTemplatesInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
TemplateSummaryTypeDef = TypedDict(
    "TemplateSummaryTypeDef",
    {
        "GeneratedTemplateId": NotRequired[str],
        "GeneratedTemplateName": NotRequired[str],
        "Status": NotRequired[GeneratedTemplateStatusType],
        "StatusReason": NotRequired[str],
        "CreationTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "NumberOfResources": NotRequired[int],
    },
)
ListImportsInputRequestTypeDef = TypedDict(
    "ListImportsInputRequestTypeDef",
    {
        "ExportName": str,
        "NextToken": NotRequired[str],
    },
)
ScannedResourceIdentifierTypeDef = TypedDict(
    "ScannedResourceIdentifierTypeDef",
    {
        "ResourceType": str,
        "ResourceIdentifier": Mapping[str, str],
    },
)
ScannedResourceTypeDef = TypedDict(
    "ScannedResourceTypeDef",
    {
        "ResourceType": NotRequired[str],
        "ResourceIdentifier": NotRequired[Dict[str, str]],
        "ManagedByStack": NotRequired[bool],
    },
)
ListResourceScanResourcesInputRequestTypeDef = TypedDict(
    "ListResourceScanResourcesInputRequestTypeDef",
    {
        "ResourceScanId": str,
        "ResourceIdentifier": NotRequired[str],
        "ResourceTypePrefix": NotRequired[str],
        "TagKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListResourceScansInputRequestTypeDef = TypedDict(
    "ListResourceScansInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ResourceScanSummaryTypeDef = TypedDict(
    "ResourceScanSummaryTypeDef",
    {
        "ResourceScanId": NotRequired[str],
        "Status": NotRequired[ResourceScanStatusType],
        "StatusReason": NotRequired[str],
        "StartTime": NotRequired[datetime],
        "EndTime": NotRequired[datetime],
        "PercentageCompleted": NotRequired[float],
    },
)
ListStackInstanceResourceDriftsInputRequestTypeDef = TypedDict(
    "ListStackInstanceResourceDriftsInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackInstanceAccount": str,
        "StackInstanceRegion": str,
        "OperationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "StackInstanceResourceDriftStatuses": NotRequired[Sequence[StackResourceDriftStatusType]],
        "CallAs": NotRequired[CallAsType],
    },
)
StackInstanceFilterTypeDef = TypedDict(
    "StackInstanceFilterTypeDef",
    {
        "Name": NotRequired[StackInstanceFilterNameType],
        "Values": NotRequired[str],
    },
)
ListStackResourcesInputRequestTypeDef = TypedDict(
    "ListStackResourcesInputRequestTypeDef",
    {
        "StackName": str,
        "NextToken": NotRequired[str],
    },
)
ListStackSetAutoDeploymentTargetsInputRequestTypeDef = TypedDict(
    "ListStackSetAutoDeploymentTargetsInputRequestTypeDef",
    {
        "StackSetName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CallAs": NotRequired[CallAsType],
    },
)
StackSetAutoDeploymentTargetSummaryTypeDef = TypedDict(
    "StackSetAutoDeploymentTargetSummaryTypeDef",
    {
        "OrganizationalUnitId": NotRequired[str],
        "Regions": NotRequired[List[str]],
    },
)
OperationResultFilterTypeDef = TypedDict(
    "OperationResultFilterTypeDef",
    {
        "Name": NotRequired[Literal["OPERATION_RESULT_STATUS"]],
        "Values": NotRequired[str],
    },
)
ListStackSetOperationsInputRequestTypeDef = TypedDict(
    "ListStackSetOperationsInputRequestTypeDef",
    {
        "StackSetName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CallAs": NotRequired[CallAsType],
    },
)
ListStackSetsInputRequestTypeDef = TypedDict(
    "ListStackSetsInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Status": NotRequired[StackSetStatusType],
        "CallAs": NotRequired[CallAsType],
    },
)
ListStacksInputRequestTypeDef = TypedDict(
    "ListStacksInputRequestTypeDef",
    {
        "NextToken": NotRequired[str],
        "StackStatusFilter": NotRequired[Sequence[StackStatusType]],
    },
)
ListTypeRegistrationsInputRequestTypeDef = TypedDict(
    "ListTypeRegistrationsInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "TypeArn": NotRequired[str],
        "RegistrationStatusFilter": NotRequired[RegistrationStatusType],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTypeVersionsInputRequestTypeDef = TypedDict(
    "ListTypeVersionsInputRequestTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "Arn": NotRequired[str],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "PublisherId": NotRequired[str],
    },
)
TypeVersionSummaryTypeDef = TypedDict(
    "TypeVersionSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "Arn": NotRequired[str],
        "TimeCreated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)
TypeFiltersTypeDef = TypedDict(
    "TypeFiltersTypeDef",
    {
        "Category": NotRequired[CategoryType],
        "PublisherId": NotRequired[str],
        "TypeNamePrefix": NotRequired[str],
    },
)
TypeSummaryTypeDef = TypedDict(
    "TypeSummaryTypeDef",
    {
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "TypeArn": NotRequired[str],
        "LastUpdated": NotRequired[datetime],
        "Description": NotRequired[str],
        "PublisherId": NotRequired[str],
        "OriginalTypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
        "LatestPublicVersion": NotRequired[str],
        "PublisherIdentity": NotRequired[IdentityProviderType],
        "PublisherName": NotRequired[str],
        "IsActivated": NotRequired[bool],
    },
)
ModuleInfoTypeDef = TypedDict(
    "ModuleInfoTypeDef",
    {
        "TypeHierarchy": NotRequired[str],
        "LogicalIdHierarchy": NotRequired[str],
    },
)
OutputTypeDef = TypedDict(
    "OutputTypeDef",
    {
        "OutputKey": NotRequired[str],
        "OutputValue": NotRequired[str],
        "Description": NotRequired[str],
        "ExportName": NotRequired[str],
    },
)
ParameterConstraintsTypeDef = TypedDict(
    "ParameterConstraintsTypeDef",
    {
        "AllowedValues": NotRequired[List[str]],
    },
)
PhysicalResourceIdContextKeyValuePairTypeDef = TypedDict(
    "PhysicalResourceIdContextKeyValuePairTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
PropertyDifferenceTypeDef = TypedDict(
    "PropertyDifferenceTypeDef",
    {
        "PropertyPath": str,
        "ExpectedValue": str,
        "ActualValue": str,
        "DifferenceType": DifferenceTypeType,
    },
)
PublishTypeInputRequestTypeDef = TypedDict(
    "PublishTypeInputRequestTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "Arn": NotRequired[str],
        "TypeName": NotRequired[str],
        "PublicVersionNumber": NotRequired[str],
    },
)
RecordHandlerProgressInputRequestTypeDef = TypedDict(
    "RecordHandlerProgressInputRequestTypeDef",
    {
        "BearerToken": str,
        "OperationStatus": OperationStatusType,
        "CurrentOperationStatus": NotRequired[OperationStatusType],
        "StatusMessage": NotRequired[str],
        "ErrorCode": NotRequired[HandlerErrorCodeType],
        "ResourceModel": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
RegisterPublisherInputRequestTypeDef = TypedDict(
    "RegisterPublisherInputRequestTypeDef",
    {
        "AcceptTermsAndConditions": NotRequired[bool],
        "ConnectionArn": NotRequired[str],
    },
)
ResourceTargetDefinitionTypeDef = TypedDict(
    "ResourceTargetDefinitionTypeDef",
    {
        "Attribute": NotRequired[ResourceAttributeType],
        "Name": NotRequired[str],
        "RequiresRecreation": NotRequired[RequiresRecreationType],
        "Path": NotRequired[str],
        "BeforeValue": NotRequired[str],
        "AfterValue": NotRequired[str],
        "AttributeChangeType": NotRequired[AttributeChangeTypeType],
    },
)
RollbackTriggerTypeDef = TypedDict(
    "RollbackTriggerTypeDef",
    {
        "Arn": str,
        "Type": str,
    },
)
RollbackStackInputRequestTypeDef = TypedDict(
    "RollbackStackInputRequestTypeDef",
    {
        "StackName": str,
        "RoleARN": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
SetStackPolicyInputRequestTypeDef = TypedDict(
    "SetStackPolicyInputRequestTypeDef",
    {
        "StackName": str,
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
    },
)
SetTypeConfigurationInputRequestTypeDef = TypedDict(
    "SetTypeConfigurationInputRequestTypeDef",
    {
        "Configuration": str,
        "TypeArn": NotRequired[str],
        "ConfigurationAlias": NotRequired[str],
        "TypeName": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
    },
)
SetTypeDefaultVersionInputRequestTypeDef = TypedDict(
    "SetTypeDefaultVersionInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[RegistryTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
    },
)
SignalResourceInputRequestTypeDef = TypedDict(
    "SignalResourceInputRequestTypeDef",
    {
        "StackName": str,
        "LogicalResourceId": str,
        "UniqueId": str,
        "Status": ResourceSignalStatusType,
    },
)
StackDriftInformationSummaryTypeDef = TypedDict(
    "StackDriftInformationSummaryTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)
StackDriftInformationTypeDef = TypedDict(
    "StackDriftInformationTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)
StackInstanceComprehensiveStatusTypeDef = TypedDict(
    "StackInstanceComprehensiveStatusTypeDef",
    {
        "DetailedStatus": NotRequired[StackInstanceDetailedStatusType],
    },
)
StackResourceDriftInformationTypeDef = TypedDict(
    "StackResourceDriftInformationTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)
StackResourceDriftInformationSummaryTypeDef = TypedDict(
    "StackResourceDriftInformationSummaryTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": NotRequired[datetime],
    },
)
StackSetDriftDetectionDetailsTypeDef = TypedDict(
    "StackSetDriftDetectionDetailsTypeDef",
    {
        "DriftStatus": NotRequired[StackSetDriftStatusType],
        "DriftDetectionStatus": NotRequired[StackSetDriftDetectionStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "TotalStackInstancesCount": NotRequired[int],
        "DriftedStackInstancesCount": NotRequired[int],
        "InSyncStackInstancesCount": NotRequired[int],
        "InProgressStackInstancesCount": NotRequired[int],
        "FailedStackInstancesCount": NotRequired[int],
    },
)
StackSetOperationPreferencesExtraOutputTypeDef = TypedDict(
    "StackSetOperationPreferencesExtraOutputTypeDef",
    {
        "RegionConcurrencyType": NotRequired[RegionConcurrencyTypeType],
        "RegionOrder": NotRequired[List[str]],
        "FailureToleranceCount": NotRequired[int],
        "FailureTolerancePercentage": NotRequired[int],
        "MaxConcurrentCount": NotRequired[int],
        "MaxConcurrentPercentage": NotRequired[int],
        "ConcurrencyMode": NotRequired[ConcurrencyModeType],
    },
)
StackSetOperationPreferencesOutputTypeDef = TypedDict(
    "StackSetOperationPreferencesOutputTypeDef",
    {
        "RegionConcurrencyType": NotRequired[RegionConcurrencyTypeType],
        "RegionOrder": NotRequired[List[str]],
        "FailureToleranceCount": NotRequired[int],
        "FailureTolerancePercentage": NotRequired[int],
        "MaxConcurrentCount": NotRequired[int],
        "MaxConcurrentPercentage": NotRequired[int],
        "ConcurrencyMode": NotRequired[ConcurrencyModeType],
    },
)
StackSetOperationStatusDetailsTypeDef = TypedDict(
    "StackSetOperationStatusDetailsTypeDef",
    {
        "FailedStackInstancesCount": NotRequired[int],
    },
)
StartResourceScanInputRequestTypeDef = TypedDict(
    "StartResourceScanInputRequestTypeDef",
    {
        "ClientRequestToken": NotRequired[str],
    },
)
StopStackSetOperationInputRequestTypeDef = TypedDict(
    "StopStackSetOperationInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "CallAs": NotRequired[CallAsType],
    },
)
TemplateParameterTypeDef = TypedDict(
    "TemplateParameterTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "NoEcho": NotRequired[bool],
        "Description": NotRequired[str],
    },
)
TestTypeInputRequestTypeDef = TypedDict(
    "TestTypeInputRequestTypeDef",
    {
        "Arn": NotRequired[str],
        "Type": NotRequired[ThirdPartyTypeType],
        "TypeName": NotRequired[str],
        "VersionId": NotRequired[str],
        "LogDeliveryBucket": NotRequired[str],
    },
)
UpdateTerminationProtectionInputRequestTypeDef = TypedDict(
    "UpdateTerminationProtectionInputRequestTypeDef",
    {
        "EnableTerminationProtection": bool,
        "StackName": str,
    },
)
ValidateTemplateInputRequestTypeDef = TypedDict(
    "ValidateTemplateInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
    },
)
WarningPropertyTypeDef = TypedDict(
    "WarningPropertyTypeDef",
    {
        "PropertyPath": NotRequired[str],
        "Required": NotRequired[bool],
        "Description": NotRequired[str],
    },
)
StackSetOperationResultSummaryTypeDef = TypedDict(
    "StackSetOperationResultSummaryTypeDef",
    {
        "Account": NotRequired[str],
        "Region": NotRequired[str],
        "Status": NotRequired[StackSetOperationResultStatusType],
        "StatusReason": NotRequired[str],
        "AccountGateResult": NotRequired[AccountGateResultTypeDef],
        "OrganizationalUnitId": NotRequired[str],
    },
)
ActivateTypeInputRequestTypeDef = TypedDict(
    "ActivateTypeInputRequestTypeDef",
    {
        "Type": NotRequired[ThirdPartyTypeType],
        "PublicTypeArn": NotRequired[str],
        "PublisherId": NotRequired[str],
        "TypeName": NotRequired[str],
        "TypeNameAlias": NotRequired[str],
        "AutoUpdate": NotRequired[bool],
        "LoggingConfig": NotRequired[LoggingConfigTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "VersionBump": NotRequired[VersionBumpType],
        "MajorVersion": NotRequired[int],
    },
)
RegisterTypeInputRequestTypeDef = TypedDict(
    "RegisterTypeInputRequestTypeDef",
    {
        "TypeName": str,
        "SchemaHandlerPackage": str,
        "Type": NotRequired[RegistryTypeType],
        "LoggingConfig": NotRequired[LoggingConfigTypeDef],
        "ExecutionRoleArn": NotRequired[str],
        "ClientRequestToken": NotRequired[str],
    },
)
ActivateTypeOutputTypeDef = TypedDict(
    "ActivateTypeOutputTypeDef",
    {
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateChangeSetOutputTypeDef = TypedDict(
    "CreateChangeSetOutputTypeDef",
    {
        "Id": str,
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGeneratedTemplateOutputTypeDef = TypedDict(
    "CreateGeneratedTemplateOutputTypeDef",
    {
        "GeneratedTemplateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStackInstancesOutputTypeDef = TypedDict(
    "CreateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStackOutputTypeDef = TypedDict(
    "CreateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateStackSetOutputTypeDef = TypedDict(
    "CreateStackSetOutputTypeDef",
    {
        "StackSetId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteStackInstancesOutputTypeDef = TypedDict(
    "DeleteStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeAccountLimitsOutputTypeDef = TypedDict(
    "DescribeAccountLimitsOutputTypeDef",
    {
        "AccountLimits": List[AccountLimitTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeOrganizationsAccessOutputTypeDef = TypedDict(
    "DescribeOrganizationsAccessOutputTypeDef",
    {
        "Status": OrganizationStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribePublisherOutputTypeDef = TypedDict(
    "DescribePublisherOutputTypeDef",
    {
        "PublisherId": str,
        "PublisherStatus": PublisherStatusType,
        "IdentityProvider": IdentityProviderType,
        "PublisherProfile": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeResourceScanOutputTypeDef = TypedDict(
    "DescribeResourceScanOutputTypeDef",
    {
        "ResourceScanId": str,
        "Status": ResourceScanStatusType,
        "StatusReason": str,
        "StartTime": datetime,
        "EndTime": datetime,
        "PercentageCompleted": float,
        "ResourceTypes": List[str],
        "ResourcesScanned": int,
        "ResourcesRead": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStackDriftDetectionStatusOutputTypeDef = TypedDict(
    "DescribeStackDriftDetectionStatusOutputTypeDef",
    {
        "StackId": str,
        "StackDriftDetectionId": str,
        "StackDriftStatus": StackDriftStatusType,
        "DetectionStatus": StackDriftDetectionStatusType,
        "DetectionStatusReason": str,
        "DriftedStackResourceCount": int,
        "Timestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeTypeRegistrationOutputTypeDef = TypedDict(
    "DescribeTypeRegistrationOutputTypeDef",
    {
        "ProgressStatus": RegistrationStatusType,
        "Description": str,
        "TypeArn": str,
        "TypeVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectStackDriftOutputTypeDef = TypedDict(
    "DetectStackDriftOutputTypeDef",
    {
        "StackDriftDetectionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DetectStackSetDriftOutputTypeDef = TypedDict(
    "DetectStackSetDriftOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EstimateTemplateCostOutputTypeDef = TypedDict(
    "EstimateTemplateCostOutputTypeDef",
    {
        "Url": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGeneratedTemplateOutputTypeDef = TypedDict(
    "GetGeneratedTemplateOutputTypeDef",
    {
        "Status": GeneratedTemplateStatusType,
        "TemplateBody": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetStackPolicyOutputTypeDef = TypedDict(
    "GetStackPolicyOutputTypeDef",
    {
        "StackPolicyBody": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetTemplateOutputTypeDef = TypedDict(
    "GetTemplateOutputTypeDef",
    {
        "TemplateBody": Dict[str, Any],
        "StagesAvailable": List["TemplateStageType"],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportStacksToStackSetOutputTypeDef = TypedDict(
    "ImportStacksToStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListImportsOutputTypeDef = TypedDict(
    "ListImportsOutputTypeDef",
    {
        "Imports": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTypeRegistrationsOutputTypeDef = TypedDict(
    "ListTypeRegistrationsOutputTypeDef",
    {
        "RegistrationTokenList": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ModuleInfoResponseTypeDef = TypedDict(
    "ModuleInfoResponseTypeDef",
    {
        "TypeHierarchy": str,
        "LogicalIdHierarchy": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PublishTypeOutputTypeDef = TypedDict(
    "PublishTypeOutputTypeDef",
    {
        "PublicTypeArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterPublisherOutputTypeDef = TypedDict(
    "RegisterPublisherOutputTypeDef",
    {
        "PublisherId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RegisterTypeOutputTypeDef = TypedDict(
    "RegisterTypeOutputTypeDef",
    {
        "RegistrationToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackStackOutputTypeDef = TypedDict(
    "RollbackStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SetTypeConfigurationOutputTypeDef = TypedDict(
    "SetTypeConfigurationOutputTypeDef",
    {
        "ConfigurationArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StackDriftInformationResponseTypeDef = TypedDict(
    "StackDriftInformationResponseTypeDef",
    {
        "StackDriftStatus": StackDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StackResourceDriftInformationResponseTypeDef = TypedDict(
    "StackResourceDriftInformationResponseTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StackResourceDriftInformationSummaryResponseTypeDef = TypedDict(
    "StackResourceDriftInformationSummaryResponseTypeDef",
    {
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "LastCheckTimestamp": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartResourceScanOutputTypeDef = TypedDict(
    "StartResourceScanOutputTypeDef",
    {
        "ResourceScanId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestTypeOutputTypeDef = TypedDict(
    "TestTypeOutputTypeDef",
    {
        "TypeVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateGeneratedTemplateOutputTypeDef = TypedDict(
    "UpdateGeneratedTemplateOutputTypeDef",
    {
        "GeneratedTemplateId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStackInstancesOutputTypeDef = TypedDict(
    "UpdateStackInstancesOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStackOutputTypeDef = TypedDict(
    "UpdateStackOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateStackSetOutputTypeDef = TypedDict(
    "UpdateStackSetOutputTypeDef",
    {
        "OperationId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateTerminationProtectionOutputTypeDef = TypedDict(
    "UpdateTerminationProtectionOutputTypeDef",
    {
        "StackId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BatchDescribeTypeConfigurationsErrorTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsErrorTypeDef",
    {
        "ErrorCode": NotRequired[str],
        "ErrorMessage": NotRequired[str],
        "TypeConfigurationIdentifier": NotRequired[TypeConfigurationIdentifierTypeDef],
    },
)
BatchDescribeTypeConfigurationsInputRequestTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsInputRequestTypeDef",
    {
        "TypeConfigurationIdentifiers": Sequence[TypeConfigurationIdentifierTypeDef],
    },
)
ChangeSetHookTargetDetailsTypeDef = TypedDict(
    "ChangeSetHookTargetDetailsTypeDef",
    {
        "TargetType": NotRequired[Literal["RESOURCE"]],
        "ResourceTargetDetails": NotRequired[ChangeSetHookResourceTargetDetailsTypeDef],
    },
)
ListChangeSetsOutputTypeDef = TypedDict(
    "ListChangeSetsOutputTypeDef",
    {
        "Summaries": List[ChangeSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
EstimateTemplateCostInputRequestTypeDef = TypedDict(
    "EstimateTemplateCostInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
    },
)
CreateGeneratedTemplateInputRequestTypeDef = TypedDict(
    "CreateGeneratedTemplateInputRequestTypeDef",
    {
        "GeneratedTemplateName": str,
        "Resources": NotRequired[Sequence[ResourceDefinitionTypeDef]],
        "StackName": NotRequired[str],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
    },
)
UpdateGeneratedTemplateInputRequestTypeDef = TypedDict(
    "UpdateGeneratedTemplateInputRequestTypeDef",
    {
        "GeneratedTemplateName": str,
        "NewGeneratedTemplateName": NotRequired[str],
        "AddResources": NotRequired[Sequence[ResourceDefinitionTypeDef]],
        "RemoveResources": NotRequired[Sequence[str]],
        "RefreshAllResources": NotRequired[bool],
        "TemplateConfiguration": NotRequired[TemplateConfigurationTypeDef],
    },
)
CreateStackInstancesInputRequestTypeDef = TypedDict(
    "CreateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired[DeploymentTargetsTypeDef],
        "ParameterOverrides": NotRequired[Sequence[ParameterTypeDef]],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
DeleteStackInstancesInputRequestTypeDef = TypedDict(
    "DeleteStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "RetainStacks": bool,
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired[DeploymentTargetsTypeDef],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
DetectStackSetDriftInputRequestTypeDef = TypedDict(
    "DetectStackSetDriftInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
ImportStacksToStackSetInputRequestTypeDef = TypedDict(
    "ImportStacksToStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "StackIds": NotRequired[Sequence[str]],
        "StackIdsUrl": NotRequired[str],
        "OrganizationalUnitIds": NotRequired[Sequence[str]],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
UpdateStackInstancesInputRequestTypeDef = TypedDict(
    "UpdateStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "Regions": Sequence[str],
        "Accounts": NotRequired[Sequence[str]],
        "DeploymentTargets": NotRequired[DeploymentTargetsTypeDef],
        "ParameterOverrides": NotRequired[Sequence[ParameterTypeDef]],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "OperationId": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
CreateStackSetInputRequestTypeDef = TypedDict(
    "CreateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "Description": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "StackId": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "PermissionModel": NotRequired[PermissionModelsType],
        "AutoDeployment": NotRequired[AutoDeploymentTypeDef],
        "CallAs": NotRequired[CallAsType],
        "ClientRequestToken": NotRequired[str],
        "ManagedExecution": NotRequired[ManagedExecutionTypeDef],
    },
)
StackSetSummaryTypeDef = TypedDict(
    "StackSetSummaryTypeDef",
    {
        "StackSetName": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[StackSetStatusType],
        "AutoDeployment": NotRequired[AutoDeploymentTypeDef],
        "PermissionModel": NotRequired[PermissionModelsType],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "ManagedExecution": NotRequired[ManagedExecutionTypeDef],
    },
)
UpdateStackSetInputRequestTypeDef = TypedDict(
    "UpdateStackSetInputRequestTypeDef",
    {
        "StackSetName": str,
        "Description": NotRequired[str],
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesTypeDef],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "DeploymentTargets": NotRequired[DeploymentTargetsTypeDef],
        "PermissionModel": NotRequired[PermissionModelsType],
        "AutoDeployment": NotRequired[AutoDeploymentTypeDef],
        "OperationId": NotRequired[str],
        "Accounts": NotRequired[Sequence[str]],
        "Regions": NotRequired[Sequence[str]],
        "CallAs": NotRequired[CallAsType],
        "ManagedExecution": NotRequired[ManagedExecutionTypeDef],
    },
)
DeploymentTargetsUnionTypeDef = Union[DeploymentTargetsTypeDef, DeploymentTargetsOutputTypeDef]
DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef = TypedDict(
    "DescribeAccountLimitsInputDescribeAccountLimitsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeChangeSetInputDescribeChangeSetPaginateTypeDef = TypedDict(
    "DescribeChangeSetInputDescribeChangeSetPaginateTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "IncludePropertyValues": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStackEventsInputDescribeStackEventsPaginateTypeDef = TypedDict(
    "DescribeStackEventsInputDescribeStackEventsPaginateTypeDef",
    {
        "StackName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeStacksInputDescribeStacksPaginateTypeDef = TypedDict(
    "DescribeStacksInputDescribeStacksPaginateTypeDef",
    {
        "StackName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListChangeSetsInputListChangeSetsPaginateTypeDef = TypedDict(
    "ListChangeSetsInputListChangeSetsPaginateTypeDef",
    {
        "StackName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListExportsInputListExportsPaginateTypeDef = TypedDict(
    "ListExportsInputListExportsPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGeneratedTemplatesInputListGeneratedTemplatesPaginateTypeDef = TypedDict(
    "ListGeneratedTemplatesInputListGeneratedTemplatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListImportsInputListImportsPaginateTypeDef = TypedDict(
    "ListImportsInputListImportsPaginateTypeDef",
    {
        "ExportName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceScanResourcesInputListResourceScanResourcesPaginateTypeDef = TypedDict(
    "ListResourceScanResourcesInputListResourceScanResourcesPaginateTypeDef",
    {
        "ResourceScanId": str,
        "ResourceIdentifier": NotRequired[str],
        "ResourceTypePrefix": NotRequired[str],
        "TagKey": NotRequired[str],
        "TagValue": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceScansInputListResourceScansPaginateTypeDef = TypedDict(
    "ListResourceScansInputListResourceScansPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStackResourcesInputListStackResourcesPaginateTypeDef = TypedDict(
    "ListStackResourcesInputListStackResourcesPaginateTypeDef",
    {
        "StackName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStackSetOperationsInputListStackSetOperationsPaginateTypeDef = TypedDict(
    "ListStackSetOperationsInputListStackSetOperationsPaginateTypeDef",
    {
        "StackSetName": str,
        "CallAs": NotRequired[CallAsType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStackSetsInputListStackSetsPaginateTypeDef = TypedDict(
    "ListStackSetsInputListStackSetsPaginateTypeDef",
    {
        "Status": NotRequired[StackSetStatusType],
        "CallAs": NotRequired[CallAsType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStacksInputListStacksPaginateTypeDef = TypedDict(
    "ListStacksInputListStacksPaginateTypeDef",
    {
        "StackStatusFilter": NotRequired[Sequence[StackStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
DescribeChangeSetInputChangeSetCreateCompleteWaitTypeDef = TypedDict(
    "DescribeChangeSetInputChangeSetCreateCompleteWaitTypeDef",
    {
        "ChangeSetName": str,
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "IncludePropertyValues": NotRequired[bool],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackCreateCompleteWaitTypeDef = TypedDict(
    "DescribeStacksInputStackCreateCompleteWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackDeleteCompleteWaitTypeDef = TypedDict(
    "DescribeStacksInputStackDeleteCompleteWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackExistsWaitTypeDef = TypedDict(
    "DescribeStacksInputStackExistsWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackImportCompleteWaitTypeDef = TypedDict(
    "DescribeStacksInputStackImportCompleteWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackRollbackCompleteWaitTypeDef = TypedDict(
    "DescribeStacksInputStackRollbackCompleteWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStacksInputStackUpdateCompleteWaitTypeDef = TypedDict(
    "DescribeStacksInputStackUpdateCompleteWaitTypeDef",
    {
        "StackName": NotRequired[str],
        "NextToken": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeTypeRegistrationInputTypeRegistrationCompleteWaitTypeDef = TypedDict(
    "DescribeTypeRegistrationInputTypeRegistrationCompleteWaitTypeDef",
    {
        "RegistrationToken": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DescribeStackEventsOutputTypeDef = TypedDict(
    "DescribeStackEventsOutputTypeDef",
    {
        "StackEvents": List[StackEventTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeTypeOutputTypeDef = TypedDict(
    "DescribeTypeOutputTypeDef",
    {
        "Arn": str,
        "Type": RegistryTypeType,
        "TypeName": str,
        "DefaultVersionId": str,
        "IsDefaultVersion": bool,
        "TypeTestsStatus": TypeTestsStatusType,
        "TypeTestsStatusDescription": str,
        "Description": str,
        "Schema": str,
        "ProvisioningType": ProvisioningTypeType,
        "DeprecatedStatus": DeprecatedStatusType,
        "LoggingConfig": LoggingConfigTypeDef,
        "RequiredActivatedTypes": List[RequiredActivatedTypeTypeDef],
        "ExecutionRoleArn": str,
        "Visibility": VisibilityType,
        "SourceUrl": str,
        "DocumentationUrl": str,
        "LastUpdated": datetime,
        "TimeCreated": datetime,
        "ConfigurationSchema": str,
        "PublisherId": str,
        "OriginalTypeName": str,
        "OriginalTypeArn": str,
        "PublicVersionNumber": str,
        "LatestPublicVersion": str,
        "IsActivated": bool,
        "AutoUpdate": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListExportsOutputTypeDef = TypedDict(
    "ListExportsOutputTypeDef",
    {
        "Exports": List[ExportTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetTemplateSummaryInputRequestTypeDef = TypedDict(
    "GetTemplateSummaryInputRequestTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "StackName": NotRequired[str],
        "StackSetName": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
        "TemplateSummaryConfig": NotRequired[TemplateSummaryConfigTypeDef],
    },
)
ListGeneratedTemplatesOutputTypeDef = TypedDict(
    "ListGeneratedTemplatesOutputTypeDef",
    {
        "Summaries": List[TemplateSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceScanRelatedResourcesInputListResourceScanRelatedResourcesPaginateTypeDef = TypedDict(
    "ListResourceScanRelatedResourcesInputListResourceScanRelatedResourcesPaginateTypeDef",
    {
        "ResourceScanId": str,
        "Resources": Sequence[ScannedResourceIdentifierTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListResourceScanRelatedResourcesInputRequestTypeDef = TypedDict(
    "ListResourceScanRelatedResourcesInputRequestTypeDef",
    {
        "ResourceScanId": str,
        "Resources": Sequence[ScannedResourceIdentifierTypeDef],
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
    },
)
ListResourceScanRelatedResourcesOutputTypeDef = TypedDict(
    "ListResourceScanRelatedResourcesOutputTypeDef",
    {
        "RelatedResources": List[ScannedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceScanResourcesOutputTypeDef = TypedDict(
    "ListResourceScanResourcesOutputTypeDef",
    {
        "Resources": List[ScannedResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListResourceScansOutputTypeDef = TypedDict(
    "ListResourceScansOutputTypeDef",
    {
        "ResourceScanSummaries": List[ResourceScanSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStackInstancesInputListStackInstancesPaginateTypeDef = TypedDict(
    "ListStackInstancesInputListStackInstancesPaginateTypeDef",
    {
        "StackSetName": str,
        "Filters": NotRequired[Sequence[StackInstanceFilterTypeDef]],
        "StackInstanceAccount": NotRequired[str],
        "StackInstanceRegion": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStackInstancesInputRequestTypeDef = TypedDict(
    "ListStackInstancesInputRequestTypeDef",
    {
        "StackSetName": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "Filters": NotRequired[Sequence[StackInstanceFilterTypeDef]],
        "StackInstanceAccount": NotRequired[str],
        "StackInstanceRegion": NotRequired[str],
        "CallAs": NotRequired[CallAsType],
    },
)
ListStackSetAutoDeploymentTargetsOutputTypeDef = TypedDict(
    "ListStackSetAutoDeploymentTargetsOutputTypeDef",
    {
        "Summaries": List[StackSetAutoDeploymentTargetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStackSetOperationResultsInputListStackSetOperationResultsPaginateTypeDef = TypedDict(
    "ListStackSetOperationResultsInputListStackSetOperationResultsPaginateTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "CallAs": NotRequired[CallAsType],
        "Filters": NotRequired[Sequence[OperationResultFilterTypeDef]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListStackSetOperationResultsInputRequestTypeDef = TypedDict(
    "ListStackSetOperationResultsInputRequestTypeDef",
    {
        "StackSetName": str,
        "OperationId": str,
        "NextToken": NotRequired[str],
        "MaxResults": NotRequired[int],
        "CallAs": NotRequired[CallAsType],
        "Filters": NotRequired[Sequence[OperationResultFilterTypeDef]],
    },
)
ListTypeVersionsOutputTypeDef = TypedDict(
    "ListTypeVersionsOutputTypeDef",
    {
        "TypeVersionSummaries": List[TypeVersionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListTypesInputListTypesPaginateTypeDef = TypedDict(
    "ListTypesInputListTypesPaginateTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "ProvisioningType": NotRequired[ProvisioningTypeType],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "Type": NotRequired[RegistryTypeType],
        "Filters": NotRequired[TypeFiltersTypeDef],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListTypesInputRequestTypeDef = TypedDict(
    "ListTypesInputRequestTypeDef",
    {
        "Visibility": NotRequired[VisibilityType],
        "ProvisioningType": NotRequired[ProvisioningTypeType],
        "DeprecatedStatus": NotRequired[DeprecatedStatusType],
        "Type": NotRequired[RegistryTypeType],
        "Filters": NotRequired[TypeFiltersTypeDef],
        "MaxResults": NotRequired[int],
        "NextToken": NotRequired[str],
    },
)
ListTypesOutputTypeDef = TypedDict(
    "ListTypesOutputTypeDef",
    {
        "TypeSummaries": List[TypeSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ParameterDeclarationTypeDef = TypedDict(
    "ParameterDeclarationTypeDef",
    {
        "ParameterKey": NotRequired[str],
        "DefaultValue": NotRequired[str],
        "ParameterType": NotRequired[str],
        "NoEcho": NotRequired[bool],
        "Description": NotRequired[str],
        "ParameterConstraints": NotRequired[ParameterConstraintsTypeDef],
    },
)
StackInstanceResourceDriftsSummaryTypeDef = TypedDict(
    "StackInstanceResourceDriftsSummaryTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "Timestamp": datetime,
        "PhysicalResourceId": NotRequired[str],
        "PhysicalResourceIdContext": NotRequired[
            List[PhysicalResourceIdContextKeyValuePairTypeDef]
        ],
        "PropertyDifferences": NotRequired[List[PropertyDifferenceTypeDef]],
    },
)
StackResourceDriftTypeDef = TypedDict(
    "StackResourceDriftTypeDef",
    {
        "StackId": str,
        "LogicalResourceId": str,
        "ResourceType": str,
        "StackResourceDriftStatus": StackResourceDriftStatusType,
        "Timestamp": datetime,
        "PhysicalResourceId": NotRequired[str],
        "PhysicalResourceIdContext": NotRequired[
            List[PhysicalResourceIdContextKeyValuePairTypeDef]
        ],
        "ExpectedProperties": NotRequired[str],
        "ActualProperties": NotRequired[str],
        "PropertyDifferences": NotRequired[List[PropertyDifferenceTypeDef]],
        "ModuleInfo": NotRequired[ModuleInfoTypeDef],
    },
)
ResourceChangeDetailTypeDef = TypedDict(
    "ResourceChangeDetailTypeDef",
    {
        "Target": NotRequired[ResourceTargetDefinitionTypeDef],
        "Evaluation": NotRequired[EvaluationTypeType],
        "ChangeSource": NotRequired[ChangeSourceType],
        "CausingEntity": NotRequired[str],
    },
)
RollbackConfigurationExtraOutputTypeDef = TypedDict(
    "RollbackConfigurationExtraOutputTypeDef",
    {
        "RollbackTriggers": NotRequired[List[RollbackTriggerTypeDef]],
        "MonitoringTimeInMinutes": NotRequired[int],
    },
)
RollbackConfigurationOutputTypeDef = TypedDict(
    "RollbackConfigurationOutputTypeDef",
    {
        "RollbackTriggers": NotRequired[List[RollbackTriggerTypeDef]],
        "MonitoringTimeInMinutes": NotRequired[int],
    },
)
RollbackConfigurationResponseTypeDef = TypedDict(
    "RollbackConfigurationResponseTypeDef",
    {
        "RollbackTriggers": List[RollbackTriggerTypeDef],
        "MonitoringTimeInMinutes": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RollbackConfigurationTypeDef = TypedDict(
    "RollbackConfigurationTypeDef",
    {
        "RollbackTriggers": NotRequired[Sequence[RollbackTriggerTypeDef]],
        "MonitoringTimeInMinutes": NotRequired[int],
    },
)
StackSummaryTypeDef = TypedDict(
    "StackSummaryTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
        "StackId": NotRequired[str],
        "TemplateDescription": NotRequired[str],
        "LastUpdatedTime": NotRequired[datetime],
        "DeletionTime": NotRequired[datetime],
        "StackStatusReason": NotRequired[str],
        "ParentId": NotRequired[str],
        "RootId": NotRequired[str],
        "DriftInformation": NotRequired[StackDriftInformationSummaryTypeDef],
    },
)
StackInstanceSummaryTypeDef = TypedDict(
    "StackInstanceSummaryTypeDef",
    {
        "StackSetId": NotRequired[str],
        "Region": NotRequired[str],
        "Account": NotRequired[str],
        "StackId": NotRequired[str],
        "Status": NotRequired[StackInstanceStatusType],
        "StatusReason": NotRequired[str],
        "StackInstanceStatus": NotRequired[StackInstanceComprehensiveStatusTypeDef],
        "OrganizationalUnitId": NotRequired[str],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "LastOperationId": NotRequired[str],
    },
)
StackInstanceTypeDef = TypedDict(
    "StackInstanceTypeDef",
    {
        "StackSetId": NotRequired[str],
        "Region": NotRequired[str],
        "Account": NotRequired[str],
        "StackId": NotRequired[str],
        "ParameterOverrides": NotRequired[List[ParameterTypeDef]],
        "Status": NotRequired[StackInstanceStatusType],
        "StackInstanceStatus": NotRequired[StackInstanceComprehensiveStatusTypeDef],
        "StatusReason": NotRequired[str],
        "OrganizationalUnitId": NotRequired[str],
        "DriftStatus": NotRequired[StackDriftStatusType],
        "LastDriftCheckTimestamp": NotRequired[datetime],
        "LastOperationId": NotRequired[str],
    },
)
StackResourceDetailTypeDef = TypedDict(
    "StackResourceDetailTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "StackName": NotRequired[str],
        "StackId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "Description": NotRequired[str],
        "Metadata": NotRequired[str],
        "DriftInformation": NotRequired[StackResourceDriftInformationTypeDef],
        "ModuleInfo": NotRequired[ModuleInfoTypeDef],
    },
)
StackResourceTypeDef = TypedDict(
    "StackResourceTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "Timestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "StackName": NotRequired[str],
        "StackId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "Description": NotRequired[str],
        "DriftInformation": NotRequired[StackResourceDriftInformationTypeDef],
        "ModuleInfo": NotRequired[ModuleInfoTypeDef],
    },
)
StackResourceSummaryTypeDef = TypedDict(
    "StackResourceSummaryTypeDef",
    {
        "LogicalResourceId": str,
        "ResourceType": str,
        "LastUpdatedTimestamp": datetime,
        "ResourceStatus": ResourceStatusType,
        "PhysicalResourceId": NotRequired[str],
        "ResourceStatusReason": NotRequired[str],
        "DriftInformation": NotRequired[StackResourceDriftInformationSummaryTypeDef],
        "ModuleInfo": NotRequired[ModuleInfoTypeDef],
    },
)
StackSetTypeDef = TypedDict(
    "StackSetTypeDef",
    {
        "StackSetName": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Status": NotRequired[StackSetStatusType],
        "TemplateBody": NotRequired[str],
        "Parameters": NotRequired[List[ParameterTypeDef]],
        "Capabilities": NotRequired[List[CapabilityType]],
        "Tags": NotRequired[List[TagTypeDef]],
        "StackSetARN": NotRequired[str],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "StackSetDriftDetectionDetails": NotRequired[StackSetDriftDetectionDetailsTypeDef],
        "AutoDeployment": NotRequired[AutoDeploymentTypeDef],
        "PermissionModel": NotRequired[PermissionModelsType],
        "OrganizationalUnitIds": NotRequired[List[str]],
        "ManagedExecution": NotRequired[ManagedExecutionTypeDef],
        "Regions": NotRequired[List[str]],
    },
)
StackSetOperationPreferencesUnionTypeDef = Union[
    StackSetOperationPreferencesTypeDef, StackSetOperationPreferencesExtraOutputTypeDef
]
StackSetOperationSummaryTypeDef = TypedDict(
    "StackSetOperationSummaryTypeDef",
    {
        "OperationId": NotRequired[str],
        "Action": NotRequired[StackSetOperationActionType],
        "Status": NotRequired[StackSetOperationStatusType],
        "CreationTimestamp": NotRequired[datetime],
        "EndTimestamp": NotRequired[datetime],
        "StatusReason": NotRequired[str],
        "StatusDetails": NotRequired[StackSetOperationStatusDetailsTypeDef],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesOutputTypeDef],
    },
)
StackSetOperationTypeDef = TypedDict(
    "StackSetOperationTypeDef",
    {
        "OperationId": NotRequired[str],
        "StackSetId": NotRequired[str],
        "Action": NotRequired[StackSetOperationActionType],
        "Status": NotRequired[StackSetOperationStatusType],
        "OperationPreferences": NotRequired[StackSetOperationPreferencesOutputTypeDef],
        "RetainStacks": NotRequired[bool],
        "AdministrationRoleARN": NotRequired[str],
        "ExecutionRoleName": NotRequired[str],
        "CreationTimestamp": NotRequired[datetime],
        "EndTimestamp": NotRequired[datetime],
        "DeploymentTargets": NotRequired[DeploymentTargetsOutputTypeDef],
        "StackSetDriftDetectionDetails": NotRequired[StackSetDriftDetectionDetailsTypeDef],
        "StatusReason": NotRequired[str],
        "StatusDetails": NotRequired[StackSetOperationStatusDetailsTypeDef],
    },
)
ValidateTemplateOutputTypeDef = TypedDict(
    "ValidateTemplateOutputTypeDef",
    {
        "Parameters": List[TemplateParameterTypeDef],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "DeclaredTransforms": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
WarningDetailTypeDef = TypedDict(
    "WarningDetailTypeDef",
    {
        "Type": NotRequired[WarningTypeType],
        "Properties": NotRequired[List[WarningPropertyTypeDef]],
    },
)
ListStackSetOperationResultsOutputTypeDef = TypedDict(
    "ListStackSetOperationResultsOutputTypeDef",
    {
        "Summaries": List[StackSetOperationResultSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
BatchDescribeTypeConfigurationsOutputTypeDef = TypedDict(
    "BatchDescribeTypeConfigurationsOutputTypeDef",
    {
        "Errors": List[BatchDescribeTypeConfigurationsErrorTypeDef],
        "UnprocessedTypeConfigurations": List[TypeConfigurationIdentifierTypeDef],
        "TypeConfigurations": List[TypeConfigurationDetailsTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ChangeSetHookTypeDef = TypedDict(
    "ChangeSetHookTypeDef",
    {
        "InvocationPoint": NotRequired[Literal["PRE_PROVISION"]],
        "FailureMode": NotRequired[HookFailureModeType],
        "TypeName": NotRequired[str],
        "TypeVersionId": NotRequired[str],
        "TypeConfigurationVersionId": NotRequired[str],
        "TargetDetails": NotRequired[ChangeSetHookTargetDetailsTypeDef],
    },
)
ListStackSetsOutputTypeDef = TypedDict(
    "ListStackSetsOutputTypeDef",
    {
        "Summaries": List[StackSetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
GetTemplateSummaryOutputTypeDef = TypedDict(
    "GetTemplateSummaryOutputTypeDef",
    {
        "Parameters": List[ParameterDeclarationTypeDef],
        "Description": str,
        "Capabilities": List[CapabilityType],
        "CapabilitiesReason": str,
        "ResourceTypes": List[str],
        "Version": str,
        "Metadata": str,
        "DeclaredTransforms": List[str],
        "ResourceIdentifierSummaries": List[ResourceIdentifierSummaryTypeDef],
        "Warnings": WarningsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStackInstanceResourceDriftsOutputTypeDef = TypedDict(
    "ListStackInstanceResourceDriftsOutputTypeDef",
    {
        "Summaries": List[StackInstanceResourceDriftsSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStackResourceDriftsOutputTypeDef = TypedDict(
    "DescribeStackResourceDriftsOutputTypeDef",
    {
        "StackResourceDrifts": List[StackResourceDriftTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DetectStackResourceDriftOutputTypeDef = TypedDict(
    "DetectStackResourceDriftOutputTypeDef",
    {
        "StackResourceDrift": StackResourceDriftTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceChangeTypeDef = TypedDict(
    "ResourceChangeTypeDef",
    {
        "PolicyAction": NotRequired[PolicyActionType],
        "Action": NotRequired[ChangeActionType],
        "LogicalResourceId": NotRequired[str],
        "PhysicalResourceId": NotRequired[str],
        "ResourceType": NotRequired[str],
        "Replacement": NotRequired[ReplacementType],
        "Scope": NotRequired[List[ResourceAttributeType]],
        "Details": NotRequired[List[ResourceChangeDetailTypeDef]],
        "ChangeSetId": NotRequired[str],
        "ModuleInfo": NotRequired[ModuleInfoTypeDef],
        "BeforeContext": NotRequired[str],
        "AfterContext": NotRequired[str],
    },
)
StackTypeDef = TypedDict(
    "StackTypeDef",
    {
        "StackName": str,
        "CreationTime": datetime,
        "StackStatus": StackStatusType,
        "StackId": NotRequired[str],
        "ChangeSetId": NotRequired[str],
        "Description": NotRequired[str],
        "Parameters": NotRequired[List[ParameterTypeDef]],
        "DeletionTime": NotRequired[datetime],
        "LastUpdatedTime": NotRequired[datetime],
        "RollbackConfiguration": NotRequired[RollbackConfigurationOutputTypeDef],
        "StackStatusReason": NotRequired[str],
        "DisableRollback": NotRequired[bool],
        "NotificationARNs": NotRequired[List[str]],
        "TimeoutInMinutes": NotRequired[int],
        "Capabilities": NotRequired[List[CapabilityType]],
        "Outputs": NotRequired[List[OutputTypeDef]],
        "RoleARN": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
        "EnableTerminationProtection": NotRequired[bool],
        "ParentId": NotRequired[str],
        "RootId": NotRequired[str],
        "DriftInformation": NotRequired[StackDriftInformationTypeDef],
        "RetainExceptOnCreate": NotRequired[bool],
        "DeletionMode": NotRequired[DeletionModeType],
        "DetailedStatus": NotRequired[DetailedStatusType],
    },
)
CreateChangeSetInputRequestTypeDef = TypedDict(
    "CreateChangeSetInputRequestTypeDef",
    {
        "StackName": str,
        "ChangeSetName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientToken": NotRequired[str],
        "Description": NotRequired[str],
        "ChangeSetType": NotRequired[ChangeSetTypeType],
        "ResourcesToImport": NotRequired[Sequence[ResourceToImportTypeDef]],
        "IncludeNestedStacks": NotRequired[bool],
        "OnStackFailure": NotRequired[OnStackFailureType],
        "ImportExistingResources": NotRequired[bool],
    },
)
CreateStackInputRequestTypeDef = TypedDict(
    "CreateStackInputRequestTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "DisableRollback": NotRequired[bool],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "TimeoutInMinutes": NotRequired[int],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "OnFailure": NotRequired[OnFailureType],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
        "EnableTerminationProtection": NotRequired[bool],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
CreateStackInputServiceResourceCreateStackTypeDef = TypedDict(
    "CreateStackInputServiceResourceCreateStackTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "DisableRollback": NotRequired[bool],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "TimeoutInMinutes": NotRequired[int],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "OnFailure": NotRequired[OnFailureType],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "ClientRequestToken": NotRequired[str],
        "EnableTerminationProtection": NotRequired[bool],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
RollbackConfigurationUnionTypeDef = Union[
    RollbackConfigurationTypeDef, RollbackConfigurationExtraOutputTypeDef
]
UpdateStackInputRequestTypeDef = TypedDict(
    "UpdateStackInputRequestTypeDef",
    {
        "StackName": str,
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "StackPolicyDuringUpdateBody": NotRequired[str],
        "StackPolicyDuringUpdateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DisableRollback": NotRequired[bool],
        "ClientRequestToken": NotRequired[str],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
UpdateStackInputStackUpdateTypeDef = TypedDict(
    "UpdateStackInputStackUpdateTypeDef",
    {
        "TemplateBody": NotRequired[str],
        "TemplateURL": NotRequired[str],
        "UsePreviousTemplate": NotRequired[bool],
        "StackPolicyDuringUpdateBody": NotRequired[str],
        "StackPolicyDuringUpdateURL": NotRequired[str],
        "Parameters": NotRequired[Sequence[ParameterTypeDef]],
        "Capabilities": NotRequired[Sequence[CapabilityType]],
        "ResourceTypes": NotRequired[Sequence[str]],
        "RoleARN": NotRequired[str],
        "RollbackConfiguration": NotRequired[RollbackConfigurationTypeDef],
        "StackPolicyBody": NotRequired[str],
        "StackPolicyURL": NotRequired[str],
        "NotificationARNs": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "DisableRollback": NotRequired[bool],
        "ClientRequestToken": NotRequired[str],
        "RetainExceptOnCreate": NotRequired[bool],
    },
)
ListStacksOutputTypeDef = TypedDict(
    "ListStacksOutputTypeDef",
    {
        "StackSummaries": List[StackSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ListStackInstancesOutputTypeDef = TypedDict(
    "ListStackInstancesOutputTypeDef",
    {
        "Summaries": List[StackInstanceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStackInstanceOutputTypeDef = TypedDict(
    "DescribeStackInstanceOutputTypeDef",
    {
        "StackInstance": StackInstanceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStackResourceOutputTypeDef = TypedDict(
    "DescribeStackResourceOutputTypeDef",
    {
        "StackResourceDetail": StackResourceDetailTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeStackResourcesOutputTypeDef = TypedDict(
    "DescribeStackResourcesOutputTypeDef",
    {
        "StackResources": List[StackResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStackResourcesOutputTypeDef = TypedDict(
    "ListStackResourcesOutputTypeDef",
    {
        "StackResourceSummaries": List[StackResourceSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStackSetOutputTypeDef = TypedDict(
    "DescribeStackSetOutputTypeDef",
    {
        "StackSet": StackSetTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListStackSetOperationsOutputTypeDef = TypedDict(
    "ListStackSetOperationsOutputTypeDef",
    {
        "Summaries": List[StackSetOperationSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeStackSetOperationOutputTypeDef = TypedDict(
    "DescribeStackSetOperationOutputTypeDef",
    {
        "StackSetOperation": StackSetOperationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceDetailTypeDef = TypedDict(
    "ResourceDetailTypeDef",
    {
        "ResourceType": NotRequired[str],
        "LogicalResourceId": NotRequired[str],
        "ResourceIdentifier": NotRequired[Dict[str, str]],
        "ResourceStatus": NotRequired[GeneratedTemplateResourceStatusType],
        "ResourceStatusReason": NotRequired[str],
        "Warnings": NotRequired[List[WarningDetailTypeDef]],
    },
)
DescribeChangeSetHooksOutputTypeDef = TypedDict(
    "DescribeChangeSetHooksOutputTypeDef",
    {
        "ChangeSetId": str,
        "ChangeSetName": str,
        "Hooks": List[ChangeSetHookTypeDef],
        "Status": ChangeSetHooksStatusType,
        "StackId": str,
        "StackName": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
ChangeTypeDef = TypedDict(
    "ChangeTypeDef",
    {
        "Type": NotRequired[Literal["Resource"]],
        "HookInvocationCount": NotRequired[int],
        "ResourceChange": NotRequired[ResourceChangeTypeDef],
    },
)
DescribeStacksOutputTypeDef = TypedDict(
    "DescribeStacksOutputTypeDef",
    {
        "Stacks": List[StackTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
DescribeGeneratedTemplateOutputTypeDef = TypedDict(
    "DescribeGeneratedTemplateOutputTypeDef",
    {
        "GeneratedTemplateId": str,
        "GeneratedTemplateName": str,
        "Resources": List[ResourceDetailTypeDef],
        "Status": GeneratedTemplateStatusType,
        "StatusReason": str,
        "CreationTime": datetime,
        "LastUpdatedTime": datetime,
        "Progress": TemplateProgressTypeDef,
        "StackId": str,
        "TemplateConfiguration": TemplateConfigurationTypeDef,
        "TotalWarnings": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DescribeChangeSetOutputTypeDef = TypedDict(
    "DescribeChangeSetOutputTypeDef",
    {
        "ChangeSetName": str,
        "ChangeSetId": str,
        "StackId": str,
        "StackName": str,
        "Description": str,
        "Parameters": List[ParameterTypeDef],
        "CreationTime": datetime,
        "ExecutionStatus": ExecutionStatusType,
        "Status": ChangeSetStatusType,
        "StatusReason": str,
        "NotificationARNs": List[str],
        "RollbackConfiguration": RollbackConfigurationOutputTypeDef,
        "Capabilities": List[CapabilityType],
        "Tags": List[TagTypeDef],
        "Changes": List[ChangeTypeDef],
        "IncludeNestedStacks": bool,
        "ParentChangeSetId": str,
        "RootChangeSetId": str,
        "OnStackFailure": OnStackFailureType,
        "ImportExistingResources": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
        "NextToken": NotRequired[str],
    },
)
