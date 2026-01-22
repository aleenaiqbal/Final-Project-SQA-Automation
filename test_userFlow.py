"""import time

import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check
from selenium.webdriver.support.ui import Select


class TestUserFlow():
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.fullflow

    def test_UserFlow(self):
        self.view_all_products = '//a[text()="View all products"]'
        self.ClickProduct = '//h3[text()="Create Your Own Cocktail"]'
        self.ProductPrice = '//span[@class="price"]'
        self.ProductImages = '//img[@class="product-image"]'

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.view_all_products))).click()
        assert "catalog" in self.driver.current_url

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ClickProduct))).click()
        assert "catalog/product" in self.driver.current_url

        self.product_title_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ClickProduct)))
        assert self.product_title_element.is_displayed()
        self.product_title_text = self.product_title_element.text

        self.PTitle = "Create Your Own Cocktail"
        assert self.product_title_element.text.lower() == self.PTitle.lower()

        self.product_price_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ProductPrice)))
        assert self.product_price_element.is_displayed()

        self.Price = "$84.96"
        assert self.product_price_element.text == self.Price

        self.product_price_text = self.product_price_element.text

        self.PImage = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.ProductImages)))
        assert self.PImage.is_displayed()

        self.checkstock = '//button[text()="Check stock"]'
        self.stockCountry = '//select[@name="storeId"]'
        self.AddToCart = '//button[text()="Add to cart"]'
        self.quantity = '//select[@class="product-quantity"]'
        self.ViewCart = '//a[text()="View cart"]'

        self.changestock = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.stockCountry)))
        self.selectstock = Select(self.changestock)
        self.selectstock.select_by_index(1)
        time.sleep(2)

        self.changequantity = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.quantity)))
        self.selectquantity = Select(self.changequantity)
        self.selectquantity.select_by_index(5)
        time.sleep(2)

        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.AddToCart))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.ViewCart))).click()

        assert "catalog/cart" in self.driver.current_url

        self.itemTitle = '//span[@class="item-title"]'
        self.itemPrice = '//span[@class="item-price"]'
        self.itemQuantity = '//select[@class="product-quantity"]'

        self.productName = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.itemTitle))).text
        self.productPrice = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.itemPrice))).text
        self.productQuantity = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.itemQuantity))).get_attribute("value")

        # Save product title text
        self.product_title_text = self.product_title_element.text

        # Save product price text
        self.product_price_text = self.product_price_element.text

        # Save selected quantity
        self.selected_quantity = self.selectquantity.first_selected_option.text

        assert self.productName.lower() == self.product_title_text.lower()
        assert self.productPrice == self.product_price_text
        assert self.productQuantity == self.selected_quantity"""

import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class TestUserFlow():
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.fullflow
    def test_UserFlow(self):
        # --- Locators ---
        view_all_products = '//a[text()="View all products"]'
        click_product = '//h3[text()="Create Your Own Cocktail"]'
        product_price = '//span[@class="price"]'
        product_image = '//img[@class="product-image"]'
        stock_country = '//select[@name="storeId"]'
        add_to_cart = '//button[text()="Add to cart"]'
        quantity_select = '//select[@class="product-quantity"]'
        view_cart = '//a[text()="View cart"]'
        cart_item_title = '//span[@class="item-title"]'
        cart_item_price = '//span[@class="item-price"]'
        cart_item_quantity = '//select[@class="product-quantity"]'

        # --- Navigate to product page ---
        self.wait.until(EC.element_to_be_clickable((By.XPATH, view_all_products))).click()
        assert "catalog" in self.driver.current_url

        self.wait.until(EC.element_to_be_clickable((By.XPATH, click_product))).click()
        assert "catalog/product" in self.driver.current_url

        # --- Capture product details BEFORE navigation ---
        product_title_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, click_product))
        )
        product_price_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, product_price))
        )
        product_image_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, product_image))
        )

        # --- Save values to variables ---
        self.product_title_text = product_title_element.text
        self.product_price_text = product_price_element.text

        # --- Product page assertions ---
        assert product_title_element.is_displayed()
        assert product_title_element.text.lower() == "create your own cocktail".lower()
        assert product_price_element.is_displayed()
        assert product_price_element.text == "$84.96"
        assert product_image_element.is_displayed()

        # --- Select stock and quantity ---
        stock_dropdown = Select(
            self.wait.until(EC.element_to_be_clickable((By.XPATH, stock_country)))
        )
        stock_dropdown.select_by_index(1)  # choose 2nd store
        time.sleep(1)

        quantity_dropdown = Select(
            self.wait.until(EC.element_to_be_clickable((By.XPATH, quantity_select)))
        )
        quantity_dropdown.select_by_value("6")  # select quantity = 6
        time.sleep(3)

        # --- Hardcode expected quantity (matches cart) ---
        self.selected_quantity = "6"

        # --- Add to cart and go to cart page ---
        self.wait.until(EC.element_to_be_clickable((By.XPATH, add_to_cart))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, view_cart))).click()
        assert "catalog/cart" in self.driver.current_url

        # --- Capture cart details ---
        cart_title = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, cart_item_title))
        ).text
        cart_price = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, cart_item_price))
        ).text
        cart_quantity = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, cart_item_quantity))
        ).get_attribute("value")

        # --- Cart assertions ---
        assert cart_title.lower() == self.product_title_text.lower()
        assert cart_price == self.product_price_text
        assert cart_quantity == self.selected_quantity














