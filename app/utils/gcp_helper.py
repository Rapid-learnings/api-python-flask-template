import datetime

from google.cloud import storage

import config
from app.exceptions.common import GcpUploadError

PRIVATE_GCP_BUCKET_NAME: str = config.PRIVATE_GCP_BUCKET_NAME
PUBLIC_GCP_BUCKET_NAME: str = config.PUBLIC_GCP_BUCKET_NAME


def get_private_presigned_url(file_name: str) -> str:
    """
    Generates a presigned URL for securely uploading a file to a private Google Cloud Storage (GCS) bucket.

    The generated URL allows for the client-side uploading of a file directly to GCS without exposing
    Google Cloud credentials. This presigned URL is specifically for private bucket access and is valid
    for 15 minutes, after which it expires and cannot be used.

    Parameters:
    - file_name (str): The name and path where the file should be stored in the bucket.

    Returns:
    - str: A presigned URL for uploading the file using a PUT request with 'application/octet-stream' content type.

    Raises:
    - GcpUploadError: If there's an issue generating the presigned URL.
    """

    bucket_name: str = PRIVATE_GCP_BUCKET_NAME

    return _generate_url(bucket_name, file_name)


def get_public_presigned_url(file_name: str) -> str:
    """
    Generates a presigned URL for securely uploading a file to a public Google Cloud Storage (GCS) bucket.

    Similar to the private presigned URL generator, this function creates a URL for uploading files
    to a publicly accessible GCS bucket. The URL facilitates client-side uploads directly to GCS, safeguarding
    Google Cloud credentials. The URL remains valid for 15 minutes before expiring.

    Parameters:
    - file_name (str): The name and path for the file's storage location in the bucket.

    Returns:
    - str: A presigned URL for file upload using a PUT request, requiring 'application/octet-stream' content type.

    Raises:
    - GcpUploadError: If generating the presigned URL fails.
    """

    bucket_name: str = PUBLIC_GCP_BUCKET_NAME

    return _generate_url(bucket_name, file_name)


def _generate_url(bucket_name: str, file_name: str) -> str:
    """
    Internal helper function to generate a GCS presigned URL for file uploads.

    This function abstracts the common logic for generating presigned URLs, reducing redundancy
    between public and private URL generation. It configures the URL to expire in 15 minutes and
    to accept PUT requests with a specific content type.

    Parameters:
    - bucket_name (str): The name of the GCS bucket where the file will be uploaded.
    - file_name (str): The intended name and path of the file within the bucket.

    Returns:
    - str: The generated presigned URL for uploading the file.

    Raises:
    - GcpUploadError: If the presigned URL generation process encounters an error.
    """

    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        content_type: str = (
            "image/jpeg"
            if file_name.endswith((".jpg", ".jpeg"))
            else (
                "image/png"
                if file_name.endswith(".png")
                else (
                    "text/csv"
                    if file_name.endswith(".csv")
                    else "application/octet-stream"
                )
            )
        )

        presigned_url: str = blob.generate_signed_url(
            version="v4",
            expiration=datetime.timedelta(minutes=15),
            method="PUT",
            content_type=content_type,
        )

        return presigned_url

    except Exception as e:
        raise GcpUploadError(description="Failed to generate GCS presigned URL.")


def download_file(user_id: str, batch_id: str, destination_path: str = None) -> str:
    """
    Downloads a file from Google Cloud Storage (GCS) to a specified local directory or temporary file.

    Parameters:
    - user_id (str): The user's unique identifier. Used to construct the file path.
    - batch_id (str): The batch's unique identifier. Used to construct the file name and path.
    - destination_path (str, optional): The destination file path for the downloaded file. If not specified,
      the file will be downloaded to '../../downloads/{batch_id}.csv'.

    Returns:
    - str: The file path of the downloaded file.
    """

    bucket_name: str = PRIVATE_GCP_BUCKET_NAME
    file_name: str = f"users/{user_id}/batches/{batch_id}/{batch_id}.csv"
    print(file_name)

    if destination_path is None:
        destination_path = f"../../downloads/{batch_id}.csv"

    try:
        # Initialize Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        # Download file
        blob = bucket.blob(file_name)
        blob.download_to_filename(destination_path)

        return destination_path

    except Exception as e:
        raise Exception(f"Failed to download file: {e}")
