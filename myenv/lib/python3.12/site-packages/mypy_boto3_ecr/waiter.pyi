"""
Type annotations for ecr service client waiters.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ecr.client import ECRClient
    from mypy_boto3_ecr.waiter import (
        ImageScanCompleteWaiter,
        LifecyclePolicyPreviewCompleteWaiter,
    )

    session = Session()
    client: ECRClient = session.client("ecr")

    image_scan_complete_waiter: ImageScanCompleteWaiter = client.get_waiter("image_scan_complete")
    lifecycle_policy_preview_complete_waiter: LifecyclePolicyPreviewCompleteWaiter = client.get_waiter("lifecycle_policy_preview_complete")
    ```
"""

from typing import Sequence

from botocore.waiter import Waiter

from .type_defs import (
    ImageIdentifierTypeDef,
    LifecyclePolicyPreviewFilterTypeDef,
    WaiterConfigTypeDef,
)

__all__ = ("ImageScanCompleteWaiter", "LifecyclePolicyPreviewCompleteWaiter")

class ImageScanCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.ImageScanComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters/#imagescancompletewaiter)
    """

    def wait(
        self,
        *,
        repositoryName: str,
        imageId: ImageIdentifierTypeDef,
        registryId: str = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        WaiterConfig: WaiterConfigTypeDef = ...,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.ImageScanComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters/#imagescancompletewaiter)
        """

class LifecyclePolicyPreviewCompleteWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters/#lifecyclepolicypreviewcompletewaiter)
    """

    def wait(
        self,
        *,
        repositoryName: str,
        registryId: str = ...,
        imageIds: Sequence[ImageIdentifierTypeDef] = ...,
        nextToken: str = ...,
        maxResults: int = ...,
        filter: LifecyclePolicyPreviewFilterTypeDef = ...,
        WaiterConfig: WaiterConfigTypeDef = ...,
    ) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ecr.html#ECR.Waiter.LifecyclePolicyPreviewComplete.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ecr/waiters/#lifecyclepolicypreviewcompletewaiter)
        """
