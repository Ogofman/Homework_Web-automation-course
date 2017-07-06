from selenium import webdriver
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

    def get_items_in_cart(self):
        self.popular_page.open(self.base_url)
        return self.popular_page.items_in_cart()

    def add_product_to_cart(self, i):
        self.popular_page.add_product(i)

    def remove_products_from_cart(self):
        self.checkout_page.open()
        self.checkout_page.remove_products()
        self.checkout_page.go_back()

