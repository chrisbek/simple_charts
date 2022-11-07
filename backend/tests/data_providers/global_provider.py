from models.chart_data_feature import ChartDataFeature
from models.chart_data_point import ChartDataPoint
from models.country import Country
from repositories.comment_threads_repository import threads
from tests.test_utils import get_datetime_of_next_day, get_datetime_of_next_week, token_example


def get_provider():
    """
    :return: thread_id, expected result of comment_threads_repository.get(thread_id)
    """
    for thread in threads.values():
        yield thread.id, thread
    yield token_example, None


def get_by_data_point_provider():
    """
    :return: chart_data_point, expected result of comment_threads_repository.get_by_data_point(chart_data_point)
    """
    for thread in threads.values():
        yield thread.chart_data_point, thread

    yield ChartDataPoint(
        feature=ChartDataFeature(ChartDataFeature.HOTDOG),
        country=Country(Country.FR)
    ), None


def create_thread_provider():
    """
    :return: a new chart_data_point, existing threads
    """
    yield ChartDataPoint(
        feature=ChartDataFeature(ChartDataFeature.HOTDOG),
        country=Country(Country.FR)
    ), threads.values()


def get_valid_email_expiration_date_pairs():
    yield 'test@gmail.com', get_datetime_of_next_day()
    yield 'another@gmail.com', get_datetime_of_next_day()
    yield 'another@gmail.com', get_datetime_of_next_week()
