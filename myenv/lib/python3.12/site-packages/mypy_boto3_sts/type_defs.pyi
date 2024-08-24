"""
Type annotations for sts service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/type_defs/)

Usage::

    ```python
    from mypy_boto3_sts.type_defs import PolicyDescriptorTypeTypeDef

    data: PolicyDescriptorTypeTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import Dict, Sequence

if sys.version_info >= (3, 12):
    from typing import NotRequired
else:
    from typing_extensions import NotRequired
if sys.version_info >= (3, 12):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "PolicyDescriptorTypeTypeDef",
    "ProvidedContextTypeDef",
    "TagTypeDef",
    "AssumedRoleUserTypeDef",
    "CredentialsTypeDef",
    "ResponseMetadataTypeDef",
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    "FederatedUserTypeDef",
    "GetAccessKeyInfoRequestRequestTypeDef",
    "GetSessionTokenRequestRequestTypeDef",
    "AssumeRoleWithSAMLRequestRequestTypeDef",
    "AssumeRoleWithWebIdentityRequestRequestTypeDef",
    "AssumeRoleRequestRequestTypeDef",
    "GetFederationTokenRequestRequestTypeDef",
    "AssumeRoleResponseTypeDef",
    "AssumeRoleWithSAMLResponseTypeDef",
    "AssumeRoleWithWebIdentityResponseTypeDef",
    "DecodeAuthorizationMessageResponseTypeDef",
    "GetAccessKeyInfoResponseTypeDef",
    "GetCallerIdentityResponseTypeDef",
    "GetSessionTokenResponseTypeDef",
    "GetFederationTokenResponseTypeDef",
)

PolicyDescriptorTypeTypeDef = TypedDict(
    "PolicyDescriptorTypeTypeDef",
    {
        "arn": NotRequired[str],
    },
)
ProvidedContextTypeDef = TypedDict(
    "ProvidedContextTypeDef",
    {
        "ProviderArn": NotRequired[str],
        "ContextAssertion": NotRequired[str],
    },
)
TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)
AssumedRoleUserTypeDef = TypedDict(
    "AssumedRoleUserTypeDef",
    {
        "AssumedRoleId": str,
        "Arn": str,
    },
)
CredentialsTypeDef = TypedDict(
    "CredentialsTypeDef",
    {
        "AccessKeyId": str,
        "SecretAccessKey": str,
        "SessionToken": str,
        "Expiration": datetime,
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
DecodeAuthorizationMessageRequestRequestTypeDef = TypedDict(
    "DecodeAuthorizationMessageRequestRequestTypeDef",
    {
        "EncodedMessage": str,
    },
)
FederatedUserTypeDef = TypedDict(
    "FederatedUserTypeDef",
    {
        "FederatedUserId": str,
        "Arn": str,
    },
)
GetAccessKeyInfoRequestRequestTypeDef = TypedDict(
    "GetAccessKeyInfoRequestRequestTypeDef",
    {
        "AccessKeyId": str,
    },
)
GetSessionTokenRequestRequestTypeDef = TypedDict(
    "GetSessionTokenRequestRequestTypeDef",
    {
        "DurationSeconds": NotRequired[int],
        "SerialNumber": NotRequired[str],
        "TokenCode": NotRequired[str],
    },
)
AssumeRoleWithSAMLRequestRequestTypeDef = TypedDict(
    "AssumeRoleWithSAMLRequestRequestTypeDef",
    {
        "RoleArn": str,
        "PrincipalArn": str,
        "SAMLAssertion": str,
        "PolicyArns": NotRequired[Sequence[PolicyDescriptorTypeTypeDef]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
    },
)
AssumeRoleWithWebIdentityRequestRequestTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "WebIdentityToken": str,
        "ProviderId": NotRequired[str],
        "PolicyArns": NotRequired[Sequence[PolicyDescriptorTypeTypeDef]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
    },
)
AssumeRoleRequestRequestTypeDef = TypedDict(
    "AssumeRoleRequestRequestTypeDef",
    {
        "RoleArn": str,
        "RoleSessionName": str,
        "PolicyArns": NotRequired[Sequence[PolicyDescriptorTypeTypeDef]],
        "Policy": NotRequired[str],
        "DurationSeconds": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "TransitiveTagKeys": NotRequired[Sequence[str]],
        "ExternalId": NotRequired[str],
        "SerialNumber": NotRequired[str],
        "TokenCode": NotRequired[str],
        "SourceIdentity": NotRequired[str],
        "ProvidedContexts": NotRequired[Sequence[ProvidedContextTypeDef]],
    },
)
GetFederationTokenRequestRequestTypeDef = TypedDict(
    "GetFederationTokenRequestRequestTypeDef",
    {
        "Name": str,
        "Policy": NotRequired[str],
        "PolicyArns": NotRequired[Sequence[PolicyDescriptorTypeTypeDef]],
        "DurationSeconds": NotRequired[int],
        "Tags": NotRequired[Sequence[TagTypeDef]],
    },
)
AssumeRoleResponseTypeDef = TypedDict(
    "AssumeRoleResponseTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "AssumedRoleUser": AssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "SourceIdentity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeRoleWithSAMLResponseTypeDef = TypedDict(
    "AssumeRoleWithSAMLResponseTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "AssumedRoleUser": AssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Subject": str,
        "SubjectType": str,
        "Issuer": str,
        "Audience": str,
        "NameQualifier": str,
        "SourceIdentity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AssumeRoleWithWebIdentityResponseTypeDef = TypedDict(
    "AssumeRoleWithWebIdentityResponseTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "SubjectFromWebIdentityToken": str,
        "AssumedRoleUser": AssumedRoleUserTypeDef,
        "PackedPolicySize": int,
        "Provider": str,
        "Audience": str,
        "SourceIdentity": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DecodeAuthorizationMessageResponseTypeDef = TypedDict(
    "DecodeAuthorizationMessageResponseTypeDef",
    {
        "DecodedMessage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetAccessKeyInfoResponseTypeDef = TypedDict(
    "GetAccessKeyInfoResponseTypeDef",
    {
        "Account": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetCallerIdentityResponseTypeDef = TypedDict(
    "GetCallerIdentityResponseTypeDef",
    {
        "UserId": str,
        "Account": str,
        "Arn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSessionTokenResponseTypeDef = TypedDict(
    "GetSessionTokenResponseTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetFederationTokenResponseTypeDef = TypedDict(
    "GetFederationTokenResponseTypeDef",
    {
        "Credentials": CredentialsTypeDef,
        "FederatedUser": FederatedUserTypeDef,
        "PackedPolicySize": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
