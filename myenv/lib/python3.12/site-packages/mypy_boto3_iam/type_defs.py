"""
Type annotations for iam service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/type_defs/)

Usage::

    ```python
    from mypy_boto3_iam.type_defs import AccessDetailTypeDef

    data: AccessDetailTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    AccessAdvisorUsageGranularityTypeType,
    AssignmentStatusTypeType,
    ContextKeyTypeEnumType,
    DeletionTaskStatusTypeType,
    EncodingTypeType,
    EntityTypeType,
    GlobalEndpointTokenVersionType,
    JobStatusTypeType,
    PolicyEvaluationDecisionTypeType,
    PolicyOwnerEntityTypeType,
    PolicyScopeTypeType,
    PolicySourceTypeType,
    PolicyTypeType,
    PolicyUsageTypeType,
    ReportStateTypeType,
    SortKeyTypeType,
    StatusTypeType,
    SummaryKeyTypeType,
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
    "AccessDetailTypeDef",
    "AccessKeyLastUsedTypeDef",
    "AccessKeyMetadataTypeDef",
    "AccessKeyTypeDef",
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    "AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef",
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    "AddUserToGroupRequestGroupAddUserTypeDef",
    "AddUserToGroupRequestRequestTypeDef",
    "AddUserToGroupRequestUserAddGroupTypeDef",
    "AttachGroupPolicyRequestGroupAttachPolicyTypeDef",
    "AttachGroupPolicyRequestPolicyAttachGroupTypeDef",
    "AttachGroupPolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestPolicyAttachRoleTypeDef",
    "AttachRolePolicyRequestRequestTypeDef",
    "AttachRolePolicyRequestRoleAttachPolicyTypeDef",
    "AttachUserPolicyRequestPolicyAttachUserTypeDef",
    "AttachUserPolicyRequestRequestTypeDef",
    "AttachUserPolicyRequestUserAttachPolicyTypeDef",
    "AttachedPermissionsBoundaryTypeDef",
    "AttachedPolicyTypeDef",
    "ChangePasswordRequestRequestTypeDef",
    "ChangePasswordRequestServiceResourceChangePasswordTypeDef",
    "ContextEntryTypeDef",
    "CreateAccessKeyRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "CreateAccountAliasRequestRequestTypeDef",
    "CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef",
    "CreateGroupRequestGroupCreateTypeDef",
    "CreateGroupRequestRequestTypeDef",
    "CreateGroupRequestServiceResourceCreateGroupTypeDef",
    "GroupTypeDef",
    "TagTypeDef",
    "CreateLoginProfileRequestLoginProfileCreateTypeDef",
    "CreateLoginProfileRequestRequestTypeDef",
    "CreateLoginProfileRequestUserCreateLoginProfileTypeDef",
    "LoginProfileTypeDef",
    "CreatePolicyVersionRequestPolicyCreateVersionTypeDef",
    "CreatePolicyVersionRequestRequestTypeDef",
    "CreateServiceLinkedRoleRequestRequestTypeDef",
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    "ServiceSpecificCredentialTypeDef",
    "DeactivateMFADeviceRequestRequestTypeDef",
    "DeleteAccessKeyRequestRequestTypeDef",
    "DeleteAccountAliasRequestRequestTypeDef",
    "DeleteGroupPolicyRequestRequestTypeDef",
    "DeleteGroupRequestRequestTypeDef",
    "DeleteInstanceProfileRequestRequestTypeDef",
    "DeleteLoginProfileRequestRequestTypeDef",
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    "DeletePolicyRequestRequestTypeDef",
    "DeletePolicyVersionRequestRequestTypeDef",
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    "DeleteRolePolicyRequestRequestTypeDef",
    "DeleteRoleRequestRequestTypeDef",
    "DeleteSAMLProviderRequestRequestTypeDef",
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    "DeleteServerCertificateRequestRequestTypeDef",
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    "DeleteServiceSpecificCredentialRequestRequestTypeDef",
    "DeleteSigningCertificateRequestRequestTypeDef",
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    "DeleteUserPolicyRequestRequestTypeDef",
    "DeleteUserRequestRequestTypeDef",
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    "RoleUsageTypeTypeDef",
    "DetachGroupPolicyRequestGroupDetachPolicyTypeDef",
    "DetachGroupPolicyRequestPolicyDetachGroupTypeDef",
    "DetachGroupPolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestPolicyDetachRoleTypeDef",
    "DetachRolePolicyRequestRequestTypeDef",
    "DetachRolePolicyRequestRoleDetachPolicyTypeDef",
    "DetachUserPolicyRequestPolicyDetachUserTypeDef",
    "DetachUserPolicyRequestRequestTypeDef",
    "DetachUserPolicyRequestUserDetachPolicyTypeDef",
    "EnableMFADeviceRequestMfaDeviceAssociateTypeDef",
    "EnableMFADeviceRequestRequestTypeDef",
    "EnableMFADeviceRequestUserEnableMfaTypeDef",
    "EntityInfoTypeDef",
    "ErrorDetailsTypeDef",
    "OrganizationsDecisionDetailTypeDef",
    "PermissionsBoundaryDecisionDetailTypeDef",
    "GenerateOrganizationsAccessReportRequestRequestTypeDef",
    "GenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    "PasswordPolicyTypeDef",
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    "GetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    "GetGroupPolicyRequestRequestTypeDef",
    "GetGroupRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "GetInstanceProfileRequestRequestTypeDef",
    "GetLoginProfileRequestRequestTypeDef",
    "GetMFADeviceRequestRequestTypeDef",
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    "GetOrganizationsAccessReportRequestRequestTypeDef",
    "GetPolicyRequestRequestTypeDef",
    "GetPolicyVersionRequestRequestTypeDef",
    "GetRolePolicyRequestRequestTypeDef",
    "GetRoleRequestRequestTypeDef",
    "GetSAMLProviderRequestRequestTypeDef",
    "GetSSHPublicKeyRequestRequestTypeDef",
    "SSHPublicKeyTypeDef",
    "GetServerCertificateRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsRequestRequestTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    "GetUserPolicyRequestRequestTypeDef",
    "GetUserRequestRequestTypeDef",
    "ListAccessKeysRequestRequestTypeDef",
    "ListAccountAliasesRequestRequestTypeDef",
    "ListAttachedGroupPoliciesRequestRequestTypeDef",
    "ListAttachedRolePoliciesRequestRequestTypeDef",
    "ListAttachedUserPoliciesRequestRequestTypeDef",
    "ListEntitiesForPolicyRequestRequestTypeDef",
    "PolicyGroupTypeDef",
    "PolicyRoleTypeDef",
    "PolicyUserTypeDef",
    "ListGroupPoliciesRequestRequestTypeDef",
    "ListGroupsForUserRequestRequestTypeDef",
    "ListGroupsRequestRequestTypeDef",
    "ListInstanceProfileTagsRequestRequestTypeDef",
    "ListInstanceProfilesForRoleRequestRequestTypeDef",
    "ListInstanceProfilesRequestRequestTypeDef",
    "ListMFADeviceTagsRequestRequestTypeDef",
    "ListMFADevicesRequestRequestTypeDef",
    "MFADeviceTypeDef",
    "ListOpenIDConnectProviderTagsRequestRequestTypeDef",
    "OpenIDConnectProviderListEntryTypeDef",
    "PolicyGrantingServiceAccessTypeDef",
    "ListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    "ListPoliciesRequestRequestTypeDef",
    "ListPolicyTagsRequestRequestTypeDef",
    "ListPolicyVersionsRequestRequestTypeDef",
    "ListRolePoliciesRequestRequestTypeDef",
    "ListRoleTagsRequestRequestTypeDef",
    "ListRolesRequestRequestTypeDef",
    "ListSAMLProviderTagsRequestRequestTypeDef",
    "SAMLProviderListEntryTypeDef",
    "ListSSHPublicKeysRequestRequestTypeDef",
    "SSHPublicKeyMetadataTypeDef",
    "ListServerCertificateTagsRequestRequestTypeDef",
    "ListServerCertificatesRequestRequestTypeDef",
    "ServerCertificateMetadataTypeDef",
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    "ServiceSpecificCredentialMetadataTypeDef",
    "ListSigningCertificatesRequestRequestTypeDef",
    "SigningCertificateTypeDef",
    "ListUserPoliciesRequestRequestTypeDef",
    "ListUserTagsRequestRequestTypeDef",
    "ListUsersRequestRequestTypeDef",
    "ListVirtualMFADevicesRequestRequestTypeDef",
    "PolicyDocumentStatementTypeDef",
    "PositionTypeDef",
    "PutGroupPolicyRequestGroupCreatePolicyTypeDef",
    "PutGroupPolicyRequestGroupPolicyPutTypeDef",
    "PutGroupPolicyRequestRequestTypeDef",
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    "PutRolePolicyRequestRequestTypeDef",
    "PutRolePolicyRequestRolePolicyPutTypeDef",
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    "PutUserPolicyRequestRequestTypeDef",
    "PutUserPolicyRequestUserCreatePolicyTypeDef",
    "PutUserPolicyRequestUserPolicyPutTypeDef",
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    "RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef",
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    "RemoveUserFromGroupRequestGroupRemoveUserTypeDef",
    "RemoveUserFromGroupRequestRequestTypeDef",
    "RemoveUserFromGroupRequestUserRemoveGroupTypeDef",
    "ResetServiceSpecificCredentialRequestRequestTypeDef",
    "ResyncMFADeviceRequestMfaDeviceResyncTypeDef",
    "ResyncMFADeviceRequestRequestTypeDef",
    "RoleLastUsedTypeDef",
    "TrackedActionLastAccessedTypeDef",
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    "UntagInstanceProfileRequestRequestTypeDef",
    "UntagMFADeviceRequestRequestTypeDef",
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    "UntagPolicyRequestRequestTypeDef",
    "UntagRoleRequestRequestTypeDef",
    "UntagSAMLProviderRequestRequestTypeDef",
    "UntagServerCertificateRequestRequestTypeDef",
    "UntagUserRequestRequestTypeDef",
    "UpdateAccessKeyRequestAccessKeyActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyDeactivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairActivateTypeDef",
    "UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef",
    "UpdateAccessKeyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef",
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    "UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef",
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef",
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    "UpdateGroupRequestGroupUpdateTypeDef",
    "UpdateGroupRequestRequestTypeDef",
    "UpdateLoginProfileRequestLoginProfileUpdateTypeDef",
    "UpdateLoginProfileRequestRequestTypeDef",
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    "UpdateRoleDescriptionRequestRequestTypeDef",
    "UpdateRoleRequestRequestTypeDef",
    "UpdateSAMLProviderRequestRequestTypeDef",
    "UpdateSAMLProviderRequestSamlProviderUpdateTypeDef",
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    "UpdateServerCertificateRequestRequestTypeDef",
    "UpdateServerCertificateRequestServerCertificateUpdateTypeDef",
    "UpdateServiceSpecificCredentialRequestRequestTypeDef",
    "UpdateSigningCertificateRequestRequestTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateActivateTypeDef",
    "UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef",
    "UpdateUserRequestRequestTypeDef",
    "UpdateUserRequestUserUpdateTypeDef",
    "UploadSSHPublicKeyRequestRequestTypeDef",
    "UploadSigningCertificateRequestRequestTypeDef",
    "UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef",
    "SimulateCustomPolicyRequestRequestTypeDef",
    "SimulatePrincipalPolicyRequestRequestTypeDef",
    "CreateAccessKeyResponseTypeDef",
    "DeleteServiceLinkedRoleResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GenerateCredentialReportResponseTypeDef",
    "GenerateOrganizationsAccessReportResponseTypeDef",
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    "GetAccessKeyLastUsedResponseTypeDef",
    "GetAccountSummaryResponseTypeDef",
    "GetContextKeysForPolicyResponseTypeDef",
    "GetCredentialReportResponseTypeDef",
    "GetMFADeviceResponseTypeDef",
    "ListAccessKeysResponseTypeDef",
    "ListAccountAliasesResponseTypeDef",
    "ListAttachedGroupPoliciesResponseTypeDef",
    "ListAttachedRolePoliciesResponseTypeDef",
    "ListAttachedUserPoliciesResponseTypeDef",
    "ListGroupPoliciesResponseTypeDef",
    "ListRolePoliciesResponseTypeDef",
    "ListUserPoliciesResponseTypeDef",
    "UpdateSAMLProviderResponseTypeDef",
    "CreateGroupResponseTypeDef",
    "ListGroupsForUserResponseTypeDef",
    "ListGroupsResponseTypeDef",
    "CreateInstanceProfileRequestRequestTypeDef",
    "CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef",
    "CreateOpenIDConnectProviderRequestRequestTypeDef",
    "CreateOpenIDConnectProviderResponseTypeDef",
    "CreatePolicyRequestRequestTypeDef",
    "CreatePolicyRequestServiceResourceCreatePolicyTypeDef",
    "CreateRoleRequestRequestTypeDef",
    "CreateRoleRequestServiceResourceCreateRoleTypeDef",
    "CreateSAMLProviderRequestRequestTypeDef",
    "CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef",
    "CreateSAMLProviderResponseTypeDef",
    "CreateUserRequestRequestTypeDef",
    "CreateUserRequestServiceResourceCreateUserTypeDef",
    "CreateUserRequestUserCreateTypeDef",
    "CreateVirtualMFADeviceRequestRequestTypeDef",
    "CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef",
    "GetOpenIDConnectProviderResponseTypeDef",
    "GetSAMLProviderResponseTypeDef",
    "ListInstanceProfileTagsResponseTypeDef",
    "ListMFADeviceTagsResponseTypeDef",
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    "ListPolicyTagsResponseTypeDef",
    "ListRoleTagsResponseTypeDef",
    "ListSAMLProviderTagsResponseTypeDef",
    "ListServerCertificateTagsResponseTypeDef",
    "ListUserTagsResponseTypeDef",
    "PolicyTypeDef",
    "TagInstanceProfileRequestRequestTypeDef",
    "TagMFADeviceRequestRequestTypeDef",
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    "TagPolicyRequestRequestTypeDef",
    "TagRoleRequestRequestTypeDef",
    "TagSAMLProviderRequestRequestTypeDef",
    "TagServerCertificateRequestRequestTypeDef",
    "TagUserRequestRequestTypeDef",
    "UploadServerCertificateRequestRequestTypeDef",
    "UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef",
    "UserTypeDef",
    "CreateLoginProfileResponseTypeDef",
    "GetLoginProfileResponseTypeDef",
    "CreateServiceSpecificCredentialResponseTypeDef",
    "ResetServiceSpecificCredentialResponseTypeDef",
    "DeletionTaskFailureReasonTypeTypeDef",
    "EntityDetailsTypeDef",
    "GetOrganizationsAccessReportResponseTypeDef",
    "GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef",
    "GetGroupRequestGetGroupPaginateTypeDef",
    "ListAccessKeysRequestListAccessKeysPaginateTypeDef",
    "ListAccountAliasesRequestListAccountAliasesPaginateTypeDef",
    "ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef",
    "ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef",
    "ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef",
    "ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef",
    "ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef",
    "ListGroupsForUserRequestListGroupsForUserPaginateTypeDef",
    "ListGroupsRequestListGroupsPaginateTypeDef",
    "ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef",
    "ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef",
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    "ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef",
    "ListMFADevicesRequestListMFADevicesPaginateTypeDef",
    "ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef",
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    "ListPolicyTagsRequestListPolicyTagsPaginateTypeDef",
    "ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef",
    "ListRolePoliciesRequestListRolePoliciesPaginateTypeDef",
    "ListRoleTagsRequestListRoleTagsPaginateTypeDef",
    "ListRolesRequestListRolesPaginateTypeDef",
    "ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef",
    "ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef",
    "ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef",
    "ListServerCertificatesRequestListServerCertificatesPaginateTypeDef",
    "ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef",
    "ListUserPoliciesRequestListUserPoliciesPaginateTypeDef",
    "ListUserTagsRequestListUserTagsPaginateTypeDef",
    "ListUsersRequestListUsersPaginateTypeDef",
    "ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef",
    "SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef",
    "SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef",
    "GetAccountPasswordPolicyResponseTypeDef",
    "GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef",
    "GetPolicyRequestPolicyExistsWaitTypeDef",
    "GetRoleRequestRoleExistsWaitTypeDef",
    "GetUserRequestUserExistsWaitTypeDef",
    "GetSSHPublicKeyResponseTypeDef",
    "UploadSSHPublicKeyResponseTypeDef",
    "ListEntitiesForPolicyResponseTypeDef",
    "ListMFADevicesResponseTypeDef",
    "ListOpenIDConnectProvidersResponseTypeDef",
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    "ListSAMLProvidersResponseTypeDef",
    "ListSSHPublicKeysResponseTypeDef",
    "ListServerCertificatesResponseTypeDef",
    "ServerCertificateTypeDef",
    "UploadServerCertificateResponseTypeDef",
    "ListServiceSpecificCredentialsResponseTypeDef",
    "ListSigningCertificatesResponseTypeDef",
    "UploadSigningCertificateResponseTypeDef",
    "PolicyDocumentDictTypeDef",
    "StatementTypeDef",
    "ServiceLastAccessedTypeDef",
    "CreatePolicyResponseTypeDef",
    "GetPolicyResponseTypeDef",
    "ListPoliciesResponseTypeDef",
    "CreateUserResponseTypeDef",
    "GetGroupResponseTypeDef",
    "GetUserResponseTypeDef",
    "ListUsersResponseTypeDef",
    "VirtualMFADeviceTypeDef",
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    "GetServerCertificateResponseTypeDef",
    "PolicyDocumentTypeDef",
    "ResourceSpecificResultTypeDef",
    "GetServiceLastAccessedDetailsResponseTypeDef",
    "CreateVirtualMFADeviceResponseTypeDef",
    "ListVirtualMFADevicesResponseTypeDef",
    "GetGroupPolicyResponseTypeDef",
    "GetRolePolicyResponseTypeDef",
    "GetUserPolicyResponseTypeDef",
    "PolicyDetailTypeDef",
    "PolicyVersionTypeDef",
    "RoleTypeDef",
    "EvaluationResultTypeDef",
    "GroupDetailTypeDef",
    "UserDetailTypeDef",
    "CreatePolicyVersionResponseTypeDef",
    "GetPolicyVersionResponseTypeDef",
    "ListPolicyVersionsResponseTypeDef",
    "ManagedPolicyDetailTypeDef",
    "CreateRoleResponseTypeDef",
    "CreateServiceLinkedRoleResponseTypeDef",
    "GetRoleResponseTypeDef",
    "InstanceProfileTypeDef",
    "ListRolesResponseTypeDef",
    "UpdateRoleDescriptionResponseTypeDef",
    "SimulatePolicyResponseTypeDef",
    "CreateInstanceProfileResponseTypeDef",
    "GetInstanceProfileResponseTypeDef",
    "ListInstanceProfilesForRoleResponseTypeDef",
    "ListInstanceProfilesResponseTypeDef",
    "RoleDetailTypeDef",
    "GetAccountAuthorizationDetailsResponseTypeDef",
)

AccessDetailTypeDef = TypedDict(
    "AccessDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "Region": NotRequired[str],
        "EntityPath": NotRequired[str],
        "LastAuthenticatedTime": NotRequired[datetime],
        "TotalAuthenticatedEntities": NotRequired[int],
    },
)
AccessKeyLastUsedTypeDef = TypedDict(
    "AccessKeyLastUsedTypeDef",
    {
        "ServiceName": str,
        "Region": str,
        "LastUsedDate": NotRequired[datetime],
    },
)
AccessKeyMetadataTypeDef = TypedDict(
    "AccessKeyMetadataTypeDef",
    {
        "UserName": NotRequired[str],
        "AccessKeyId": NotRequired[str],
        "Status": NotRequired[StatusTypeType],
        "CreateDate": NotRequired[datetime],
    },
)
AccessKeyTypeDef = TypedDict(
    "AccessKeyTypeDef",
    {
        "UserName": str,
        "AccessKeyId": str,
        "Status": StatusTypeType,
        "SecretAccessKey": str,
        "CreateDate": NotRequired[datetime],
    },
)
AddClientIDToOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "AddClientIDToOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)
AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestInstanceProfileAddRoleTypeDef",
    {
        "RoleName": str,
    },
)
AddRoleToInstanceProfileRequestRequestTypeDef = TypedDict(
    "AddRoleToInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)
AddUserToGroupRequestGroupAddUserTypeDef = TypedDict(
    "AddUserToGroupRequestGroupAddUserTypeDef",
    {
        "UserName": str,
    },
)
AddUserToGroupRequestRequestTypeDef = TypedDict(
    "AddUserToGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)
AddUserToGroupRequestUserAddGroupTypeDef = TypedDict(
    "AddUserToGroupRequestUserAddGroupTypeDef",
    {
        "GroupName": str,
    },
)
AttachGroupPolicyRequestGroupAttachPolicyTypeDef = TypedDict(
    "AttachGroupPolicyRequestGroupAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
AttachGroupPolicyRequestPolicyAttachGroupTypeDef = TypedDict(
    "AttachGroupPolicyRequestPolicyAttachGroupTypeDef",
    {
        "GroupName": str,
    },
)
AttachGroupPolicyRequestRequestTypeDef = TypedDict(
    "AttachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)
AttachRolePolicyRequestPolicyAttachRoleTypeDef = TypedDict(
    "AttachRolePolicyRequestPolicyAttachRoleTypeDef",
    {
        "RoleName": str,
    },
)
AttachRolePolicyRequestRequestTypeDef = TypedDict(
    "AttachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)
AttachRolePolicyRequestRoleAttachPolicyTypeDef = TypedDict(
    "AttachRolePolicyRequestRoleAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
AttachUserPolicyRequestPolicyAttachUserTypeDef = TypedDict(
    "AttachUserPolicyRequestPolicyAttachUserTypeDef",
    {
        "UserName": str,
    },
)
AttachUserPolicyRequestRequestTypeDef = TypedDict(
    "AttachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)
AttachUserPolicyRequestUserAttachPolicyTypeDef = TypedDict(
    "AttachUserPolicyRequestUserAttachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
AttachedPermissionsBoundaryTypeDef = TypedDict(
    "AttachedPermissionsBoundaryTypeDef",
    {
        "PermissionsBoundaryType": NotRequired[Literal["PermissionsBoundaryPolicy"]],
        "PermissionsBoundaryArn": NotRequired[str],
    },
)
AttachedPolicyTypeDef = TypedDict(
    "AttachedPolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyArn": NotRequired[str],
    },
)
ChangePasswordRequestRequestTypeDef = TypedDict(
    "ChangePasswordRequestRequestTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)
ChangePasswordRequestServiceResourceChangePasswordTypeDef = TypedDict(
    "ChangePasswordRequestServiceResourceChangePasswordTypeDef",
    {
        "OldPassword": str,
        "NewPassword": str,
    },
)
ContextEntryTypeDef = TypedDict(
    "ContextEntryTypeDef",
    {
        "ContextKeyName": NotRequired[str],
        "ContextKeyValues": NotRequired[Sequence[str]],
        "ContextKeyType": NotRequired[ContextKeyTypeEnumType],
    },
)
CreateAccessKeyRequestRequestTypeDef = TypedDict(
    "CreateAccessKeyRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
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
CreateAccountAliasRequestRequestTypeDef = TypedDict(
    "CreateAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)
CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef = TypedDict(
    "CreateAccountAliasRequestServiceResourceCreateAccountAliasTypeDef",
    {
        "AccountAlias": str,
    },
)
CreateGroupRequestGroupCreateTypeDef = TypedDict(
    "CreateGroupRequestGroupCreateTypeDef",
    {
        "Path": NotRequired[str],
    },
)
CreateGroupRequestRequestTypeDef = TypedDict(
    "CreateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "Path": NotRequired[str],
    },
)
CreateGroupRequestServiceResourceCreateGroupTypeDef = TypedDict(
    "CreateGroupRequestServiceResourceCreateGroupTypeDef",
    {
        "GroupName": str,
        "Path": NotRequired[str],
    },
)
GroupTypeDef = TypedDict(
    "GroupTypeDef",
    {
        "Path": str,
        "GroupName": str,
        "GroupId": str,
        "Arn": str,
        "CreateDate": datetime,
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
CreateLoginProfileRequestLoginProfileCreateTypeDef = TypedDict(
    "CreateLoginProfileRequestLoginProfileCreateTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)
CreateLoginProfileRequestRequestTypeDef = TypedDict(
    "CreateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)
CreateLoginProfileRequestUserCreateLoginProfileTypeDef = TypedDict(
    "CreateLoginProfileRequestUserCreateLoginProfileTypeDef",
    {
        "Password": str,
        "PasswordResetRequired": NotRequired[bool],
    },
)
LoginProfileTypeDef = TypedDict(
    "LoginProfileTypeDef",
    {
        "UserName": str,
        "CreateDate": datetime,
        "PasswordResetRequired": NotRequired[bool],
    },
)
CreatePolicyVersionRequestPolicyCreateVersionTypeDef = TypedDict(
    "CreatePolicyVersionRequestPolicyCreateVersionTypeDef",
    {
        "PolicyDocument": str,
        "SetAsDefault": NotRequired[bool],
    },
)
CreatePolicyVersionRequestRequestTypeDef = TypedDict(
    "CreatePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "PolicyDocument": str,
        "SetAsDefault": NotRequired[bool],
    },
)
CreateServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "CreateServiceLinkedRoleRequestRequestTypeDef",
    {
        "AWSServiceName": str,
        "Description": NotRequired[str],
        "CustomSuffix": NotRequired[str],
    },
)
CreateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "CreateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "UserName": str,
        "ServiceName": str,
    },
)
ServiceSpecificCredentialTypeDef = TypedDict(
    "ServiceSpecificCredentialTypeDef",
    {
        "CreateDate": datetime,
        "ServiceName": str,
        "ServiceUserName": str,
        "ServicePassword": str,
        "ServiceSpecificCredentialId": str,
        "UserName": str,
        "Status": StatusTypeType,
    },
)
DeactivateMFADeviceRequestRequestTypeDef = TypedDict(
    "DeactivateMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
    },
)
DeleteAccessKeyRequestRequestTypeDef = TypedDict(
    "DeleteAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
        "UserName": NotRequired[str],
    },
)
DeleteAccountAliasRequestRequestTypeDef = TypedDict(
    "DeleteAccountAliasRequestRequestTypeDef",
    {
        "AccountAlias": str,
    },
)
DeleteGroupPolicyRequestRequestTypeDef = TypedDict(
    "DeleteGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)
DeleteGroupRequestRequestTypeDef = TypedDict(
    "DeleteGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
DeleteInstanceProfileRequestRequestTypeDef = TypedDict(
    "DeleteInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
DeleteLoginProfileRequestRequestTypeDef = TypedDict(
    "DeleteLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
DeleteOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "DeleteOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)
DeletePolicyRequestRequestTypeDef = TypedDict(
    "DeletePolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
DeletePolicyVersionRequestRequestTypeDef = TypedDict(
    "DeletePolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)
DeleteRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
DeleteRolePolicyRequestRequestTypeDef = TypedDict(
    "DeleteRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)
DeleteRoleRequestRequestTypeDef = TypedDict(
    "DeleteRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
DeleteSAMLProviderRequestRequestTypeDef = TypedDict(
    "DeleteSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)
DeleteSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "DeleteSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
    },
)
DeleteServerCertificateRequestRequestTypeDef = TypedDict(
    "DeleteServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
DeleteServiceLinkedRoleRequestRequestTypeDef = TypedDict(
    "DeleteServiceLinkedRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
DeleteServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "DeleteServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "UserName": NotRequired[str],
    },
)
DeleteSigningCertificateRequestRequestTypeDef = TypedDict(
    "DeleteSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "UserName": NotRequired[str],
    },
)
DeleteUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "DeleteUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
DeleteUserPolicyRequestRequestTypeDef = TypedDict(
    "DeleteUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)
DeleteUserRequestRequestTypeDef = TypedDict(
    "DeleteUserRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
DeleteVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "DeleteVirtualMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
    },
)
RoleUsageTypeTypeDef = TypedDict(
    "RoleUsageTypeTypeDef",
    {
        "Region": NotRequired[str],
        "Resources": NotRequired[List[str]],
    },
)
DetachGroupPolicyRequestGroupDetachPolicyTypeDef = TypedDict(
    "DetachGroupPolicyRequestGroupDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
DetachGroupPolicyRequestPolicyDetachGroupTypeDef = TypedDict(
    "DetachGroupPolicyRequestPolicyDetachGroupTypeDef",
    {
        "GroupName": str,
    },
)
DetachGroupPolicyRequestRequestTypeDef = TypedDict(
    "DetachGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyArn": str,
    },
)
DetachRolePolicyRequestPolicyDetachRoleTypeDef = TypedDict(
    "DetachRolePolicyRequestPolicyDetachRoleTypeDef",
    {
        "RoleName": str,
    },
)
DetachRolePolicyRequestRequestTypeDef = TypedDict(
    "DetachRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyArn": str,
    },
)
DetachRolePolicyRequestRoleDetachPolicyTypeDef = TypedDict(
    "DetachRolePolicyRequestRoleDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
DetachUserPolicyRequestPolicyDetachUserTypeDef = TypedDict(
    "DetachUserPolicyRequestPolicyDetachUserTypeDef",
    {
        "UserName": str,
    },
)
DetachUserPolicyRequestRequestTypeDef = TypedDict(
    "DetachUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyArn": str,
    },
)
DetachUserPolicyRequestUserDetachPolicyTypeDef = TypedDict(
    "DetachUserPolicyRequestUserDetachPolicyTypeDef",
    {
        "PolicyArn": str,
    },
)
EnableMFADeviceRequestMfaDeviceAssociateTypeDef = TypedDict(
    "EnableMFADeviceRequestMfaDeviceAssociateTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)
EnableMFADeviceRequestRequestTypeDef = TypedDict(
    "EnableMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)
EnableMFADeviceRequestUserEnableMfaTypeDef = TypedDict(
    "EnableMFADeviceRequestUserEnableMfaTypeDef",
    {
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)
EntityInfoTypeDef = TypedDict(
    "EntityInfoTypeDef",
    {
        "Arn": str,
        "Name": str,
        "Type": PolicyOwnerEntityTypeType,
        "Id": str,
        "Path": NotRequired[str],
    },
)
ErrorDetailsTypeDef = TypedDict(
    "ErrorDetailsTypeDef",
    {
        "Message": str,
        "Code": str,
    },
)
OrganizationsDecisionDetailTypeDef = TypedDict(
    "OrganizationsDecisionDetailTypeDef",
    {
        "AllowedByOrganizations": NotRequired[bool],
    },
)
PermissionsBoundaryDecisionDetailTypeDef = TypedDict(
    "PermissionsBoundaryDecisionDetailTypeDef",
    {
        "AllowedByPermissionsBoundary": NotRequired[bool],
    },
)
GenerateOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportRequestRequestTypeDef",
    {
        "EntityPath": str,
        "OrganizationsPolicyId": NotRequired[str],
    },
)
GenerateServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "Arn": str,
        "Granularity": NotRequired[AccessAdvisorUsageGranularityTypeType],
    },
)
GetAccessKeyLastUsedRequestRequestTypeDef = TypedDict(
    "GetAccessKeyLastUsedRequestRequestTypeDef",
    {
        "AccessKeyId": str,
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
GetAccountAuthorizationDetailsRequestRequestTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsRequestRequestTypeDef",
    {
        "Filter": NotRequired[Sequence[EntityTypeType]],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
PasswordPolicyTypeDef = TypedDict(
    "PasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "ExpirePasswords": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)
GetContextKeysForCustomPolicyRequestRequestTypeDef = TypedDict(
    "GetContextKeysForCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": Sequence[str],
    },
)
GetContextKeysForPrincipalPolicyRequestRequestTypeDef = TypedDict(
    "GetContextKeysForPrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
        "PolicyInputList": NotRequired[Sequence[str]],
    },
)
GetGroupPolicyRequestRequestTypeDef = TypedDict(
    "GetGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
    },
)
GetGroupRequestRequestTypeDef = TypedDict(
    "GetGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
GetInstanceProfileRequestRequestTypeDef = TypedDict(
    "GetInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
    },
)
GetLoginProfileRequestRequestTypeDef = TypedDict(
    "GetLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
    },
)
GetMFADeviceRequestRequestTypeDef = TypedDict(
    "GetMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "UserName": NotRequired[str],
    },
)
GetOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "GetOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
    },
)
GetOrganizationsAccessReportRequestRequestTypeDef = TypedDict(
    "GetOrganizationsAccessReportRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
        "SortKey": NotRequired[SortKeyTypeType],
    },
)
GetPolicyRequestRequestTypeDef = TypedDict(
    "GetPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
    },
)
GetPolicyVersionRequestRequestTypeDef = TypedDict(
    "GetPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)
GetRolePolicyRequestRequestTypeDef = TypedDict(
    "GetRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
    },
)
GetRoleRequestRequestTypeDef = TypedDict(
    "GetRoleRequestRequestTypeDef",
    {
        "RoleName": str,
    },
)
GetSAMLProviderRequestRequestTypeDef = TypedDict(
    "GetSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
    },
)
GetSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "GetSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Encoding": EncodingTypeType,
    },
)
SSHPublicKeyTypeDef = TypedDict(
    "SSHPublicKeyTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Fingerprint": str,
        "SSHPublicKeyBody": str,
        "Status": StatusTypeType,
        "UploadDate": NotRequired[datetime],
    },
)
GetServerCertificateRequestRequestTypeDef = TypedDict(
    "GetServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
    },
)
GetServiceLastAccessedDetailsRequestRequestTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsRequestRequestTypeDef",
    {
        "JobId": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesRequestRequestTypeDef",
    {
        "JobId": str,
        "ServiceNamespace": str,
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusRequestRequestTypeDef",
    {
        "DeletionTaskId": str,
    },
)
GetUserPolicyRequestRequestTypeDef = TypedDict(
    "GetUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
    },
)
GetUserRequestRequestTypeDef = TypedDict(
    "GetUserRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
    },
)
ListAccessKeysRequestRequestTypeDef = TypedDict(
    "ListAccessKeysRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListAccountAliasesRequestRequestTypeDef = TypedDict(
    "ListAccountAliasesRequestRequestTypeDef",
    {
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListAttachedGroupPoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListAttachedRolePoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListAttachedUserPoliciesRequestRequestTypeDef = TypedDict(
    "ListAttachedUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListEntitiesForPolicyRequestRequestTypeDef = TypedDict(
    "ListEntitiesForPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "EntityFilter": NotRequired[EntityTypeType],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
PolicyGroupTypeDef = TypedDict(
    "PolicyGroupTypeDef",
    {
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
    },
)
PolicyRoleTypeDef = TypedDict(
    "PolicyRoleTypeDef",
    {
        "RoleName": NotRequired[str],
        "RoleId": NotRequired[str],
    },
)
PolicyUserTypeDef = TypedDict(
    "PolicyUserTypeDef",
    {
        "UserName": NotRequired[str],
        "UserId": NotRequired[str],
    },
)
ListGroupPoliciesRequestRequestTypeDef = TypedDict(
    "ListGroupPoliciesRequestRequestTypeDef",
    {
        "GroupName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListGroupsForUserRequestRequestTypeDef = TypedDict(
    "ListGroupsForUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListGroupsRequestRequestTypeDef = TypedDict(
    "ListGroupsRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListInstanceProfileTagsRequestRequestTypeDef = TypedDict(
    "ListInstanceProfileTagsRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListInstanceProfilesForRoleRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesForRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListInstanceProfilesRequestRequestTypeDef = TypedDict(
    "ListInstanceProfilesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListMFADeviceTagsRequestRequestTypeDef = TypedDict(
    "ListMFADeviceTagsRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListMFADevicesRequestRequestTypeDef = TypedDict(
    "ListMFADevicesRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
MFADeviceTypeDef = TypedDict(
    "MFADeviceTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "EnableDate": datetime,
    },
)
ListOpenIDConnectProviderTagsRequestRequestTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
OpenIDConnectProviderListEntryTypeDef = TypedDict(
    "OpenIDConnectProviderListEntryTypeDef",
    {
        "Arn": NotRequired[str],
    },
)
PolicyGrantingServiceAccessTypeDef = TypedDict(
    "PolicyGrantingServiceAccessTypeDef",
    {
        "PolicyName": str,
        "PolicyType": PolicyTypeType,
        "PolicyArn": NotRequired[str],
        "EntityType": NotRequired[PolicyOwnerEntityTypeType],
        "EntityName": NotRequired[str],
    },
)
ListPoliciesGrantingServiceAccessRequestRequestTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessRequestRequestTypeDef",
    {
        "Arn": str,
        "ServiceNamespaces": Sequence[str],
        "Marker": NotRequired[str],
    },
)
ListPoliciesRequestRequestTypeDef = TypedDict(
    "ListPoliciesRequestRequestTypeDef",
    {
        "Scope": NotRequired[PolicyScopeTypeType],
        "OnlyAttached": NotRequired[bool],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListPolicyTagsRequestRequestTypeDef = TypedDict(
    "ListPolicyTagsRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListPolicyVersionsRequestRequestTypeDef = TypedDict(
    "ListPolicyVersionsRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListRolePoliciesRequestRequestTypeDef = TypedDict(
    "ListRolePoliciesRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListRoleTagsRequestRequestTypeDef = TypedDict(
    "ListRoleTagsRequestRequestTypeDef",
    {
        "RoleName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListRolesRequestRequestTypeDef = TypedDict(
    "ListRolesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListSAMLProviderTagsRequestRequestTypeDef = TypedDict(
    "ListSAMLProviderTagsRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
SAMLProviderListEntryTypeDef = TypedDict(
    "SAMLProviderListEntryTypeDef",
    {
        "Arn": NotRequired[str],
        "ValidUntil": NotRequired[datetime],
        "CreateDate": NotRequired[datetime],
    },
)
ListSSHPublicKeysRequestRequestTypeDef = TypedDict(
    "ListSSHPublicKeysRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
SSHPublicKeyMetadataTypeDef = TypedDict(
    "SSHPublicKeyMetadataTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": StatusTypeType,
        "UploadDate": datetime,
    },
)
ListServerCertificateTagsRequestRequestTypeDef = TypedDict(
    "ListServerCertificateTagsRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListServerCertificatesRequestRequestTypeDef = TypedDict(
    "ListServerCertificatesRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ServerCertificateMetadataTypeDef = TypedDict(
    "ServerCertificateMetadataTypeDef",
    {
        "Path": str,
        "ServerCertificateName": str,
        "ServerCertificateId": str,
        "Arn": str,
        "UploadDate": NotRequired[datetime],
        "Expiration": NotRequired[datetime],
    },
)
ListServiceSpecificCredentialsRequestRequestTypeDef = TypedDict(
    "ListServiceSpecificCredentialsRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "ServiceName": NotRequired[str],
    },
)
ServiceSpecificCredentialMetadataTypeDef = TypedDict(
    "ServiceSpecificCredentialMetadataTypeDef",
    {
        "UserName": str,
        "Status": StatusTypeType,
        "ServiceUserName": str,
        "CreateDate": datetime,
        "ServiceSpecificCredentialId": str,
        "ServiceName": str,
    },
)
ListSigningCertificatesRequestRequestTypeDef = TypedDict(
    "ListSigningCertificatesRequestRequestTypeDef",
    {
        "UserName": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
SigningCertificateTypeDef = TypedDict(
    "SigningCertificateTypeDef",
    {
        "UserName": str,
        "CertificateId": str,
        "CertificateBody": str,
        "Status": StatusTypeType,
        "UploadDate": NotRequired[datetime],
    },
)
ListUserPoliciesRequestRequestTypeDef = TypedDict(
    "ListUserPoliciesRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListUserTagsRequestRequestTypeDef = TypedDict(
    "ListUserTagsRequestRequestTypeDef",
    {
        "UserName": str,
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListUsersRequestRequestTypeDef = TypedDict(
    "ListUsersRequestRequestTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
ListVirtualMFADevicesRequestRequestTypeDef = TypedDict(
    "ListVirtualMFADevicesRequestRequestTypeDef",
    {
        "AssignmentStatus": NotRequired[AssignmentStatusTypeType],
        "Marker": NotRequired[str],
        "MaxItems": NotRequired[int],
    },
)
PolicyDocumentStatementTypeDef = TypedDict(
    "PolicyDocumentStatementTypeDef",
    {
        "Effect": str,
        "Resource": Union[str, List[str]],
        "Sid": str,
        "Action": Union[str, List[str]],
    },
)
PositionTypeDef = TypedDict(
    "PositionTypeDef",
    {
        "Line": NotRequired[int],
        "Column": NotRequired[int],
    },
)
PutGroupPolicyRequestGroupCreatePolicyTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
PutGroupPolicyRequestGroupPolicyPutTypeDef = TypedDict(
    "PutGroupPolicyRequestGroupPolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)
PutGroupPolicyRequestRequestTypeDef = TypedDict(
    "PutGroupPolicyRequestRequestTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
PutRolePermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutRolePermissionsBoundaryRequestRequestTypeDef",
    {
        "RoleName": str,
        "PermissionsBoundary": str,
    },
)
PutRolePolicyRequestRequestTypeDef = TypedDict(
    "PutRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
PutRolePolicyRequestRolePolicyPutTypeDef = TypedDict(
    "PutRolePolicyRequestRolePolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)
PutUserPermissionsBoundaryRequestRequestTypeDef = TypedDict(
    "PutUserPermissionsBoundaryRequestRequestTypeDef",
    {
        "UserName": str,
        "PermissionsBoundary": str,
    },
)
PutUserPolicyRequestRequestTypeDef = TypedDict(
    "PutUserPolicyRequestRequestTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
PutUserPolicyRequestUserCreatePolicyTypeDef = TypedDict(
    "PutUserPolicyRequestUserCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
    },
)
PutUserPolicyRequestUserPolicyPutTypeDef = TypedDict(
    "PutUserPolicyRequestUserPolicyPutTypeDef",
    {
        "PolicyDocument": str,
    },
)
RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "RemoveClientIDFromOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ClientID": str,
    },
)
RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestInstanceProfileRemoveRoleTypeDef",
    {
        "RoleName": str,
    },
)
RemoveRoleFromInstanceProfileRequestRequestTypeDef = TypedDict(
    "RemoveRoleFromInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "RoleName": str,
    },
)
RemoveUserFromGroupRequestGroupRemoveUserTypeDef = TypedDict(
    "RemoveUserFromGroupRequestGroupRemoveUserTypeDef",
    {
        "UserName": str,
    },
)
RemoveUserFromGroupRequestRequestTypeDef = TypedDict(
    "RemoveUserFromGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "UserName": str,
    },
)
RemoveUserFromGroupRequestUserRemoveGroupTypeDef = TypedDict(
    "RemoveUserFromGroupRequestUserRemoveGroupTypeDef",
    {
        "GroupName": str,
    },
)
ResetServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "ResetServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "UserName": NotRequired[str],
    },
)
ResyncMFADeviceRequestMfaDeviceResyncTypeDef = TypedDict(
    "ResyncMFADeviceRequestMfaDeviceResyncTypeDef",
    {
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)
ResyncMFADeviceRequestRequestTypeDef = TypedDict(
    "ResyncMFADeviceRequestRequestTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "AuthenticationCode1": str,
        "AuthenticationCode2": str,
    },
)
RoleLastUsedTypeDef = TypedDict(
    "RoleLastUsedTypeDef",
    {
        "LastUsedDate": NotRequired[datetime],
        "Region": NotRequired[str],
    },
)
TrackedActionLastAccessedTypeDef = TypedDict(
    "TrackedActionLastAccessedTypeDef",
    {
        "ActionName": NotRequired[str],
        "LastAccessedEntity": NotRequired[str],
        "LastAccessedTime": NotRequired[datetime],
        "LastAccessedRegion": NotRequired[str],
    },
)
SetDefaultPolicyVersionRequestRequestTypeDef = TypedDict(
    "SetDefaultPolicyVersionRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "VersionId": str,
    },
)
SetSecurityTokenServicePreferencesRequestRequestTypeDef = TypedDict(
    "SetSecurityTokenServicePreferencesRequestRequestTypeDef",
    {
        "GlobalEndpointTokenVersion": GlobalEndpointTokenVersionType,
    },
)
UntagInstanceProfileRequestRequestTypeDef = TypedDict(
    "UntagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "TagKeys": Sequence[str],
    },
)
UntagMFADeviceRequestRequestTypeDef = TypedDict(
    "UntagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "TagKeys": Sequence[str],
    },
)
UntagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "UntagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "TagKeys": Sequence[str],
    },
)
UntagPolicyRequestRequestTypeDef = TypedDict(
    "UntagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "TagKeys": Sequence[str],
    },
)
UntagRoleRequestRequestTypeDef = TypedDict(
    "UntagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "TagKeys": Sequence[str],
    },
)
UntagSAMLProviderRequestRequestTypeDef = TypedDict(
    "UntagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "TagKeys": Sequence[str],
    },
)
UntagServerCertificateRequestRequestTypeDef = TypedDict(
    "UntagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "TagKeys": Sequence[str],
    },
)
UntagUserRequestRequestTypeDef = TypedDict(
    "UntagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "TagKeys": Sequence[str],
    },
)
UpdateAccessKeyRequestAccessKeyActivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyActivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateAccessKeyRequestAccessKeyDeactivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyDeactivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateAccessKeyRequestAccessKeyPairActivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairActivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef = TypedDict(
    "UpdateAccessKeyRequestAccessKeyPairDeactivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateAccessKeyRequestRequestTypeDef = TypedDict(
    "UpdateAccessKeyRequestRequestTypeDef",
    {
        "AccessKeyId": str,
        "Status": StatusTypeType,
        "UserName": NotRequired[str],
    },
)
UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestAccountPasswordPolicyUpdateTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)
UpdateAccountPasswordPolicyRequestRequestTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestRequestTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)
UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef = TypedDict(
    "UpdateAccountPasswordPolicyRequestServiceResourceCreateAccountPasswordPolicyTypeDef",
    {
        "MinimumPasswordLength": NotRequired[int],
        "RequireSymbols": NotRequired[bool],
        "RequireNumbers": NotRequired[bool],
        "RequireUppercaseCharacters": NotRequired[bool],
        "RequireLowercaseCharacters": NotRequired[bool],
        "AllowUsersToChangePassword": NotRequired[bool],
        "MaxPasswordAge": NotRequired[int],
        "PasswordReusePrevention": NotRequired[int],
        "HardExpiry": NotRequired[bool],
    },
)
UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestAssumeRolePolicyUpdateTypeDef",
    {
        "PolicyDocument": str,
    },
)
UpdateAssumeRolePolicyRequestRequestTypeDef = TypedDict(
    "UpdateAssumeRolePolicyRequestRequestTypeDef",
    {
        "RoleName": str,
        "PolicyDocument": str,
    },
)
UpdateGroupRequestGroupUpdateTypeDef = TypedDict(
    "UpdateGroupRequestGroupUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewGroupName": NotRequired[str],
    },
)
UpdateGroupRequestRequestTypeDef = TypedDict(
    "UpdateGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "NewPath": NotRequired[str],
        "NewGroupName": NotRequired[str],
    },
)
UpdateLoginProfileRequestLoginProfileUpdateTypeDef = TypedDict(
    "UpdateLoginProfileRequestLoginProfileUpdateTypeDef",
    {
        "Password": NotRequired[str],
        "PasswordResetRequired": NotRequired[bool],
    },
)
UpdateLoginProfileRequestRequestTypeDef = TypedDict(
    "UpdateLoginProfileRequestRequestTypeDef",
    {
        "UserName": str,
        "Password": NotRequired[str],
        "PasswordResetRequired": NotRequired[bool],
    },
)
UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef = TypedDict(
    "UpdateOpenIDConnectProviderThumbprintRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "ThumbprintList": Sequence[str],
    },
)
UpdateRoleDescriptionRequestRequestTypeDef = TypedDict(
    "UpdateRoleDescriptionRequestRequestTypeDef",
    {
        "RoleName": str,
        "Description": str,
    },
)
UpdateRoleRequestRequestTypeDef = TypedDict(
    "UpdateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
    },
)
UpdateSAMLProviderRequestRequestTypeDef = TypedDict(
    "UpdateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "SAMLProviderArn": str,
    },
)
UpdateSAMLProviderRequestSamlProviderUpdateTypeDef = TypedDict(
    "UpdateSAMLProviderRequestSamlProviderUpdateTypeDef",
    {
        "SAMLMetadataDocument": str,
    },
)
UpdateSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UpdateSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyId": str,
        "Status": StatusTypeType,
    },
)
UpdateServerCertificateRequestRequestTypeDef = TypedDict(
    "UpdateServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "NewPath": NotRequired[str],
        "NewServerCertificateName": NotRequired[str],
    },
)
UpdateServerCertificateRequestServerCertificateUpdateTypeDef = TypedDict(
    "UpdateServerCertificateRequestServerCertificateUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewServerCertificateName": NotRequired[str],
    },
)
UpdateServiceSpecificCredentialRequestRequestTypeDef = TypedDict(
    "UpdateServiceSpecificCredentialRequestRequestTypeDef",
    {
        "ServiceSpecificCredentialId": str,
        "Status": StatusTypeType,
        "UserName": NotRequired[str],
    },
)
UpdateSigningCertificateRequestRequestTypeDef = TypedDict(
    "UpdateSigningCertificateRequestRequestTypeDef",
    {
        "CertificateId": str,
        "Status": StatusTypeType,
        "UserName": NotRequired[str],
    },
)
UpdateSigningCertificateRequestSigningCertificateActivateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateActivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef = TypedDict(
    "UpdateSigningCertificateRequestSigningCertificateDeactivateTypeDef",
    {
        "Status": NotRequired[StatusTypeType],
    },
)
UpdateUserRequestRequestTypeDef = TypedDict(
    "UpdateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "NewPath": NotRequired[str],
        "NewUserName": NotRequired[str],
    },
)
UpdateUserRequestUserUpdateTypeDef = TypedDict(
    "UpdateUserRequestUserUpdateTypeDef",
    {
        "NewPath": NotRequired[str],
        "NewUserName": NotRequired[str],
    },
)
UploadSSHPublicKeyRequestRequestTypeDef = TypedDict(
    "UploadSSHPublicKeyRequestRequestTypeDef",
    {
        "UserName": str,
        "SSHPublicKeyBody": str,
    },
)
UploadSigningCertificateRequestRequestTypeDef = TypedDict(
    "UploadSigningCertificateRequestRequestTypeDef",
    {
        "CertificateBody": str,
        "UserName": NotRequired[str],
    },
)
UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef = TypedDict(
    "UploadSigningCertificateRequestServiceResourceCreateSigningCertificateTypeDef",
    {
        "CertificateBody": str,
        "UserName": NotRequired[str],
    },
)
SimulateCustomPolicyRequestRequestTypeDef = TypedDict(
    "SimulateCustomPolicyRequestRequestTypeDef",
    {
        "PolicyInputList": Sequence[str],
        "ActionNames": Sequence[str],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence[ContextEntryTypeDef]],
        "ResourceHandlingOption": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
SimulatePrincipalPolicyRequestRequestTypeDef = TypedDict(
    "SimulatePrincipalPolicyRequestRequestTypeDef",
    {
        "PolicySourceArn": str,
        "ActionNames": Sequence[str],
        "PolicyInputList": NotRequired[Sequence[str]],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence[ContextEntryTypeDef]],
        "ResourceHandlingOption": NotRequired[str],
        "MaxItems": NotRequired[int],
        "Marker": NotRequired[str],
    },
)
CreateAccessKeyResponseTypeDef = TypedDict(
    "CreateAccessKeyResponseTypeDef",
    {
        "AccessKey": AccessKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeleteServiceLinkedRoleResponseTypeDef = TypedDict(
    "DeleteServiceLinkedRoleResponseTypeDef",
    {
        "DeletionTaskId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateCredentialReportResponseTypeDef = TypedDict(
    "GenerateCredentialReportResponseTypeDef",
    {
        "State": ReportStateTypeType,
        "Description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GenerateOrganizationsAccessReportResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GenerateServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GenerateServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessKeyLastUsedResponseTypeDef = TypedDict(
    "GetAccessKeyLastUsedResponseTypeDef",
    {
        "UserName": str,
        "AccessKeyLastUsed": AccessKeyLastUsedTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountSummaryResponseTypeDef = TypedDict(
    "GetAccountSummaryResponseTypeDef",
    {
        "SummaryMap": Dict[SummaryKeyTypeType, int],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetContextKeysForPolicyResponseTypeDef = TypedDict(
    "GetContextKeysForPolicyResponseTypeDef",
    {
        "ContextKeyNames": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCredentialReportResponseTypeDef = TypedDict(
    "GetCredentialReportResponseTypeDef",
    {
        "Content": bytes,
        "ReportFormat": Literal["text/csv"],
        "GeneratedTime": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetMFADeviceResponseTypeDef = TypedDict(
    "GetMFADeviceResponseTypeDef",
    {
        "UserName": str,
        "SerialNumber": str,
        "EnableDate": datetime,
        "Certifications": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccessKeysResponseTypeDef = TypedDict(
    "ListAccessKeysResponseTypeDef",
    {
        "AccessKeyMetadata": List[AccessKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAccountAliasesResponseTypeDef = TypedDict(
    "ListAccountAliasesResponseTypeDef",
    {
        "AccountAliases": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttachedGroupPoliciesResponseTypeDef = TypedDict(
    "ListAttachedGroupPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[AttachedPolicyTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttachedRolePoliciesResponseTypeDef = TypedDict(
    "ListAttachedRolePoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[AttachedPolicyTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListAttachedUserPoliciesResponseTypeDef = TypedDict(
    "ListAttachedUserPoliciesResponseTypeDef",
    {
        "AttachedPolicies": List[AttachedPolicyTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupPoliciesResponseTypeDef = TypedDict(
    "ListGroupPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRolePoliciesResponseTypeDef = TypedDict(
    "ListRolePoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserPoliciesResponseTypeDef = TypedDict(
    "ListUserPoliciesResponseTypeDef",
    {
        "PolicyNames": List[str],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateSAMLProviderResponseTypeDef = TypedDict(
    "UpdateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateGroupResponseTypeDef = TypedDict(
    "CreateGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsForUserResponseTypeDef = TypedDict(
    "ListGroupsForUserResponseTypeDef",
    {
        "Groups": List[GroupTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListGroupsResponseTypeDef = TypedDict(
    "ListGroupsResponseTypeDef",
    {
        "Groups": List[GroupTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceProfileRequestRequestTypeDef = TypedDict(
    "CreateInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef = TypedDict(
    "CreateInstanceProfileRequestServiceResourceCreateInstanceProfileTypeDef",
    {
        "InstanceProfileName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "CreateOpenIDConnectProviderRequestRequestTypeDef",
    {
        "Url": str,
        "ClientIDList": NotRequired[Sequence[str]],
        "ThumbprintList": NotRequired[Sequence[str]],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateOpenIDConnectProviderResponseTypeDef = TypedDict(
    "CreateOpenIDConnectProviderResponseTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreatePolicyRequestRequestTypeDef = TypedDict(
    "CreatePolicyRequestRequestTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreatePolicyRequestServiceResourceCreatePolicyTypeDef = TypedDict(
    "CreatePolicyRequestServiceResourceCreatePolicyTypeDef",
    {
        "PolicyName": str,
        "PolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRoleRequestRequestTypeDef = TypedDict(
    "CreateRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateRoleRequestServiceResourceCreateRoleTypeDef = TypedDict(
    "CreateRoleRequestServiceResourceCreateRoleTypeDef",
    {
        "RoleName": str,
        "AssumeRolePolicyDocument": str,
        "Path": NotRequired[str],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSAMLProviderRequestRequestTypeDef = TypedDict(
    "CreateSAMLProviderRequestRequestTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef = TypedDict(
    "CreateSAMLProviderRequestServiceResourceCreateSamlProviderTypeDef",
    {
        "SAMLMetadataDocument": str,
        "Name": str,
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateSAMLProviderResponseTypeDef = TypedDict(
    "CreateSAMLProviderResponseTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserRequestRequestTypeDef = TypedDict(
    "CreateUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserRequestServiceResourceCreateUserTypeDef = TypedDict(
    "CreateUserRequestServiceResourceCreateUserTypeDef",
    {
        "UserName": str,
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateUserRequestUserCreateTypeDef = TypedDict(
    "CreateUserRequestUserCreateTypeDef",
    {
        "Path": NotRequired[str],
        "PermissionsBoundary": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVirtualMFADeviceRequestRequestTypeDef = TypedDict(
    "CreateVirtualMFADeviceRequestRequestTypeDef",
    {
        "VirtualMFADeviceName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef = TypedDict(
    "CreateVirtualMFADeviceRequestServiceResourceCreateVirtualMfaDeviceTypeDef",
    {
        "VirtualMFADeviceName": str,
        "Path": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
GetOpenIDConnectProviderResponseTypeDef = TypedDict(
    "GetOpenIDConnectProviderResponseTypeDef",
    {
        "Url": str,
        "ClientIDList": List[str],
        "ThumbprintList": List[str],
        "CreateDate": datetime,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSAMLProviderResponseTypeDef = TypedDict(
    "GetSAMLProviderResponseTypeDef",
    {
        "SAMLMetadataDocument": str,
        "CreateDate": datetime,
        "ValidUntil": datetime,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceProfileTagsResponseTypeDef = TypedDict(
    "ListInstanceProfileTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMFADeviceTagsResponseTypeDef = TypedDict(
    "ListMFADeviceTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOpenIDConnectProviderTagsResponseTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPolicyTagsResponseTypeDef = TypedDict(
    "ListPolicyTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListRoleTagsResponseTypeDef = TypedDict(
    "ListRoleTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSAMLProviderTagsResponseTypeDef = TypedDict(
    "ListSAMLProviderTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServerCertificateTagsResponseTypeDef = TypedDict(
    "ListServerCertificateTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUserTagsResponseTypeDef = TypedDict(
    "ListUserTagsResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyTypeDef = TypedDict(
    "PolicyTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyId": NotRequired[str],
        "Arn": NotRequired[str],
        "Path": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "AttachmentCount": NotRequired[int],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "IsAttachable": NotRequired[bool],
        "Description": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
TagInstanceProfileRequestRequestTypeDef = TypedDict(
    "TagInstanceProfileRequestRequestTypeDef",
    {
        "InstanceProfileName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagMFADeviceRequestRequestTypeDef = TypedDict(
    "TagMFADeviceRequestRequestTypeDef",
    {
        "SerialNumber": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagOpenIDConnectProviderRequestRequestTypeDef = TypedDict(
    "TagOpenIDConnectProviderRequestRequestTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagPolicyRequestRequestTypeDef = TypedDict(
    "TagPolicyRequestRequestTypeDef",
    {
        "PolicyArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagRoleRequestRequestTypeDef = TypedDict(
    "TagRoleRequestRequestTypeDef",
    {
        "RoleName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagSAMLProviderRequestRequestTypeDef = TypedDict(
    "TagSAMLProviderRequestRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagServerCertificateRequestRequestTypeDef = TypedDict(
    "TagServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
TagUserRequestRequestTypeDef = TypedDict(
    "TagUserRequestRequestTypeDef",
    {
        "UserName": str,
        "Tags": Sequence[TagTypeDef],
    },
)
UploadServerCertificateRequestRequestTypeDef = TypedDict(
    "UploadServerCertificateRequestRequestTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
        "Path": NotRequired[str],
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef = TypedDict(
    "UploadServerCertificateRequestServiceResourceCreateServerCertificateTypeDef",
    {
        "ServerCertificateName": str,
        "CertificateBody": str,
        "PrivateKey": str,
        "Path": NotRequired[str],
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
UserTypeDef = TypedDict(
    "UserTypeDef",
    {
        "Path": str,
        "UserName": str,
        "UserId": str,
        "Arn": str,
        "CreateDate": datetime,
        "PasswordLastUsed": NotRequired[datetime],
        "PermissionsBoundary": NotRequired[AttachedPermissionsBoundaryTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreateLoginProfileResponseTypeDef = TypedDict(
    "CreateLoginProfileResponseTypeDef",
    {
        "LoginProfile": LoginProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetLoginProfileResponseTypeDef = TypedDict(
    "GetLoginProfileResponseTypeDef",
    {
        "LoginProfile": LoginProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceSpecificCredentialResponseTypeDef = TypedDict(
    "CreateServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ServiceSpecificCredentialTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResetServiceSpecificCredentialResponseTypeDef = TypedDict(
    "ResetServiceSpecificCredentialResponseTypeDef",
    {
        "ServiceSpecificCredential": ServiceSpecificCredentialTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeletionTaskFailureReasonTypeTypeDef = TypedDict(
    "DeletionTaskFailureReasonTypeTypeDef",
    {
        "Reason": NotRequired[str],
        "RoleUsageList": NotRequired[List[RoleUsageTypeTypeDef]],
    },
)
EntityDetailsTypeDef = TypedDict(
    "EntityDetailsTypeDef",
    {
        "EntityInfo": EntityInfoTypeDef,
        "LastAuthenticated": NotRequired[datetime],
    },
)
GetOrganizationsAccessReportResponseTypeDef = TypedDict(
    "GetOrganizationsAccessReportResponseTypeDef",
    {
        "JobStatus": JobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "NumberOfServicesAccessible": int,
        "NumberOfServicesNotAccessed": int,
        "AccessDetails": List[AccessDetailTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ErrorDetails": ErrorDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsRequestGetAccountAuthorizationDetailsPaginateTypeDef",
    {
        "Filter": NotRequired[Sequence[EntityTypeType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetGroupRequestGetGroupPaginateTypeDef = TypedDict(
    "GetGroupRequestGetGroupPaginateTypeDef",
    {
        "GroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccessKeysRequestListAccessKeysPaginateTypeDef = TypedDict(
    "ListAccessKeysRequestListAccessKeysPaginateTypeDef",
    {
        "UserName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAccountAliasesRequestListAccountAliasesPaginateTypeDef = TypedDict(
    "ListAccountAliasesRequestListAccountAliasesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef = TypedDict(
    "ListAttachedGroupPoliciesRequestListAttachedGroupPoliciesPaginateTypeDef",
    {
        "GroupName": str,
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef = TypedDict(
    "ListAttachedRolePoliciesRequestListAttachedRolePoliciesPaginateTypeDef",
    {
        "RoleName": str,
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef = TypedDict(
    "ListAttachedUserPoliciesRequestListAttachedUserPoliciesPaginateTypeDef",
    {
        "UserName": str,
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef = TypedDict(
    "ListEntitiesForPolicyRequestListEntitiesForPolicyPaginateTypeDef",
    {
        "PolicyArn": str,
        "EntityFilter": NotRequired[EntityTypeType],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef = TypedDict(
    "ListGroupPoliciesRequestListGroupPoliciesPaginateTypeDef",
    {
        "GroupName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsForUserRequestListGroupsForUserPaginateTypeDef = TypedDict(
    "ListGroupsForUserRequestListGroupsForUserPaginateTypeDef",
    {
        "UserName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListGroupsRequestListGroupsPaginateTypeDef = TypedDict(
    "ListGroupsRequestListGroupsPaginateTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef = TypedDict(
    "ListInstanceProfileTagsRequestListInstanceProfileTagsPaginateTypeDef",
    {
        "InstanceProfileName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef = TypedDict(
    "ListInstanceProfilesForRoleRequestListInstanceProfilesForRolePaginateTypeDef",
    {
        "RoleName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef = TypedDict(
    "ListInstanceProfilesRequestListInstanceProfilesPaginateTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef = TypedDict(
    "ListMFADeviceTagsRequestListMFADeviceTagsPaginateTypeDef",
    {
        "SerialNumber": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListMFADevicesRequestListMFADevicesPaginateTypeDef = TypedDict(
    "ListMFADevicesRequestListMFADevicesPaginateTypeDef",
    {
        "UserName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef = TypedDict(
    "ListOpenIDConnectProviderTagsRequestListOpenIDConnectProviderTagsPaginateTypeDef",
    {
        "OpenIDConnectProviderArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPoliciesRequestListPoliciesPaginateTypeDef = TypedDict(
    "ListPoliciesRequestListPoliciesPaginateTypeDef",
    {
        "Scope": NotRequired[PolicyScopeTypeType],
        "OnlyAttached": NotRequired[bool],
        "PathPrefix": NotRequired[str],
        "PolicyUsageFilter": NotRequired[PolicyUsageTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyTagsRequestListPolicyTagsPaginateTypeDef = TypedDict(
    "ListPolicyTagsRequestListPolicyTagsPaginateTypeDef",
    {
        "PolicyArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef = TypedDict(
    "ListPolicyVersionsRequestListPolicyVersionsPaginateTypeDef",
    {
        "PolicyArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRolePoliciesRequestListRolePoliciesPaginateTypeDef = TypedDict(
    "ListRolePoliciesRequestListRolePoliciesPaginateTypeDef",
    {
        "RoleName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRoleTagsRequestListRoleTagsPaginateTypeDef = TypedDict(
    "ListRoleTagsRequestListRoleTagsPaginateTypeDef",
    {
        "RoleName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListRolesRequestListRolesPaginateTypeDef = TypedDict(
    "ListRolesRequestListRolesPaginateTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef = TypedDict(
    "ListSAMLProviderTagsRequestListSAMLProviderTagsPaginateTypeDef",
    {
        "SAMLProviderArn": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef = TypedDict(
    "ListSSHPublicKeysRequestListSSHPublicKeysPaginateTypeDef",
    {
        "UserName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef = TypedDict(
    "ListServerCertificateTagsRequestListServerCertificateTagsPaginateTypeDef",
    {
        "ServerCertificateName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListServerCertificatesRequestListServerCertificatesPaginateTypeDef = TypedDict(
    "ListServerCertificatesRequestListServerCertificatesPaginateTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef = TypedDict(
    "ListSigningCertificatesRequestListSigningCertificatesPaginateTypeDef",
    {
        "UserName": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserPoliciesRequestListUserPoliciesPaginateTypeDef = TypedDict(
    "ListUserPoliciesRequestListUserPoliciesPaginateTypeDef",
    {
        "UserName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUserTagsRequestListUserTagsPaginateTypeDef = TypedDict(
    "ListUserTagsRequestListUserTagsPaginateTypeDef",
    {
        "UserName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListUsersRequestListUsersPaginateTypeDef = TypedDict(
    "ListUsersRequestListUsersPaginateTypeDef",
    {
        "PathPrefix": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef = TypedDict(
    "ListVirtualMFADevicesRequestListVirtualMFADevicesPaginateTypeDef",
    {
        "AssignmentStatus": NotRequired[AssignmentStatusTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef = TypedDict(
    "SimulateCustomPolicyRequestSimulateCustomPolicyPaginateTypeDef",
    {
        "PolicyInputList": Sequence[str],
        "ActionNames": Sequence[str],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence[ContextEntryTypeDef]],
        "ResourceHandlingOption": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef = TypedDict(
    "SimulatePrincipalPolicyRequestSimulatePrincipalPolicyPaginateTypeDef",
    {
        "PolicySourceArn": str,
        "ActionNames": Sequence[str],
        "PolicyInputList": NotRequired[Sequence[str]],
        "PermissionsBoundaryPolicyInputList": NotRequired[Sequence[str]],
        "ResourceArns": NotRequired[Sequence[str]],
        "ResourcePolicy": NotRequired[str],
        "ResourceOwner": NotRequired[str],
        "CallerArn": NotRequired[str],
        "ContextEntries": NotRequired[Sequence[ContextEntryTypeDef]],
        "ResourceHandlingOption": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAccountPasswordPolicyResponseTypeDef = TypedDict(
    "GetAccountPasswordPolicyResponseTypeDef",
    {
        "PasswordPolicy": PasswordPolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef = TypedDict(
    "GetInstanceProfileRequestInstanceProfileExistsWaitTypeDef",
    {
        "InstanceProfileName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetPolicyRequestPolicyExistsWaitTypeDef = TypedDict(
    "GetPolicyRequestPolicyExistsWaitTypeDef",
    {
        "PolicyArn": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetRoleRequestRoleExistsWaitTypeDef = TypedDict(
    "GetRoleRequestRoleExistsWaitTypeDef",
    {
        "RoleName": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetUserRequestUserExistsWaitTypeDef = TypedDict(
    "GetUserRequestUserExistsWaitTypeDef",
    {
        "UserName": NotRequired[str],
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
GetSSHPublicKeyResponseTypeDef = TypedDict(
    "GetSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": SSHPublicKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadSSHPublicKeyResponseTypeDef = TypedDict(
    "UploadSSHPublicKeyResponseTypeDef",
    {
        "SSHPublicKey": SSHPublicKeyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListEntitiesForPolicyResponseTypeDef = TypedDict(
    "ListEntitiesForPolicyResponseTypeDef",
    {
        "PolicyGroups": List[PolicyGroupTypeDef],
        "PolicyUsers": List[PolicyUserTypeDef],
        "PolicyRoles": List[PolicyRoleTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListMFADevicesResponseTypeDef = TypedDict(
    "ListMFADevicesResponseTypeDef",
    {
        "MFADevices": List[MFADeviceTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListOpenIDConnectProvidersResponseTypeDef = TypedDict(
    "ListOpenIDConnectProvidersResponseTypeDef",
    {
        "OpenIDConnectProviderList": List[OpenIDConnectProviderListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPoliciesGrantingServiceAccessEntryTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessEntryTypeDef",
    {
        "ServiceNamespace": NotRequired[str],
        "Policies": NotRequired[List[PolicyGrantingServiceAccessTypeDef]],
    },
)
ListSAMLProvidersResponseTypeDef = TypedDict(
    "ListSAMLProvidersResponseTypeDef",
    {
        "SAMLProviderList": List[SAMLProviderListEntryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSSHPublicKeysResponseTypeDef = TypedDict(
    "ListSSHPublicKeysResponseTypeDef",
    {
        "SSHPublicKeys": List[SSHPublicKeyMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServerCertificatesResponseTypeDef = TypedDict(
    "ListServerCertificatesResponseTypeDef",
    {
        "ServerCertificateMetadataList": List[ServerCertificateMetadataTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ServerCertificateTypeDef = TypedDict(
    "ServerCertificateTypeDef",
    {
        "ServerCertificateMetadata": ServerCertificateMetadataTypeDef,
        "CertificateBody": str,
        "CertificateChain": NotRequired[str],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
UploadServerCertificateResponseTypeDef = TypedDict(
    "UploadServerCertificateResponseTypeDef",
    {
        "ServerCertificateMetadata": ServerCertificateMetadataTypeDef,
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListServiceSpecificCredentialsResponseTypeDef = TypedDict(
    "ListServiceSpecificCredentialsResponseTypeDef",
    {
        "ServiceSpecificCredentials": List[ServiceSpecificCredentialMetadataTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSigningCertificatesResponseTypeDef = TypedDict(
    "ListSigningCertificatesResponseTypeDef",
    {
        "Certificates": List[SigningCertificateTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UploadSigningCertificateResponseTypeDef = TypedDict(
    "UploadSigningCertificateResponseTypeDef",
    {
        "Certificate": SigningCertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyDocumentDictTypeDef = TypedDict(
    "PolicyDocumentDictTypeDef",
    {
        "Version": str,
        "Statement": List[PolicyDocumentStatementTypeDef],
    },
)
StatementTypeDef = TypedDict(
    "StatementTypeDef",
    {
        "SourcePolicyId": NotRequired[str],
        "SourcePolicyType": NotRequired[PolicySourceTypeType],
        "StartPosition": NotRequired[PositionTypeDef],
        "EndPosition": NotRequired[PositionTypeDef],
    },
)
ServiceLastAccessedTypeDef = TypedDict(
    "ServiceLastAccessedTypeDef",
    {
        "ServiceName": str,
        "ServiceNamespace": str,
        "LastAuthenticated": NotRequired[datetime],
        "LastAuthenticatedEntity": NotRequired[str],
        "LastAuthenticatedRegion": NotRequired[str],
        "TotalAuthenticatedEntities": NotRequired[int],
        "TrackedActionsLastAccessed": NotRequired[List[TrackedActionLastAccessedTypeDef]],
    },
)
CreatePolicyResponseTypeDef = TypedDict(
    "CreatePolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPolicyResponseTypeDef = TypedDict(
    "GetPolicyResponseTypeDef",
    {
        "Policy": PolicyTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPoliciesResponseTypeDef = TypedDict(
    "ListPoliciesResponseTypeDef",
    {
        "Policies": List[PolicyTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUserResponseTypeDef = TypedDict(
    "CreateUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupResponseTypeDef = TypedDict(
    "GetGroupResponseTypeDef",
    {
        "Group": GroupTypeDef,
        "Users": List[UserTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserResponseTypeDef = TypedDict(
    "GetUserResponseTypeDef",
    {
        "User": UserTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListUsersResponseTypeDef = TypedDict(
    "ListUsersResponseTypeDef",
    {
        "Users": List[UserTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VirtualMFADeviceTypeDef = TypedDict(
    "VirtualMFADeviceTypeDef",
    {
        "SerialNumber": str,
        "Base32StringSeed": NotRequired[bytes],
        "QRCodePNG": NotRequired[bytes],
        "User": NotRequired[UserTypeDef],
        "EnableDate": NotRequired[datetime],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
GetServiceLinkedRoleDeletionStatusResponseTypeDef = TypedDict(
    "GetServiceLinkedRoleDeletionStatusResponseTypeDef",
    {
        "Status": DeletionTaskStatusTypeType,
        "Reason": DeletionTaskFailureReasonTypeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsWithEntitiesResponseTypeDef",
    {
        "JobStatus": JobStatusTypeType,
        "JobCreationDate": datetime,
        "JobCompletionDate": datetime,
        "EntityDetailsList": List[EntityDetailsTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "Error": ErrorDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPoliciesGrantingServiceAccessResponseTypeDef = TypedDict(
    "ListPoliciesGrantingServiceAccessResponseTypeDef",
    {
        "PoliciesGrantingServiceAccess": List[ListPoliciesGrantingServiceAccessEntryTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetServerCertificateResponseTypeDef = TypedDict(
    "GetServerCertificateResponseTypeDef",
    {
        "ServerCertificate": ServerCertificateTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyDocumentTypeDef = Union[str, PolicyDocumentDictTypeDef]
ResourceSpecificResultTypeDef = TypedDict(
    "ResourceSpecificResultTypeDef",
    {
        "EvalResourceName": str,
        "EvalResourceDecision": PolicyEvaluationDecisionTypeType,
        "MatchedStatements": NotRequired[List[StatementTypeDef]],
        "MissingContextValues": NotRequired[List[str]],
        "EvalDecisionDetails": NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]],
        "PermissionsBoundaryDecisionDetail": NotRequired[PermissionsBoundaryDecisionDetailTypeDef],
    },
)
GetServiceLastAccessedDetailsResponseTypeDef = TypedDict(
    "GetServiceLastAccessedDetailsResponseTypeDef",
    {
        "JobStatus": JobStatusTypeType,
        "JobType": AccessAdvisorUsageGranularityTypeType,
        "JobCreationDate": datetime,
        "ServicesLastAccessed": List[ServiceLastAccessedTypeDef],
        "JobCompletionDate": datetime,
        "IsTruncated": bool,
        "Marker": str,
        "Error": ErrorDetailsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateVirtualMFADeviceResponseTypeDef = TypedDict(
    "CreateVirtualMFADeviceResponseTypeDef",
    {
        "VirtualMFADevice": VirtualMFADeviceTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListVirtualMFADevicesResponseTypeDef = TypedDict(
    "ListVirtualMFADevicesResponseTypeDef",
    {
        "VirtualMFADevices": List[VirtualMFADeviceTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetGroupPolicyResponseTypeDef = TypedDict(
    "GetGroupPolicyResponseTypeDef",
    {
        "GroupName": str,
        "PolicyName": str,
        "PolicyDocument": PolicyDocumentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRolePolicyResponseTypeDef = TypedDict(
    "GetRolePolicyResponseTypeDef",
    {
        "RoleName": str,
        "PolicyName": str,
        "PolicyDocument": PolicyDocumentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetUserPolicyResponseTypeDef = TypedDict(
    "GetUserPolicyResponseTypeDef",
    {
        "UserName": str,
        "PolicyName": str,
        "PolicyDocument": PolicyDocumentTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PolicyDetailTypeDef = TypedDict(
    "PolicyDetailTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyDocument": NotRequired[PolicyDocumentTypeDef],
    },
)
PolicyVersionTypeDef = TypedDict(
    "PolicyVersionTypeDef",
    {
        "Document": NotRequired[PolicyDocumentTypeDef],
        "VersionId": NotRequired[str],
        "IsDefaultVersion": NotRequired[bool],
        "CreateDate": NotRequired[datetime],
    },
)
RoleTypeDef = TypedDict(
    "RoleTypeDef",
    {
        "Path": str,
        "RoleName": str,
        "RoleId": str,
        "Arn": str,
        "CreateDate": datetime,
        "AssumeRolePolicyDocument": NotRequired[PolicyDocumentTypeDef],
        "Description": NotRequired[str],
        "MaxSessionDuration": NotRequired[int],
        "PermissionsBoundary": NotRequired[AttachedPermissionsBoundaryTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "RoleLastUsed": NotRequired[RoleLastUsedTypeDef],
    },
)
EvaluationResultTypeDef = TypedDict(
    "EvaluationResultTypeDef",
    {
        "EvalActionName": str,
        "EvalDecision": PolicyEvaluationDecisionTypeType,
        "EvalResourceName": NotRequired[str],
        "MatchedStatements": NotRequired[List[StatementTypeDef]],
        "MissingContextValues": NotRequired[List[str]],
        "OrganizationsDecisionDetail": NotRequired[OrganizationsDecisionDetailTypeDef],
        "PermissionsBoundaryDecisionDetail": NotRequired[PermissionsBoundaryDecisionDetailTypeDef],
        "EvalDecisionDetails": NotRequired[Dict[str, PolicyEvaluationDecisionTypeType]],
        "ResourceSpecificResults": NotRequired[List[ResourceSpecificResultTypeDef]],
    },
)
GroupDetailTypeDef = TypedDict(
    "GroupDetailTypeDef",
    {
        "Path": NotRequired[str],
        "GroupName": NotRequired[str],
        "GroupId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "GroupPolicyList": NotRequired[List[PolicyDetailTypeDef]],
        "AttachedManagedPolicies": NotRequired[List[AttachedPolicyTypeDef]],
    },
)
UserDetailTypeDef = TypedDict(
    "UserDetailTypeDef",
    {
        "Path": NotRequired[str],
        "UserName": NotRequired[str],
        "UserId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UserPolicyList": NotRequired[List[PolicyDetailTypeDef]],
        "GroupList": NotRequired[List[str]],
        "AttachedManagedPolicies": NotRequired[List[AttachedPolicyTypeDef]],
        "PermissionsBoundary": NotRequired[AttachedPermissionsBoundaryTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
CreatePolicyVersionResponseTypeDef = TypedDict(
    "CreatePolicyVersionResponseTypeDef",
    {
        "PolicyVersion": PolicyVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetPolicyVersionResponseTypeDef = TypedDict(
    "GetPolicyVersionResponseTypeDef",
    {
        "PolicyVersion": PolicyVersionTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListPolicyVersionsResponseTypeDef = TypedDict(
    "ListPolicyVersionsResponseTypeDef",
    {
        "Versions": List[PolicyVersionTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ManagedPolicyDetailTypeDef = TypedDict(
    "ManagedPolicyDetailTypeDef",
    {
        "PolicyName": NotRequired[str],
        "PolicyId": NotRequired[str],
        "Arn": NotRequired[str],
        "Path": NotRequired[str],
        "DefaultVersionId": NotRequired[str],
        "AttachmentCount": NotRequired[int],
        "PermissionsBoundaryUsageCount": NotRequired[int],
        "IsAttachable": NotRequired[bool],
        "Description": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "UpdateDate": NotRequired[datetime],
        "PolicyVersionList": NotRequired[List[PolicyVersionTypeDef]],
    },
)
CreateRoleResponseTypeDef = TypedDict(
    "CreateRoleResponseTypeDef",
    {
        "Role": RoleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateServiceLinkedRoleResponseTypeDef = TypedDict(
    "CreateServiceLinkedRoleResponseTypeDef",
    {
        "Role": RoleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRoleResponseTypeDef = TypedDict(
    "GetRoleResponseTypeDef",
    {
        "Role": RoleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
InstanceProfileTypeDef = TypedDict(
    "InstanceProfileTypeDef",
    {
        "Path": str,
        "InstanceProfileName": str,
        "InstanceProfileId": str,
        "Arn": str,
        "CreateDate": datetime,
        "Roles": List[RoleTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
    },
)
ListRolesResponseTypeDef = TypedDict(
    "ListRolesResponseTypeDef",
    {
        "Roles": List[RoleTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateRoleDescriptionResponseTypeDef = TypedDict(
    "UpdateRoleDescriptionResponseTypeDef",
    {
        "Role": RoleTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SimulatePolicyResponseTypeDef = TypedDict(
    "SimulatePolicyResponseTypeDef",
    {
        "EvaluationResults": List[EvaluationResultTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateInstanceProfileResponseTypeDef = TypedDict(
    "CreateInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetInstanceProfileResponseTypeDef = TypedDict(
    "GetInstanceProfileResponseTypeDef",
    {
        "InstanceProfile": InstanceProfileTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceProfilesForRoleResponseTypeDef = TypedDict(
    "ListInstanceProfilesForRoleResponseTypeDef",
    {
        "InstanceProfiles": List[InstanceProfileTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListInstanceProfilesResponseTypeDef = TypedDict(
    "ListInstanceProfilesResponseTypeDef",
    {
        "InstanceProfiles": List[InstanceProfileTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RoleDetailTypeDef = TypedDict(
    "RoleDetailTypeDef",
    {
        "Path": NotRequired[str],
        "RoleName": NotRequired[str],
        "RoleId": NotRequired[str],
        "Arn": NotRequired[str],
        "CreateDate": NotRequired[datetime],
        "AssumeRolePolicyDocument": NotRequired[PolicyDocumentTypeDef],
        "InstanceProfileList": NotRequired[List[InstanceProfileTypeDef]],
        "RolePolicyList": NotRequired[List[PolicyDetailTypeDef]],
        "AttachedManagedPolicies": NotRequired[List[AttachedPolicyTypeDef]],
        "PermissionsBoundary": NotRequired[AttachedPermissionsBoundaryTypeDef],
        "Tags": NotRequired[List[TagTypeDef]],
        "RoleLastUsed": NotRequired[RoleLastUsedTypeDef],
    },
)
GetAccountAuthorizationDetailsResponseTypeDef = TypedDict(
    "GetAccountAuthorizationDetailsResponseTypeDef",
    {
        "UserDetailList": List[UserDetailTypeDef],
        "GroupDetailList": List[GroupDetailTypeDef],
        "RoleDetailList": List[RoleDetailTypeDef],
        "Policies": List[ManagedPolicyDetailTypeDef],
        "IsTruncated": bool,
        "Marker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
