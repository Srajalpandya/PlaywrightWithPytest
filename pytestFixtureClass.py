import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class')
def browser(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()


@pytest.fixture(scope='funtion')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.mark.usefixtures('browser')
class Test_Title_Class:
    def test_google(self, page):
        page.goto("https://www.google.com/")
        assert page.url == 'https://www.google.com/'

    def test_OrangeHRM(self, page):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert page.url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
