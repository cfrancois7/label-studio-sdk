# This file was auto-generated by Fern from our API Definition.

import typing

from label_studio_sdk.client import AsyncLabelStudio, LabelStudio

from ..utilities import validate_response


async def test_list_(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = [
        {
            "id": 1,
            "type": "type",
            "synchronizable": True,
            "presign": True,
            "bucket": "bucket",
            "prefix": "prefix",
            "regex_filter": "regex_filter",
            "use_blob_urls": True,
            "google_application_credentials": "google_application_credentials",
            "google_project_id": "google_project_id",
            "last_sync": "2024-01-15T09:30:00Z",
            "last_sync_count": 1,
            "last_sync_job": "last_sync_job",
            "status": "initialized",
            "traceback": "traceback",
            "meta": {"meta": {"key": "value"}},
            "title": "title",
            "description": "description",
            "created_at": "2024-01-15T09:30:00Z",
            "presign_ttl": 1,
            "project": 1,
        }
    ]
    expected_types: typing.Any = (
        "list",
        {
            0: {
                "id": "integer",
                "type": None,
                "synchronizable": None,
                "presign": None,
                "bucket": None,
                "prefix": None,
                "regex_filter": None,
                "use_blob_urls": None,
                "google_application_credentials": None,
                "google_project_id": None,
                "last_sync": "datetime",
                "last_sync_count": "integer",
                "last_sync_job": None,
                "status": None,
                "traceback": None,
                "meta": ("dict", {0: (None, None)}),
                "title": None,
                "description": None,
                "created_at": "datetime",
                "presign_ttl": "integer",
                "project": "integer",
            }
        },
    )
    response = client.import_storage.gcs.list()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.gcs.list()
    validate_response(async_response, expected_response, expected_types)


async def test_create(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "presign": True,
        "presign_ttl": 1,
        "title": "title",
        "description": "description",
        "project": 1,
        "bucket": "bucket",
        "prefix": "prefix",
        "google_application_credentials": "google_application_credentials",
        "google_project_id": "google_project_id",
    }
    expected_types: typing.Any = {
        "regex_filter": None,
        "use_blob_urls": None,
        "presign": None,
        "presign_ttl": "integer",
        "title": None,
        "description": None,
        "project": "integer",
        "bucket": None,
        "prefix": None,
        "google_application_credentials": None,
        "google_project_id": None,
    }
    response = client.import_storage.gcs.create()
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.gcs.create()
    validate_response(async_response, expected_response, expected_types)


async def test_validate(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.gcs.validate() is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.gcs.validate() is None  # type: ignore[func-returns-value]


async def test_get(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "presign": True,
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "google_application_credentials": "google_application_credentials",
        "google_project_id": "google_project_id",
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "presign_ttl": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "presign": None,
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "google_application_credentials": None,
        "google_project_id": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "presign_ttl": "integer",
        "project": "integer",
    }
    response = client.import_storage.gcs.get(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.gcs.get(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_delete(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    # Type ignore to avoid mypy complaining about the function not being meant to return a value
    assert client.import_storage.gcs.delete(id=1) is None  # type: ignore[func-returns-value]

    assert await async_client.import_storage.gcs.delete(id=1) is None  # type: ignore[func-returns-value]


async def test_update(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "presign": True,
        "presign_ttl": 1,
        "title": "title",
        "description": "description",
        "project": 1,
        "bucket": "bucket",
        "prefix": "prefix",
        "google_application_credentials": "google_application_credentials",
        "google_project_id": "google_project_id",
    }
    expected_types: typing.Any = {
        "regex_filter": None,
        "use_blob_urls": None,
        "presign": None,
        "presign_ttl": "integer",
        "title": None,
        "description": None,
        "project": "integer",
        "bucket": None,
        "prefix": None,
        "google_application_credentials": None,
        "google_project_id": None,
    }
    response = client.import_storage.gcs.update(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.gcs.update(id=1)
    validate_response(async_response, expected_response, expected_types)


async def test_sync(client: LabelStudio, async_client: AsyncLabelStudio) -> None:
    expected_response = {
        "id": 1,
        "type": "type",
        "synchronizable": True,
        "presign": True,
        "bucket": "bucket",
        "prefix": "prefix",
        "regex_filter": "regex_filter",
        "use_blob_urls": True,
        "google_application_credentials": "google_application_credentials",
        "google_project_id": "google_project_id",
        "last_sync": "2024-01-15T09:30:00Z",
        "last_sync_count": 1,
        "last_sync_job": "last_sync_job",
        "status": "initialized",
        "traceback": "traceback",
        "meta": {"meta": {"key": "value"}},
        "title": "title",
        "description": "description",
        "created_at": "2024-01-15T09:30:00Z",
        "presign_ttl": 1,
        "project": 1,
    }
    expected_types: typing.Any = {
        "id": "integer",
        "type": None,
        "synchronizable": None,
        "presign": None,
        "bucket": None,
        "prefix": None,
        "regex_filter": None,
        "use_blob_urls": None,
        "google_application_credentials": None,
        "google_project_id": None,
        "last_sync": "datetime",
        "last_sync_count": "integer",
        "last_sync_job": None,
        "status": None,
        "traceback": None,
        "meta": ("dict", {0: (None, None)}),
        "title": None,
        "description": None,
        "created_at": "datetime",
        "presign_ttl": "integer",
        "project": "integer",
    }
    response = client.import_storage.gcs.sync(id=1)
    validate_response(response, expected_response, expected_types)

    async_response = await async_client.import_storage.gcs.sync(id=1)
    validate_response(async_response, expected_response, expected_types)
