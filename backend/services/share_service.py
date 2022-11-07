from datetime import datetime
from fastapi import HTTPException
from repositories import share_token_repository


def validate_token(token: str, user_email: str) -> None:
    """
    :raises HTTPException
     with 404, when token cannot be found
     with 401, when link has expired
     with 401, when email is not matching the token
    """
    try:
        expected_email, expiration_date = share_token_repository.get_email_expiration_date(token)
    except Exception:
        raise HTTPException(404, "Invalid Link")

    if user_email != expected_email:
        raise HTTPException(401, "Invalid Email")

    if expiration_date < datetime.now():
        raise HTTPException(401, "Link Expired")


def get_share_token(email: str, expiration_date: datetime) -> str:
    """
    :param email: email for which we share the link
    :param expiration_date: expiration date
    """
    token = share_token_repository.get_existing_token(email, expiration_date)
    if token:
        return token

    return share_token_repository.create_token(email, expiration_date)
