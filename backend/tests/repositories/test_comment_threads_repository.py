import uuid
import pytest
from models.chart_data_feature import ChartDataFeature
from models.chart_data_point import ChartDataPoint
from models.country import Country
from models.comment import Comment
from repositories.comment_threads_repository import (
    load_initial_values,
    initial_threads,
    get_all,
    get,
    get_by_data_point, create_thread, threads, add_comment_to_thread
)


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    # execute before all tests
    load_initial_values()


@pytest.mark.asyncio
async def test_get_all_matches_the_initial_values():
    comment_threads = get_all()
    for comment_thread, initial_thread in zip(comment_threads, initial_threads):
        assert comment_thread.chart_data_point == initial_thread.chart_data_point
        assert comment_thread.comments_count == initial_thread.comments_count
        assert comment_thread.id == initial_thread.id


@pytest.mark.asyncio
async def test_get_non_existing_thread():
    assert get(uuid.uuid4()) is None
    # self.assertIsNone()


@pytest.mark.asyncio
async def test_get_existing_thread():
    for thread in initial_threads:
        assert get(thread.id), thread


@pytest.mark.asyncio
async def test_get_by_data_point():
    """TODO: use a provider to get all existing threads"""
    existing_thread = initial_threads[0]
    existing_data_point = existing_thread.chart_data_point
    result = get_by_data_point(existing_data_point)

    assert result == existing_thread


@pytest.mark.asyncio
async def test_get_by_data_point_non_existing_data_point():
    """TODO: use a provider to get mocked non existing ChartDataPoint"""
    assert get_by_data_point(
        ChartDataPoint(
            feature=ChartDataFeature(ChartDataFeature.HOTDOG),
            country=Country(Country.FR)
        )
    ) is None


@pytest.mark.asyncio
async def test_create_thread():
    chart_data_point = ChartDataPoint(
        feature=ChartDataFeature(ChartDataFeature.HOTDOG),
        country=Country(Country.FR)
    )

    thread_with_comments = create_thread(
        chart_data_point,
        'my comment'
    )

    assert thread_with_comments in [t for t in threads.values()]


@pytest.mark.asyncio
async def test_add_comment_to_thread():
    existing_thread = initial_threads[0]
    previous_comment_count = existing_thread.comments_count
    comment = Comment(
        user_name='dummy',
        text='any text'
    )

    thread = add_comment_to_thread(existing_thread, comment)

    assert thread == existing_thread
    assert existing_thread.comments_count == previous_comment_count + 1
    assert comment in existing_thread.comments
