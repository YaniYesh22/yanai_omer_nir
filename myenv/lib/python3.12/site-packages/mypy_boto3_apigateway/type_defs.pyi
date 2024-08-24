"""
Type annotations for apigateway service type definitions.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_apigateway/type_defs/)

Usage::

    ```python
    from mypy_boto3_apigateway.type_defs import AccessLogSettingsTypeDef

    data: AccessLogSettingsTypeDef = ...
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Mapping, Sequence, Union

from botocore.response import StreamingBody

from .literals import (
    ApiKeySourceTypeType,
    AuthorizerTypeType,
    CacheClusterSizeType,
    CacheClusterStatusType,
    ConnectionTypeType,
    ContentHandlingStrategyType,
    DocumentationPartTypeType,
    DomainNameStatusType,
    EndpointTypeType,
    GatewayResponseTypeType,
    IntegrationTypeType,
    LocationStatusTypeType,
    OpType,
    PutModeType,
    QuotaPeriodTypeType,
    SecurityPolicyType,
    UnauthorizedCacheControlHeaderStrategyType,
    VpcLinkStatusType,
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
    "AccessLogSettingsTypeDef",
    "ResponseMetadataTypeDef",
    "ThrottleSettingsTypeDef",
    "ApiKeyTypeDef",
    "AuthorizerTypeDef",
    "BasePathMappingTypeDef",
    "BlobTypeDef",
    "CanarySettingsOutputTypeDef",
    "CanarySettingsTypeDef",
    "ClientCertificateTypeDef",
    "StageKeyTypeDef",
    "CreateAuthorizerRequestRequestTypeDef",
    "CreateBasePathMappingRequestRequestTypeDef",
    "DeploymentCanarySettingsTypeDef",
    "DocumentationPartLocationTypeDef",
    "CreateDocumentationVersionRequestRequestTypeDef",
    "EndpointConfigurationTypeDef",
    "MutualTlsAuthenticationInputTypeDef",
    "CreateModelRequestRequestTypeDef",
    "CreateRequestValidatorRequestRequestTypeDef",
    "CreateResourceRequestRequestTypeDef",
    "CreateUsagePlanKeyRequestRequestTypeDef",
    "QuotaSettingsTypeDef",
    "CreateVpcLinkRequestRequestTypeDef",
    "DeleteApiKeyRequestRequestTypeDef",
    "DeleteAuthorizerRequestRequestTypeDef",
    "DeleteBasePathMappingRequestRequestTypeDef",
    "DeleteClientCertificateRequestRequestTypeDef",
    "DeleteDeploymentRequestRequestTypeDef",
    "DeleteDocumentationPartRequestRequestTypeDef",
    "DeleteDocumentationVersionRequestRequestTypeDef",
    "DeleteDomainNameRequestRequestTypeDef",
    "DeleteGatewayResponseRequestRequestTypeDef",
    "DeleteIntegrationRequestRequestTypeDef",
    "DeleteIntegrationResponseRequestRequestTypeDef",
    "DeleteMethodRequestRequestTypeDef",
    "DeleteMethodResponseRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DeleteRequestValidatorRequestRequestTypeDef",
    "DeleteResourceRequestRequestTypeDef",
    "DeleteRestApiRequestRequestTypeDef",
    "DeleteStageRequestRequestTypeDef",
    "DeleteUsagePlanKeyRequestRequestTypeDef",
    "DeleteUsagePlanRequestRequestTypeDef",
    "DeleteVpcLinkRequestRequestTypeDef",
    "MethodSnapshotTypeDef",
    "DocumentationVersionTypeDef",
    "EndpointConfigurationOutputTypeDef",
    "MutualTlsAuthenticationTypeDef",
    "EndpointConfigurationExtraOutputTypeDef",
    "FlushStageAuthorizersCacheRequestRequestTypeDef",
    "FlushStageCacheRequestRequestTypeDef",
    "GatewayResponseTypeDef",
    "GenerateClientCertificateRequestRequestTypeDef",
    "GetApiKeyRequestRequestTypeDef",
    "PaginatorConfigTypeDef",
    "GetApiKeysRequestRequestTypeDef",
    "GetAuthorizerRequestRequestTypeDef",
    "GetAuthorizersRequestRequestTypeDef",
    "GetBasePathMappingRequestRequestTypeDef",
    "GetBasePathMappingsRequestRequestTypeDef",
    "GetClientCertificateRequestRequestTypeDef",
    "GetClientCertificatesRequestRequestTypeDef",
    "GetDeploymentRequestRequestTypeDef",
    "GetDeploymentsRequestRequestTypeDef",
    "GetDocumentationPartRequestRequestTypeDef",
    "GetDocumentationPartsRequestRequestTypeDef",
    "GetDocumentationVersionRequestRequestTypeDef",
    "GetDocumentationVersionsRequestRequestTypeDef",
    "GetDomainNameRequestRequestTypeDef",
    "GetDomainNamesRequestRequestTypeDef",
    "GetExportRequestRequestTypeDef",
    "GetGatewayResponseRequestRequestTypeDef",
    "GetGatewayResponsesRequestRequestTypeDef",
    "GetIntegrationRequestRequestTypeDef",
    "GetIntegrationResponseRequestRequestTypeDef",
    "GetMethodRequestRequestTypeDef",
    "GetMethodResponseRequestRequestTypeDef",
    "GetModelRequestRequestTypeDef",
    "GetModelTemplateRequestRequestTypeDef",
    "GetModelsRequestRequestTypeDef",
    "GetRequestValidatorRequestRequestTypeDef",
    "GetRequestValidatorsRequestRequestTypeDef",
    "GetResourceRequestRequestTypeDef",
    "GetResourcesRequestRequestTypeDef",
    "GetRestApiRequestRequestTypeDef",
    "GetRestApisRequestRequestTypeDef",
    "GetSdkRequestRequestTypeDef",
    "GetSdkTypeRequestRequestTypeDef",
    "GetSdkTypesRequestRequestTypeDef",
    "GetStageRequestRequestTypeDef",
    "GetStagesRequestRequestTypeDef",
    "GetTagsRequestRequestTypeDef",
    "GetUsagePlanKeyRequestRequestTypeDef",
    "GetUsagePlanKeysRequestRequestTypeDef",
    "GetUsagePlanRequestRequestTypeDef",
    "GetUsagePlansRequestRequestTypeDef",
    "GetUsageRequestRequestTypeDef",
    "GetVpcLinkRequestRequestTypeDef",
    "GetVpcLinksRequestRequestTypeDef",
    "IntegrationResponseTypeDef",
    "TlsConfigTypeDef",
    "MethodResponseTypeDef",
    "MethodSettingTypeDef",
    "ModelTypeDef",
    "PatchOperationTypeDef",
    "PutGatewayResponseRequestRequestTypeDef",
    "PutIntegrationResponseRequestRequestTypeDef",
    "PutMethodRequestRequestTypeDef",
    "PutMethodResponseRequestRequestTypeDef",
    "RequestValidatorTypeDef",
    "SdkConfigurationPropertyTypeDef",
    "TagResourceRequestRequestTypeDef",
    "TestInvokeAuthorizerRequestRequestTypeDef",
    "TestInvokeMethodRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "UsagePlanKeyTypeDef",
    "VpcLinkTypeDef",
    "ApiKeyIdsTypeDef",
    "ApiKeyResponseTypeDef",
    "AuthorizerResponseTypeDef",
    "BasePathMappingResponseTypeDef",
    "ClientCertificateResponseTypeDef",
    "DocumentationPartIdsTypeDef",
    "DocumentationVersionResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ExportResponseTypeDef",
    "GatewayResponseResponseTypeDef",
    "IntegrationResponseResponseTypeDef",
    "MethodResponseResponseTypeDef",
    "ModelResponseTypeDef",
    "RequestValidatorResponseTypeDef",
    "SdkResponseTypeDef",
    "TagsTypeDef",
    "TemplateTypeDef",
    "TestInvokeAuthorizerResponseTypeDef",
    "TestInvokeMethodResponseTypeDef",
    "UsagePlanKeyResponseTypeDef",
    "UsageTypeDef",
    "VpcLinkResponseTypeDef",
    "AccountTypeDef",
    "ApiStageExtraOutputTypeDef",
    "ApiStageOutputTypeDef",
    "ApiStageTypeDef",
    "ApiKeysTypeDef",
    "AuthorizersTypeDef",
    "BasePathMappingsTypeDef",
    "ImportApiKeysRequestRequestTypeDef",
    "ImportDocumentationPartsRequestRequestTypeDef",
    "ImportRestApiRequestRequestTypeDef",
    "PutRestApiRequestRequestTypeDef",
    "CanarySettingsUnionTypeDef",
    "CreateStageRequestRequestTypeDef",
    "ClientCertificatesTypeDef",
    "CreateApiKeyRequestRequestTypeDef",
    "CreateDeploymentRequestRequestTypeDef",
    "CreateDocumentationPartRequestRequestTypeDef",
    "DocumentationPartResponseTypeDef",
    "DocumentationPartTypeDef",
    "CreateRestApiRequestRequestTypeDef",
    "CreateDomainNameRequestRequestTypeDef",
    "DeploymentResponseTypeDef",
    "DeploymentTypeDef",
    "DocumentationVersionsTypeDef",
    "RestApiResponseTypeDef",
    "RestApiTypeDef",
    "DomainNameResponseTypeDef",
    "DomainNameTypeDef",
    "EndpointConfigurationUnionTypeDef",
    "GatewayResponsesTypeDef",
    "GetApiKeysRequestGetApiKeysPaginateTypeDef",
    "GetAuthorizersRequestGetAuthorizersPaginateTypeDef",
    "GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef",
    "GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef",
    "GetDeploymentsRequestGetDeploymentsPaginateTypeDef",
    "GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef",
    "GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef",
    "GetDomainNamesRequestGetDomainNamesPaginateTypeDef",
    "GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef",
    "GetModelsRequestGetModelsPaginateTypeDef",
    "GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef",
    "GetResourcesRequestGetResourcesPaginateTypeDef",
    "GetRestApisRequestGetRestApisPaginateTypeDef",
    "GetSdkTypesRequestGetSdkTypesPaginateTypeDef",
    "GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef",
    "GetUsagePlansRequestGetUsagePlansPaginateTypeDef",
    "GetUsageRequestGetUsagePaginateTypeDef",
    "GetVpcLinksRequestGetVpcLinksPaginateTypeDef",
    "IntegrationExtraResponseTypeDef",
    "IntegrationTypeDef",
    "PutIntegrationRequestRequestTypeDef",
    "StageResponseTypeDef",
    "StageTypeDef",
    "ModelsTypeDef",
    "UpdateAccountRequestRequestTypeDef",
    "UpdateApiKeyRequestRequestTypeDef",
    "UpdateAuthorizerRequestRequestTypeDef",
    "UpdateBasePathMappingRequestRequestTypeDef",
    "UpdateClientCertificateRequestRequestTypeDef",
    "UpdateDeploymentRequestRequestTypeDef",
    "UpdateDocumentationPartRequestRequestTypeDef",
    "UpdateDocumentationVersionRequestRequestTypeDef",
    "UpdateDomainNameRequestRequestTypeDef",
    "UpdateGatewayResponseRequestRequestTypeDef",
    "UpdateIntegrationRequestRequestTypeDef",
    "UpdateIntegrationResponseRequestRequestTypeDef",
    "UpdateMethodRequestRequestTypeDef",
    "UpdateMethodResponseRequestRequestTypeDef",
    "UpdateModelRequestRequestTypeDef",
    "UpdateRequestValidatorRequestRequestTypeDef",
    "UpdateResourceRequestRequestTypeDef",
    "UpdateRestApiRequestRequestTypeDef",
    "UpdateStageRequestRequestTypeDef",
    "UpdateUsagePlanRequestRequestTypeDef",
    "UpdateUsageRequestRequestTypeDef",
    "UpdateVpcLinkRequestRequestTypeDef",
    "RequestValidatorsTypeDef",
    "SdkTypeResponseTypeDef",
    "SdkTypeTypeDef",
    "UsagePlanKeysTypeDef",
    "VpcLinksTypeDef",
    "UsagePlanResponseTypeDef",
    "UsagePlanTypeDef",
    "ApiStageUnionTypeDef",
    "DocumentationPartsTypeDef",
    "DeploymentsTypeDef",
    "RestApisTypeDef",
    "DomainNamesTypeDef",
    "MethodExtraResponseTypeDef",
    "MethodTypeDef",
    "StagesTypeDef",
    "SdkTypesTypeDef",
    "UsagePlansTypeDef",
    "CreateUsagePlanRequestRequestTypeDef",
    "ResourceResponseTypeDef",
    "ResourceTypeDef",
    "ResourcesTypeDef",
)

AccessLogSettingsTypeDef = TypedDict(
    "AccessLogSettingsTypeDef",
    {
        "format": NotRequired[str],
        "destinationArn": NotRequired[str],
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
ThrottleSettingsTypeDef = TypedDict(
    "ThrottleSettingsTypeDef",
    {
        "burstLimit": NotRequired[int],
        "rateLimit": NotRequired[float],
    },
)
ApiKeyTypeDef = TypedDict(
    "ApiKeyTypeDef",
    {
        "id": NotRequired[str],
        "value": NotRequired[str],
        "name": NotRequired[str],
        "customerId": NotRequired[str],
        "description": NotRequired[str],
        "enabled": NotRequired[bool],
        "createdDate": NotRequired[datetime],
        "lastUpdatedDate": NotRequired[datetime],
        "stageKeys": NotRequired[List[str]],
        "tags": NotRequired[Dict[str, str]],
    },
)
AuthorizerTypeDef = TypedDict(
    "AuthorizerTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "type": NotRequired[AuthorizerTypeType],
        "providerARNs": NotRequired[List[str]],
        "authType": NotRequired[str],
        "authorizerUri": NotRequired[str],
        "authorizerCredentials": NotRequired[str],
        "identitySource": NotRequired[str],
        "identityValidationExpression": NotRequired[str],
        "authorizerResultTtlInSeconds": NotRequired[int],
    },
)
BasePathMappingTypeDef = TypedDict(
    "BasePathMappingTypeDef",
    {
        "basePath": NotRequired[str],
        "restApiId": NotRequired[str],
        "stage": NotRequired[str],
    },
)
BlobTypeDef = Union[str, bytes, IO[Any], StreamingBody]
CanarySettingsOutputTypeDef = TypedDict(
    "CanarySettingsOutputTypeDef",
    {
        "percentTraffic": NotRequired[float],
        "deploymentId": NotRequired[str],
        "stageVariableOverrides": NotRequired[Dict[str, str]],
        "useStageCache": NotRequired[bool],
    },
)
CanarySettingsTypeDef = TypedDict(
    "CanarySettingsTypeDef",
    {
        "percentTraffic": NotRequired[float],
        "deploymentId": NotRequired[str],
        "stageVariableOverrides": NotRequired[Mapping[str, str]],
        "useStageCache": NotRequired[bool],
    },
)
ClientCertificateTypeDef = TypedDict(
    "ClientCertificateTypeDef",
    {
        "clientCertificateId": NotRequired[str],
        "description": NotRequired[str],
        "pemEncodedCertificate": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "expirationDate": NotRequired[datetime],
        "tags": NotRequired[Dict[str, str]],
    },
)
StageKeyTypeDef = TypedDict(
    "StageKeyTypeDef",
    {
        "restApiId": NotRequired[str],
        "stageName": NotRequired[str],
    },
)
CreateAuthorizerRequestRequestTypeDef = TypedDict(
    "CreateAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "type": AuthorizerTypeType,
        "providerARNs": NotRequired[Sequence[str]],
        "authType": NotRequired[str],
        "authorizerUri": NotRequired[str],
        "authorizerCredentials": NotRequired[str],
        "identitySource": NotRequired[str],
        "identityValidationExpression": NotRequired[str],
        "authorizerResultTtlInSeconds": NotRequired[int],
    },
)
CreateBasePathMappingRequestRequestTypeDef = TypedDict(
    "CreateBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "restApiId": str,
        "basePath": NotRequired[str],
        "stage": NotRequired[str],
    },
)
DeploymentCanarySettingsTypeDef = TypedDict(
    "DeploymentCanarySettingsTypeDef",
    {
        "percentTraffic": NotRequired[float],
        "stageVariableOverrides": NotRequired[Mapping[str, str]],
        "useStageCache": NotRequired[bool],
    },
)
DocumentationPartLocationTypeDef = TypedDict(
    "DocumentationPartLocationTypeDef",
    {
        "type": DocumentationPartTypeType,
        "path": NotRequired[str],
        "method": NotRequired[str],
        "statusCode": NotRequired[str],
        "name": NotRequired[str],
    },
)
CreateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "CreateDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
        "stageName": NotRequired[str],
        "description": NotRequired[str],
    },
)
EndpointConfigurationTypeDef = TypedDict(
    "EndpointConfigurationTypeDef",
    {
        "types": NotRequired[Sequence[EndpointTypeType]],
        "vpcEndpointIds": NotRequired[Sequence[str]],
    },
)
MutualTlsAuthenticationInputTypeDef = TypedDict(
    "MutualTlsAuthenticationInputTypeDef",
    {
        "truststoreUri": NotRequired[str],
        "truststoreVersion": NotRequired[str],
    },
)
CreateModelRequestRequestTypeDef = TypedDict(
    "CreateModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "name": str,
        "contentType": str,
        "description": NotRequired[str],
        "schema": NotRequired[str],
    },
)
CreateRequestValidatorRequestRequestTypeDef = TypedDict(
    "CreateRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "name": NotRequired[str],
        "validateRequestBody": NotRequired[bool],
        "validateRequestParameters": NotRequired[bool],
    },
)
CreateResourceRequestRequestTypeDef = TypedDict(
    "CreateResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "parentId": str,
        "pathPart": str,
    },
)
CreateUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "CreateUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
        "keyType": str,
    },
)
QuotaSettingsTypeDef = TypedDict(
    "QuotaSettingsTypeDef",
    {
        "limit": NotRequired[int],
        "offset": NotRequired[int],
        "period": NotRequired[QuotaPeriodTypeType],
    },
)
CreateVpcLinkRequestRequestTypeDef = TypedDict(
    "CreateVpcLinkRequestRequestTypeDef",
    {
        "name": str,
        "targetArns": Sequence[str],
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
DeleteApiKeyRequestRequestTypeDef = TypedDict(
    "DeleteApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
    },
)
DeleteAuthorizerRequestRequestTypeDef = TypedDict(
    "DeleteAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
DeleteBasePathMappingRequestRequestTypeDef = TypedDict(
    "DeleteBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)
DeleteClientCertificateRequestRequestTypeDef = TypedDict(
    "DeleteClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)
DeleteDeploymentRequestRequestTypeDef = TypedDict(
    "DeleteDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
    },
)
DeleteDocumentationPartRequestRequestTypeDef = TypedDict(
    "DeleteDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)
DeleteDocumentationVersionRequestRequestTypeDef = TypedDict(
    "DeleteDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
DeleteDomainNameRequestRequestTypeDef = TypedDict(
    "DeleteDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
DeleteGatewayResponseRequestRequestTypeDef = TypedDict(
    "DeleteGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
DeleteIntegrationRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
DeleteIntegrationResponseRequestRequestTypeDef = TypedDict(
    "DeleteIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
DeleteMethodRequestRequestTypeDef = TypedDict(
    "DeleteMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
DeleteMethodResponseRequestRequestTypeDef = TypedDict(
    "DeleteMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
DeleteRequestValidatorRequestRequestTypeDef = TypedDict(
    "DeleteRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)
DeleteResourceRequestRequestTypeDef = TypedDict(
    "DeleteResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
    },
)
DeleteRestApiRequestRequestTypeDef = TypedDict(
    "DeleteRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
DeleteStageRequestRequestTypeDef = TypedDict(
    "DeleteStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
DeleteUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "DeleteUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)
DeleteUsagePlanRequestRequestTypeDef = TypedDict(
    "DeleteUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
DeleteVpcLinkRequestRequestTypeDef = TypedDict(
    "DeleteVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)
MethodSnapshotTypeDef = TypedDict(
    "MethodSnapshotTypeDef",
    {
        "authorizationType": NotRequired[str],
        "apiKeyRequired": NotRequired[bool],
    },
)
DocumentationVersionTypeDef = TypedDict(
    "DocumentationVersionTypeDef",
    {
        "version": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "description": NotRequired[str],
    },
)
EndpointConfigurationOutputTypeDef = TypedDict(
    "EndpointConfigurationOutputTypeDef",
    {
        "types": NotRequired[List[EndpointTypeType]],
        "vpcEndpointIds": NotRequired[List[str]],
    },
)
MutualTlsAuthenticationTypeDef = TypedDict(
    "MutualTlsAuthenticationTypeDef",
    {
        "truststoreUri": NotRequired[str],
        "truststoreVersion": NotRequired[str],
        "truststoreWarnings": NotRequired[List[str]],
    },
)
EndpointConfigurationExtraOutputTypeDef = TypedDict(
    "EndpointConfigurationExtraOutputTypeDef",
    {
        "types": NotRequired[List[EndpointTypeType]],
        "vpcEndpointIds": NotRequired[List[str]],
    },
)
FlushStageAuthorizersCacheRequestRequestTypeDef = TypedDict(
    "FlushStageAuthorizersCacheRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
FlushStageCacheRequestRequestTypeDef = TypedDict(
    "FlushStageCacheRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
GatewayResponseTypeDef = TypedDict(
    "GatewayResponseTypeDef",
    {
        "responseType": NotRequired[GatewayResponseTypeType],
        "statusCode": NotRequired[str],
        "responseParameters": NotRequired[Dict[str, str]],
        "responseTemplates": NotRequired[Dict[str, str]],
        "defaultResponse": NotRequired[bool],
    },
)
GenerateClientCertificateRequestRequestTypeDef = TypedDict(
    "GenerateClientCertificateRequestRequestTypeDef",
    {
        "description": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
GetApiKeyRequestRequestTypeDef = TypedDict(
    "GetApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
        "includeValue": NotRequired[bool],
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
GetApiKeysRequestRequestTypeDef = TypedDict(
    "GetApiKeysRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
        "nameQuery": NotRequired[str],
        "customerId": NotRequired[str],
        "includeValues": NotRequired[bool],
    },
)
GetAuthorizerRequestRequestTypeDef = TypedDict(
    "GetAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
    },
)
GetAuthorizersRequestRequestTypeDef = TypedDict(
    "GetAuthorizersRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetBasePathMappingRequestRequestTypeDef = TypedDict(
    "GetBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
    },
)
GetBasePathMappingsRequestRequestTypeDef = TypedDict(
    "GetBasePathMappingsRequestRequestTypeDef",
    {
        "domainName": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetClientCertificateRequestRequestTypeDef = TypedDict(
    "GetClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
    },
)
GetClientCertificatesRequestRequestTypeDef = TypedDict(
    "GetClientCertificatesRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetDeploymentRequestRequestTypeDef = TypedDict(
    "GetDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
        "embed": NotRequired[Sequence[str]],
    },
)
GetDeploymentsRequestRequestTypeDef = TypedDict(
    "GetDeploymentsRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetDocumentationPartRequestRequestTypeDef = TypedDict(
    "GetDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
    },
)
GetDocumentationPartsRequestRequestTypeDef = TypedDict(
    "GetDocumentationPartsRequestRequestTypeDef",
    {
        "restApiId": str,
        "type": NotRequired[DocumentationPartTypeType],
        "nameQuery": NotRequired[str],
        "path": NotRequired[str],
        "position": NotRequired[str],
        "limit": NotRequired[int],
        "locationStatus": NotRequired[LocationStatusTypeType],
    },
)
GetDocumentationVersionRequestRequestTypeDef = TypedDict(
    "GetDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
    },
)
GetDocumentationVersionsRequestRequestTypeDef = TypedDict(
    "GetDocumentationVersionsRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetDomainNameRequestRequestTypeDef = TypedDict(
    "GetDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
    },
)
GetDomainNamesRequestRequestTypeDef = TypedDict(
    "GetDomainNamesRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetExportRequestRequestTypeDef = TypedDict(
    "GetExportRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "exportType": str,
        "parameters": NotRequired[Mapping[str, str]],
        "accepts": NotRequired[str],
    },
)
GetGatewayResponseRequestRequestTypeDef = TypedDict(
    "GetGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
    },
)
GetGatewayResponsesRequestRequestTypeDef = TypedDict(
    "GetGatewayResponsesRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetIntegrationRequestRequestTypeDef = TypedDict(
    "GetIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
GetIntegrationResponseRequestRequestTypeDef = TypedDict(
    "GetIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
GetMethodRequestRequestTypeDef = TypedDict(
    "GetMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
    },
)
GetMethodResponseRequestRequestTypeDef = TypedDict(
    "GetMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
    },
)
GetModelRequestRequestTypeDef = TypedDict(
    "GetModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
        "flatten": NotRequired[bool],
    },
)
GetModelTemplateRequestRequestTypeDef = TypedDict(
    "GetModelTemplateRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
    },
)
GetModelsRequestRequestTypeDef = TypedDict(
    "GetModelsRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetRequestValidatorRequestRequestTypeDef = TypedDict(
    "GetRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
    },
)
GetRequestValidatorsRequestRequestTypeDef = TypedDict(
    "GetRequestValidatorsRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetResourceRequestRequestTypeDef = TypedDict(
    "GetResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "embed": NotRequired[Sequence[str]],
    },
)
GetResourcesRequestRequestTypeDef = TypedDict(
    "GetResourcesRequestRequestTypeDef",
    {
        "restApiId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
        "embed": NotRequired[Sequence[str]],
    },
)
GetRestApiRequestRequestTypeDef = TypedDict(
    "GetRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
    },
)
GetRestApisRequestRequestTypeDef = TypedDict(
    "GetRestApisRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetSdkRequestRequestTypeDef = TypedDict(
    "GetSdkRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "sdkType": str,
        "parameters": NotRequired[Mapping[str, str]],
    },
)
GetSdkTypeRequestRequestTypeDef = TypedDict(
    "GetSdkTypeRequestRequestTypeDef",
    {
        "id": str,
    },
)
GetSdkTypesRequestRequestTypeDef = TypedDict(
    "GetSdkTypesRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetStageRequestRequestTypeDef = TypedDict(
    "GetStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
    },
)
GetStagesRequestRequestTypeDef = TypedDict(
    "GetStagesRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": NotRequired[str],
    },
)
GetTagsRequestRequestTypeDef = TypedDict(
    "GetTagsRequestRequestTypeDef",
    {
        "resourceArn": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetUsagePlanKeyRequestRequestTypeDef = TypedDict(
    "GetUsagePlanKeyRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
    },
)
GetUsagePlanKeysRequestRequestTypeDef = TypedDict(
    "GetUsagePlanKeysRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "position": NotRequired[str],
        "limit": NotRequired[int],
        "nameQuery": NotRequired[str],
    },
)
GetUsagePlanRequestRequestTypeDef = TypedDict(
    "GetUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
    },
)
GetUsagePlansRequestRequestTypeDef = TypedDict(
    "GetUsagePlansRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "keyId": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetUsageRequestRequestTypeDef = TypedDict(
    "GetUsageRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "keyId": NotRequired[str],
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
GetVpcLinkRequestRequestTypeDef = TypedDict(
    "GetVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
    },
)
GetVpcLinksRequestRequestTypeDef = TypedDict(
    "GetVpcLinksRequestRequestTypeDef",
    {
        "position": NotRequired[str],
        "limit": NotRequired[int],
    },
)
IntegrationResponseTypeDef = TypedDict(
    "IntegrationResponseTypeDef",
    {
        "statusCode": NotRequired[str],
        "selectionPattern": NotRequired[str],
        "responseParameters": NotRequired[Dict[str, str]],
        "responseTemplates": NotRequired[Dict[str, str]],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
    },
)
TlsConfigTypeDef = TypedDict(
    "TlsConfigTypeDef",
    {
        "insecureSkipVerification": NotRequired[bool],
    },
)
MethodResponseTypeDef = TypedDict(
    "MethodResponseTypeDef",
    {
        "statusCode": NotRequired[str],
        "responseParameters": NotRequired[Dict[str, bool]],
        "responseModels": NotRequired[Dict[str, str]],
    },
)
MethodSettingTypeDef = TypedDict(
    "MethodSettingTypeDef",
    {
        "metricsEnabled": NotRequired[bool],
        "loggingLevel": NotRequired[str],
        "dataTraceEnabled": NotRequired[bool],
        "throttlingBurstLimit": NotRequired[int],
        "throttlingRateLimit": NotRequired[float],
        "cachingEnabled": NotRequired[bool],
        "cacheTtlInSeconds": NotRequired[int],
        "cacheDataEncrypted": NotRequired[bool],
        "requireAuthorizationForCacheControl": NotRequired[bool],
        "unauthorizedCacheControlHeaderStrategy": NotRequired[
            UnauthorizedCacheControlHeaderStrategyType
        ],
    },
)
ModelTypeDef = TypedDict(
    "ModelTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "schema": NotRequired[str],
        "contentType": NotRequired[str],
    },
)
PatchOperationTypeDef = TypedDict(
    "PatchOperationTypeDef",
    {
        "op": NotRequired[OpType],
        "path": NotRequired[str],
        "value": NotRequired[str],
        "from": NotRequired[str],
    },
)
PutGatewayResponseRequestRequestTypeDef = TypedDict(
    "PutGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
        "statusCode": NotRequired[str],
        "responseParameters": NotRequired[Mapping[str, str]],
        "responseTemplates": NotRequired[Mapping[str, str]],
    },
)
PutIntegrationResponseRequestRequestTypeDef = TypedDict(
    "PutIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
        "selectionPattern": NotRequired[str],
        "responseParameters": NotRequired[Mapping[str, str]],
        "responseTemplates": NotRequired[Mapping[str, str]],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
    },
)
PutMethodRequestRequestTypeDef = TypedDict(
    "PutMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": NotRequired[str],
        "apiKeyRequired": NotRequired[bool],
        "operationName": NotRequired[str],
        "requestParameters": NotRequired[Mapping[str, bool]],
        "requestModels": NotRequired[Mapping[str, str]],
        "requestValidatorId": NotRequired[str],
        "authorizationScopes": NotRequired[Sequence[str]],
    },
)
PutMethodResponseRequestRequestTypeDef = TypedDict(
    "PutMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
        "responseParameters": NotRequired[Mapping[str, bool]],
        "responseModels": NotRequired[Mapping[str, str]],
    },
)
RequestValidatorTypeDef = TypedDict(
    "RequestValidatorTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "validateRequestBody": NotRequired[bool],
        "validateRequestParameters": NotRequired[bool],
    },
)
SdkConfigurationPropertyTypeDef = TypedDict(
    "SdkConfigurationPropertyTypeDef",
    {
        "name": NotRequired[str],
        "friendlyName": NotRequired[str],
        "description": NotRequired[str],
        "required": NotRequired[bool],
        "defaultValue": NotRequired[str],
    },
)
TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tags": Mapping[str, str],
    },
)
TestInvokeAuthorizerRequestRequestTypeDef = TypedDict(
    "TestInvokeAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
        "headers": NotRequired[Mapping[str, str]],
        "multiValueHeaders": NotRequired[Mapping[str, Sequence[str]]],
        "pathWithQueryString": NotRequired[str],
        "body": NotRequired[str],
        "stageVariables": NotRequired[Mapping[str, str]],
        "additionalContext": NotRequired[Mapping[str, str]],
    },
)
TestInvokeMethodRequestRequestTypeDef = TypedDict(
    "TestInvokeMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "pathWithQueryString": NotRequired[str],
        "body": NotRequired[str],
        "headers": NotRequired[Mapping[str, str]],
        "multiValueHeaders": NotRequired[Mapping[str, Sequence[str]]],
        "clientCertificateId": NotRequired[str],
        "stageVariables": NotRequired[Mapping[str, str]],
    },
)
UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "resourceArn": str,
        "tagKeys": Sequence[str],
    },
)
UsagePlanKeyTypeDef = TypedDict(
    "UsagePlanKeyTypeDef",
    {
        "id": NotRequired[str],
        "type": NotRequired[str],
        "value": NotRequired[str],
        "name": NotRequired[str],
    },
)
VpcLinkTypeDef = TypedDict(
    "VpcLinkTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "targetArns": NotRequired[List[str]],
        "status": NotRequired[VpcLinkStatusType],
        "statusMessage": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ApiKeyIdsTypeDef = TypedDict(
    "ApiKeyIdsTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApiKeyResponseTypeDef = TypedDict(
    "ApiKeyResponseTypeDef",
    {
        "id": str,
        "value": str,
        "name": str,
        "customerId": str,
        "description": str,
        "enabled": bool,
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "stageKeys": List[str],
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizerResponseTypeDef = TypedDict(
    "AuthorizerResponseTypeDef",
    {
        "id": str,
        "name": str,
        "type": AuthorizerTypeType,
        "providerARNs": List[str],
        "authType": str,
        "authorizerUri": str,
        "authorizerCredentials": str,
        "identitySource": str,
        "identityValidationExpression": str,
        "authorizerResultTtlInSeconds": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BasePathMappingResponseTypeDef = TypedDict(
    "BasePathMappingResponseTypeDef",
    {
        "basePath": str,
        "restApiId": str,
        "stage": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ClientCertificateResponseTypeDef = TypedDict(
    "ClientCertificateResponseTypeDef",
    {
        "clientCertificateId": str,
        "description": str,
        "pemEncodedCertificate": str,
        "createdDate": datetime,
        "expirationDate": datetime,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentationPartIdsTypeDef = TypedDict(
    "DocumentationPartIdsTypeDef",
    {
        "ids": List[str],
        "warnings": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentationVersionResponseTypeDef = TypedDict(
    "DocumentationVersionResponseTypeDef",
    {
        "version": str,
        "createdDate": datetime,
        "description": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ExportResponseTypeDef = TypedDict(
    "ExportResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GatewayResponseResponseTypeDef = TypedDict(
    "GatewayResponseResponseTypeDef",
    {
        "responseType": GatewayResponseTypeType,
        "statusCode": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "defaultResponse": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationResponseResponseTypeDef = TypedDict(
    "IntegrationResponseResponseTypeDef",
    {
        "statusCode": str,
        "selectionPattern": str,
        "responseParameters": Dict[str, str],
        "responseTemplates": Dict[str, str],
        "contentHandling": ContentHandlingStrategyType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MethodResponseResponseTypeDef = TypedDict(
    "MethodResponseResponseTypeDef",
    {
        "statusCode": str,
        "responseParameters": Dict[str, bool],
        "responseModels": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ModelResponseTypeDef = TypedDict(
    "ModelResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "schema": str,
        "contentType": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RequestValidatorResponseTypeDef = TypedDict(
    "RequestValidatorResponseTypeDef",
    {
        "id": str,
        "name": str,
        "validateRequestBody": bool,
        "validateRequestParameters": bool,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SdkResponseTypeDef = TypedDict(
    "SdkResponseTypeDef",
    {
        "contentType": str,
        "contentDisposition": str,
        "body": StreamingBody,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TagsTypeDef = TypedDict(
    "TagsTypeDef",
    {
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TemplateTypeDef = TypedDict(
    "TemplateTypeDef",
    {
        "value": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestInvokeAuthorizerResponseTypeDef = TypedDict(
    "TestInvokeAuthorizerResponseTypeDef",
    {
        "clientStatus": int,
        "log": str,
        "latency": int,
        "principalId": str,
        "policy": str,
        "authorization": Dict[str, List[str]],
        "claims": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
TestInvokeMethodResponseTypeDef = TypedDict(
    "TestInvokeMethodResponseTypeDef",
    {
        "status": int,
        "body": str,
        "headers": Dict[str, str],
        "multiValueHeaders": Dict[str, List[str]],
        "log": str,
        "latency": int,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsagePlanKeyResponseTypeDef = TypedDict(
    "UsagePlanKeyResponseTypeDef",
    {
        "id": str,
        "type": str,
        "value": str,
        "name": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsageTypeDef = TypedDict(
    "UsageTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "position": str,
        "items": Dict[str, List[List[int]]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcLinkResponseTypeDef = TypedDict(
    "VpcLinkResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "targetArns": List[str],
        "status": VpcLinkStatusType,
        "statusMessage": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AccountTypeDef = TypedDict(
    "AccountTypeDef",
    {
        "cloudwatchRoleArn": str,
        "throttleSettings": ThrottleSettingsTypeDef,
        "features": List[str],
        "apiKeyVersion": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ApiStageExtraOutputTypeDef = TypedDict(
    "ApiStageExtraOutputTypeDef",
    {
        "apiId": NotRequired[str],
        "stage": NotRequired[str],
        "throttle": NotRequired[Dict[str, ThrottleSettingsTypeDef]],
    },
)
ApiStageOutputTypeDef = TypedDict(
    "ApiStageOutputTypeDef",
    {
        "apiId": NotRequired[str],
        "stage": NotRequired[str],
        "throttle": NotRequired[Dict[str, ThrottleSettingsTypeDef]],
    },
)
ApiStageTypeDef = TypedDict(
    "ApiStageTypeDef",
    {
        "apiId": NotRequired[str],
        "stage": NotRequired[str],
        "throttle": NotRequired[Mapping[str, ThrottleSettingsTypeDef]],
    },
)
ApiKeysTypeDef = TypedDict(
    "ApiKeysTypeDef",
    {
        "warnings": List[str],
        "position": str,
        "items": List[ApiKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
AuthorizersTypeDef = TypedDict(
    "AuthorizersTypeDef",
    {
        "position": str,
        "items": List[AuthorizerTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
BasePathMappingsTypeDef = TypedDict(
    "BasePathMappingsTypeDef",
    {
        "position": str,
        "items": List[BasePathMappingTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ImportApiKeysRequestRequestTypeDef = TypedDict(
    "ImportApiKeysRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "format": Literal["csv"],
        "failOnWarnings": NotRequired[bool],
    },
)
ImportDocumentationPartsRequestRequestTypeDef = TypedDict(
    "ImportDocumentationPartsRequestRequestTypeDef",
    {
        "restApiId": str,
        "body": BlobTypeDef,
        "mode": NotRequired[PutModeType],
        "failOnWarnings": NotRequired[bool],
    },
)
ImportRestApiRequestRequestTypeDef = TypedDict(
    "ImportRestApiRequestRequestTypeDef",
    {
        "body": BlobTypeDef,
        "failOnWarnings": NotRequired[bool],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
PutRestApiRequestRequestTypeDef = TypedDict(
    "PutRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
        "body": BlobTypeDef,
        "mode": NotRequired[PutModeType],
        "failOnWarnings": NotRequired[bool],
        "parameters": NotRequired[Mapping[str, str]],
    },
)
CanarySettingsUnionTypeDef = Union[CanarySettingsTypeDef, CanarySettingsOutputTypeDef]
CreateStageRequestRequestTypeDef = TypedDict(
    "CreateStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "deploymentId": str,
        "description": NotRequired[str],
        "cacheClusterEnabled": NotRequired[bool],
        "cacheClusterSize": NotRequired[CacheClusterSizeType],
        "variables": NotRequired[Mapping[str, str]],
        "documentationVersion": NotRequired[str],
        "canarySettings": NotRequired[CanarySettingsTypeDef],
        "tracingEnabled": NotRequired[bool],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ClientCertificatesTypeDef = TypedDict(
    "ClientCertificatesTypeDef",
    {
        "position": str,
        "items": List[ClientCertificateTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateApiKeyRequestRequestTypeDef = TypedDict(
    "CreateApiKeyRequestRequestTypeDef",
    {
        "name": NotRequired[str],
        "description": NotRequired[str],
        "enabled": NotRequired[bool],
        "generateDistinctId": NotRequired[bool],
        "value": NotRequired[str],
        "stageKeys": NotRequired[Sequence[StageKeyTypeDef]],
        "customerId": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
    },
)
CreateDeploymentRequestRequestTypeDef = TypedDict(
    "CreateDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": NotRequired[str],
        "stageDescription": NotRequired[str],
        "description": NotRequired[str],
        "cacheClusterEnabled": NotRequired[bool],
        "cacheClusterSize": NotRequired[CacheClusterSizeType],
        "variables": NotRequired[Mapping[str, str]],
        "canarySettings": NotRequired[DeploymentCanarySettingsTypeDef],
        "tracingEnabled": NotRequired[bool],
    },
)
CreateDocumentationPartRequestRequestTypeDef = TypedDict(
    "CreateDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "location": DocumentationPartLocationTypeDef,
        "properties": str,
    },
)
DocumentationPartResponseTypeDef = TypedDict(
    "DocumentationPartResponseTypeDef",
    {
        "id": str,
        "location": DocumentationPartLocationTypeDef,
        "properties": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DocumentationPartTypeDef = TypedDict(
    "DocumentationPartTypeDef",
    {
        "id": NotRequired[str],
        "location": NotRequired[DocumentationPartLocationTypeDef],
        "properties": NotRequired[str],
    },
)
CreateRestApiRequestRequestTypeDef = TypedDict(
    "CreateRestApiRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "version": NotRequired[str],
        "cloneFrom": NotRequired[str],
        "binaryMediaTypes": NotRequired[Sequence[str]],
        "minimumCompressionSize": NotRequired[int],
        "apiKeySource": NotRequired[ApiKeySourceTypeType],
        "endpointConfiguration": NotRequired[EndpointConfigurationTypeDef],
        "policy": NotRequired[str],
        "tags": NotRequired[Mapping[str, str]],
        "disableExecuteApiEndpoint": NotRequired[bool],
    },
)
CreateDomainNameRequestRequestTypeDef = TypedDict(
    "CreateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "certificateName": NotRequired[str],
        "certificateBody": NotRequired[str],
        "certificatePrivateKey": NotRequired[str],
        "certificateChain": NotRequired[str],
        "certificateArn": NotRequired[str],
        "regionalCertificateName": NotRequired[str],
        "regionalCertificateArn": NotRequired[str],
        "endpointConfiguration": NotRequired[EndpointConfigurationTypeDef],
        "tags": NotRequired[Mapping[str, str]],
        "securityPolicy": NotRequired[SecurityPolicyType],
        "mutualTlsAuthentication": NotRequired[MutualTlsAuthenticationInputTypeDef],
        "ownershipVerificationCertificateArn": NotRequired[str],
    },
)
DeploymentResponseTypeDef = TypedDict(
    "DeploymentResponseTypeDef",
    {
        "id": str,
        "description": str,
        "createdDate": datetime,
        "apiSummary": Dict[str, Dict[str, MethodSnapshotTypeDef]],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentTypeDef = TypedDict(
    "DeploymentTypeDef",
    {
        "id": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "apiSummary": NotRequired[Dict[str, Dict[str, MethodSnapshotTypeDef]]],
    },
)
DocumentationVersionsTypeDef = TypedDict(
    "DocumentationVersionsTypeDef",
    {
        "position": str,
        "items": List[DocumentationVersionTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestApiResponseTypeDef = TypedDict(
    "RestApiResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "createdDate": datetime,
        "version": str,
        "warnings": List[str],
        "binaryMediaTypes": List[str],
        "minimumCompressionSize": int,
        "apiKeySource": ApiKeySourceTypeType,
        "endpointConfiguration": EndpointConfigurationOutputTypeDef,
        "policy": str,
        "tags": Dict[str, str],
        "disableExecuteApiEndpoint": bool,
        "rootResourceId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestApiTypeDef = TypedDict(
    "RestApiTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "createdDate": NotRequired[datetime],
        "version": NotRequired[str],
        "warnings": NotRequired[List[str]],
        "binaryMediaTypes": NotRequired[List[str]],
        "minimumCompressionSize": NotRequired[int],
        "apiKeySource": NotRequired[ApiKeySourceTypeType],
        "endpointConfiguration": NotRequired[EndpointConfigurationOutputTypeDef],
        "policy": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "disableExecuteApiEndpoint": NotRequired[bool],
        "rootResourceId": NotRequired[str],
    },
)
DomainNameResponseTypeDef = TypedDict(
    "DomainNameResponseTypeDef",
    {
        "domainName": str,
        "certificateName": str,
        "certificateArn": str,
        "certificateUploadDate": datetime,
        "regionalDomainName": str,
        "regionalHostedZoneId": str,
        "regionalCertificateName": str,
        "regionalCertificateArn": str,
        "distributionDomainName": str,
        "distributionHostedZoneId": str,
        "endpointConfiguration": EndpointConfigurationOutputTypeDef,
        "domainNameStatus": DomainNameStatusType,
        "domainNameStatusMessage": str,
        "securityPolicy": SecurityPolicyType,
        "tags": Dict[str, str],
        "mutualTlsAuthentication": MutualTlsAuthenticationTypeDef,
        "ownershipVerificationCertificateArn": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainNameTypeDef = TypedDict(
    "DomainNameTypeDef",
    {
        "domainName": NotRequired[str],
        "certificateName": NotRequired[str],
        "certificateArn": NotRequired[str],
        "certificateUploadDate": NotRequired[datetime],
        "regionalDomainName": NotRequired[str],
        "regionalHostedZoneId": NotRequired[str],
        "regionalCertificateName": NotRequired[str],
        "regionalCertificateArn": NotRequired[str],
        "distributionDomainName": NotRequired[str],
        "distributionHostedZoneId": NotRequired[str],
        "endpointConfiguration": NotRequired[EndpointConfigurationOutputTypeDef],
        "domainNameStatus": NotRequired[DomainNameStatusType],
        "domainNameStatusMessage": NotRequired[str],
        "securityPolicy": NotRequired[SecurityPolicyType],
        "tags": NotRequired[Dict[str, str]],
        "mutualTlsAuthentication": NotRequired[MutualTlsAuthenticationTypeDef],
        "ownershipVerificationCertificateArn": NotRequired[str],
    },
)
EndpointConfigurationUnionTypeDef = Union[
    EndpointConfigurationTypeDef, EndpointConfigurationExtraOutputTypeDef
]
GatewayResponsesTypeDef = TypedDict(
    "GatewayResponsesTypeDef",
    {
        "position": str,
        "items": List[GatewayResponseTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
GetApiKeysRequestGetApiKeysPaginateTypeDef = TypedDict(
    "GetApiKeysRequestGetApiKeysPaginateTypeDef",
    {
        "nameQuery": NotRequired[str],
        "customerId": NotRequired[str],
        "includeValues": NotRequired[bool],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetAuthorizersRequestGetAuthorizersPaginateTypeDef = TypedDict(
    "GetAuthorizersRequestGetAuthorizersPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef = TypedDict(
    "GetBasePathMappingsRequestGetBasePathMappingsPaginateTypeDef",
    {
        "domainName": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef = TypedDict(
    "GetClientCertificatesRequestGetClientCertificatesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDeploymentsRequestGetDeploymentsPaginateTypeDef = TypedDict(
    "GetDeploymentsRequestGetDeploymentsPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef = TypedDict(
    "GetDocumentationPartsRequestGetDocumentationPartsPaginateTypeDef",
    {
        "restApiId": str,
        "type": NotRequired[DocumentationPartTypeType],
        "nameQuery": NotRequired[str],
        "path": NotRequired[str],
        "locationStatus": NotRequired[LocationStatusTypeType],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef = TypedDict(
    "GetDocumentationVersionsRequestGetDocumentationVersionsPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetDomainNamesRequestGetDomainNamesPaginateTypeDef = TypedDict(
    "GetDomainNamesRequestGetDomainNamesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef = TypedDict(
    "GetGatewayResponsesRequestGetGatewayResponsesPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetModelsRequestGetModelsPaginateTypeDef = TypedDict(
    "GetModelsRequestGetModelsPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef = TypedDict(
    "GetRequestValidatorsRequestGetRequestValidatorsPaginateTypeDef",
    {
        "restApiId": str,
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetResourcesRequestGetResourcesPaginateTypeDef = TypedDict(
    "GetResourcesRequestGetResourcesPaginateTypeDef",
    {
        "restApiId": str,
        "embed": NotRequired[Sequence[str]],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetRestApisRequestGetRestApisPaginateTypeDef = TypedDict(
    "GetRestApisRequestGetRestApisPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetSdkTypesRequestGetSdkTypesPaginateTypeDef = TypedDict(
    "GetSdkTypesRequestGetSdkTypesPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef = TypedDict(
    "GetUsagePlanKeysRequestGetUsagePlanKeysPaginateTypeDef",
    {
        "usagePlanId": str,
        "nameQuery": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetUsagePlansRequestGetUsagePlansPaginateTypeDef = TypedDict(
    "GetUsagePlansRequestGetUsagePlansPaginateTypeDef",
    {
        "keyId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetUsageRequestGetUsagePaginateTypeDef = TypedDict(
    "GetUsageRequestGetUsagePaginateTypeDef",
    {
        "usagePlanId": str,
        "startDate": str,
        "endDate": str,
        "keyId": NotRequired[str],
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
GetVpcLinksRequestGetVpcLinksPaginateTypeDef = TypedDict(
    "GetVpcLinksRequestGetVpcLinksPaginateTypeDef",
    {
        "PaginationConfig": NotRequired[PaginatorConfigTypeDef],
    },
)
IntegrationExtraResponseTypeDef = TypedDict(
    "IntegrationExtraResponseTypeDef",
    {
        "type": IntegrationTypeType,
        "httpMethod": str,
        "uri": str,
        "connectionType": ConnectionTypeType,
        "connectionId": str,
        "credentials": str,
        "requestParameters": Dict[str, str],
        "requestTemplates": Dict[str, str],
        "passthroughBehavior": str,
        "contentHandling": ContentHandlingStrategyType,
        "timeoutInMillis": int,
        "cacheNamespace": str,
        "cacheKeyParameters": List[str],
        "integrationResponses": Dict[str, IntegrationResponseTypeDef],
        "tlsConfig": TlsConfigTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
IntegrationTypeDef = TypedDict(
    "IntegrationTypeDef",
    {
        "type": NotRequired[IntegrationTypeType],
        "httpMethod": NotRequired[str],
        "uri": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "connectionId": NotRequired[str],
        "credentials": NotRequired[str],
        "requestParameters": NotRequired[Dict[str, str]],
        "requestTemplates": NotRequired[Dict[str, str]],
        "passthroughBehavior": NotRequired[str],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
        "timeoutInMillis": NotRequired[int],
        "cacheNamespace": NotRequired[str],
        "cacheKeyParameters": NotRequired[List[str]],
        "integrationResponses": NotRequired[Dict[str, IntegrationResponseTypeDef]],
        "tlsConfig": NotRequired[TlsConfigTypeDef],
    },
)
PutIntegrationRequestRequestTypeDef = TypedDict(
    "PutIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "type": IntegrationTypeType,
        "integrationHttpMethod": NotRequired[str],
        "uri": NotRequired[str],
        "connectionType": NotRequired[ConnectionTypeType],
        "connectionId": NotRequired[str],
        "credentials": NotRequired[str],
        "requestParameters": NotRequired[Mapping[str, str]],
        "requestTemplates": NotRequired[Mapping[str, str]],
        "passthroughBehavior": NotRequired[str],
        "cacheNamespace": NotRequired[str],
        "cacheKeyParameters": NotRequired[Sequence[str]],
        "contentHandling": NotRequired[ContentHandlingStrategyType],
        "timeoutInMillis": NotRequired[int],
        "tlsConfig": NotRequired[TlsConfigTypeDef],
    },
)
StageResponseTypeDef = TypedDict(
    "StageResponseTypeDef",
    {
        "deploymentId": str,
        "clientCertificateId": str,
        "stageName": str,
        "description": str,
        "cacheClusterEnabled": bool,
        "cacheClusterSize": CacheClusterSizeType,
        "cacheClusterStatus": CacheClusterStatusType,
        "methodSettings": Dict[str, MethodSettingTypeDef],
        "variables": Dict[str, str],
        "documentationVersion": str,
        "accessLogSettings": AccessLogSettingsTypeDef,
        "canarySettings": CanarySettingsOutputTypeDef,
        "tracingEnabled": bool,
        "webAclArn": str,
        "tags": Dict[str, str],
        "createdDate": datetime,
        "lastUpdatedDate": datetime,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
StageTypeDef = TypedDict(
    "StageTypeDef",
    {
        "deploymentId": NotRequired[str],
        "clientCertificateId": NotRequired[str],
        "stageName": NotRequired[str],
        "description": NotRequired[str],
        "cacheClusterEnabled": NotRequired[bool],
        "cacheClusterSize": NotRequired[CacheClusterSizeType],
        "cacheClusterStatus": NotRequired[CacheClusterStatusType],
        "methodSettings": NotRequired[Dict[str, MethodSettingTypeDef]],
        "variables": NotRequired[Dict[str, str]],
        "documentationVersion": NotRequired[str],
        "accessLogSettings": NotRequired[AccessLogSettingsTypeDef],
        "canarySettings": NotRequired[CanarySettingsOutputTypeDef],
        "tracingEnabled": NotRequired[bool],
        "webAclArn": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
        "createdDate": NotRequired[datetime],
        "lastUpdatedDate": NotRequired[datetime],
    },
)
ModelsTypeDef = TypedDict(
    "ModelsTypeDef",
    {
        "position": str,
        "items": List[ModelTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UpdateAccountRequestRequestTypeDef = TypedDict(
    "UpdateAccountRequestRequestTypeDef",
    {
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateApiKeyRequestRequestTypeDef = TypedDict(
    "UpdateApiKeyRequestRequestTypeDef",
    {
        "apiKey": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateAuthorizerRequestRequestTypeDef = TypedDict(
    "UpdateAuthorizerRequestRequestTypeDef",
    {
        "restApiId": str,
        "authorizerId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateBasePathMappingRequestRequestTypeDef = TypedDict(
    "UpdateBasePathMappingRequestRequestTypeDef",
    {
        "domainName": str,
        "basePath": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateClientCertificateRequestRequestTypeDef = TypedDict(
    "UpdateClientCertificateRequestRequestTypeDef",
    {
        "clientCertificateId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateDeploymentRequestRequestTypeDef = TypedDict(
    "UpdateDeploymentRequestRequestTypeDef",
    {
        "restApiId": str,
        "deploymentId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateDocumentationPartRequestRequestTypeDef = TypedDict(
    "UpdateDocumentationPartRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationPartId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateDocumentationVersionRequestRequestTypeDef = TypedDict(
    "UpdateDocumentationVersionRequestRequestTypeDef",
    {
        "restApiId": str,
        "documentationVersion": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateDomainNameRequestRequestTypeDef = TypedDict(
    "UpdateDomainNameRequestRequestTypeDef",
    {
        "domainName": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateGatewayResponseRequestRequestTypeDef = TypedDict(
    "UpdateGatewayResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "responseType": GatewayResponseTypeType,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateIntegrationRequestRequestTypeDef = TypedDict(
    "UpdateIntegrationRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateIntegrationResponseRequestRequestTypeDef = TypedDict(
    "UpdateIntegrationResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateMethodRequestRequestTypeDef = TypedDict(
    "UpdateMethodRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateMethodResponseRequestRequestTypeDef = TypedDict(
    "UpdateMethodResponseRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "httpMethod": str,
        "statusCode": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateModelRequestRequestTypeDef = TypedDict(
    "UpdateModelRequestRequestTypeDef",
    {
        "restApiId": str,
        "modelName": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateRequestValidatorRequestRequestTypeDef = TypedDict(
    "UpdateRequestValidatorRequestRequestTypeDef",
    {
        "restApiId": str,
        "requestValidatorId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateResourceRequestRequestTypeDef = TypedDict(
    "UpdateResourceRequestRequestTypeDef",
    {
        "restApiId": str,
        "resourceId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateRestApiRequestRequestTypeDef = TypedDict(
    "UpdateRestApiRequestRequestTypeDef",
    {
        "restApiId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateStageRequestRequestTypeDef = TypedDict(
    "UpdateStageRequestRequestTypeDef",
    {
        "restApiId": str,
        "stageName": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateUsagePlanRequestRequestTypeDef = TypedDict(
    "UpdateUsagePlanRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateUsageRequestRequestTypeDef = TypedDict(
    "UpdateUsageRequestRequestTypeDef",
    {
        "usagePlanId": str,
        "keyId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
UpdateVpcLinkRequestRequestTypeDef = TypedDict(
    "UpdateVpcLinkRequestRequestTypeDef",
    {
        "vpcLinkId": str,
        "patchOperations": NotRequired[Sequence[PatchOperationTypeDef]],
    },
)
RequestValidatorsTypeDef = TypedDict(
    "RequestValidatorsTypeDef",
    {
        "position": str,
        "items": List[RequestValidatorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SdkTypeResponseTypeDef = TypedDict(
    "SdkTypeResponseTypeDef",
    {
        "id": str,
        "friendlyName": str,
        "description": str,
        "configurationProperties": List[SdkConfigurationPropertyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SdkTypeTypeDef = TypedDict(
    "SdkTypeTypeDef",
    {
        "id": NotRequired[str],
        "friendlyName": NotRequired[str],
        "description": NotRequired[str],
        "configurationProperties": NotRequired[List[SdkConfigurationPropertyTypeDef]],
    },
)
UsagePlanKeysTypeDef = TypedDict(
    "UsagePlanKeysTypeDef",
    {
        "position": str,
        "items": List[UsagePlanKeyTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
VpcLinksTypeDef = TypedDict(
    "VpcLinksTypeDef",
    {
        "position": str,
        "items": List[VpcLinkTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsagePlanResponseTypeDef = TypedDict(
    "UsagePlanResponseTypeDef",
    {
        "id": str,
        "name": str,
        "description": str,
        "apiStages": List[ApiStageOutputTypeDef],
        "throttle": ThrottleSettingsTypeDef,
        "quota": QuotaSettingsTypeDef,
        "productCode": str,
        "tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsagePlanTypeDef = TypedDict(
    "UsagePlanTypeDef",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "description": NotRequired[str],
        "apiStages": NotRequired[List[ApiStageOutputTypeDef]],
        "throttle": NotRequired[ThrottleSettingsTypeDef],
        "quota": NotRequired[QuotaSettingsTypeDef],
        "productCode": NotRequired[str],
        "tags": NotRequired[Dict[str, str]],
    },
)
ApiStageUnionTypeDef = Union[ApiStageTypeDef, ApiStageExtraOutputTypeDef]
DocumentationPartsTypeDef = TypedDict(
    "DocumentationPartsTypeDef",
    {
        "position": str,
        "items": List[DocumentationPartTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DeploymentsTypeDef = TypedDict(
    "DeploymentsTypeDef",
    {
        "position": str,
        "items": List[DeploymentTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
RestApisTypeDef = TypedDict(
    "RestApisTypeDef",
    {
        "position": str,
        "items": List[RestApiTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
DomainNamesTypeDef = TypedDict(
    "DomainNamesTypeDef",
    {
        "position": str,
        "items": List[DomainNameTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MethodExtraResponseTypeDef = TypedDict(
    "MethodExtraResponseTypeDef",
    {
        "httpMethod": str,
        "authorizationType": str,
        "authorizerId": str,
        "apiKeyRequired": bool,
        "requestValidatorId": str,
        "operationName": str,
        "requestParameters": Dict[str, bool],
        "requestModels": Dict[str, str],
        "methodResponses": Dict[str, MethodResponseTypeDef],
        "methodIntegration": IntegrationTypeDef,
        "authorizationScopes": List[str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
MethodTypeDef = TypedDict(
    "MethodTypeDef",
    {
        "httpMethod": NotRequired[str],
        "authorizationType": NotRequired[str],
        "authorizerId": NotRequired[str],
        "apiKeyRequired": NotRequired[bool],
        "requestValidatorId": NotRequired[str],
        "operationName": NotRequired[str],
        "requestParameters": NotRequired[Dict[str, bool]],
        "requestModels": NotRequired[Dict[str, str]],
        "methodResponses": NotRequired[Dict[str, MethodResponseTypeDef]],
        "methodIntegration": NotRequired[IntegrationTypeDef],
        "authorizationScopes": NotRequired[List[str]],
    },
)
StagesTypeDef = TypedDict(
    "StagesTypeDef",
    {
        "item": List[StageTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
SdkTypesTypeDef = TypedDict(
    "SdkTypesTypeDef",
    {
        "position": str,
        "items": List[SdkTypeTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
UsagePlansTypeDef = TypedDict(
    "UsagePlansTypeDef",
    {
        "position": str,
        "items": List[UsagePlanTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
CreateUsagePlanRequestRequestTypeDef = TypedDict(
    "CreateUsagePlanRequestRequestTypeDef",
    {
        "name": str,
        "description": NotRequired[str],
        "apiStages": NotRequired[Sequence[ApiStageUnionTypeDef]],
        "throttle": NotRequired[ThrottleSettingsTypeDef],
        "quota": NotRequired[QuotaSettingsTypeDef],
        "tags": NotRequired[Mapping[str, str]],
    },
)
ResourceResponseTypeDef = TypedDict(
    "ResourceResponseTypeDef",
    {
        "id": str,
        "parentId": str,
        "pathPart": str,
        "path": str,
        "resourceMethods": Dict[str, MethodTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
ResourceTypeDef = TypedDict(
    "ResourceTypeDef",
    {
        "id": NotRequired[str],
        "parentId": NotRequired[str],
        "pathPart": NotRequired[str],
        "path": NotRequired[str],
        "resourceMethods": NotRequired[Dict[str, MethodTypeDef]],
    },
)
ResourcesTypeDef = TypedDict(
    "ResourcesTypeDef",
    {
        "position": str,
        "items": List[ResourceTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
