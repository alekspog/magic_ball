from selenium import webdriver
import numpy as np

driver = webdriver.Firefox()
driver.implicitly_wait(10)
id_list = [4718782, 7151273, 6322695, 7969581, 8528976, 969052, 6144371, 7883365, 6065466, 2110693, 1042117, 8368816, 2110694, 2110692, 6275009, 974259, 7350061, 12481513, 971224, 971227, 1570528, 8264603, 10591147, 7853691, 9380210, 7883356, 9355600, 991500, 6194142, 12749272, 8217282, 10956390, 9254902, 10972528, 9281366, 13624158, 10706925, 8291579, 7267753, 974323, 10866331, 6296822, 12753898, 7969615, 7978987, 12749276, 10958612, 12481446, 13624155, 10591142, 10986728, 10695112, 10986513, 10956387, 971236, 6845702, 7342802, 11884557, 6103514, 10860981, 8352434, 10695121, 8368813, 11885050, 9349966, 12481350, 10894074, 12397526, 10401604, 10983277, 6498360, 10378069, 6122178, 9380205, 1027915, 974322, 10958739, 11883507, 12403570, 11597006, 10860982, 1623472, 12607737, 10378070, 6201860, 969050, 12637132, 12608498, 10445822, 8532303, 10882915, 10777345, 7282333, 12527608, 12637207, 7880984, 10477214, 11009217, 974507, 1030577]
for id in id_list:
    link = "https://market.yandex.ru/product/" + str(id) + "/spec?hid=90796&track=char"
    driver.get(link)

    # criteria_list_el = np.array(driver.find_elements_by_css_selector("dt.product-spec__name > span"))
    criteria_list_el = driver.find_elements_by_id("product-spec-")
    # criteria_list = []
    for criteria in criteria_list_el:
        criteria_name = criteria.find_element_by_css_selector(".product-spec__name-inner")
        value = criteria.find_element_by_css_selector(".product-spec__value-inner")
        print str(id) + "$$$" + criteria_name.text + "$$$" + value.text

driver.close()
