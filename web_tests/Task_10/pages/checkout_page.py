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
        try:
            WebDriverWait(self.driver, 2).until(
                ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
        finally:
            while self.items(".//*[@id='box-checkout-cart']//tbody/tr") > 0:
                try:
                    WebDriverWait(self.driver, 2).until(
                        ec.presence_of_element_located((By.XPATH, ".//div[@class='loader-wrapper']")))
                except:
                    self.driver.find_element_by_xpath(
                        ".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()

    def cart_empty(self):
        self.driver.find_element_by_xpath(".//*[@id='box-checkout']//a[contains(., Back)]").click()
        self.quan = self.driver.find_element_by_xpath(".//*[@id='cart']//span[@class='quantity']").get_attribute("text")
        return self.quan