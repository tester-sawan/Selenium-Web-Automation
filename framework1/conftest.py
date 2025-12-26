import pytest
from pygments.lexer import default
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

# Fixture for invoking the chrome browser.
@pytest.fixture(scope="function")
def invoke_chrome(request):
    browser=request.config.getoption("--browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    elif browser == "firefox":
        driver = webdriver.Firefox()
    yield driver
    driver.quit()