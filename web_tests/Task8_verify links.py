from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def test_open_firefox():
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button[name=login]").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-sign-out")))

def test_links():
    driver.find_element_by_xpath(".//*[@id='app-']//span[contains(., 'Countries')]").click()
    hrefs = []
    for url in driver.find_elements_by_xpath(".//*[@id='main']/form/table/tbody//td[5]/a"):
        hrefs.append(url.get_attribute('href'))

    for href in hrefs:
        driver.get(href)
        for arrow in driver.find_elements_by_xpath(".//*[@id='main']//i[@class='fa fa-external-link']"):
            current_window = driver.current_window_handle
            old_windows = driver.window_handles
            arrow.click()
            WebDriverWait(driver, 3).until(EC.new_window_is_opened(old_windows))
            new_window = [i for i in driver.window_handles if i not in old_windows]
            driver.switch_to.window(new_window[0])
            driver.close()
            driver.switch_to.window(current_window)