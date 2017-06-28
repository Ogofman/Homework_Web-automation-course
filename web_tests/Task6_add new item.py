from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(3)

def test_open_admin_page():
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button[name=login]").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-sign-out")))

def test_info_general_tab():
    driver.find_element_by_xpath(".//*[@id='app-']//span[contains(., 'Catalog')]").click()
    driver.find_element_by_xpath(".//*[@id='main']//li[contains(., 'Add New Product')]").click()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/label/input[@value='1-3']").click()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='date_valid_from']").send_keys("2017-06-28")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='date_valid_to']").send_keys("2018-06-28")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='code']").send_keys("67864")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='name[en]']").send_keys("Kovalski")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='sku']").send_keys("24356")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='gtin']").send_keys("94756")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='taric']").send_keys("324775")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='quantity']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='quantity']").send_keys("10")
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='weight']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//input[@name='weight']").send_keys("1")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_x']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_x']").send_keys("0,5")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_y']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_y']").send_keys("0,6")
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_z']").clear()
    driver.find_element_by_xpath(".//*[@id='tab-general']//div/input[@name='dim_z']").send_keys("0,4")
    driver.find_element_by_xpath(".//*[@id='images']//div/input[@name='new_images[]']").send_keys("D:\Web automation course\web_tests\Kowalski.jpeg")