from selenium import webdriver
from catalogue import Catalogue

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)

first_page_link = "https://market.yandex.ru/catalog/54933/list?hid=90580&how=dpop&in-stock=1"
page_numbers = 2

cat = Catalogue(driver, first_page_link, page_numbers)

# get list of items and its ids
items_id = cat.get_items_id()
# get item data with criteria text and its values
cat.get_items_cards(items_id)

driver.close()
