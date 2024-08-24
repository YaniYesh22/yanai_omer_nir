"""
Type annotations for schemas service client.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/)

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_schemas.client import SchemasClient

    session = Session()
    client: SchemasClient = session.client("schemas")
    ```
"""

import sys
from typing import Any, Dict, Mapping, Sequence, Type, overload

from botocore.client import BaseClient, ClientMeta

from .literals import TypeType
from .paginator import (
    ListDiscoverersPaginator,
    ListRegistriesPaginator,
    ListSchemasPaginator,
    ListSchemaVersionsPaginator,
    SearchSchemasPaginator,
)
from .type_defs import (
    CreateDiscovererResponseTypeDef,
    CreateRegistryResponseTypeDef,
    CreateSchemaResponseTypeDef,
    DescribeCodeBindingResponseTypeDef,
    DescribeDiscovererResponseTypeDef,
    DescribeRegistryResponseTypeDef,
    DescribeSchemaResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    ExportSchemaResponseTypeDef,
    GetCodeBindingSourceResponseTypeDef,
    GetDiscoveredSchemaResponseTypeDef,
    GetResourcePolicyResponseTypeDef,
    ListDiscoverersResponseTypeDef,
    ListRegistriesResponseTypeDef,
    ListSchemasResponseTypeDef,
    ListSchemaVersionsResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    PutCodeBindingResponseTypeDef,
    PutResourcePolicyResponseTypeDef,
    SearchSchemasResponseTypeDef,
    StartDiscovererResponseTypeDef,
    StopDiscovererResponseTypeDef,
    UpdateDiscovererResponseTypeDef,
    UpdateRegistryResponseTypeDef,
    UpdateSchemaResponseTypeDef,
)
from .waiter import CodeBindingExistsWaiter

if sys.version_info >= (3, 12):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("SchemasClient",)


class BotocoreClientError(Exception):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    ForbiddenException: Type[BotocoreClientError]
    GoneException: Type[BotocoreClientError]
    InternalServerErrorException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]
    PreconditionFailedException: Type[BotocoreClientError]
    ServiceUnavailableException: Type[BotocoreClientError]
    TooManyRequestsException: Type[BotocoreClientError]
    UnauthorizedException: Type[BotocoreClientError]


class SchemasClient(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        SchemasClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.exceptions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.can_paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#can_paginate)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.close)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#close)
        """

    def create_discoverer(
        self,
        *,
        SourceArn: str,
        Description: str = ...,
        CrossAccount: bool = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateDiscovererResponseTypeDef:
        """
        Creates a discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#create_discoverer)
        """

    def create_registry(
        self, *, RegistryName: str, Description: str = ..., Tags: Mapping[str, str] = ...
    ) -> CreateRegistryResponseTypeDef:
        """
        Creates a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_registry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#create_registry)
        """

    def create_schema(
        self,
        *,
        Content: str,
        RegistryName: str,
        SchemaName: str,
        Type: TypeType,
        Description: str = ...,
        Tags: Mapping[str, str] = ...
    ) -> CreateSchemaResponseTypeDef:
        """
        Creates a schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.create_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#create_schema)
        """

    def delete_discoverer(self, *, DiscovererId: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#delete_discoverer)
        """

    def delete_registry(self, *, RegistryName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a Registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_registry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#delete_registry)
        """

    def delete_resource_policy(self, *, RegistryName: str = ...) -> EmptyResponseMetadataTypeDef:
        """
        Delete the resource-based policy attached to the specified registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_resource_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#delete_resource_policy)
        """

    def delete_schema(self, *, RegistryName: str, SchemaName: str) -> EmptyResponseMetadataTypeDef:
        """
        Delete a schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#delete_schema)
        """

    def delete_schema_version(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Delete the schema version definition See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/DeleteSchemaVersion).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.delete_schema_version)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#delete_schema_version)
        """

    def describe_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = ...
    ) -> DescribeCodeBindingResponseTypeDef:
        """
        Describe the code binding URI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_code_binding)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#describe_code_binding)
        """

    def describe_discoverer(self, *, DiscovererId: str) -> DescribeDiscovererResponseTypeDef:
        """
        Describes the discoverer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#describe_discoverer)
        """

    def describe_registry(self, *, RegistryName: str) -> DescribeRegistryResponseTypeDef:
        """
        Describes the registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_registry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#describe_registry)
        """

    def describe_schema(
        self, *, RegistryName: str, SchemaName: str, SchemaVersion: str = ...
    ) -> DescribeSchemaResponseTypeDef:
        """
        Retrieve the schema definition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.describe_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#describe_schema)
        """

    def export_schema(
        self, *, RegistryName: str, SchemaName: str, Type: str, SchemaVersion: str = ...
    ) -> ExportSchemaResponseTypeDef:
        """
        See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/ExportSchema).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.export_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#export_schema)
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

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#generate_presigned_url)
        """

    def get_code_binding_source(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = ...
    ) -> GetCodeBindingSourceResponseTypeDef:
        """
        Get the code binding source URI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_code_binding_source)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_code_binding_source)
        """

    def get_discovered_schema(
        self, *, Events: Sequence[str], Type: TypeType
    ) -> GetDiscoveredSchemaResponseTypeDef:
        """
        Get the discovered schema that was generated based on sampled events.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_discovered_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_discovered_schema)
        """

    def get_resource_policy(self, *, RegistryName: str = ...) -> GetResourcePolicyResponseTypeDef:
        """
        Retrieves the resource-based policy attached to a given registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_resource_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_resource_policy)
        """

    def list_discoverers(
        self,
        *,
        DiscovererIdPrefix: str = ...,
        Limit: int = ...,
        NextToken: str = ...,
        SourceArnPrefix: str = ...
    ) -> ListDiscoverersResponseTypeDef:
        """
        List the discoverers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_discoverers)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#list_discoverers)
        """

    def list_registries(
        self,
        *,
        Limit: int = ...,
        NextToken: str = ...,
        RegistryNamePrefix: str = ...,
        Scope: str = ...
    ) -> ListRegistriesResponseTypeDef:
        """
        List the registries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_registries)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#list_registries)
        """

    def list_schema_versions(
        self, *, RegistryName: str, SchemaName: str, Limit: int = ..., NextToken: str = ...
    ) -> ListSchemaVersionsResponseTypeDef:
        """
        Provides a list of the schema versions and related information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_schema_versions)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#list_schema_versions)
        """

    def list_schemas(
        self,
        *,
        RegistryName: str,
        Limit: int = ...,
        NextToken: str = ...,
        SchemaNamePrefix: str = ...
    ) -> ListSchemasResponseTypeDef:
        """
        List the schemas.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_schemas)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#list_schemas)
        """

    def list_tags_for_resource(self, *, ResourceArn: str) -> ListTagsForResourceResponseTypeDef:
        """
        Get tags for resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.list_tags_for_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#list_tags_for_resource)
        """

    def put_code_binding(
        self, *, Language: str, RegistryName: str, SchemaName: str, SchemaVersion: str = ...
    ) -> PutCodeBindingResponseTypeDef:
        """
        Put code binding URI See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/PutCodeBinding).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.put_code_binding)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#put_code_binding)
        """

    def put_resource_policy(
        self, *, Policy: str, RegistryName: str = ..., RevisionId: str = ...
    ) -> PutResourcePolicyResponseTypeDef:
        """
        The name of the policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.put_resource_policy)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#put_resource_policy)
        """

    def search_schemas(
        self, *, Keywords: str, RegistryName: str, Limit: int = ..., NextToken: str = ...
    ) -> SearchSchemasResponseTypeDef:
        """
        Search the schemas See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/SearchSchemas).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.search_schemas)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#search_schemas)
        """

    def start_discoverer(self, *, DiscovererId: str) -> StartDiscovererResponseTypeDef:
        """
        Starts the discoverer See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/StartDiscoverer).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.start_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#start_discoverer)
        """

    def stop_discoverer(self, *, DiscovererId: str) -> StopDiscovererResponseTypeDef:
        """
        Stops the discoverer See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/StopDiscoverer).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.stop_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#stop_discoverer)
        """

    def tag_resource(
        self, *, ResourceArn: str, Tags: Mapping[str, str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Add tags to a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.tag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#tag_resource)
        """

    def untag_resource(
        self, *, ResourceArn: str, TagKeys: Sequence[str]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Removes tags from a resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.untag_resource)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#untag_resource)
        """

    def update_discoverer(
        self, *, DiscovererId: str, Description: str = ..., CrossAccount: bool = ...
    ) -> UpdateDiscovererResponseTypeDef:
        """
        Updates the discoverer See also: [AWS API
        Documentation](https://docs.aws.amazon.com/goto/WebAPI/schemas-2019-12-02/UpdateDiscoverer).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_discoverer)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#update_discoverer)
        """

    def update_registry(
        self, *, RegistryName: str, Description: str = ...
    ) -> UpdateRegistryResponseTypeDef:
        """
        Updates a registry.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_registry)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#update_registry)
        """

    def update_schema(
        self,
        *,
        RegistryName: str,
        SchemaName: str,
        ClientTokenId: str = ...,
        Content: str = ...,
        Description: str = ...,
        Type: TypeType = ...
    ) -> UpdateSchemaResponseTypeDef:
        """
        Updates the schema definition .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.update_schema)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#update_schema)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_discoverers"]
    ) -> ListDiscoverersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_registries"]) -> ListRegistriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_paginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_schema_versions"]
    ) -> ListSchemaVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["list_schemas"]) -> ListSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_paginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["search_schemas"]) -> SearchSchemasPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_paginator)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_paginator)
        """

    def get_waiter(self, waiter_name: Literal["code_binding_exists"]) -> CodeBindingExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/schemas.html#Schemas.Client.get_waiter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_schemas/client/#get_waiter)
        """
