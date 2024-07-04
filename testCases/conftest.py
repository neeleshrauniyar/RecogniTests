import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        return driver
    elif browser == "edge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=options)
        return driver
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        # options.add_experimental_option("detach", True)
        driver = webdriver.Firefox(options=options)
        return driver
    elif browser == "safari":
        # 1. Run Once: sudo safaridriver --enable
        # 2. Go to Safari>>Develop>>Developer Settings>>Check Remote Automation
        options = webdriver.SafariOptions()
        # options.add_experimental_option("detach", True)
        driver = webdriver.Safari(options=options)
        return driver
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
