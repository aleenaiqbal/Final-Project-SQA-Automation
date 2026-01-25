import time
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class Testflow():
    # Declare driver type for better readability
    driver: WebDriver

    def setup_method(self):
        # Initialize explicit wait (10 seconds)
        self.wait = WebDriverWait(self.driver, 10)

    @pytest.mark.flow
    def test_Flow(self):

        # ---------- Locators ----------
        self.view_all_products = '//a[text()="View all products"]'
        self.ClickProduct = '//h3[text()="Create Your Own Cocktail"]'
        self.ProductPrice = '//span[@class="price"]'
        self.ProductImages = '//img[@class="product-image"]'

        # ---------- Navigate to All Products ----------
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.view_all_products))
        ).click()

        # Validate navigation to catalog page
        assert "catalog" in self.driver.current_url

        # ---------- Open Product Detail Page ----------
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ClickProduct))
        ).click()

        # Validate product page URL
        assert "catalog/product" in self.driver.current_url

        # ---------- Validate Product Title ----------
        self.product_title_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ClickProduct))
        )

        assert self.product_title_element.is_displayed()

        self.PTitle = "Create Your Own Cocktail"
        assert self.product_title_element.text.lower() == self.PTitle.lower()

        # ---------- Validate Product Price ----------
        self.product_price_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ProductPrice))
        )

        assert self.product_price_element.is_displayed()

        self.Price = "$84.96"
        assert self.product_price_element.text == self.Price

        # ---------- Validate Product Image ----------
        self.PImage = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.ProductImages))
        )
        assert self.PImage.is_displayed()

        # ---------- Cart & Stock Locators ----------
        self.checkstock = '//button[text()="Check stock"]'
        self.stockCountry = '//select[@name="storeId"]'
        self.AddToCart = '//button[text()="Add to cart"]'
        self.quantity = '//select[@class="product-quantity"]'
        self.ViewCart = '//a[text()="View cart"]'

        # ---------- Select Stock Country ----------
        self.changestock = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.stockCountry))
        )
        self.selectstock = Select(self.changestock)
        self.selectstock.select_by_index(1)
        time.sleep(2)

        # ---------- Select Product Quantity ----------
        self.changequantity = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.quantity))
        )
        self.selectquantity = Select(self.changequantity)
        self.selectquantity.select_by_index(5)  # quantity = 6
        time.sleep(2)

        # ---------- Add Product to Cart ----------
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.AddToCart))
        ).click()

        # ---------- View Cart ----------
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ViewCart))
        ).click()

        # Validate cart page URL
        assert "catalog/cart" in self.driver.current_url

        # ---------- Get Single Item Price ----------
        self.itemPrice = '//span[@class="item-price"]'
        self.SingleProduct = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.itemPrice))
        ).text

        print("UI Total Text With $:", self.SingleProduct)

        # ---------- Convert Price from String to Float ----------
        ui_total = float(self.SingleProduct.replace("$", ""))
        print("UI Text Without $:", ui_total)

        # ---------- Calculate Expected Total (Price × Quantity) ----------
        AddValue = round(ui_total * 6, 2)
        print("Calculated Total:", AddValue)

        # ---------- Get Total Price from Cart ----------
        self.TotalPrice = '//strong[text()="$509.76"]'
        self.Total = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.TotalPrice))
        ).text

        print("SUM OF PRODUCTS:", self.Total)

        # ---------- Convert Cart Total to Float ----------
        SumPTotal = float(self.Total.replace("$", ""))
        print("Total Sum:", SumPTotal)

        # ---------- Final Assertion ----------
        assert AddValue == SumPTotal



        #---- Place Order ----------
        self.PlaceOrder = '//button[text()="Place order"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.PlaceOrder))).click()

        #Login

        self.usernameinput = '//input[@name="username"]'
        self.passwordinput = '//input[@name="password"]'
        self.Loginbtn = '//button[text()=" Log in "]'

        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.usernameinput))).send_keys("carlos")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Loginbtn))).click()

        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.passwordinput))).send_keys("hunter2")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.Loginbtn))).click()



