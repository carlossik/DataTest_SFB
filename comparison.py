import pandas as pd
from pandas import DataFrame
import itertools
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.common.keys import Keys
import pytest
import colored
from colored import stylize
import sys
from termcolor import colored
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.common.exceptions import TimeoutException

# driver = webdriver.Chrome(executable_path='donotuse.exe')
# #driver = webdriver.Chrome(executable_path='donotuse.exe')
# dev_values = []
# gis_values = []
# def do_alert(dev_url):
#     try:
#         Alert = driver.switch_to.alert
#         Alert.send_keys(f'internal{Keys.TAB}sfb_pwesepss')
#         Alert.accept()
#         print(dev_url)
#     except NoAlertPresentException:
#         pass
#
#
#
#
# def get_edudata():
#     testSheet = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\edutest.xlsx',sheet_name='Sheet1', skipinitialspace=True, usecols='A')
#     mylist = testSheet.values.tolist()
#     flattened_URN_list = [y for x in mylist for y in x]
#     new_list = list(itertools.chain(*mylist))
#     return new_list
#     print(new_list)
#
#
#     # testSheet = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\edubasealldata20190130.xlsx',sheet_name='sheet1', skipinitialspace=True, usecols='A')
#     # mylist = testSheet.values.tolist()
#     # flattened_URN_list = [y for x in mylist for y in x]
#     # new_list = list(itertools.chain(*mylist))
#     # print(new_list)
#     # gis_url = "https://get-information-schools.service.gov.uk/Establishments/Establishment/Details/" + str(number)
#     # # print(gis_url)
#     # driver.get(gis_url)
#     # driver.implicitly_wait(10)
#     # elements_to_collect = []
#     # for number in new_list:
#     #     print("getting Edubase values" + "For" + " " + number)
#     #     try:
#     #         telephone_number = driver.find_element_by_xpath(
#     #             '/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[2]/dl/dd[12]').text
#     #         if telephone_number: print(telephone_number)
#     #         ofsted = driver.find_element_by_xpath(
#     #             "/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[2]/dl/dd[13]/span[1]").text
#     #         if ofsted: elements_to_collect.append(ofsted)
#     #         website = driver.find_element_by_xpath(
#     #             "/html/body/div[1]/main/div[2]/div/div[2]/div[1]/div[2]/dl/dd[11]/a").text
#     #         if website: elements_to_collect.append(website)
#     #         headteacher = driver.find_element_by_css_selector(
#     #             "#school-dashboard > div.detail-summary > dl > dt:nth-child(5)").text
#     #         if headteacher: elements_to_collect.append(headteacher)
#     #         print(elements_to_collect)
#     #     except NoSuchElementException:
#     #         print("Data not available" + " " + "For" + "" + number)
#     #         pass
#     #     return elements_to_collect
#     #     # data from edubase goes here
#
#
# def get_devData():
#     print(str(get_edudata()))
#     elements_to_collect = []
#     for number in get_edudata():
#         dev_url = "https://internal:sfb_pwesepss@as-t1dv-sfb.azurewebsites.net/School/Detail?urn=" + str(number)
#         driver.get(dev_url)
#         print(dev_url)
#         try:
#             print("getting dev values" + "For" + " " + str(number))
#             dev_phone_number = driver.find_element_by_class_name('sfb_gtm_tel').text
#             if dev_phone_number: elements_to_collect.append(dev_phone_number)
#             dev_website_address = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/dl/dd[14]/a').text
#             if dev_website_address: elements_to_collect.append(dev_website_address)
#             dev_offsted = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/dl/dd[7]/span[2]').text
#             if dev_offsted: elements_to_collect.append(dev_offsted)
#             dev_headteacher = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/dl/dd[10]').text
#             if dev_headteacher: elements_to_collect.append(dev_headteacher)
#         except NoSuchElementException:
#             print('Data not available" + " " + "For" + ""' + str(number))
#             pass
#         except (NoAlertPresentException, UnexpectedAlertPresentException):
#             Alert = driver.switch_to.alert
#             Alert.send_keys(f'internal{Keys.TAB}sfb_pwesepss')
#             Alert.accept()
#         print(elements_to_collect)
#         return elements_to_collect
#
#     def create_report():
#         df1 = DataFrame({'DevData': get_devData(number=None)})
#         df1.to_excel('DevData.xlsx', 'Sheet1', index=[0])
#         df2 = DataFrame({'Edudata': get_edudata(number=None)})
#         df2.to_excel('EduData.xlsx', 'Sheet1', index=[0])
#
#
# # dev data goes here
#
#
# # laestab_no = ['100004',
# # '100005',
# # '100006',
# # '100007',
# # '100008']
# # '100009',
# # '100010',
# # '100011',
# # '100012',
# # '100013',
# # '100014',
# # '100015',
# # '100016',
# # '100017',
# # '100018',
# # '100019',
# # '100020',
# # '100021',
# # '100022',
# # '100023',
# # '100024',
# # '100025',
# # '100026',
# # '100027',
# # '100028']
#
# # for number in (laestab_no):
# get_devData()
#
#
#
#
#
#
#
#
#








a = [100087,100088,100089,
100090,
100091,
100092,
100093,
100094,
100095,
100096,
100097,
100098,
100099,
100100,
100101,
100102,
100103,
100104,
100105,
100106,
100107,
100108,
100109,
100110,
100111,
100112,
100113,
100114,
100115,
100116,
100117,
100118,
100119,
100120,
100121,
100122,
100123,
100124,
100125,
100126,
100127,
100128,
100129,
100130,
100131,
100132,
100133,
100134,
100135,
100136,
100137,
100138,
100139,
100140,
100141,
100142,
100143,
100144,
100145,
100146,
100147,
100148,
100149,
100150,
100151,
100152,
100153]

from selenium import webdriver

browser = webdriver.PhantomJS('C:\\Users\\kwaku\\OneDrive\\Desktop\\Phantom\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')
browser.get('https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=100004')
browser.save_screenshot('screen.png')











