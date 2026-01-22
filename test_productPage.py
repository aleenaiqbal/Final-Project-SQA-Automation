import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check

class TestProductPage:
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://ginandjuice.shop/catalog/'

    @pytest.mark.product

    def test_Product_page_title(self):
        self.driver.get(self.base_url)
        title = self.driver.title
        print("Product Page Title:", title)
        assert "Products - Gin & Juice Shop" in title

    @pytest.mark.product

    def test_page_load(self):
        self.driver.get(self.base_url)
        assert "catalog" in self.driver.current_url

    @pytest.mark.addproduct

    def test_click_first_product(self):
        self.driver.get(self.base_url)
        self.ViewDetails = '//span[text()="View details"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ViewDetails))).click()

        self.checkstock = '//button[text()="Check stock"]'
        self.stockCountry = '//select[@name="storeId"]'
        self.AddToCart = '//button[text()="Add to cart"]'
        self.quantity = '//select[@class="product-quantity"]'
        self.ViewCart ='//a[text()="View cart"]'

        self.changestock = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.stockCountry)))
        self.selectstock = Select(self.changestock)
        self.selectstock.select_by_index(1)
        time.sleep(2)

        self.changequantity = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.quantity)))
        self.selectquantity = Select(self.changequantity)
        self.selectquantity.select_by_index(5)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddToCart))).click()


    @pytest.mark.product

    def test_product_price_visible(self):
        self.driver.get(self.base_url)
        self.ProductPrice = '//span[text()="$30.50"]'
        self.product_price = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ProductPrice)))
        assert self.product_price.is_displayed()

    @pytest.mark.product
    def test_product_image_visible(self):
        self.driver.get(self.base_url)
        self.ProductImage = '/html/body/div[2]/section/div/section[3]/a[1]/img[1]'
        self.Image_Element =self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ProductImage)))
        assert self.Image_Element.is_displayed()

    @pytest.mark.product

    def test_search_product(self):
        self.driver.get(self.base_url)
        self.search_product_input = '//input[@id="searchBar"]'
        self.search_product = '//button[@type="submit"]'

        self.wait.until(EC.presence_of_element_located((By.XPATH, self.search_product_input))).send_keys("fruit")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.search_product))).click()

