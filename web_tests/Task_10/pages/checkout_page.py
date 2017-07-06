from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait (driver,10)

    def waiting(self, time):
        self.driver.implicitly_wait(time)

    def open(self):
        self.driver.find_element_by_xpath(".//*[@id='cart']").click()
        self.waiting(2)
        return self

    def items(self, xpath):
        return len(self.driver.find_elements_by_xpath(xpath))

    def remove_products(self):
        while self.items(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']") > 0:
            table = self.driver.find_element_by_xpath(".//*[@id='order_confirmation-wrapper']/table")
            self.driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()
            WebDriverWait(self.driver, 3).until(ec.staleness_of(table))

    def go_back(self):
        self.driver.find_element_by_xpath(".//*[@id='box-checkout']//a[contains(., Back)]").click()
