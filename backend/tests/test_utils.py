from datetime import datetime, timedelta


def get_datetime_of_next_day() -> datetime:
    return datetime.now() + timedelta(days=1)


def get_datetime_of_next_week() -> datetime:
    return datetime.now() + timedelta(days=7)


def get_datetime_of_previous_day() -> datetime:
    return datetime.now() - timedelta(days=1)


email_example = 'example@gmail.com'
token_example = 'c10f268c-81ab-4bc3-9da6-12a23532a567'
