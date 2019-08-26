import pytest
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


@pytest.yield_fixture(scope="module", params=["firefox", "chrome"])
def driver(request):
    if request.param == "firefox":
        opt = FirefoxOptions()
        opt.headless = request.config.option.headless
        browser = webdriver.Firefox(executable_path=f"{ROOT_DIR}/drivers/geckodriver", options=opt)
    else:
        opt = ChromeOptions()
        opt.headless = request.config.option.headless
        browser = webdriver.Chrome(executable_path=f"{ROOT_DIR}/drivers/chromedriver", options=opt)

    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption("-H", "--headless", action="store_true", help="browser headless mode")
