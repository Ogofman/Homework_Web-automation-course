from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from web_tests.Task_10.pages.popular_page import PopularPage
from web_tests.Task_10.pages.checkout_page import CheckoutPage


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.base_url = "http://localhost/litecart/en/"
        self.popular_page = PopularPage(self.driver)
        self.checkout_page = CheckoutPage(self.driver)

    def quit(self):
        self.driver.quit()

    def open_popular(self):
        self.popular_page.open(self.base_url)

    def add_product_to_cart(self, i):
        self.popular_page.add_product(i)

    def remove_product_from_cart(self):
        self.checkout_page.remove_products()









