import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check

class TestOurStoryPage:
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://ginandjuice.shop/about/'

    @pytest.mark.ourStory
    def test_outStoryPageload(self):
        self.driver.get(self.base_url)
        assert "about" in self.driver.current_url

    @pytest.mark.ourStory
    def test_ourStoryTitle(self):
        self.driver.get(self.base_url)
        assert "Our story - Gin & Juice Shop" in self.driver.title