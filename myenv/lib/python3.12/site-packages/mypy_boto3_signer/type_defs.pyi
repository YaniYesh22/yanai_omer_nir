"""
Type annotations for signer service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/type_defs/)

Usage::

    ```python
    from mypy_boto3_signer.type_defs import AddProfilePermissionRequestRequestTypeDef

    data: AddProfilePermissionRequestRequestTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    EncryptionAlgorithmType,
    HashAlgorithmType,
    ImageFormatType,
    SigningProfileStatusType,
    SigningStatusType,
    ValidityTypeType,
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
    "AddProfilePermissionRequestRequestTypeDef",
    "ResponseMetadataTypeDef",
    "BlobTypeDef",
    "CancelSigningProfileRequestRequestTypeDef",
    "DescribeSigningJobRequestRequestTypeDef",
    "WaiterConfigTypeDef",
    "SigningJobRevocationRecordTypeDef",
    "SigningMaterialTypeDef",
    "S3DestinationTypeDef",
    "EncryptionAlgorithmOptionsTypeDef",
    "TimestampTypeDef",
    "GetSigningPlatformRequestRequestTypeDef",
    "SigningImageFormatTypeDef",
    "GetSigningProfileRequestRequestTypeDef",
    "SignatureValidityPeriodTypeDef",
    "SigningProfileRevocationRecordTypeDef",
    "HashAlgorithmOptionsTypeDef",
    "ListProfilePermissionsRequestRequestTypeDef",
    "PermissionTypeDef",
    "PaginatorConfigTypeDef",
    "ListSigningPlatformsRequestRequestTypeDef",
    "ListSigningProfilesRequestRequestTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "RemoveProfilePermissionRequestRequestTypeDef",
    "RevokeSignatureRequestRequestTypeDef",
    "S3SignedObjectTypeDef",
    "S3SourceTypeDef",
    "SigningConfigurationOverridesTypeDef",
    "TagResourceRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "AddProfilePermissionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetRevocationStatusResponseTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "PutSigningProfileResponseTypeDef",
    "RemoveProfilePermissionResponseTypeDef",
    "SignPayloadResponseTypeDef",
    "StartSigningJobResponseTypeDef",
    "SignPayloadRequestRequestTypeDef",
    "DescribeSigningJobRequestSuccessfulSigningJobWaitTypeDef",
    "DestinationTypeDef",
    "GetRevocationStatusRequestRequestTypeDef",
    "ListSigningJobsRequestRequestTypeDef",
    "RevokeSigningProfileRequestRequestTypeDef",
    "SigningProfileTypeDef",
    "SigningConfigurationTypeDef",
    "ListProfilePermissionsResponseTypeDef",
    "ListSigningJobsRequestListSigningJobsPaginateTypeDef",
    "ListSigningPlatformsRequestListSigningPlatformsPaginateTypeDef",
    "ListSigningProfilesRequestListSigningProfilesPaginateTypeDef",
    "SignedObjectTypeDef",
    "SourceTypeDef",
    "SigningPlatformOverridesTypeDef",
    "ListSigningProfilesResponseTypeDef",
    "GetSigningPlatformResponseTypeDef",
    "SigningPlatformTypeDef",
    "SigningJobTypeDef",
    "StartSigningJobRequestRequestTypeDef",
    "DescribeSigningJobResponseTypeDef",
    "GetSigningProfileResponseTypeDef",
    "PutSigningProfileRequestRequestTypeDef",
    "ListSigningPlatformsResponseTypeDef",
    "ListSigningJobsResponseTypeDef",
)

AddProfilePermissionRequestRequestTypeDef = TypedDict(
    "AddProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "action": str,
        "principal": str,
        "statementId": str,
        "profileVersion": NotRequired[str],
        "revisionId": NotRequired[str],
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
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CancelSigningProfileRequestRequestTypeDef = TypedDict(
    "CancelSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
    },
)
DescribeSigningJobRequestRequestTypeDef = TypedDict(
    "DescribeSigningJobRequestRequestTypeDef",
    {
        "jobId": str,
    },
)
WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": NotRequired[int],
        "MaxAttempts": NotRequired[int],
    },
)
SigningJobRevocationRecordTypeDef = TypedDict(
    "SigningJobRevocationRecordTypeDef",
    {
        "reason": NotRequired[str],
        "revokedAt": NotRequired[datetime],
        "revokedBy": NotRequired[str],
    },
)
SigningMaterialTypeDef = TypedDict(
    "SigningMaterialTypeDef",
    {
        "certificateArn": str,
    },
)
S3DestinationTypeDef = TypedDict(
    "S3DestinationTypeDef",
    {
        "bucketName": NotRequired[str],
        "prefix": NotRequired[str],
    },
)
EncryptionAlgorithmOptionsTypeDef = TypedDict(
    "EncryptionAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[EncryptionAlgorithmType],
        "defaultValue": EncryptionAlgorithmType,
    },
)
TimestampTypeDef = Union[datetime, str]
GetSigningPlatformRequestRequestTypeDef = TypedDict(
    "GetSigningPlatformRequestRequestTypeDef",
    {
        "platformId": str,
    },
)
SigningImageFormatTypeDef = TypedDict(
    "SigningImageFormatTypeDef",
    {
        "supportedFormats": List[ImageFormatType],
        "defaultFormat": ImageFormatType,
    },
)
GetSigningProfileRequestRequestTypeDef = TypedDict(
    "GetSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "profileOwner": NotRequired[str],
    },
)
SignatureValidityPeriodTypeDef = TypedDict(
    "SignatureValidityPeriodTypeDef",
    {
        "value": NotRequired[int],
        "type": NotRequired[ValidityTypeType],
    },
)
SigningProfileRevocationRecordTypeDef = TypedDict(
    "SigningProfileRevocationRecordTypeDef",
    {
        "revocationEffectiveFrom": NotRequired[datetime],
        "revokedAt": NotRequired[datetime],
        "revokedBy": NotRequired[str],
    },
)
HashAlgorithmOptionsTypeDef = TypedDict(
    "HashAlgorithmOptionsTypeDef",
    {
        "allowedValues": List[HashAlgorithmType],
        "defaultValue": HashAlgorithmType,
    },
)
ListProfilePermissionsRequestRequestTypeDef = TypedDict(
    "ListProfilePermissionsRequestRequestTypeDef",
    {
        "profileName": str,
        "nextToken": NotRequired[str],
    },
)
PermissionTypeDef = TypedDict(
    "PermissionTypeDef",
    {
        "action": NotRequired[str],
        "principal": NotRequired[str],
        "statementId": NotRequired[str],
        "profileVersion": NotRequired[str],
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
ListSigningPlatformsRequestRequestTypeDef = TypedDict(
    "ListSigningPlatformsRequestRequestTypeDef",
    {
        "category": NotRequired[str],
        "partner": NotRequired[str],
        "target": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
    },
)
ListSigningProfilesRequestRequestTypeDef = TypedDict(
    "ListSigningProfilesRequestRequestTypeDef",
    {
        "includeCanceled": NotRequired[bool],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "platformId": NotRequired[str],
        "statuses": NotRequired[Sequence[SigningProfileStatusType]],
    },
)
ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
    },
)
RemoveProfilePermissionRequestRequestTypeDef = TypedDict(
    "RemoveProfilePermissionRequestRequestTypeDef",
    {
        "profileName": str,
        "revisionId": str,
        "statementId": str,
    },
)
RevokeSignatureRequestRequestTypeDef = TypedDict(
    "RevokeSignatureRequestRequestTypeDef",
    {
        "jobId": str,
        "reason": str,
        "jobOwner": NotRequired[str],
    },
)
S3SignedObjectTypeDef = TypedDict(
    "S3SignedObjectTypeDef",
    {
        "bucketName": NotRequired[str],
        "key": NotRequired[str],
    },
)
S3SourceTypeDef = TypedDict(
    "S3SourceTypeDef",
    {
        "bucketName": str,
        "key": str,
        "version": str,
    },
)
SigningConfigurationOverridesTypeDef = TypedDict(
    "SigningConfigurationOverridesTypeDef",
    {
        "encryptionAlgorithm": NotRequired[EncryptionAlgorithmType],
        "hashAlgorithm": NotRequired[HashAlgorithmType],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
AddProfilePermissionResponseTypeDef = TypedDict(
    "AddProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetRevocationStatusResponseTypeDef = TypedDict(
    "GetRevocationStatusResponseTypeDef",
    {
        "revokedEntities": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSigningProfileResponseTypeDef = TypedDict(
    "PutSigningProfileResponseTypeDef",
    {
        "arn": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RemoveProfilePermissionResponseTypeDef = TypedDict(
    "RemoveProfilePermissionResponseTypeDef",
    {
        "revisionId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SignPayloadResponseTypeDef = TypedDict(
    "SignPayloadResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
        "metadata": Dict[str, str],
        "signature": bytes,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StartSigningJobResponseTypeDef = TypedDict(
    "StartSigningJobResponseTypeDef",
    {
        "jobId": str,
        "jobOwner": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SignPayloadRequestRequestTypeDef = TypedDict(
    "SignPayloadRequestRequestTypeDef",
    {
        "profileName": str,
        "payload": BlobTypeDef,
        "payloadFormat": str,
        "profileOwner": NotRequired[str],
    },
)
DescribeSigningJobRequestSuccessfulSigningJobWaitTypeDef = TypedDict(
    "DescribeSigningJobRequestSuccessfulSigningJobWaitTypeDef",
    {
        "jobId": str,
        "WaiterConfig": NotRequired[WaiterConfigTypeDef],
    },
)
DestinationTypeDef = TypedDict(
    "DestinationTypeDef",
    {
        "s3": NotRequired[S3DestinationTypeDef],
    },
)
GetRevocationStatusRequestRequestTypeDef = TypedDict(
    "GetRevocationStatusRequestRequestTypeDef",
    {
        "signatureTimestamp": TimestampTypeDef,
        "platformId": str,
        "profileVersionArn": str,
        "jobArn": str,
        "certificateHashes": Sequence[str],
    },
)
ListSigningJobsRequestRequestTypeDef = TypedDict(
    "ListSigningJobsRequestRequestTypeDef",
    {
        "status": NotRequired[SigningStatusType],
        "platformId": NotRequired[str],
        "requestedBy": NotRequired[str],
        "maxResults": NotRequired[int],
        "nextToken": NotRequired[str],
        "isRevoked": NotRequired[bool],
        "signatureExpiresBefore": NotRequired[TimestampTypeDef],
        "signatureExpiresAfter": NotRequired[TimestampTypeDef],
        "jobInvoker": NotRequired[str],
    },
)
RevokeSigningProfileRequestRequestTypeDef = TypedDict(
    "RevokeSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "reason": str,
        "effectiveTime": TimestampTypeDef,
    },
)
SigningProfileTypeDef = TypedDict(
    "SigningProfileTypeDef",
    {
        "profileName": NotRequired[str],
        "profileVersion": NotRequired[str],
        "profileVersionArn": NotRequired[str],
        "signingMaterial": NotRequired[SigningMaterialTypeDef],
        "signatureValidityPeriod": NotRequired[SignatureValidityPeriodTypeDef],
        "platformId": NotRequired[str],
        "platformDisplayName": NotRequired[str],
        "signingParameters": NotRequired[Dict[str, str]],
        "status": NotRequired[SigningProfileStatusType],
        "arn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
SigningConfigurationTypeDef = TypedDict(
    "SigningConfigurationTypeDef",
    {
        "encryptionAlgorithmOptions": EncryptionAlgorithmOptionsTypeDef,
        "hashAlgorithmOptions": HashAlgorithmOptionsTypeDef,
    },
)
ListProfilePermissionsResponseTypeDef = TypedDict(
    "ListProfilePermissionsResponseTypeDef",
    {
        "revisionId": str,
        "policySizeBytes": int,
        "permissions": List[PermissionTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSigningJobsRequestListSigningJobsPaginateTypeDef = TypedDict(
    "ListSigningJobsRequestListSigningJobsPaginateTypeDef",
    {
        "status": NotRequired[SigningStatusType],
        "platformId": NotRequired[str],
        "requestedBy": NotRequired[str],
        "isRevoked": NotRequired[bool],
        "signatureExpiresBefore": NotRequired[TimestampTypeDef],
        "signatureExpiresAfter": NotRequired[TimestampTypeDef],
        "jobInvoker": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSigningPlatformsRequestListSigningPlatformsPaginateTypeDef = TypedDict(
    "ListSigningPlatformsRequestListSigningPlatformsPaginateTypeDef",
    {
        "category": NotRequired[str],
        "partner": NotRequired[str],
        "target": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
ListSigningProfilesRequestListSigningProfilesPaginateTypeDef = TypedDict(
    "ListSigningProfilesRequestListSigningProfilesPaginateTypeDef",
    {
        "includeCanceled": NotRequired[bool],
        "platformId": NotRequired[str],
        "statuses": NotRequired[Sequence[SigningProfileStatusType]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
SignedObjectTypeDef = TypedDict(
    "SignedObjectTypeDef",
    {
        "s3": NotRequired[S3SignedObjectTypeDef],
    },
)
SourceTypeDef = TypedDict(
    "SourceTypeDef",
    {
        "s3": NotRequired[S3SourceTypeDef],
    },
)
SigningPlatformOverridesTypeDef = TypedDict(
    "SigningPlatformOverridesTypeDef",
    {
        "signingConfiguration": NotRequired[SigningConfigurationOverridesTypeDef],
        "signingImageFormat": NotRequired[ImageFormatType],
    },
)
ListSigningProfilesResponseTypeDef = TypedDict(
    "ListSigningProfilesResponseTypeDef",
    {
        "profiles": List[SigningProfileTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSigningPlatformResponseTypeDef = TypedDict(
    "GetSigningPlatformResponseTypeDef",
    {
        "platformId": str,
        "displayName": str,
        "partner": str,
        "target": str,
        "category": Literal["AWSIoT"],
        "signingConfiguration": SigningConfigurationTypeDef,
        "signingImageFormat": SigningImageFormatTypeDef,
        "maxSizeInMB": int,
        "revocationSupported": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SigningPlatformTypeDef = TypedDict(
    "SigningPlatformTypeDef",
    {
        "platformId": NotRequired[str],
        "displayName": NotRequired[str],
        "partner": NotRequired[str],
        "target": NotRequired[str],
        "category": NotRequired[Literal["AWSIoT"]],
        "signingConfiguration": NotRequired[SigningConfigurationTypeDef],
        "signingImageFormat": NotRequired[SigningImageFormatTypeDef],
        "maxSizeInMB": NotRequired[int],
        "revocationSupported": NotRequired[bool],
    },
)
SigningJobTypeDef = TypedDict(
    "SigningJobTypeDef",
    {
        "jobId": NotRequired[str],
        "source": NotRequired[SourceTypeDef],
        "signedObject": NotRequired[SignedObjectTypeDef],
        "signingMaterial": NotRequired[SigningMaterialTypeDef],
        "createdAt": NotRequired[datetime],
        "status": NotRequired[SigningStatusType],
        "isRevoked": NotRequired[bool],
        "profileName": NotRequired[str],
        "profileVersion": NotRequired[str],
        "platformId": NotRequired[str],
        "platformDisplayName": NotRequired[str],
        "signatureExpiresAt": NotRequired[datetime],
        "jobOwner": NotRequired[str],
        "jobInvoker": NotRequired[str],
    },
)
StartSigningJobRequestRequestTypeDef = TypedDict(
    "StartSigningJobRequestRequestTypeDef",
    {
        "source": SourceTypeDef,
        "destination": DestinationTypeDef,
        "profileName": str,
        "clientRequestToken": str,
        "profileOwner": NotRequired[str],
    },
)
DescribeSigningJobResponseTypeDef = TypedDict(
    "DescribeSigningJobResponseTypeDef",
    {
        "jobId": str,
        "source": SourceTypeDef,
        "signingMaterial": SigningMaterialTypeDef,
        "platformId": str,
        "platformDisplayName": str,
        "profileName": str,
        "profileVersion": str,
        "overrides": SigningPlatformOverridesTypeDef,
        "signingParameters": Dict[str, str],
        "createdAt": datetime,
        "completedAt": datetime,
        "signatureExpiresAt": datetime,
        "requestedBy": str,
        "status": SigningStatusType,
        "statusReason": str,
        "revocationRecord": SigningJobRevocationRecordTypeDef,
        "signedObject": SignedObjectTypeDef,
        "jobOwner": str,
        "jobInvoker": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetSigningProfileResponseTypeDef = TypedDict(
    "GetSigningProfileResponseTypeDef",
    {
        "profileName": str,
        "profileVersion": str,
        "profileVersionArn": str,
        "revocationRecord": SigningProfileRevocationRecordTypeDef,
        "signingMaterial": SigningMaterialTypeDef,
        "platformId": str,
        "platformDisplayName": str,
        "signatureValidityPeriod": SignatureValidityPeriodTypeDef,
        "overrides": SigningPlatformOverridesTypeDef,
        "signingParameters": Dict[str, str],
        "status": SigningProfileStatusType,
        "statusReason": str,
        "arn": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
PutSigningProfileRequestRequestTypeDef = TypedDict(
    "PutSigningProfileRequestRequestTypeDef",
    {
        "profileName": str,
        "platformId": str,
        "signingMaterial": NotRequired[SigningMaterialTypeDef],
        "signatureValidityPeriod": NotRequired[SignatureValidityPeriodTypeDef],
        "overrides": NotRequired[SigningPlatformOverridesTypeDef],
        "signingParameters": NotRequired[Mapping[str, str]],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ListSigningPlatformsResponseTypeDef = TypedDict(
    "ListSigningPlatformsResponseTypeDef",
    {
        "platforms": List[SigningPlatformTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ListSigningJobsResponseTypeDef = TypedDict(
    "ListSigningJobsResponseTypeDef",
    {
        "jobs": List[SigningJobTypeDef],
        "nextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
