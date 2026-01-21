import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage:
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = "https://ginandjuice.shop/login/"

    @pytest.mark.loging

    def test_loginPage(self):
        self.driver.get(self.base_url)
        self.username = '//input[@type="username"]'
        self.loginbtn = '//button[@type="submit"]'
        self.passwd = '//input[@type="password"]'
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.username))).send_keys("carlos")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.loginbtn))).click()

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.passwd))).send_keys("hunter2")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.loginbtn))).click()





