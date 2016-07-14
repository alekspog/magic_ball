# -*- coding: utf-8 -*-
import re
from selenium.common.exceptions import NoSuchElementException
import csv


class Catalogue(object):
    def __init__(self, driver, first_page, page_numbers):
        self.driver = driver
        self.first_page = first_page
        self.page_numbers = page_numbers

    def get_goods_id(self):
        with open('goods_id.csv', mode='wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            goods_list = []
            for page in range(1, self.page_numbers + 1):

                link = self.first_page + "&page=" + str(page)
                self.driver.get(link)

                good_header = self.driver.find_elements_by_css_selector(".snippet-card")
                for good in good_header:
                    good_name = good.find_element_by_css_selector('.snippet-card__header-text').text
                    good_href = good.find_element_by_css_selector('.snippet-card__header-link')
                    # get goods id from link
                    result = re.search("https://market.yandex.ru/product/(\d*)", good_href.get_attribute('href'))
                    good_id = result.groups()[0]
                    # get min price of good
                    try:
                        good_init_price_str = good.find_element_by_css_selector('.price').text
                        result = re.findall("(\d+)", good_init_price_str)
                        good_init_price = "".join(result)
                        # get goods rating
                        try:
                            good_rating = good.find_element_by_css_selector('.rating').text
                        except NoSuchElementException:
                            good_rating = "0"
                    except NoSuchElementException:
                        result = False

                    if result:
                        print good_id + ";" + good_name + ";" + good_init_price + ";" + good_rating
                        good_line = [good_id, good_name.encode('utf8').strip(), good_init_price, good_rating]
                        writer.writerow(good_line)
                        goods_list.append(good_line)
        return goods_list

    def get_goods_criteria(self, goods_list):
        with open('goods_criteria.csv', mode='wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for good in goods_list:
                link = "https://market.yandex.ru/product/" + str(good[0])
                self.driver.get(link)
                # add price to criteria
                print(good[0] + "$$$" + "initial price" + "$$$" + good[2])
                writer.writerow([str(good[0]), "initial price", str(good[2])])
                # add rating to criteria
                print(good[0] + "$$$" + "rating" + "$$$" + good[3])
                writer.writerow([str(good[0]), "rating", str(good[3])])

                criteria_list_el = self.driver.find_elements_by_id("product-spec-")
                for criteria in criteria_list_el:
                    criteria_name = criteria.find_element_by_css_selector(".product-spec__name-inner")
                    value = criteria.find_element_by_css_selector(".product-spec__value-inner")
                    print(good[0] + "$$$" + criteria_name.text + "$$$" + value.text)
                    writer.writerow([str(good[0]), criteria_name.text.encode('utf8').strip(), value.text.encode('utf8').strip()])

