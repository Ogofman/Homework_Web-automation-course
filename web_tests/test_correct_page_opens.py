from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
driver.implicitly_wait(5)

def test_open_browser():
    driver.get("http://localhost/litecart")
    driver.find_element_by_name("email").send_keys("admin@admin.com")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_css_selector(".btn.btn-default").click()
    WebDriverWait(driver, 3).until(ec.title_is("My Store | Online Store"))

def get_elem_attr(xpath, attr):
    return driver.find_element_by_xpath(xpath).get_attribute(attr)

def test_if_names_equal():
    name_on_mpage = get_elem_attr(".//*[@id ='box-campaign-products']//div[@class='name']", "textContent")
    driver.find_element_by_css_selector(".image.img-responsive").click()
    name_on_ipage = get_elem_attr(".//*[@id='box-product']//h1[@class='title']", "textContent")
    assert(name_on_mpage == name_on_ipage)
    driver.find_element_by_css_selector(".featherlight-close-icon.featherlight-close").click()

def test_if_prices_equal():
    regprice_on_mpage = get_elem_attr(".//*[@id='box-campaign-products']//s[@class='regular-price']", "textContent")
    camprice_on_mpage = get_elem_attr(".//*[@id='box-campaign-products']//strong[@class='campaign-price']", "textContent")
    driver.find_element_by_css_selector(".image.img-responsive").click()
    regprice_on_ipage = get_elem_attr(".//*[@id='box-product']//del[@class='regular-price']","textContent")
    camprice_on_ipage = get_elem_attr(".//*[@id='box-product']//strong[@class='campaign-price']","textContent")
    assert (regprice_on_mpage == regprice_on_ipage)
    assert (camprice_on_mpage == camprice_on_ipage)
    driver.find_element_by_css_selector(".featherlight-close-icon.featherlight-close").click()



