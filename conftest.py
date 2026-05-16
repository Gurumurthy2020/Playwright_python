import pytest
from playwright.sync_api import Playwright, expect


@pytest.fixture
def user_credentials(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store",default="chrome")

@pytest.fixture
def browserInstance(playwright:Playwright,request):
    browser_name=request.config.getoption("--browser_name")
    if browser_name=="chrome":
        browser = playwright.chromium.launch(headless=False)
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    # context.tracing.start(
    #     screenshots=True,
    #     snapshots=True,
    #     sources=True
    # )
    page = context.new_page()
    yield page
    # context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()