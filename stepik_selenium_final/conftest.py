import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BROWSERS_LIST = ("chrome", "firefox")
BASE_URL = 'http://selenium1py.pythonanywhere.com/'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name',
        action='store',
        default="chrome",
        help="Choose browser: chrome or firefox"
    )
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help="Choose language"
    )
    parser.addoption(
        '--url', "-U",
        action='store',
        default=BASE_URL,
        help='choose your host'
    )


@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='class')
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")

    if browser_name not in BROWSERS_LIST:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=profile)

    browser.implicitly_wait(10)
    yield browser
    browser.quit()
