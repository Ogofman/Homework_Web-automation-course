from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def test_open_chrome():
    driver = webdriver.Chrome()
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".btn.btn-default").click()
    WebDriverWait(driver,5).until(ec.title_is("My Store"))
    driver.quit()