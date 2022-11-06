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
from tests.data_providers import global_provider


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


@pytest.mark.parametrize("thread_id, expected", global_provider.get_provider())
@pytest.mark.asyncio
async def test_get_existing_thread(thread_id, expected):
    assert get(thread_id) == expected


@pytest.mark.parametrize("chart_data_point, expected_result", global_provider.get_by_data_point_provider())
@pytest.mark.asyncio
async def test_get_by_data_point(chart_data_point, expected_result):
    assert get_by_data_point(chart_data_point) == expected_result


@pytest.mark.parametrize("new_chart_data_point, existing_threads", global_provider.create_thread_provider())
@pytest.mark.asyncio
async def test_create_thread(new_chart_data_point, existing_threads):
    thread_with_comments = create_thread(
        new_chart_data_point,
        'my comment'
    )

    assert thread_with_comments in existing_threads


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
