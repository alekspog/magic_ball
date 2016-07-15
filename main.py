# -*- coding: utf-8 -*-
from selenium import webdriver
from catalogue import Catalogue

driver = webdriver.PhantomJS()
driver.implicitly_wait(3)

first_page_link = "https://market.yandex.ru/catalog/55939/list?hid=91529&how=dpop&gfilter=2142357015%3A477105268&in-stock=1&priceto=20000"
page_numbers = 1

cat = Catalogue(driver, first_page_link, page_numbers)

# get list of goods and its ids
goods_id = cat.get_goods_id()
# get good data with criteria text and its values
cat.get_goods_criteria(goods_id)

driver.close()
driver.quit()
