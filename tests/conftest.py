import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser selection"
    )
@pytest.fixture(scope="function")
def browser_setup(request):
    browser_name = request.config.getoption("browser_name")
    global driver

    if browser_name == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    elif browser_name == "firefox":
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
