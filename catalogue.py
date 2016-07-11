# -*- coding: utf-8 -*-
import re
from selenium.common.exceptions import NoSuchElementException
import csv


class Catalogue(object):
    def __init__(self, driver, first_page, page_numbers):
        self.driver = driver
        self.first_page = first_page
        self.page_numbers = page_numbers

    def get_items_id(self):
        with open('goods_id.csv', mode='wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            id_list = []
            for page in range(1, self.page_numbers + 1):

                link = self.first_page + "&page=" + str(page)
                self.driver.get(link)

                item_header = self.driver.find_elements_by_css_selector(".snippet-card")
                for item in item_header:
                    item_name = item.find_element_by_css_selector('.snippet-card__header-text').text
                    item_href = item.find_element_by_css_selector('.snippet-card__header-link')
                    # get goods id from link
                    result = re.search("https://market.yandex.ru/product/(\d*)", item_href.get_attribute('href'))
                    item_id = result.groups()[0]
                    # make goods id list
                    id_list.append(item_id)
                    # get min price of good
                    try:
                        item_init_price_str = item.find_element_by_css_selector('.price').text
                        result = re.findall("(\d+)", item_init_price_str)
                        item_init_price = "".join(result)
                    except NoSuchElementException:
                        item_init_price = "0"
                    # get goods rating
                    try:
                        item_rating = item.find_element_by_css_selector('.rating').text
                    except NoSuchElementException:
                        item_rating = "0"

                    if result:
                        print item_id + ";" + item_name + ";" + item_init_price + ";" + item_rating
                        writer.writerow([item_id, item_name.encode('utf8').strip(), item_init_price, item_rating])
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
