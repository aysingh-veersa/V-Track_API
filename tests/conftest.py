import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture(scope="class")
def init_driver(request, browser):
    driver = ""
    if browser == "chrome":
        driver = webdriver.Chrome()

    else:
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    url = "https://vtrack-dev-web.azurewebsites.net/dashboard"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(60)
    request.cls.driver = driver
    yield
    driver.close()
    
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    
    
@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption("--browser")
    

@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass