import pytest
from repositories.share_token_repository import (
    share_token,
    get_token
)


@pytest.mark.asyncio
async def test_get_token():
    token = get_token()
    assert isinstance(token, str)
    assert token == share_token


@pytest.mark.asyncio
async def test_get_token_returns_same_result():
    assert get_token() == get_token()
