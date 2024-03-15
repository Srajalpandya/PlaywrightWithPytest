import pytest
from playwright.sync_api import sync_playwright



@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()



@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()



def open_google(page):
    page.goto("https://www.google.com/")
    assert page.title() == 'Google'



def open_orangehrm(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    assert page.title() == "OrangeHRM"

#pytest --html==test_report.html