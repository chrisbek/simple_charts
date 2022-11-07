from datetime import datetime
from uuid import uuid4
from threading import Lock

"""
For this simplified example we are using two dictionaries in order to 
map the relations between (email, expiration_date) and tokens.
If a MySQL was used, the schema would look like:
    Table: token_data
        key: token
        index: email, expiration_date
        
We use the two dicts in order to have O(1) access to the token using the (email, expiration_date), and vice versa.
We create a new token for every new combination of (email, expiration_date).
If the combination already exists, we return the existing.

Example:
If provided a new pair of (email, expiration_date) = (any@gmail.com, 2022-11-03T12:33:00) 
we will create the following entries:
    - token_email_expiration_date_hash_relation: {'4c6785d4-4ddc-4250-918b-46f0456c0f91': 'any@gmail.com___delim___2022-11-03T12:33:00'}
    - email_expiration_date_hash_token_relation: {'any@gmail.com___delim___2022-11-03T12:33:00': '4c6785d4-4ddc-4250-918b-46f0456c0f91'}
"""
token_email_expiration_date_hash_relation = dict()
email_expiration_date_hash_token_relation = dict()
delimeter = '___delim___'
token_lock = Lock()


def create_token(email: str, expiration_date: datetime) -> str:
    # In general there should be a token per chart but since chart is hardcoded it's ok to hardcode a single token too
    token = str(uuid4())
    token_info = _serialize_email_expiration_date(email, expiration_date)

    with token_lock:
        token_email_expiration_date_hash_relation[token] = token_info
        email_expiration_date_hash_token_relation[token_info] = token

    return token


def get_existing_token(email: str, expiration_date: datetime) -> str | None:
    key = _serialize_email_expiration_date(email, expiration_date)
    return email_expiration_date_hash_token_relation.get(key)


def get_email_expiration_date(token: str) -> (str, datetime):
    """
    :raises Exception when no token is found
    """
    value = token_email_expiration_date_hash_relation.get(token)
    if value is None:
        raise Exception('Not Found')

    return _deserialize_email_expiration_date(value)


def _serialize_email_expiration_date(email: str, expiration_date: datetime) -> str:
    return f'{email}{delimeter}{expiration_date.isoformat()}'


def _deserialize_email_expiration_date(value: str) -> (str, datetime):
    email, expiration_str = value.split(delimeter)
    return email, datetime.fromisoformat(expiration_str)
