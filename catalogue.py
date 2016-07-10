# -*- coding: utf-8 -*-
import re
from selenium.common.exceptions import NoSuchElementException

class Catalogue(object):
    def __init__(self, driver, first_page, page_numbers):
        self.driver = driver
        self.first_page = first_page
        self.page_numbers = page_numbers

    def get_items_id(self):
        id_list = []
        for page in range(1, self.page_numbers + 1):

            link = self.first_page + "&page=" + str(page)
            self.driver.get(link)

            item_header = self.driver.find_elements_by_css_selector(".snippet-card")
            for item in item_header:
                item_name = item.find_element_by_css_selector('.snippet-card__header-text').text
                item_href = item.find_element_by_css_selector('.snippet-card__header-link')
                # получаем id товара из ссылки
                result = re.search("https://market.yandex.ru/product/(\d*)", item_href.get_attribute('href'))
                item_id = result.groups()[0]
                # создаем список id товаров
                id_list.append(item_id)
                # находим минимальную цену товара
                try:
                    item_init_price_str = item.find_element_by_css_selector('.price').text
                    result = re.findall("(\d+)", item_init_price_str)
                    item_init_price = "".join(result)
                except NoSuchElementException:
                    item_init_price = "0"
                # находим рейтинг товара
                try:
                    item_rating = item.find_element_by_css_selector('.rating').text
                except NoSuchElementException:
                    item_rating = "0"

                if result:
                    print item_id + ";" + item_name + ";" + item_init_price + ";" + item_rating
        return id_list

    def get_items_cards(self, id_list):
        for id in id_list:
            link = "https://market.yandex.ru/product/" + str(id)
            self.driver.get(link)

            criteria_list_el = self.driver.find_elements_by_id("product-spec-")
            # criteria_list = []
            for criteria in criteria_list_el:
                criteria_name = criteria.find_element_by_css_selector(".product-spec__name-inner")
                value = criteria.find_element_by_css_selector(".product-spec__value-inner")
                print str(id) + "$$$" + criteria_name.text + "$$$" + value.text
