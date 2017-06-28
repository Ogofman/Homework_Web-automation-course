from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

driver = webdriver.Firefox()
driver.implicitly_wait(5)

def rgb_to_hex(rgb):
    return Color.from_string(rgb).hex

def test_open_browser():
    driver.get("http://localhost/litecart/en/")
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

def test_regular_price():
    color1 = driver.find_element(By.XPATH, ".//*[@id='box-campaign-products']//s[@class='regular-price']").value_of_css_property('color')
    color_regprice_on_mpage = rgb_to_hex(color1)
    tag_name1 = driver.find_element(By.XPATH, ".//*[@id='box-campaign-products']//s[@class='regular-price']").value_of_css_property('text-decoration-line')
    driver.find_element_by_css_selector(".image.img-responsive").click()
    color2 = driver.find_element(By.XPATH, ".//*[@id='box-product']//del[@class='regular-price']").value_of_css_property('color')
    color_regprice_on_ipage = rgb_to_hex(color2)
    tag_name2 = driver.find_element(By.XPATH,".//*[@id='box-product']//del[@class='regular-price']").value_of_css_property('text-decoration-line')
    assert (color_regprice_on_mpage == color_regprice_on_ipage == "#333333")
    assert (tag_name1 == tag_name2 == "line-through")
    driver.find_element_by_css_selector(".featherlight-close-icon.featherlight-close").click()

def test_campaigns_price():
    color1 = driver.find_element(By.XPATH, ".//*[@id='box-campaign-products']//strong[@class='campaign-price']").value_of_css_property('color')
    color_camprice_on_mpage = rgb_to_hex(color1)
    font_weight1 = driver.find_element(By.XPATH,".//*[@id='box-campaign-products']//strong[@class='campaign-price']").value_of_css_property('font-weight')
    driver.find_element_by_css_selector(".image.img-responsive").click()
    color2 = driver.find_element(By.XPATH, ".//*[@id='box-product']//strong[@class='campaign-price']").value_of_css_property('color')
    color_camprice_on_ipage = rgb_to_hex(color2)
    font_weight2 = driver.find_element(By.XPATH, ".//*[@id='box-product']//strong[@class='campaign-price']").value_of_css_property('font-weight')
    assert (color_camprice_on_mpage == color_camprice_on_ipage == "#cc0000")
    assert (font_weight1 == font_weight2 == "700")
    driver.find_element_by_css_selector(".featherlight-close-icon.featherlight-close").click()

    driver.quit()