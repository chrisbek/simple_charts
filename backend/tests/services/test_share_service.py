import pytest
from fastapi import HTTPException
from services import share_service


@pytest.mark.asyncio
async def test_successful_validation():
    """
    It should successfully validate issued token
    """
    token = share_service.get_share_token()

    result = share_service.validate_token(token)

    assert result is None


@pytest.mark.asyncio
async def test_failed_validation():
    """
    It should throw 404 error if worng token is passed
    """
    with pytest.raises(HTTPException) as error:
        share_service.validate_token("bad_token")

    assert error.value.status_code == 404
