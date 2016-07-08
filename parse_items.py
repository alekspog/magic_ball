from selenium import webdriver
import re

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
pages_number = 10
id_list = []
for page in range(1, pages_number + 1):

    first_page_link = "https://market.yandex.ru/catalog/55070/list?hid=90796&how=dpop&in-stock=1"
    link = first_page_link + "&page=" + str(page)
    driver.get(link)

    item_header = driver.find_elements_by_css_selector(".snippet-card__header")
    for item in item_header:
        item_name = item.find_element_by_css_selector('.snippet-card__header-text')
        item_href = item.find_element_by_css_selector('.snippet-card__header-link')
        # получаем id товара из ссылки
        result = re.search("https://market.yandex.ru/product/(\d*)", item_href.get_attribute('href'))
        item_id = result.groups()[0]
        # создаем список id товаров
        id_list.append(item_id)

        if result:
            print item_id + ";" + item_name.text

driver.close()


