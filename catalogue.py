# -*- coding: utf-8 -*-
import re
from selenium.common.exceptions import NoSuchElementException
import csv
from datetime import datetime

class Catalogue(object):
    def __init__(self, driver, first_page, page_numbers):
        self.driver = driver
        self.first_page = first_page
        self.page_numbers = page_numbers
        self.now = datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S')

    def get_goods_id(self):
        file_name = str(self.now) + '_goods_id.csv'
        with open(file_name, mode='wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            goods_list = []
            goods_id_list = []
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
                    if good_id not in goods_id_list:
                        goods_id_list.append(good_id)
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
                            print (good_id + ";" + good_name + ";" + good_init_price + ";" + good_rating).encode('utf-8')
                            good_line = [good_id, good_name.encode('utf8').strip(), good_init_price, good_rating]
                            writer.writerow(good_line)
                            goods_list.append(good_line)
        return goods_list

    def get_goods_criteria(self, goods_list):
        file_name = str(self.now) + '_goods_criteria.csv'
        with open(file_name, mode='wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for good in goods_list:
                link = "https://market.yandex.ru/product/" + str(good[0]) + "/spec"
                self.driver.get(link)
                # add price to criteria
                print(good[0] + "$$$" + unicode("Цена", 'utf-8') + "$$$" + good[2])
                writer.writerow([str(good[0]), "Цена", str(good[2])])
                # add rating to criteria
                print(good[0] + "$$$" + unicode("Рейтинг", 'utf-8') + "$$$" + good[3])
                writer.writerow([str(good[0]), "Рейтинг", str(good[3])])
                # add block name to criteria name
                criteria_block = self.driver.find_elements_by_css_selector(".product-spec-wrap__body")
                for block in criteria_block:
                    block_title = block.find_element_by_css_selector(".title").text
                    criteria_list_el = block.find_elements_by_css_selector(".product-spec")
                    for criteria_el in criteria_list_el:
                        criteria_text = criteria_el.find_element_by_css_selector(".product-spec__name-inner").text
                        criteria = block_title + " - " + criteria_text
                        value = criteria_el.find_element_by_css_selector(".product-spec__value-inner").text
                        print(good[0] + "$$$" + criteria + "$$$" + value)
                        writer.writerow([str(good[0]), criteria.encode('utf8').strip(), value.encode('utf8').strip()])


