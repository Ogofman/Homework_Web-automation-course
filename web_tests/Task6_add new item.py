from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Firefox()
driver.implicitly_wait(3)

count_items_catalog = 0

def open_admin_page():
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button[name=login]").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-sign-out")))

def general_tab():
    global count_items_catalog
    driver.find_element_by_xpath(".//*[@id='app-']//span[contains(., 'Catalog')]").click()
    count_items_catalog = len(driver.find_elements_by_xpath(".//*[@id='main']/form/table/tbody/tr"))
    driver.find_element_by_xpath(".//*[@id='main']//li[contains(., 'Add New Product')]").click()
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='status'][@value=1]/parent::label").click()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/label/input[@value='1-3']").click()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='date_valid_from']").send_keys("2017-06-28")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='date_valid_to']").send_keys("2018-06-28")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='code']").send_keys("67864")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='name[en]']").send_keys("Kowalski")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='sku']").send_keys("24356")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='gtin']").send_keys("94756")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='taric']").send_keys("324775")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='quantity']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='quantity']").send_keys("10")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='weight']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='weight']").send_keys("1")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_x']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_x']").send_keys("0.5")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_y']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_y']").send_keys("0.6")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_z']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_z']").send_keys("0.4")
    p = os.path.abspath("D:\Web automation course\web_tests\Kowalski.jpeg")
    driver.find_element_by_xpath(".//*[@id='images']//div/input[@name='new_images[]']").send_keys(p)

def info_tab():
    driver.find_element_by_xpath(".//*[@id='main']/form/div/ul/li[contains(., 'Information')]").click()
    driver.find_element_by_xpath(".//*[@id='tab-information']//div/input[@name='keywords']").send_keys("toy, penguin")
    driver.find_element_by_xpath(".//*[@id='tab-information']//div/input[@name='short_description[en]']").send_keys("Baby Kowalski Plush")
    driver.find_element_by_xpath(".//*[@id='tab-information']//div[@class='trumbowyg-editor']").send_keys("Spend your day with the Penguin of Madagascar!")
    driver.find_element_by_xpath(".//*[@id='tab-information']//div/textarea[@name='attributes[en]']").send_keys('soft, plush')

def prices_tab():
    driver.find_element_by_xpath(".//*[@id='main']/form/div/ul/li[contains(., 'Prices')]").click()
    driver.find_element_by_xpath(".//*[@id='prices']//div/input[@name='purchase_price']").clear()
    driver.find_element_by_xpath(".//*[@id='prices']//input[@name='prices[USD]']").send_keys("25")
    driver.find_element_by_xpath(".//*[@id='prices']//input[@name='prices[EUR]']").send_keys("30")
    driver.find_element_by_xpath(".//*[@id='main']//button[@name='save']").click()

open_admin_page()
general_tab()
info_tab()
prices_tab()

def test_product_added():
    count_items = len(driver.find_elements_by_xpath(".//*[@id='main']/form/table/tbody/tr"))
    assert (count_items > count_items_catalog)