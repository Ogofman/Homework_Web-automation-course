from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
added_items = 0

def waiting(time):
    driver.implicitly_wait(time)

def test_open_browser():
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 3).until(ec.title_is("My Store | Online Store"))

def drop_down_present(locator):
    driver.find_element_by_xpath(locator).click()
    driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/select/option[@value='Small']").click()

def test_add_products():
    i = 1
    drop_dowm_xpath = ".//*[@id='box-product']//div/form//div/select[@class='form-control']"
    driver.find_element_by_xpath(".//*[@id='content']//a[@href='#popular-products']").click()
    while i <= 3:
        driver.find_element_by_xpath(".//*[@id='box-popular-products']/div/div[%s]" %i).click()
        waiting(1)
        if len(driver.find_elements_by_xpath(drop_dowm_xpath)) > 0:
            drop_down_present(drop_dowm_xpath)
        else:
            waiting(0)
        driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/button[@class='btn btn-success']").click()
        driver.find_element_by_xpath(".//button[@class='featherlight-close-icon featherlight-close']").click()
        WebDriverWait(driver, 5).until(ec.text_to_be_present_in_element((By.XPATH, ".//*[@id='cart']//span[@class='quantity']"), str(i)))
        i += 1

def test_remove_products():
    global added_items
    driver.find_element_by_xpath(".//*[@id='cart']").click()
    waiting(2)
    added_items = len(driver.find_elements_by_xpath(".//*[@id='box-checkout-cart']//tbody/tr"))
    print(added_items)
    while added_items > 0:
        try:
            driver.find_element_by_xpath(".//div[@class='loader-wrapper']")
        except:
            driver.find_element_by_xpath(".//*[@id='box-checkout-cart']//button[@class='btn btn-danger']").click()
            added_items = len(driver.find_elements_by_xpath(".//*[@id='box-checkout-cart']//tbody/tr"))