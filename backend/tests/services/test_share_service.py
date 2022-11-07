from unittest.mock import patch
import pytest
from fastapi import HTTPException
from services import share_service
from tests.test_utils import get_datetime_of_next_day, get_datetime_of_previous_day, email_example, token_example


@patch("repositories.share_token_repository.get_existing_token")
@patch("repositories.share_token_repository.create_token")
@pytest.mark.asyncio
async def test_get_share_token_create_new_token(repo_create_token, repo_get_existing_token):
    expiration_date = get_datetime_of_next_day()
    expected_token = token_example

    repo_get_existing_token.return_value = None
    repo_create_token.return_value = expected_token

    token = share_service.get_share_token(email_example, expiration_date)

    assert token == expected_token
    repo_get_existing_token.assert_called_once_with(email_example, expiration_date)
    repo_create_token.assert_called_once_with(email_example, expiration_date)


@patch("repositories.share_token_repository.get_email_expiration_date")
@pytest.mark.asyncio
async def test_successful_validation(get_email_expiration_date):
    expiration_date = get_datetime_of_next_day()

    get_email_expiration_date.return_value = email_example, expiration_date

    share_service.validate_token(token_example, email_example)


@patch("repositories.share_token_repository.get_email_expiration_date")
@pytest.mark.asyncio
async def test_invalid_token(get_email_expiration_date):
    token = 'safdasdfa'

    get_email_expiration_date.side_effect = Exception

    with pytest.raises(HTTPException) as error:
        share_service.validate_token(token, email_example)

    assert error.value.status_code == 404


@patch("repositories.share_token_repository.get_email_expiration_date")
@pytest.mark.asyncio
async def test_invalid_email(get_email_expiration_date):
    expiration_date = get_datetime_of_next_day()

    get_email_expiration_date.return_value = 'wrong@email', expiration_date

    with pytest.raises(HTTPException) as error:
        share_service.validate_token(token_example, email_example)

    assert error.value.status_code == 401


@patch("repositories.share_token_repository.get_email_expiration_date")
@pytest.mark.asyncio
async def test_expired_link(get_email_expiration_date):
    expiration_date = get_datetime_of_previous_day()

    get_email_expiration_date.return_value = email_example, expiration_date

    with pytest.raises(HTTPException) as error:
        share_service.validate_token(token_example, email_example)

    assert error.value.status_code == 401
