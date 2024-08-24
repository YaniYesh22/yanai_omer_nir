"""
Type annotations for signer service client waiters.

[Open documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters/)

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_signer.client import SignerClient
    from mypy_boto3_signer.waiter import (
        SuccessfulSigningJobWaiter,
    )

    session = Session()
    client: SignerClient = session.client("signer")

    successful_signing_job_waiter: SuccessfulSigningJobWaiter = client.get_waiter("successful_signing_job")
    ```
"""

from botocore.waiter import Waiter

from .type_defs import WaiterConfigTypeDef

__all__ = ("SuccessfulSigningJobWaiter",)


class SuccessfulSigningJobWaiter(Waiter):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters/#successfulsigningjobwaiter)
    """

    def wait(self, *, jobId: str, WaiterConfig: WaiterConfigTypeDef = ...) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/signer.html#Signer.Waiter.SuccessfulSigningJob.wait)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_signer/waiters/#successfulsigningjobwaiter)
        """
