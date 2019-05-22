import pandas as pd
from pandas import DataFrame
import itertools
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import pytest
import colored
from colored import stylize
import sys
from termcolor import colored
import data_set

#lets create a dataframe to read excel file
fields = ['Test Area' ,'Tested by','Outcome pass/fail/ pass caveat','School URN / Trust number/name tested','Test Area']

testSheet = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_Academies_2017-18_v1.5.xlsx',sheet_name='Academies 2016 to 17',skipinitialspace=True, usecols='A')
testSheet2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_Academies_2016-17_v1.8.xlsx',sheet_name='Academies 2016 to 17',skipinitialspace=True, usecols='F')
testSheet3 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_Academies_2016-17_v1.8.xlsx',sheet_name='Academies 2016 to 17',skipinitialspace=True, usecols='Q')
mylist = testSheet.values.tolist()
mylist2 = testSheet2.values.tolist()
mumber_of_pupils_list = testSheet3.values.tolist()
flattened_URN_list = [y for x in mylist for y in x]
flattened_trustName_list= [y for x in mylist2 for y in x]
flattened_numberof_Pupils = [y for x in mumber_of_pupils_list for y in x]
new_list = list(itertools.chain(*mylist))
new_list2 = list(itertools.chain(*mylist2))

#print(flattened_URN_list)
#print(flattened_trustName_list)
number_or_urns = len(new_list)
print(len(new_list))
print(len(new_list2))
driver = webdriver.Chrome(executable_path='C:\\Users\\kwaku\\PycharmProjects\\untitled1\\donotuse.exe')
driver.get("https://as-t1pp-sfb.azurewebsites.net/")
unable_to_test = []
did_not_match = []
zero_schools= []

for urn,trustname in zip(new_list,new_list2):

    inputElement = driver.find_element_by_id("SchoolOrCollegeNameId").click()
    inputElement = driver.find_element_by_id("FindByNameId").send_keys(urn)
    driver.find_element_by_name("searchtype").click()
    driver.implicitly_wait(0)
    try:
        nameOnPage = driver.find_element_by_xpath("/html/body/div/main/h1").text
        assert nameOnPage == str(trustname)
        number_of_pupils = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/div/dl/dd[5]").text
        try:
            if int(number_of_pupils) == 0: zero_schools.append((urn, nameOnPage))
            print(number_of_pupils + " " + "Number of Pupils")
            print(colored(nameOnPage + " " + " On website Matches" + " " + str(trustname), ("green")))
            number_or_urns -= 1
            print(str(number_or_urns) + " " + "Schools Remaining")
        except ValueError:
            print("This is not a Valid Value")
    except AssertionError:
        did_not_match.append(urn)
        print(did_not_match)
        print(colored(nameOnPage + " " + " On website  Does Not Match" + " " + str(trustname), ("red")))
        # driver.find_element_by_class_name("home-link").click()
    except NoSuchElementException:
        unable_to_test.append(urn)
        print(colored("Unable to test LAESTAT number " + " " + str(urn) + " " + "Please do this manually",("red")))
        pass
    driver.refresh()
    driver.find_element_by_class_name("home-link").click()

    def create_report():
        df1 = DataFrame({'Tests To Re-Run': unable_to_test})
        df1.to_excel('Data_Test1_Report.xlsx', 'Sheet1', index=False)
        df2 = DataFrame({'School Names Not Matching': did_not_match})
        df2.to_excel('Data_Test2_Report.xlsx', 'Sheet1', index=False)
        df3 = DataFrame({'Closed Schools': zero_schools})
        df3.to_excel('Data_Test3_Report.xlsx', 'Sheet1', index=False)

create_report()






