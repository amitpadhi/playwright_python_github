import pytest
from utils.config import BASE_URL
from tests.conftest import page, context

@pytest.mark.asyncio
async def test_dynamic_page_shows_content(page):
    await page.goto(BASE_URL + 'dynamic-content')
    assert page.url == 'https://play-qa.com/dynamic-content'


