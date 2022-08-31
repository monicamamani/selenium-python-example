# from behave import fixture, use_fixture
# from behave4my_project.fixtures import wsgi_server
# from selenium import webdriver
from behave import fixture
from pages.search_page import SearchPage
import os
import warnings
from pathlib import Path
import yaml

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium.webdriver.firefox.service import Service as ServiceFirefox
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'

def config():
    path = Path(__file__).parent / "../data/config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()


@fixture
def selenium_browser_chrome(context):
    path = Path(__file__).parent / "../data/config.yaml"
    try:
        with open(path) as config_file:
            data = yaml.load(config_file, Loader=yaml.FullLoader)
        return data
    finally:
        config_file.close()

def before_all(context):
    warnings.simplefilter("ignore", ResourceWarning)
    if config()['browser'] == 'chrome':
        options = webdriver.ChromeOptions()
        if config()['headless']:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(service=ServiceChrome(ChromeDriverManager().install()), options=options)
    elif config()['browser'] == 'firefox':
        options = webdriver.FirefoxOptions()
        if config()['headless']:
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
            options.add_argument('--window-size=1920,1080')
        driver = webdriver.Firefox(service=ServiceFirefox(GeckoDriverManager().install()), options=options)
    else:
        raise Exception("Incorrect Browser")

    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    yield wait, driver

    if driver is not None:
        driver.close()
        driver.quit()

    context.page = SearchPage(context.feature.driver, context.feature.wait)
    context.page.go_to_search_page()
#
# @fixture
# def selenium_browser_chrome(context):
#     # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
#     context.browser = webdriver.Chrome()
#     yield context.browser
#     # -- CLEANUP-FIXTURE PART:
#     context.browser.quit()
#
# def before_all(context):
#     use_fixture(wsgi_server, context, port=8000)
#     use_fixture(selenium_browser_chrome, context)
#     # -- HINT: CLEANUP-FIXTURE is performed after after_all() hook is called.
#
# def before_feature(context, feature):
#     model.init(environment='test')