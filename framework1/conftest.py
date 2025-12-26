import pytest
from pygments.lexer import default
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name",action="store",default="chrome",help="browser selection")

# Fixture for invoking the chrome browser.
@pytest.fixture(scope="function")
def invoke_chrome(request):
    options = Options()
    options.add_argument("--incognito")
    browser=request.config.getoption("--browser_name")
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver # This will return the driver object.
    driver.quit()