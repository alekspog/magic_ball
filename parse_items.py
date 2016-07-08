from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.implicitly_wait(10)
for page in range(1, 11):

    first_page_link = "https://market.yandex.ru/catalog/55070/list?hid=90796&how=dpop&in-stock=1"
    link = first_page_link + "&page=" + str(page)
    driver.get(link)

    item_names = driver.find_elements_by_css_selector('.snippet-card__header-text')
    item_hrefs = driver.find_elements_by_css_selector('.snippet-card__header-link')

    for item in item_names:
        print(item.text)

    for item in item_hrefs:
        # print(item.get_attribute('href'))
        result = re.search("https://market.yandex.ru/product/(\d*)", item.get_attribute('href'))
        if result:
            print result.groups()[0]

driver.close()


