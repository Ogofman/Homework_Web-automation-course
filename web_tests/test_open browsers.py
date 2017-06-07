from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

def test_open_chrome():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver,3).until(ec.title_is("webdriver - Пошук Google"))
    driver.quit()

def test_open_firefox():
    driver = webdriver.Firefox()
    driver.get("http://www.google.com")
    driver.find_element_by_name("q").send_keys("webdriver")
    driver.find_element_by_name("btnG").click()
    WebDriverWait(driver,3).until(ec.title_is("webdriver - Пошук Google"))
    driver.quit()