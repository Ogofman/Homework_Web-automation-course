from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

def waiting(time):
    driver.implicitly_wait(time)

def test_open_firefox():
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector("button[name=login]").click()
    WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "fa-sign-out")))

def is_submenu_present(locator):
    if len(driver.find_elements_by_xpath(locator)) > 0:
        return 1
    else:
        waiting(0)

def if_header_present(locator):
    try:
        return driver.find_element_by_xpath(locator)
    except:
        return 0

def get_sub_menu_after_click(selector, index):
    subMenu = driver.find_elements_by_xpath(selector)
    return subMenu[index]

def test_get_main_menu():
    i = 0
    lenMenu = len(driver.find_elements_by_xpath(".//*[@id='box-apps-menu']/li"))

    while i < lenMenu:
        i += 1
        xpath = ".//*[@id='box-apps-menu']/li[%s]" % i
        if xpath:
            driver.find_element_by_xpath(xpath).click()
            assert if_header_present(".//*[@id='main']/h1")

            subMenuSelector = ".//*[@id='box-apps-menu']/li[%s]/ul/li" % i
            if is_submenu_present(subMenuSelector):
                lenSubMenu = len(driver.find_elements_by_xpath(subMenuSelector))

                for index in range(0, lenSubMenu):
                    elem = get_sub_menu_after_click(subMenuSelector, index)
                    elem.click()
                    assert if_header_present(".//*[@id='main']/h1")
            else:
                waiting(1)

    driver.quit()