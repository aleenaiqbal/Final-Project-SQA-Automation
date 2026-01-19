import pytest
from selenium import webdriver

@pytest.fixture(autouse=True,scope='function')
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://ginandjuice.shop/")
    request.cls.driver = driver
    yield
    driver.quit()