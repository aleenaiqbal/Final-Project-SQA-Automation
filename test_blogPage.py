import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest_check as check

class TestBlogPage:
    driver: WebDriver

    def setup_method(self):
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = 'https://ginandjuice.shop/blog/'


    @pytest.mark.blog

    def test_blogpageload(self):
        self.driver.get(self.base_url)
        assert "blog" in self.driver.current_url

    @pytest.mark.blog

    def test_blogPageTitle(self):
        self.driver.get(self.base_url)
        assert "Blog - Gin & Juice Shop" in self.driver.title

    @pytest.mark.blog
    def test_blogPostTitle(self):
        self.driver.get(self.base_url)
        self.FirstPostTitle = '//h2[text()="A Hairy Day"]'
        self.BlogTitle = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.FirstPostTitle)))
        assert self.BlogTitle.is_displayed()

    @pytest.mark.blog
    def test_blogImage(self):
        self.driver.get(self.base_url)
        self.FirstPostImage = '/html/body/div[2]/section/div/section[2]/div[1]/a[1]/img'
        self.FirstBlog = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.FirstPostImage)))
        assert self.FirstBlog.is_displayed()

    @pytest.mark.blog
    def test_BlogDescription(self):
        self.driver.get(self.base_url)
        self.FirstBlogDes = '/html/body/div[2]/section/div/section[2]/div[1]/p'
        self.BlogDes = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.FirstBlogDes)))
        assert self.BlogDes.is_displayed()

    @pytest.mark.blog
    def test_searchblog(self):
        self.driver.get(self.base_url)
        self.search_input = '//input[@type="text"]'
        self.searchbtn ='//button[@type="submit"]'
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.search_input))).send_keys('WHEEL')
        self.wait.until(EC.visibility_of_element_located((By.XPATH, self.searchbtn))).click()

    @pytest.mark.blog
    def test_viewpost(self):
        self.driver.get(self.base_url)
        self.viewPostBtn = '//a[@class="button is-small"]'
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.viewPostBtn))).click()



