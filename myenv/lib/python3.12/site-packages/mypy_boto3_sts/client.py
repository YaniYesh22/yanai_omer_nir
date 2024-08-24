"""
Type annotations for sts service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_sts.client import STSClient

    session = Session()
    client: STSClient = session.client("sts")
    ```
"""

from typing import Any, Dict, Mapping, Sequence, Type

from botocore.client import BaseClient, ClientMeta

from .type_defs import (
    AssumeRoleResponseTypeDef,
    AssumeRoleWithSAMLResponseTypeDef,
    AssumeRoleWithWebIdentityResponseTypeDef,
    DecodeAuthorizationMessageResponseTypeDef,
    GetAccessKeyInfoResponseTypeDef,
    GetCallerIdentityResponseTypeDef,
    GetFederationTokenResponseTypeDef,
    GetSessionTokenResponseTypeDef,
    PolicyDescriptorTypeTypeDef,
    ProvidedContextTypeDef,
    TagTypeDef,
)

__all__ = ("STSClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    ClientError: Type[BotocoreClientError]
    ExpiredTokenException: Type[BotocoreClientError]
    IDPCommunicationErrorException: Type[BotocoreClientError]
    IDPRejectedClaimException: Type[BotocoreClientError]
    InvalidAuthorizationMessageException: Type[BotocoreClientError]
    InvalidIdentityTokenException: Type[BotocoreClientError]
    MalformedPolicyDocumentException: Type[BotocoreClientError]
    PackedPolicyTooLargeException: Type[BotocoreClientError]
    RegionDisabledException: Type[BotocoreClientError]


class STSClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        STSClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#exceptions)
        """

    def assume_role(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: Sequence[PolicyDescriptorTypeTypeDef] = ...,
        Policy: str = ...,
        DurationSeconds: int = ...,
        Tags: Sequence[TagTypeDef] = ...,
        TransitiveTagKeys: Sequence[str] = ...,
        ExternalId: str = ...,
        SerialNumber: str = ...,
        TokenCode: str = ...,
        SourceIdentity: str = ...,
        ProvidedContexts: Sequence[ProvidedContextTypeDef] = ...
    ) -> AssumeRoleResponseTypeDef:
        """
        Returns a set of temporary security credentials that you can use to access
        Amazon Web Services
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role)
        """

    def assume_role_with_saml(
        self,
        *,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: Sequence[PolicyDescriptorTypeTypeDef] = ...,
        Policy: str = ...,
        DurationSeconds: int = ...
    ) -> AssumeRoleWithSAMLResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been
        authenticated via a SAML authentication
        response.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role_with_saml)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role_with_saml)
        """

    def assume_role_with_web_identity(
        self,
        *,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = ...,
        PolicyArns: Sequence[PolicyDescriptorTypeTypeDef] = ...,
        Policy: str = ...,
        DurationSeconds: int = ...
    ) -> AssumeRoleWithWebIdentityResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been
        authenticated in a mobile or web application with a web identity
        provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.assume_role_with_web_identity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#assume_role_with_web_identity)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#close)
        """

    def decode_authorization_message(
        self, *, EncodedMessage: str
    ) -> DecodeAuthorizationMessageResponseTypeDef:
        """
        Decodes additional information about the authorization status of a request from
        an encoded message returned in response to an Amazon Web Services
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.decode_authorization_message)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#decode_authorization_message)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#generate_presigned_url)
        """

    def get_access_key_info(self, *, AccessKeyId: str) -> GetAccessKeyInfoResponseTypeDef:
        """
        Returns the account identifier for the specified access key ID.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_access_key_info)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_access_key_info)
        """

    def get_caller_identity(self) -> GetCallerIdentityResponseTypeDef:
        """
        Returns details about the IAM user or role whose credentials are used to call
        the
        operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_caller_identity)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_caller_identity)
        """

    def get_federation_token(
        self,
        *,
        Name: str,
        Policy: str = ...,
        PolicyArns: Sequence[PolicyDescriptorTypeTypeDef] = ...,
        DurationSeconds: int = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> GetFederationTokenResponseTypeDef:
        """
        Returns a set of temporary security credentials (consisting of an access key
        ID, a secret access key, and a security token) for a
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_federation_token)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_federation_token)
        """

    def get_session_token(
        self, *, DurationSeconds: int = ..., SerialNumber: str = ..., TokenCode: str = ...
    ) -> GetSessionTokenResponseTypeDef:
        """
        Returns a set of temporary credentials for an Amazon Web Services account or
        IAM
        user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sts.html#STS.Client.get_session_token)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_sts/client/#get_session_token)
        """
