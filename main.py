from selenium import webdriver
from pages import Page

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)

page = Page(driver)
first_page_link = "https://market.yandex.ru/catalog/54933/list?hid=90580&how=dpop&in-stock=1"

items_id = page.get_items_id(first_page_link, page_numbers=2)
page.get_items_cards(items_id)

driver.close()
