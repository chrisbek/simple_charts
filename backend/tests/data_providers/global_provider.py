from models.chart_data_feature import ChartDataFeature
from models.chart_data_point import ChartDataPoint
from models.country import Country
from repositories.comment_threads_repository import threads


def get_provider():
    """
    :return: thread_id, expected result of comment_threads_repository.get(thread_id)
    """
    for thread in threads.values():
        yield thread.id, thread
    yield 'c10f268c-81ab-4bc3-9da6-12a23532a567', None


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
