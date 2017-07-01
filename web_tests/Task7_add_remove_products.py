from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)

def test_open_browser():
    driver.get("http://localhost/litecart/en/")
    WebDriverWait(driver, 3).until(ec.title_is("My Store | Online Store"))

def test_add_products():
    i = 0
    while i < 3:
        driver.find_element_by_xpath(".//*[@id='box-campaign-products']//div/img").click()
        driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/select[@class='form-control']").click()
        driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/select/option[@value='Small']").click()
        driver.find_element_by_xpath(".//*[@id='box-product']//div/form//div/button[@class='btn btn-success']").click()
        driver.find_element_by_xpath(".//button[@class='featherlight-close-icon featherlight-close']").click()
        WebDriverWait(driver, 3).until(ec.text_to_be_present_in_element((By.XPATH, ".//*[@id='cart']//span[@class='quantity']"), str(i+1)))
        quan = driver.find_element_by_xpath(".//*[@id='cart']//span[@class='quantity']").text
        print(quan)
        i += 1




