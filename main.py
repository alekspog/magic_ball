# -*- coding: utf-8 -*-
from selenium import webdriver
from catalogue import Catalogue

driver = webdriver.PhantomJS()
driver.implicitly_wait(3)

# first_page_link = "https://market.yandex.ru/catalog/55939/list?hid=91529&gfilter=2133581720%3A353518528&gfilter=2142357015%3A477105268%2C2020334334&gfilter=2142357018%3A1897526220&in-stock=1&priceto=30000&how=dopinions"
first_page_link = "https://market.yandex.ru/catalog/55939/list?hid=91529&gfilter=2142357018%3A1897526220&in-stock=1&how=aprice"
page_numbers = 1

cat = Catalogue(driver, first_page_link, page_numbers)

# get list of items and its ids
items_id = cat.get_items_id()
# get item data with criteria text and its values
cat.get_items_cards(items_id)

driver.close()
driver.quit()
