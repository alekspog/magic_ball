# -*- coding: utf-8 -*-
import re

class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def get_items_id(self, page_numbers=1):
        id_list = []
        for page in range(1, page_numbers + 1):

            first_page_link = "https://market.yandex.ru/catalog/55070/list?hid=90796&how=dpop&in-stock=1"
            link = first_page_link + "&page=" + str(page)
            self.driver.get(link)

            item_header = self.driver.find_elements_by_css_selector(".snippet-card__header")
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
        return id_list

    def get_items_cards(self, id_list):
        for id in id_list:
            link = "https://market.yandex.ru/product/" + str(id) + "/spec?hid=90796&track=char"
            self.driver.get(link)

            # criteria_list_el = np.array(driver.find_elements_by_css_selector("dt.product-spec__name > span"))
            criteria_list_el = self.driver.find_elements_by_id("product-spec-")
            # criteria_list = []
            for criteria in criteria_list_el:
                criteria_name = criteria.find_element_by_css_selector(".product-spec__name-inner")
                value = criteria.find_element_by_css_selector(".product-spec__value-inner")
                print str(id) + "$$$" + criteria_name.text + "$$$" + value.text
