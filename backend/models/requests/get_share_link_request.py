from pydantic import BaseModel, validator
from datetime import datetime


class ShareDataDto(BaseModel):
    """
    For simplicity, we don't validate the email in the backend. In a real world prod app we would do.
    """
    email: str
    expiration_date: datetime

    @validator('expiration_date', pre=True)
    def ensure_expiration_date_in_iso_format(cls, v):
        try:
            return datetime.fromisoformat(v)
        except Exception:
            raise ValueError('expiration_date must be an ISO formatted string')
