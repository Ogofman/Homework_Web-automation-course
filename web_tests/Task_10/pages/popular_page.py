from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

class PopularPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def open(self, base_url):
        self.driver.get(base_url)
        self.driver.find_element_by_xpath(".//*[@id='content']//a[@href='#popular-products']").click()
        return self

    def waiting(self, time):
        self.driver.implicitly_wait(time)

    def drop_down_present(self, locator):
        self.driver.find_element_by_xpath(locator).click()
        self.driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/select/option[@value='Small']").click()

    def add_product(self, i):
        self.drop_dowm_xpath = ".//*[@id='box-product']//div/form//div/select[@class='form-control']"
        self.driver.find_element_by_xpath(".//*[@id='box-popular-products']/div/div[%s]" % i).click()
        self.waiting(1)
        if len(self.driver.find_elements_by_xpath(self.drop_dowm_xpath)) > 0:
            self.drop_down_present(self.drop_dowm_xpath)
        else:
            self.waiting(0)
        self.driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/button[@class='btn btn-success']").click()
        self.driver.find_element_by_xpath(".//button[@class='featherlight-close-icon featherlight-close']").click()
        WebDriverWait(self.driver, 5).until(
            ec.text_to_be_present_in_element((By.XPATH, ".//*[@id='cart']//span[@class='quantity']"), str(i)))

