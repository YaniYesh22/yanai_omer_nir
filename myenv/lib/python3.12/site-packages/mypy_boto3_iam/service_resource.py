"""
Type annotations for iam service ServiceResource

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_iam.service_resource import IAMServiceResource
    import mypy_boto3_iam.service_resource as iam_resources

    session = Session()
    resource: IAMServiceResource = session.resource("iam")

    my_access_key: iam_resources.AccessKey = resource.AccessKey(...)
    my_access_key_pair: iam_resources.AccessKeyPair = resource.AccessKeyPair(...)
    my_account_password_policy: iam_resources.AccountPasswordPolicy = resource.AccountPasswordPolicy(...)
    my_account_summary: iam_resources.AccountSummary = resource.AccountSummary(...)
    my_assume_role_policy: iam_resources.AssumeRolePolicy = resource.AssumeRolePolicy(...)
    my_current_user: iam_resources.CurrentUser = resource.CurrentUser(...)
    my_group: iam_resources.Group = resource.Group(...)
    my_group_policy: iam_resources.GroupPolicy = resource.GroupPolicy(...)
    my_instance_profile: iam_resources.InstanceProfile = resource.InstanceProfile(...)
    my_login_profile: iam_resources.LoginProfile = resource.LoginProfile(...)
    my_mfa_device: iam_resources.MfaDevice = resource.MfaDevice(...)
    my_policy: iam_resources.Policy = resource.Policy(...)
    my_policy_version: iam_resources.PolicyVersion = resource.PolicyVersion(...)
    my_role: iam_resources.Role = resource.Role(...)
    my_role_policy: iam_resources.RolePolicy = resource.RolePolicy(...)
    my_saml_provider: iam_resources.SamlProvider = resource.SamlProvider(...)
    my_server_certificate: iam_resources.ServerCertificate = resource.ServerCertificate(...)
    my_signing_certificate: iam_resources.SigningCertificate = resource.SigningCertificate(...)
    my_user: iam_resources.User = resource.User(...)
    my_user_policy: iam_resources.UserPolicy = resource.UserPolicy(...)
    my_virtual_mfa_device: iam_resources.VirtualMfaDevice = resource.VirtualMfaDevice(...)
```
"""

from datetime import datetime
from typing import Dict, Iterator, List, Sequence

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import IAMClient
from .literals import (
    AssignmentStatusTypeType,
    EntityTypeType,
    PolicyScopeTypeType,
    PolicyUsageTypeType,
    StatusTypeType,
    SummaryKeyTypeType,
)
from .type_defs import (
    AttachedPermissionsBoundaryTypeDef,
    PolicyDocumentTypeDef,
    RoleLastUsedTypeDef,
    RoleTypeDef,
    ServerCertificateMetadataTypeDef,
    TagTypeDef,
    UpdateSAMLProviderResponseTypeDef,
    UserTypeDef,
)

__all__ = (
    "IAMServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
    """

    def all(self) -> "ServiceResourceGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "ServiceResourceGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def limit(self, count: int) -> "ServiceResourceGroupsCollection":
        """
        Return at most this many Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceGroupsCollection":
        """
        Fetch at most this many Groups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def pages(self) -> Iterator[List["Group"]]:
        """
        A generator which yields pages of Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """

    def __iter__(self) -> Iterator["Group"]:
        """
        A generator which yields Groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.groups)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcegroupscollection)
        """


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
    """

    def all(self) -> "ServiceResourceInstanceProfilesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "ServiceResourceInstanceProfilesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def limit(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        """
        Return at most this many InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceInstanceProfilesCollection":
        """
        Fetch at most this many InstanceProfiles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        """
        A generator which yields pages of InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """

    def __iter__(self) -> Iterator["InstanceProfile"]:
        """
        A generator which yields InstanceProfiles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.instance_profiles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceinstanceprofilescollection)
        """


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
    """

    def all(self) -> "ServiceResourcePoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        Scope: PolicyScopeTypeType = ...,
        OnlyAttached: bool = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> "ServiceResourcePoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def limit(self, count: int) -> "ServiceResourcePoliciesCollection":
        """
        Return at most this many Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def page_size(self, count: int) -> "ServiceResourcePoliciesCollection":
        """
        Fetch at most this many Policys per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def pages(self) -> Iterator[List["Policy"]]:
        """
        A generator which yields pages of Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """

    def __iter__(self) -> Iterator["Policy"]:
        """
        A generator which yields Policys.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.policies)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcepoliciescollection)
        """


class ServiceResourceRolesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
    """

    def all(self) -> "ServiceResourceRolesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "ServiceResourceRolesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def limit(self, count: int) -> "ServiceResourceRolesCollection":
        """
        Return at most this many Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceRolesCollection":
        """
        Fetch at most this many Roles per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def pages(self) -> Iterator[List["Role"]]:
        """
        A generator which yields pages of Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """

    def __iter__(self) -> Iterator["Role"]:
        """
        A generator which yields Roles.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.roles)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcerolescollection)
        """


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
    """

    def all(self) -> "ServiceResourceSamlProvidersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def filter(self) -> "ServiceResourceSamlProvidersCollection":  # type: ignore
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def limit(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        """
        Return at most this many SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceSamlProvidersCollection":
        """
        Fetch at most this many SamlProviders per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def pages(self) -> Iterator[List["SamlProvider"]]:
        """
        A generator which yields pages of SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """

    def __iter__(self) -> Iterator["SamlProvider"]:
        """
        A generator which yields SamlProviders.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.saml_providers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcesamlproviderscollection)
        """


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
    """

    def all(self) -> "ServiceResourceServerCertificatesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "ServiceResourceServerCertificatesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def limit(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        """
        Return at most this many ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceServerCertificatesCollection":
        """
        Fetch at most this many ServerCertificates per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def pages(self) -> Iterator[List["ServerCertificate"]]:
        """
        A generator which yields pages of ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """

    def __iter__(self) -> Iterator["ServerCertificate"]:
        """
        A generator which yields ServerCertificates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.server_certificates)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceservercertificatescollection)
        """


class ServiceResourceUsersCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
    """

    def all(self) -> "ServiceResourceUsersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "ServiceResourceUsersCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def limit(self, count: int) -> "ServiceResourceUsersCollection":
        """
        Return at most this many Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def page_size(self, count: int) -> "ServiceResourceUsersCollection":
        """
        Fetch at most this many Users per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def pages(self) -> Iterator[List["User"]]:
        """
        A generator which yields pages of Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """

    def __iter__(self) -> Iterator["User"]:
        """
        A generator which yields Users.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.users)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourceuserscollection)
        """


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
    """

    def all(self) -> "ServiceResourceVirtualMfaDevicesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def filter(  # type: ignore
        self,
        *,
        AssignmentStatus: AssignmentStatusTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> "ServiceResourceVirtualMfaDevicesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def limit(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        """
        Return at most this many VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def page_size(self, count: int) -> "ServiceResourceVirtualMfaDevicesCollection":
        """
        Fetch at most this many VirtualMfaDevices per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def pages(self) -> Iterator[List["VirtualMfaDevice"]]:
        """
        A generator which yields pages of VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """

    def __iter__(self) -> Iterator["VirtualMfaDevice"]:
        """
        A generator which yields VirtualMfaDevices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.virtual_mfa_devices)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#serviceresourcevirtualmfadevicescollection)
        """


class CurrentUserAccessKeysCollection(ResourceCollection):
    def all(self) -> "CurrentUserAccessKeysCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "CurrentUserAccessKeysCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "CurrentUserAccessKeysCollection":
        """
        Return at most this many AccessKeys.
        """

    def page_size(self, count: int) -> "CurrentUserAccessKeysCollection":
        """
        Fetch at most this many AccessKeys per service request.
        """

    def pages(self) -> Iterator[List["AccessKey"]]:
        """
        A generator which yields pages of AccessKeys.
        """

    def __iter__(self) -> Iterator["AccessKey"]:
        """
        A generator which yields AccessKeys.
        """


class CurrentUserMfaDevicesCollection(ResourceCollection):
    def all(self) -> "CurrentUserMfaDevicesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "CurrentUserMfaDevicesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "CurrentUserMfaDevicesCollection":
        """
        Return at most this many MfaDevices.
        """

    def page_size(self, count: int) -> "CurrentUserMfaDevicesCollection":
        """
        Fetch at most this many MfaDevices per service request.
        """

    def pages(self) -> Iterator[List["MfaDevice"]]:
        """
        A generator which yields pages of MfaDevices.
        """

    def __iter__(self) -> Iterator["MfaDevice"]:
        """
        A generator which yields MfaDevices.
        """


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    def all(self) -> "CurrentUserSigningCertificatesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "CurrentUserSigningCertificatesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        """
        Return at most this many SigningCertificates.
        """

    def page_size(self, count: int) -> "CurrentUserSigningCertificatesCollection":
        """
        Fetch at most this many SigningCertificates per service request.
        """

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        """
        A generator which yields pages of SigningCertificates.
        """

    def __iter__(self) -> Iterator["SigningCertificate"]:
        """
        A generator which yields SigningCertificates.
        """


class GroupAttachedPoliciesCollection(ResourceCollection):
    def all(self) -> "GroupAttachedPoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "GroupAttachedPoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "GroupAttachedPoliciesCollection":
        """
        Return at most this many Policys.
        """

    def page_size(self, count: int) -> "GroupAttachedPoliciesCollection":
        """
        Fetch at most this many Policys per service request.
        """

    def pages(self) -> Iterator[List["Policy"]]:
        """
        A generator which yields pages of Policys.
        """

    def __iter__(self) -> Iterator["Policy"]:
        """
        A generator which yields Policys.
        """


class GroupPoliciesCollection(ResourceCollection):
    def all(self) -> "GroupPoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "GroupPoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "GroupPoliciesCollection":
        """
        Return at most this many GroupPolicys.
        """

    def page_size(self, count: int) -> "GroupPoliciesCollection":
        """
        Fetch at most this many GroupPolicys per service request.
        """

    def pages(self) -> Iterator[List["GroupPolicy"]]:
        """
        A generator which yields pages of GroupPolicys.
        """

    def __iter__(self) -> Iterator["GroupPolicy"]:
        """
        A generator which yields GroupPolicys.
        """


class GroupUsersCollection(ResourceCollection):
    def all(self) -> "GroupUsersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "GroupUsersCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "GroupUsersCollection":
        """
        Return at most this many Users.
        """

    def page_size(self, count: int) -> "GroupUsersCollection":
        """
        Fetch at most this many Users per service request.
        """

    def pages(self) -> Iterator[List["User"]]:
        """
        A generator which yields pages of Users.
        """

    def __iter__(self) -> Iterator["User"]:
        """
        A generator which yields Users.
        """


class PolicyAttachedGroupsCollection(ResourceCollection):
    def all(self) -> "PolicyAttachedGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> "PolicyAttachedGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "PolicyAttachedGroupsCollection":
        """
        Return at most this many Groups.
        """

    def page_size(self, count: int) -> "PolicyAttachedGroupsCollection":
        """
        Fetch at most this many Groups per service request.
        """

    def pages(self) -> Iterator[List["Group"]]:
        """
        A generator which yields pages of Groups.
        """

    def __iter__(self) -> Iterator["Group"]:
        """
        A generator which yields Groups.
        """


class PolicyAttachedRolesCollection(ResourceCollection):
    def all(self) -> "PolicyAttachedRolesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> "PolicyAttachedRolesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "PolicyAttachedRolesCollection":
        """
        Return at most this many Roles.
        """

    def page_size(self, count: int) -> "PolicyAttachedRolesCollection":
        """
        Fetch at most this many Roles per service request.
        """

    def pages(self) -> Iterator[List["Role"]]:
        """
        A generator which yields pages of Roles.
        """

    def __iter__(self) -> Iterator["Role"]:
        """
        A generator which yields Roles.
        """


class PolicyAttachedUsersCollection(ResourceCollection):
    def all(self) -> "PolicyAttachedUsersCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self,
        *,
        EntityFilter: EntityTypeType = ...,
        PathPrefix: str = ...,
        PolicyUsageFilter: PolicyUsageTypeType = ...,
        Marker: str = ...,
        MaxItems: int = ...,
    ) -> "PolicyAttachedUsersCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "PolicyAttachedUsersCollection":
        """
        Return at most this many Users.
        """

    def page_size(self, count: int) -> "PolicyAttachedUsersCollection":
        """
        Fetch at most this many Users per service request.
        """

    def pages(self) -> Iterator[List["User"]]:
        """
        A generator which yields pages of Users.
        """

    def __iter__(self) -> Iterator["User"]:
        """
        A generator which yields Users.
        """


class PolicyVersionsCollection(ResourceCollection):
    def all(self) -> "PolicyVersionsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "PolicyVersionsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "PolicyVersionsCollection":
        """
        Return at most this many PolicyVersions.
        """

    def page_size(self, count: int) -> "PolicyVersionsCollection":
        """
        Fetch at most this many PolicyVersions per service request.
        """

    def pages(self) -> Iterator[List["PolicyVersion"]]:
        """
        A generator which yields pages of PolicyVersions.
        """

    def __iter__(self) -> Iterator["PolicyVersion"]:
        """
        A generator which yields PolicyVersions.
        """


class RoleAttachedPoliciesCollection(ResourceCollection):
    def all(self) -> "RoleAttachedPoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "RoleAttachedPoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "RoleAttachedPoliciesCollection":
        """
        Return at most this many Policys.
        """

    def page_size(self, count: int) -> "RoleAttachedPoliciesCollection":
        """
        Fetch at most this many Policys per service request.
        """

    def pages(self) -> Iterator[List["Policy"]]:
        """
        A generator which yields pages of Policys.
        """

    def __iter__(self) -> Iterator["Policy"]:
        """
        A generator which yields Policys.
        """


class RoleInstanceProfilesCollection(ResourceCollection):
    def all(self) -> "RoleInstanceProfilesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "RoleInstanceProfilesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "RoleInstanceProfilesCollection":
        """
        Return at most this many InstanceProfiles.
        """

    def page_size(self, count: int) -> "RoleInstanceProfilesCollection":
        """
        Fetch at most this many InstanceProfiles per service request.
        """

    def pages(self) -> Iterator[List["InstanceProfile"]]:
        """
        A generator which yields pages of InstanceProfiles.
        """

    def __iter__(self) -> Iterator["InstanceProfile"]:
        """
        A generator which yields InstanceProfiles.
        """


class RolePoliciesCollection(ResourceCollection):
    def all(self) -> "RolePoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "RolePoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "RolePoliciesCollection":
        """
        Return at most this many RolePolicys.
        """

    def page_size(self, count: int) -> "RolePoliciesCollection":
        """
        Fetch at most this many RolePolicys per service request.
        """

    def pages(self) -> Iterator[List["RolePolicy"]]:
        """
        A generator which yields pages of RolePolicys.
        """

    def __iter__(self) -> Iterator["RolePolicy"]:
        """
        A generator which yields RolePolicys.
        """


class UserAccessKeysCollection(ResourceCollection):
    def all(self) -> "UserAccessKeysCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "UserAccessKeysCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserAccessKeysCollection":
        """
        Return at most this many AccessKeys.
        """

    def page_size(self, count: int) -> "UserAccessKeysCollection":
        """
        Fetch at most this many AccessKeys per service request.
        """

    def pages(self) -> Iterator[List["AccessKey"]]:
        """
        A generator which yields pages of AccessKeys.
        """

    def __iter__(self) -> Iterator["AccessKey"]:
        """
        A generator which yields AccessKeys.
        """


class UserAttachedPoliciesCollection(ResourceCollection):
    def all(self) -> "UserAttachedPoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, PathPrefix: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "UserAttachedPoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserAttachedPoliciesCollection":
        """
        Return at most this many Policys.
        """

    def page_size(self, count: int) -> "UserAttachedPoliciesCollection":
        """
        Fetch at most this many Policys per service request.
        """

    def pages(self) -> Iterator[List["Policy"]]:
        """
        A generator which yields pages of Policys.
        """

    def __iter__(self) -> Iterator["Policy"]:
        """
        A generator which yields Policys.
        """


class UserGroupsCollection(ResourceCollection):
    def all(self) -> "UserGroupsCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "UserGroupsCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserGroupsCollection":
        """
        Return at most this many Groups.
        """

    def page_size(self, count: int) -> "UserGroupsCollection":
        """
        Fetch at most this many Groups per service request.
        """

    def pages(self) -> Iterator[List["Group"]]:
        """
        A generator which yields pages of Groups.
        """

    def __iter__(self) -> Iterator["Group"]:
        """
        A generator which yields Groups.
        """


class UserMfaDevicesCollection(ResourceCollection):
    def all(self) -> "UserMfaDevicesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "UserMfaDevicesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserMfaDevicesCollection":
        """
        Return at most this many MfaDevices.
        """

    def page_size(self, count: int) -> "UserMfaDevicesCollection":
        """
        Fetch at most this many MfaDevices per service request.
        """

    def pages(self) -> Iterator[List["MfaDevice"]]:
        """
        A generator which yields pages of MfaDevices.
        """

    def __iter__(self) -> Iterator["MfaDevice"]:
        """
        A generator which yields MfaDevices.
        """


class UserPoliciesCollection(ResourceCollection):
    def all(self) -> "UserPoliciesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, Marker: str = ..., MaxItems: int = ...
    ) -> "UserPoliciesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserPoliciesCollection":
        """
        Return at most this many UserPolicys.
        """

    def page_size(self, count: int) -> "UserPoliciesCollection":
        """
        Fetch at most this many UserPolicys per service request.
        """

    def pages(self) -> Iterator[List["UserPolicy"]]:
        """
        A generator which yields pages of UserPolicys.
        """

    def __iter__(self) -> Iterator["UserPolicy"]:
        """
        A generator which yields UserPolicys.
        """


class UserSigningCertificatesCollection(ResourceCollection):
    def all(self) -> "UserSigningCertificatesCollection":
        """
        Get all items from the collection, optionally with a custom page size and item count limit.
        """

    def filter(  # type: ignore
        self, *, UserName: str = ..., Marker: str = ..., MaxItems: int = ...
    ) -> "UserSigningCertificatesCollection":
        """
        Get items from the collection, passing keyword arguments along as parameters to the underlying service operation, which are typically used to filter the results.
        """

    def limit(self, count: int) -> "UserSigningCertificatesCollection":
        """
        Return at most this many SigningCertificates.
        """

    def page_size(self, count: int) -> "UserSigningCertificatesCollection":
        """
        Fetch at most this many SigningCertificates per service request.
        """

    def pages(self) -> Iterator[List["SigningCertificate"]]:
        """
        A generator which yields pages of SigningCertificates.
        """

    def __iter__(self) -> Iterator["SigningCertificate"]:
        """
        A generator which yields SigningCertificates.
        """


class AccessKeyPair(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypair)
    """

    access_key_id: str
    status: StatusTypeType
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str
    meta: "IAMResourceMeta"

    def activate(self, *, Status: StatusTypeType = "Active") -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.activate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairactivate-method)
        """

    def deactivate(self, *, Status: StatusTypeType = "Inactive") -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.deactivate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairdeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairdelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKeyPair.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeypairget_available_subresources-method)
        """


_AccessKeyPair = AccessKeyPair


class AccountPasswordPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicy)
    """

    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool
    meta: "IAMResourceMeta"

    def delete(self) -> None:
        """
        Deletes the password policy for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicydelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_password_policy` to update the
        attributes of the AccountPasswordPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_password_policy` to update the
        attributes of the AccountPasswordPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyreload-method)
        """

    def update(
        self,
        *,
        MinimumPasswordLength: int = ...,
        RequireSymbols: bool = ...,
        RequireNumbers: bool = ...,
        RequireUppercaseCharacters: bool = ...,
        RequireLowercaseCharacters: bool = ...,
        AllowUsersToChangePassword: bool = ...,
        MaxPasswordAge: int = ...,
        PasswordReusePrevention: int = ...,
        HardExpiry: bool = ...,
    ) -> None:
        """
        Updates the password policy settings for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountPasswordPolicy.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountpasswordpolicyupdate-method)
        """


_AccountPasswordPolicy = AccountPasswordPolicy


class AccountSummary(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummary)
    """

    summary_map: Dict[SummaryKeyTypeType, int]
    meta: "IAMResourceMeta"

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_summary` to update the attributes of the
        AccountSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_summary` to update the attributes of the
        AccountSummary
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccountSummary.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accountsummaryreload-method)
        """


_AccountSummary = AccountSummary


class CurrentUser(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuser)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    user: "User"
    access_keys: CurrentUserAccessKeysCollection
    mfa_devices: CurrentUserMfaDevicesCollection
    signing_certificates: CurrentUserSigningCertificatesCollection
    meta: "IAMResourceMeta"

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the
        CurrentUser
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the
        CurrentUser
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.CurrentUser.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#currentuserreload-method)
        """


_CurrentUser = CurrentUser


class InstanceProfile(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofile)
    """

    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[RoleTypeDef]
    tags: List[TagTypeDef]
    name: str
    roles: List["Role"]
    meta: "IAMResourceMeta"

    def add_role(self, *, RoleName: str) -> None:
        """
        Adds the specified IAM role to the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.add_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileadd_role-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofiledelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_instance_profile` to update the attributes of
        the InstanceProfile
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_instance_profile` to update the attributes of
        the InstanceProfile
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofilereload-method)
        """

    def remove_role(self, *, RoleName: str) -> None:
        """
        Removes the specified IAM role from the specified Amazon EC2 instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.InstanceProfile.remove_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#instanceprofileremove_role-method)
        """


_InstanceProfile = InstanceProfile


class PolicyVersion(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversion)
    """

    document: PolicyDocumentTypeDef
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str
    meta: "IAMResourceMeta"

    def delete(self) -> None:
        """
        Deletes the specified version from the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversiondelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy_version` to update the attributes of the
        PolicyVersion
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy_version` to update the attributes of the
        PolicyVersion
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionreload-method)
        """

    def set_as_default(self) -> None:
        """
        Sets the specified version of the specified policy as the policy's default
        (operative)
        version.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.PolicyVersion.set_as_default)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyversionset_as_default-method)
        """


_PolicyVersion = PolicyVersion


class SamlProvider(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlprovider)
    """

    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    tags: List[TagTypeDef]
    arn: str
    meta: "IAMResourceMeta"

    def delete(self) -> None:
        """
        Deletes a SAML provider resource in IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderdelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_saml_provider` to update the attributes of the
        SamlProvider
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_saml_provider` to update the attributes of the
        SamlProvider
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderreload-method)
        """

    def update(self, *, SAMLMetadataDocument: str) -> UpdateSAMLProviderResponseTypeDef:
        """
        Updates the metadata document for an existing SAML provider resource object.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SamlProvider.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#samlproviderupdate-method)
        """


_SamlProvider = SamlProvider


class VirtualMfaDevice(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadevice)
    """

    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: UserTypeDef
    enable_date: datetime
    tags: List[TagTypeDef]
    serial_number: str
    user: "User"
    meta: "IAMResourceMeta"

    def delete(self) -> None:
        """
        Deletes a virtual MFA device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.VirtualMfaDevice.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadevicedelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.VirtualMfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#virtualmfadeviceget_available_subresources-method)
        """


_VirtualMfaDevice = VirtualMfaDevice


class AccessKey(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKey)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskey)
    """

    access_key_id: str
    status: StatusTypeType
    create_date: datetime
    user_name: str
    id: str
    meta: "IAMResourceMeta"

    def User(self) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyuser-method)
        """

    def activate(self, *, Status: StatusTypeType = "Active") -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.activate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyactivate-method)
        """

    def deactivate(self, *, Status: StatusTypeType = "Inactive") -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.deactivate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeydeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeydelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AccessKey.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#accesskeyget_available_subresources-method)
        """


_AccessKey = AccessKey


class AssumeRolePolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicy)
    """

    role_name: str
    meta: "IAMResourceMeta"

    def Role(self) -> "_Role":
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.Role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyrole-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyget_available_subresources-method)
        """

    def update(self, *, PolicyDocument: str) -> None:
        """
        Updates the policy that grants an IAM entity permission to assume a role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.AssumeRolePolicy.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#assumerolepolicyupdate-method)
        """


_AssumeRolePolicy = AssumeRolePolicy


class GroupPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicy)
    """

    policy_name: str
    policy_document: PolicyDocumentTypeDef
    group_name: str
    name: str
    meta: "IAMResourceMeta"

    def Group(self) -> "_Group":
        """
        Creates a Group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.Group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicygroup-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicydelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group_policy` to update the attributes of the
        GroupPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyload-method)
        """

    def put(self, *, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.put)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyput-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group_policy` to update the attributes of the
        GroupPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.GroupPolicy.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicyreload-method)
        """


_GroupPolicy = GroupPolicy


class MfaDevice(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadevice)
    """

    enable_date: datetime
    user_name: str
    serial_number: str
    meta: "IAMResourceMeta"

    def User(self) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceuser-method)
        """

    def associate(self, *, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        Enables the specified MFA device and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.associate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceassociate-method)
        """

    def disassociate(self) -> None:
        """
        Deactivates the specified MFA device and removes it from association with the
        user name for which it was originally
        enabled.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.disassociate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadevicedisassociate-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceget_available_subresources-method)
        """

    def resync(self, *, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        Synchronizes the specified MFA device with its IAM resource object on the
        Amazon Web Services
        servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.MfaDevice.resync)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#mfadeviceresync-method)
        """


_MfaDevice = MfaDevice


class Policy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Policy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policy)
    """

    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    tags: List[TagTypeDef]
    arn: str
    default_version: "PolicyVersion"
    attached_groups: PolicyAttachedGroupsCollection
    attached_roles: PolicyAttachedRolesCollection
    attached_users: PolicyAttachedUsersCollection
    versions: PolicyVersionsCollection
    meta: "IAMResourceMeta"

    def attach_group(self, *, GroupName: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_group-method)
        """

    def attach_role(self, *, RoleName: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_role-method)
        """

    def attach_user(self, *, UserName: str) -> None:
        """
        Attaches the specified managed policy to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.attach_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyattach_user-method)
        """

    def create_version(self, *, PolicyDocument: str, SetAsDefault: bool = ...) -> "_PolicyVersion":
        """
        Creates a new version of the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.create_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policycreate_version-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified managed policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydelete-method)
        """

    def detach_group(self, *, GroupName: str) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_group-method)
        """

    def detach_role(self, *, RoleName: str) -> None:
        """
        Removes the specified managed policy from the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_role-method)
        """

    def detach_user(self, *, UserName: str) -> None:
        """
        Removes the specified managed policy from the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.detach_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policydetach_user-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy` to update the attributes of the Policy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy` to update the attributes of the Policy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Policy.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#policyreload-method)
        """


_Policy = Policy


class RolePolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicy)
    """

    policy_name: str
    policy_document: PolicyDocumentTypeDef
    role_name: str
    name: str
    meta: "IAMResourceMeta"

    def Role(self) -> "_Role":
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.Role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyrole-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicydelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role_policy` to update the attributes of the
        RolePolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyload-method)
        """

    def put(self, *, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.put)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyput-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role_policy` to update the attributes of the
        RolePolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.RolePolicy.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicyreload-method)
        """


_RolePolicy = RolePolicy


class ServerCertificate(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificate)
    """

    server_certificate_metadata: ServerCertificateMetadataTypeDef
    certificate_body: str
    certificate_chain: str
    tags: List[TagTypeDef]
    name: str
    meta: "IAMResourceMeta"

    def delete(self) -> None:
        """
        Deletes the specified server certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificatedelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_server_certificate` to update the attributes of
        the ServerCertificate
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_server_certificate` to update the attributes of
        the ServerCertificate
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificatereload-method)
        """

    def update(
        self, *, NewPath: str = ..., NewServerCertificateName: str = ...
    ) -> "_ServerCertificate":
        """
        Updates the name and/or the path of the specified server certificate stored in
        IAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServerCertificate.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#servercertificateupdate-method)
        """


_ServerCertificate = ServerCertificate


class SigningCertificate(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificate)
    """

    certificate_id: str
    certificate_body: str
    status: StatusTypeType
    upload_date: datetime
    user_name: str
    id: str
    meta: "IAMResourceMeta"

    def User(self) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateuser-method)
        """

    def activate(self, *, Status: StatusTypeType = "Active") -> None:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.activate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateactivate-method)
        """

    def deactivate(self, *, Status: StatusTypeType = "Inactive") -> None:
        """
        Changes the status of the specified user signing certificate from active to
        disabled, or vice
        versa.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.deactivate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificatedeactivate-method)
        """

    def delete(self) -> None:
        """
        Deletes a signing certificate associated with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificatedelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.SigningCertificate.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#signingcertificateget_available_subresources-method)
        """


_SigningCertificate = SigningCertificate


class UserPolicy(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicy)
    """

    policy_name: str
    policy_document: PolicyDocumentTypeDef
    user_name: str
    name: str
    meta: "IAMResourceMeta"

    def User(self) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyuser-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicydelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user_policy` to update the attributes of the
        UserPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyload-method)
        """

    def put(self, *, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.put)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyput-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user_policy` to update the attributes of the
        UserPolicy
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.UserPolicy.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicyreload-method)
        """


_UserPolicy = UserPolicy


class Group(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Group)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#group)
    """

    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: GroupAttachedPoliciesCollection
    policies: GroupPoliciesCollection
    users: GroupUsersCollection
    meta: "IAMResourceMeta"

    def Policy(self, name: str) -> "_GroupPolicy":
        """
        Creates a GroupPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.Policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#grouppolicy-method)
        """

    def add_user(self, *, UserName: str) -> None:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.add_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupadd_user-method)
        """

    def attach_policy(self, *, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.attach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupattach_policy-method)
        """

    def create(self, *, Path: str = ...) -> "_Group":
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.create)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupcreate-method)
        """

    def create_policy(self, *, PolicyName: str, PolicyDocument: str) -> "_GroupPolicy":
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.create_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupcreate_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupdelete-method)
        """

    def detach_policy(self, *, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.detach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupdetach_policy-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group` to update the attributes of the Group
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group` to update the attributes of the Group
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupreload-method)
        """

    def remove_user(self, *, UserName: str) -> None:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.remove_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupremove_user-method)
        """

    def update(self, *, NewPath: str = ..., NewGroupName: str = ...) -> "_Group":
        """
        Updates the name and/or the path of the specified IAM group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Group.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#groupupdate-method)
        """


_Group = Group


class LoginProfile(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofile)
    """

    create_date: datetime
    password_reset_required: bool
    user_name: str
    meta: "IAMResourceMeta"

    def User(self) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileuser-method)
        """

    def create(self, *, Password: str, PasswordResetRequired: bool = ...) -> "_LoginProfile":
        """
        Creates a password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.create)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofilecreate-method)
        """

    def delete(self) -> None:
        """
        Deletes the password for the specified IAM user, For more information, see
        [Managing passwords for IAM
        users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofiledelete-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_login_profile` to update the attributes of the
        LoginProfile
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_login_profile` to update the attributes of the
        LoginProfile
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofilereload-method)
        """

    def update(self, *, Password: str = ..., PasswordResetRequired: bool = ...) -> None:
        """
        Changes the password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.LoginProfile.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#loginprofileupdate-method)
        """


_LoginProfile = LoginProfile


class Role(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Role)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#role)
    """

    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: PolicyDocumentTypeDef
    description: str
    max_session_duration: int
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    role_last_used: RoleLastUsedTypeDef
    name: str
    attached_policies: RoleAttachedPoliciesCollection
    instance_profiles: RoleInstanceProfilesCollection
    policies: RolePoliciesCollection
    meta: "IAMResourceMeta"

    def AssumeRolePolicy(self) -> "_AssumeRolePolicy":
        """
        Creates a AssumeRolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleassumerolepolicy-method)
        """

    def Policy(self, name: str) -> "_RolePolicy":
        """
        Creates a RolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.Policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolepolicy-method)
        """

    def attach_policy(self, *, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.attach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleattach_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roledelete-method)
        """

    def detach_policy(self, *, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified role.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.detach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roledetach_policy-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role` to update the attributes of the Role
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#roleload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role` to update the attributes of the Role
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.Role.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#rolereload-method)
        """


_Role = Role


class User(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.User)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#user)
    """

    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: AttachedPermissionsBoundaryTypeDef
    tags: List[TagTypeDef]
    name: str
    access_keys: UserAccessKeysCollection
    attached_policies: UserAttachedPoliciesCollection
    groups: UserGroupsCollection
    mfa_devices: UserMfaDevicesCollection
    policies: UserPoliciesCollection
    signing_certificates: UserSigningCertificatesCollection
    meta: "IAMResourceMeta"

    def AccessKey(self, id: str) -> "_AccessKey":
        """
        Creates a AccessKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.AccessKey)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useraccesskey-method)
        """

    def LoginProfile(self) -> "_LoginProfile":
        """
        Creates a LoginProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.LoginProfile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userloginprofile-method)
        """

    def MfaDevice(self, serial_number: str) -> "_MfaDevice":
        """
        Creates a MfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.MfaDevice)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usermfadevice-method)
        """

    def Policy(self, name: str) -> "_UserPolicy":
        """
        Creates a UserPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.Policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userpolicy-method)
        """

    def SigningCertificate(self, id: str) -> "_SigningCertificate":
        """
        Creates a SigningCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.SigningCertificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usersigningcertificate-method)
        """

    def add_group(self, *, GroupName: str) -> None:
        """
        Adds the specified user to the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.add_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#useradd_group-method)
        """

    def attach_policy(self, *, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.attach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userattach_policy-method)
        """

    def create(
        self, *, Path: str = ..., PermissionsBoundary: str = ..., Tags: Sequence[TagTypeDef] = ...
    ) -> "_User":
        """
        Creates a new IAM user for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate-method)
        """

    def create_access_key_pair(self) -> "_AccessKeyPair":
        """
        Creates a new Amazon Web Services secret access key and corresponding Amazon
        Web Services access key ID for the specified
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_access_key_pair)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_access_key_pair-method)
        """

    def create_login_profile(
        self, *, Password: str, PasswordResetRequired: bool = ...
    ) -> "_LoginProfile":
        """
        Creates a password for the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_login_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_login_profile-method)
        """

    def create_policy(self, *, PolicyName: str, PolicyDocument: str) -> "_UserPolicy":
        """
        Adds or updates an inline policy document that is embedded in the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.create_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#usercreate_policy-method)
        """

    def delete(self) -> None:
        """
        Deletes the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.delete)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userdelete-method)
        """

    def detach_policy(self, *, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.detach_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userdetach_policy-method)
        """

    def enable_mfa(
        self, *, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> "_MfaDevice":
        """
        Enables the specified MFA device and associates it with the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.enable_mfa)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userenable_mfa-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userget_available_subresources-method)
        """

    def load(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the User
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.load)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userload-method)
        """

    def reload(self) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the User
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.reload)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userreload-method)
        """

    def remove_group(self, *, GroupName: str) -> None:
        """
        Removes the specified user from the specified group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.remove_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userremove_group-method)
        """

    def update(self, *, NewPath: str = ..., NewUserName: str = ...) -> "_User":
        """
        Updates the name and/or the path of the specified IAM user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.User.update)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#userupdate-method)
        """


_User = User


class IAMResourceMeta(ResourceMeta):
    client: IAMClient


class IAMServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/)
    """

    meta: "IAMResourceMeta"
    groups: ServiceResourceGroupsCollection
    instance_profiles: ServiceResourceInstanceProfilesCollection
    policies: ServiceResourcePoliciesCollection
    roles: ServiceResourceRolesCollection
    saml_providers: ServiceResourceSamlProvidersCollection
    server_certificates: ServiceResourceServerCertificatesCollection
    users: ServiceResourceUsersCollection
    virtual_mfa_devices: ServiceResourceVirtualMfaDevicesCollection

    def AccessKey(self, user_name: str, id: str) -> "_AccessKey":
        """
        Creates a AccessKey resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKey)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccesskey-method)
        """

    def AccessKeyPair(self, user_name: str, id: str, secret: str) -> "_AccessKeyPair":
        """
        Creates a AccessKeyPair resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccessKeyPair)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccesskeypair-method)
        """

    def AccountPasswordPolicy(self) -> "_AccountPasswordPolicy":
        """
        Creates a AccountPasswordPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountPasswordPolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccountpasswordpolicy-method)
        """

    def AccountSummary(self) -> "_AccountSummary":
        """
        Creates a AccountSummary resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AccountSummary)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceaccountsummary-method)
        """

    def AssumeRolePolicy(self, role_name: str) -> "_AssumeRolePolicy":
        """
        Creates a AssumeRolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.AssumeRolePolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceassumerolepolicy-method)
        """

    def CurrentUser(self) -> "_CurrentUser":
        """
        Creates a CurrentUser resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.CurrentUser)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecurrentuser-method)
        """

    def Group(self, name: str) -> "_Group":
        """
        Creates a Group resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcegroup-method)
        """

    def GroupPolicy(self, group_name: str, name: str) -> "_GroupPolicy":
        """
        Creates a GroupPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.GroupPolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcegrouppolicy-method)
        """

    def InstanceProfile(self, name: str) -> "_InstanceProfile":
        """
        Creates a InstanceProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.InstanceProfile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceinstanceprofile-method)
        """

    def LoginProfile(self, user_name: str) -> "_LoginProfile":
        """
        Creates a LoginProfile resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.LoginProfile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceloginprofile-method)
        """

    def MfaDevice(self, user_name: str, serial_number: str) -> "_MfaDevice":
        """
        Creates a MfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.MfaDevice)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcemfadevice-method)
        """

    def Policy(self, arn: str) -> "_Policy":
        """
        Creates a Policy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcepolicy-method)
        """

    def PolicyVersion(self, arn: str, version_id: str) -> "_PolicyVersion":
        """
        Creates a PolicyVersion resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.PolicyVersion)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcepolicyversion-method)
        """

    def Role(self, name: str) -> "_Role":
        """
        Creates a Role resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.Role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcerole-method)
        """

    def RolePolicy(self, role_name: str, name: str) -> "_RolePolicy":
        """
        Creates a RolePolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.RolePolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcerolepolicy-method)
        """

    def SamlProvider(self, arn: str) -> "_SamlProvider":
        """
        Creates a SamlProvider resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SamlProvider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcesamlprovider-method)
        """

    def ServerCertificate(self, name: str) -> "_ServerCertificate":
        """
        Creates a ServerCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.ServerCertificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceservercertificate-method)
        """

    def SigningCertificate(self, user_name: str, id: str) -> "_SigningCertificate":
        """
        Creates a SigningCertificate resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.SigningCertificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcesigningcertificate-method)
        """

    def User(self, name: str) -> "_User":
        """
        Creates a User resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.User)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceuser-method)
        """

    def UserPolicy(self, user_name: str, name: str) -> "_UserPolicy":
        """
        Creates a UserPolicy resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.UserPolicy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceuserpolicy-method)
        """

    def VirtualMfaDevice(self, serial_number: str) -> "_VirtualMfaDevice":
        """
        Creates a VirtualMfaDevice resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.VirtualMfaDevice)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcevirtualmfadevice-method)
        """

    def change_password(self, *, OldPassword: str, NewPassword: str) -> None:
        """
        Changes the password of the IAM user who is calling this operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.change_password)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcechange_password-method)
        """

    def create_account_alias(self, *, AccountAlias: str) -> None:
        """
        Creates an alias for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_account_alias)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_account_alias-method)
        """

    def create_account_password_policy(
        self,
        *,
        MinimumPasswordLength: int = ...,
        RequireSymbols: bool = ...,
        RequireNumbers: bool = ...,
        RequireUppercaseCharacters: bool = ...,
        RequireLowercaseCharacters: bool = ...,
        AllowUsersToChangePassword: bool = ...,
        MaxPasswordAge: int = ...,
        PasswordReusePrevention: int = ...,
        HardExpiry: bool = ...,
    ) -> "_AccountPasswordPolicy":
        """
        Updates the password policy settings for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_account_password_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_account_password_policy-method)
        """

    def create_group(self, *, GroupName: str, Path: str = ...) -> "_Group":
        """
        Creates a new group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_group)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_group-method)
        """

    def create_instance_profile(
        self, *, InstanceProfileName: str, Path: str = ..., Tags: Sequence[TagTypeDef] = ...
    ) -> "_InstanceProfile":
        """
        Creates a new instance profile.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_instance_profile)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_instance_profile-method)
        """

    def create_policy(
        self,
        *,
        PolicyName: str,
        PolicyDocument: str,
        Path: str = ...,
        Description: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> "_Policy":
        """
        Creates a new managed policy for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_policy-method)
        """

    def create_role(
        self,
        *,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = ...,
        Description: str = ...,
        MaxSessionDuration: int = ...,
        PermissionsBoundary: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> "_Role":
        """
        Creates a new role for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_role-method)
        """

    def create_saml_provider(
        self, *, SAMLMetadataDocument: str, Name: str, Tags: Sequence[TagTypeDef] = ...
    ) -> "_SamlProvider":
        """
        Creates an IAM resource that describes an identity provider (IdP) that supports
        SAML
        2.0.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_saml_provider)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_saml_provider-method)
        """

    def create_server_certificate(
        self,
        *,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = ...,
        CertificateChain: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> "_ServerCertificate":
        """
        Uploads a server certificate entity for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_server_certificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_server_certificate-method)
        """

    def create_signing_certificate(
        self, *, CertificateBody: str, UserName: str = ...
    ) -> "_SigningCertificate":
        """
        Uploads an X.509 signing certificate and associates it with the specified IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_signing_certificate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_signing_certificate-method)
        """

    def create_user(
        self,
        *,
        UserName: str,
        Path: str = ...,
        PermissionsBoundary: str = ...,
        Tags: Sequence[TagTypeDef] = ...,
    ) -> "_User":
        """
        Creates a new IAM user for your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_user)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_user-method)
        """

    def create_virtual_mfa_device(
        self, *, VirtualMFADeviceName: str, Path: str = ..., Tags: Sequence[TagTypeDef] = ...
    ) -> "_VirtualMfaDevice":
        """
        Creates a new virtual MFA device for the Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.create_virtual_mfa_device)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourcecreate_virtual_mfa_device-method)
        """

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html#IAM.ServiceResource.get_available_subresources)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_iam/service_resource/#iamserviceresourceget_available_subresources-method)
        """
