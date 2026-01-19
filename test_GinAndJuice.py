from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import pytest_check as check
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePage:
    driver: WebDriver

    def test_HomePageTitle(self):
        self.wait = WebDriverWait(self.driver, 10)
        title = self.driver.title
        print("Home Page Title: ",title)
        assert "Home - Gin & Juice Shop" in title



    def test_ViewAllProduct(self):

        self.wait = WebDriverWait(self.driver, 10)
        self.view_all_products = '//a[text()="View all products"]'

        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.view_all_products))).click()
        assert "/catalog" in self.driver.current_url

    def test_click_first_product(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.click_first_product = '//*[@id="productsPreview"]/div[2]/div[2]/section/a[1]/span[2]'
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.click_first_product))).click()
        assert "catalog/product?productId=1" in self.driver.current_url


    def test_ViewPost(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.viewpost='//a[text()="View post"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.viewpost))).click()
        assert "blog/post?postId=3" in self.driver.current_url

    def test_subscribe_section(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.subscribe_input = '//input[@name="email"]'
        self.subscribe_btn = '//button[@type="submit"]'

        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.subscribe_input))).send_keys('test@example.com')
        self.wait.until(EC.element_to_be_clickable((By.XPATH,self.subscribe_btn))).click()


    def test_web_vulnerability(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.Web_vulnerability = '//*[@id="productsPreview"]/div[1]/p/span'
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.Web_vulnerability))).click()
        assert "vulnerabilities" in self.driver.current_url

    def test_view_all_product_link(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.view_all_product_link = '//*[@id="productsPreview"]/a'
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_all_product_link))).click()
        assert "catalog" in self.driver.current_url

    def test_view_all_blog_post(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.view_all_blog_post = '//*[@id="blogPreview"]/a'
        self.wait.until(EC.visibility_of_element_located((By.XPATH,self.view_all_blog_post))).click()
        assert "blog" in self.driver.current_url








