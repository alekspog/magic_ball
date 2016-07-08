from selenium import webdriver
import re

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS(executable_path="C:\\Users\\alekspog\\PycharmProjects\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.implicitly_wait(10)
pages_number = 10
for page in range(1, pages_number + 1):

    first_page_link = "https://market.yandex.ru/catalog/55070/list?hid=90796&how=dpop&in-stock=1"
    link = first_page_link + "&page=" + str(page)
    driver.get(link)

    item_header = driver.find_elements_by_css_selector(".snippet-card__header")
    for item in item_header:
        item_name = item.find_element_by_css_selector('.snippet-card__header-text')
        item_href = item.find_element_by_css_selector('.snippet-card__header-link')
        result = re.search("https://market.yandex.ru/product/(\d*)", item_href.get_attribute('href'))
        if result:
            print result.groups()[0] + ";" + item_name.text

    # for item in item_hrefs:
    #     # print(item.get_attribute('href'))
    #     result = re.search("https://market.yandex.ru/product/(\d*)", item.get_attribute('href'))
    #     if result:
    #         print result.groups()[0]

driver.close()


