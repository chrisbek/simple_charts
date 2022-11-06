import json
import pytest

from services.data_service import (
    get_chart_data
)

chart_data: list = json.load(open('stub_data/chart_data.json'))


@pytest.mark.asyncio
async def test_get_chart_data_returns_correct_data():
    result = get_chart_data()
    assert result == chart_data
