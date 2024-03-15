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


@pytest.mark.parametrize('invalid_username, invalid_password', [ ('admin', 'admin'), ('sdfsdf', 'sdfsdgsdg')])
def test_invalid_login(page, invalid_username,invalid_password):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_selector("//input[@placeholder='username']").type(invalid_username)
    page.wait_for_selector("//input[@placeholder='password']").type(invalid_password)
    page.wait_for_selector("//button[@type='submit']").click()
    page.wait_for_timeout(3000)
    error_message = page.wait_for_selector("//div[@role='alert']//p").text_content()
    assert error_message == 'Invalid Credentials'