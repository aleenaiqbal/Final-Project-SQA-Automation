import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check

class TestProductPage:
    driver: WebDriver

    @pytest.mark.product

    def test_Product_page_title(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        title = self.driver.title
        print("Product Page Title:", title)
        assert "Products - Gin & Juice Shop" in title

    @pytest.mark.pageload

    def test_page_load(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        assert "catalog" in self.driver.current_url

    @pytest.mark.firstproduct

    def test_click_first_product(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        self.ViewDetails = '//span[text()="View details"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ViewDetails))).click()

    @pytest.mark.pricevisible

    def test_product_price_visible(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        self.ProductPrice = '//span[text()="$30.50"]'
        self.product_price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ProductPrice)))
        assert self.product_price.is_displayed()


    def test_product_image_visible(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        self.ProductImage = '/html/body/div[2]/section/div/section[3]/a[1]/img[1]'
        self.Image_Element =self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ProductImage)))
        assert self.Image_Element.is_displayed()

    @pytest.mark.searchproduct

    def test_search_product(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://ginandjuice.shop/catalog")
        self.search_product_input = '//input[@id="searchBar"]'
        self.search_product = '//button[@type="submit"]'

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_product_input))).send_keys("fruit")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_product))).click()

