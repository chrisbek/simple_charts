import pytest
from repositories.share_token_repository import (
    delimeter,
    token_email_expiration_date_hash_relation,
    email_expiration_date_hash_token_relation,
    create_token,
    get_existing_token,
    get_email_expiration_date
)
from tests.data_providers import global_provider


@pytest.mark.parametrize("email, expiration_date", global_provider.get_valid_email_expiration_date_pairs())
@pytest.mark.asyncio
async def test_create_token(email, expiration_date):
    token = create_token(email, expiration_date)

    assert isinstance(token, str)
    assert token in token_email_expiration_date_hash_relation
    assert f'{email}{delimeter}{expiration_date.isoformat()}' in email_expiration_date_hash_token_relation


@pytest.mark.parametrize("email, expiration_date", global_provider.get_valid_email_expiration_date_pairs())
@pytest.mark.asyncio
async def test_get_existing_token(email, expiration_date):
    expected_token = create_token(email, expiration_date)

    assert get_existing_token(email, expiration_date) == expected_token


@pytest.mark.asyncio
async def test_get_email_expiration_date_raises_exception_if_not_found():
    with pytest.raises(Exception):
        get_email_expiration_date('non existing token')


@pytest.mark.parametrize(
    "expected_email, expected_expiration_date", global_provider.get_valid_email_expiration_date_pairs())
@pytest.mark.asyncio
async def test_get_email_expiration_date(expected_email, expected_expiration_date):
    token = create_token(expected_email, expected_expiration_date)

    email, expiration_date = get_email_expiration_date(token)
    assert email == expected_email
    assert expiration_date == expected_expiration_date
