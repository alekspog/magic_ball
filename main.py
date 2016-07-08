from selenium import webdriver
from pages import Page

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)

page = Page(driver)
items_id = page.get_items_id(page_numbers=2)
page.get_items_cards(items_id)

driver.close()
