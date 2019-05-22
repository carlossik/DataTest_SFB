import pandas as pd
import numpy as np
from pandas import DataFrame
import itertools
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from pandas import DataFrame
import re
import time
import csv

# dev = "https://as-t1dv-sfb.azurewebsites.net"
# datadict = {}
# suspect_Finances = []
# schoolName = []
# NoDataSubmitted = []
# NoDataName = []
# schoolName2 = []
# df = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',sheet_name='Central Services 2017 to 18',skipinitialspace=True,skiprows=2,nrows=2000,index_col=None,usecols='C,D,AW')
# df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',sheet_name='Academies 2017 to 18',skipinitialspace=True,skiprows=2,nrows=20,index_col=None,usecols='B,C')
# def convert_figures(expenditure):
#     multipliers = {'k': 1e3,'m': 1e6,'b': 1e9,}
#     pattern = r'([0-9.]+)([bkm])'
#     for number, suffix in re.findall(pattern, expenditure):
#         number = float(number)
#         return (number * multipliers[suffix])
#
#
#
#
# #a = [2032471]
# a = df.values.tolist()
# urns = df2.values.tolist()
# driver = webdriver.Chrome()
# driver.get(dev)
# ]


# def timeout():
#     timeoutUrl ="https://as-t1dv-sfb.azurewebsites.net/Account/Login?ReturnUrl=%2F"
#     if driver.current_url == timeoutUrl:
#         login()





# def advanced_compare_senCharacteristics():
#     noschooldata = []
#     withoutofsted = []
#     noprogr8 = []
#     NoKeystageValue = []
#     rerrunRuns = []
#     login()
#     try:
#         for urn in urns:
#             schoolUrn = str(urn[0])
#             school_name = str(urn[1])
#             sen_url = "https://as-t1dv-sfb.azurewebsites.net/BenchmarkCriteria/AdvancedCharacteristics?areaType=All&lacode=&lanametext=&Urn=" + str( urn[0]) + "&ComparisonType=Advanced&EstType=Maintained"
#
#             driver.get(sen_url)
#             no_value_text = "No value was supplied for "
#
#             openall = driver.find_element_by_class_name("accordion-expand-all")
#             openall.click()
#             number_of_pupils_button = driver.find_element_by_id("checkbox-MinNoPupil")
#             number_of_pupils_button.click()
#             number_of_pupils_displayed = driver.find_element_by_css_selector( "div.accordion-section:nth-child(2) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)").text
#             progress8 = driver.find_element_by_id("checkbox-MinP8Mea")
#             progress8.click()
#             progress8_Value = progress8.text
#             ofstedRating = driver.find_element_by_id("checkbox-OfstedRating")
#             ofstedRating.click()
#             ofsted_value = driver.find_element_by_css_selector("div.accordion-section:nth-child(4) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
#             keystage2 = driver.find_element_by_id("checkbox-MinKs2Actual")
#             keystage2.click()
#             keystage2_Value = keystage2.text
#             elements_to_test = [number_of_pupils_displayed, progress8_Value,ofsted_value,keystage2_Value]
#             for element in elements_to_test:
#                 if no_value_text in element:
#                     print("Failed" )
#                 else:
#                     pass
            # def verify_ofsted():
            #     if "No value was supplied for " in (ofsted_value):
            #         withoutofsted.append(schoolUrn)
            #         print("No Ofsted Value for " + "" + schoolUrn)
            #
            # def verify_progress8():
            #     if "No value was supplied for " in progress8_Value:
            #         noprogr8.append(schoolUrn)
            #         print("No progress8 Value for " + "" + schoolUrn)
            #
            # def verify_Keystage2():
            #     if "No value was supplied for " in keystage2_Value:
            #         NoKeystageValue.append(schoolUrn)
            #         print("No Key stage 2 Value for " + "" + schoolUrn)
            #
            # def verify_prog8():
            #     if "No value was supplied for " in progress8_Value:
            #         noprogr8.append(schoolUrn)
            #         print("No progress8 Value for " + "" + schoolUrn)
            #
            # def verify_numberPupils():
            #     if "No value was supplied for " in number_of_pupils_displayed:
            #         print("Error this school has no number of pupils " + "" + str(urn[0]))
            #         noschooldata.append(str(urn[0]))

    # except (NoSuchElementException, selenium.common.exceptions.WebDriverException):
    #     rerrunRuns.append(schoolUrn)
    #     pass
    #
    # df = pd.DataFrame.from_dict({'URN': schoolUrn, 'SchoolNames': school_name,'No Ofsted':withoutofsted,'No Prog8':noprogr8,'No KeystageValue':NoKeystageValue},orient='index')
    # df.to_excel('SenCharacteristicsTest.xlsx', sheet_name='Sheet1',header=True, index=False)
    #


                # elif "No value was supplied for " in progress8_Value:
                #     noprogr8.append(schoolUrn)
                #     print("No progress8 Value for " + "" + schoolUrn)
                #     if "No value was supplied for " in keystage2_Value:
                #         NoKeystageValue.append(schoolUrn)
                #         print("No Key stage 2 Value for " + "" + schoolUrn)
                #         if "No value was supplied for " in number_of_pupils_displayed:
                #             print("Error this school has no number of pupils " + "" + str(urn[0]))
                #             noschooldata.append(str(urn[0]))











# advanced_compare_senCharacteristics()
# login()
# for list in a:
#     trustno = str(list[0])
#     schooName = str(list[1])
#     expected_expenditure = (str(list[2]))
#     for trustno in list:
#         try:
#             url = "https://as-t1dv-sfb.azurewebsites.net/Trust?companyNo=" + str(trustno)
#             driver.get(url)
#
#             expenditure = ((driver.find_element_by_css_selector(".exp-total").text).replace("£", ""))
#             print(expenditure)
#             converted_expenditure = convert_figures(expenditure)
#             print(converted_expenditure)
#             nodatasubmitted = driver.find_element_by_css_selector("div.panel:nth-child(4) > p:nth-child(1)").text
#             print("********************************")
#         #     if finalExpenditure ==  str(list[2]):
#         #         print("Expenditure matched for " + " " + str(list[1]))
#         #     else:
#         #         print("Expenditure did not  match for " + " " + str(list[1]) + " " + "Expected " + " " + str(
#         #             list[2]) + " " + "But Got" + "" + final_expenditure2)
#         #         suspect_Finances.append(trustno)
#         #         schoolName.append(schooName)
#         #         #datadict.update(trustno,schooName)
#         #     if nodatasubmitted == "This trust has not submitted any data":
#         #         NoDataSubmitted.append(trustno)
#         #         NoDataName.append(schooName)
#         except NoSuchElementException:
#             print("Data cannot be found for " + " " + str(list[0]))
#             driver.refresh()
#             if  "https://as-t1dv-sfb.azurewebsites.net/Account/Login?ReturnUrl=%2F" in  driver.current_url:
#                 login()
#
#             else:pass








# print(suspect_Finances)
# print(schoolName)
# #print(NoDataSubmitted)
#
# LAESTAB = suspect_Finances
# TrustName = schoolName
# LAESTAB2 = NoDataSubmitted
# TrustName2 = NoDataName
#
# df = pd.DataFrame.from_dict({'LAESTAB':LAESTAB,'SchoolNames':schoolName})
# df.to_excel('test.xlsx', sheet_name='Sheet1',header=True, index=False)
# df2 = pd.DataFrame.from_dict({'LAESTAB':LAESTAB2,'SchoolNames':NoDataName})
# df2.to_excel('test.xlsx', sheet_name='Sheet2',header=True, index=False)
#

#todo duplicate trusts
#todo test for finance data
#todo ancilliary data
#todo location testing
timestr = time.strftime("%A-%d%B%Y-%H%M%S")
filename = "Regression_test_resuls for " + " " + timestr+".xlsx"



def verify_Ofsted_advancedcomp():
    filename = "verifySenOftstedValues" + " " + timestr + ".xlsx"
    withoutofsted = []
    withOfsted = []
    reruns = []
    rerunschools = []
    matchingschool = []
    withofstedschools = []
    df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000, index_col=None,usecols='B,C')
    urns = df2.values.tolist()
    df3 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000,
                        index_col=None,
                        usecols='C')
    urns = df2.values.tolist()
    schoolNames = df3.values.tolist()
    dev = "https://as-t1dv-sfb.azurewebsites.net"
    driver = webdriver.firefox()
    driver.get(dev)
    driver.find_element_by_id('Username').send_keys('internal')
    driver.find_element_by_id('Password').click()
    driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
    driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    try:
            for urn, sch in zip(urns, schoolNames):
                schoolUrn = str(urn[0])
                school_name = str(schoolNames[0])
            sen_url = "https://as-t1dv-sfb.azurewebsites.net/BenchmarkCriteria/AdvancedCharacteristics?areaType=All&lacode=&lanametext=&Urn=" + str(
                urn[0]) + "&ComparisonType=Advanced&EstType=Maintained"
            driver.get(sen_url)
            openall = driver.find_element_by_class_name("accordion-expand-all")
            openall.click()
            ofstedRating = driver.find_element_by_id("checkbox-OfstedRating")
            ofstedRating.click()
            ofsted_value = driver.find_element_by_css_selector(
                "div.accordion-section:nth-child(4) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            if "No value was supplied for " in (ofsted_value):
                withoutofsted.append(str(urn))
                matchingschool.append(str(sch))
                print("No Ofsted Value for " + "" + (str(sch)))


    except (NoSuchElementException, selenium.common.exceptions.WebDriverException):

        reruns.append(str(urn))

        rerunschools.append(str(sch))

        print("Have to Re-run" + "" + schoolUrn)

        pass
    df = pd.DataFrame.from_dict({'URNS': withoutofsted, 'SchoolNames': matchingschool})
    dfreruns = pd.DataFrame.from_dict({'URNS': reruns, 'SchoolNames': rerunschools})
    dfpassed = pd.DataFrame.from_dict({'URNS': withOfsted, 'SchoolNames': withofstedschools})
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        myreport = df.to_excel(writer, sheet_name='Ofsted_test results', index=None)
        worksheet = writer.sheets['Ofsted_test results']
        myreport2 = dfreruns.to_excel(writer, sheet_name='URNS to Re-Run', index=None)
        myreport3 = dfpassed.to_excel(writer, sheet_name='URNS with OfstedValues', index=None)
    driver.quit()






def verify_keystage2_advancedcomp():
    filename = "verifySenValuesKeystage" + " " + timestr + ".xlsx"
    print("Testing For Key Stage 2 Values ")
    withoutkeystage2 = []
    withkeystage2 = []
    reruns = []
    rerunschools = []
    matchingschool = []
    withkeystageschools = []
    df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000, index_col=None,
                        usecols='B,C')
    df3 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000,
                        index_col=None,
                        usecols='C')

    schoolNames = df3.values.tolist()
    urns = df2.values.tolist()

    dev = "https://as-t1dv-sfb.azurewebsites.net"
    driver = webdriver.Firefox()
    driver.get(dev)
    driver.find_element_by_id('Username').send_keys('internal')
    driver.find_element_by_id('Password').click()
    driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
    driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    try:
        for urn, sch in zip(urns, schoolNames):
            schoolUrn = str(urn[0])
            school_name = str(schoolNames[0])
            print("Testing for " + " " + schoolUrn + " "+ school_name)
            sen_url = "https://as-t1dv-sfb.azurewebsites.net/BenchmarkCriteria/AdvancedCharacteristics?areaType=All&lacode=&lanametext=&Urn=" + str(
                urn[0]) + "&ComparisonType=Advanced&EstType=Maintained"
            driver.get(sen_url)
            openall = driver.find_element_by_class_name("accordion-expand-all")
            openall.click()
            keystage2 = driver.find_element_by_id("checkbox-MinKs2Actual")
            keystage2.click()
            keystage2_Value = driver.find_element_by_css_selector("div.accordion-section:nth-child(4) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            print(keystage2_Value)
            if "No value was supplied for " in (keystage2_Value):
                withoutkeystage2.append(str(urn))
                matchingschool.append(str(sch))
                print("No Keystage 2 value for " + " " + str(urn) + " :" +str(sch))
            else:
                print(keystage2_Value)
                withkeystage2.append(str(urn))
                withkeystageschools.append(str(sch))
    except (NoSuchElementException, selenium.common.exceptions.WebDriverException):
        reruns.append(str(urn))
        rerunschools.append(str(sch))
        print("Have to Re-run" + "" +schoolUrn)
        pass
    df = pd.DataFrame.from_dict({'URNS': withoutkeystage2, 'SchoolNames': matchingschool})
    dfreruns = pd.DataFrame.from_dict({'URNS': reruns, 'SchoolNames': rerunschools})
    dfpassed = pd.DataFrame.from_dict({'URNS': withkeystage2, 'SchoolNames': withkeystageschools})
    with pd.ExcelWriter(filename, engine='xlsxwriter') as writer:
        myreport = df.to_excel(writer, sheet_name='Keystage2 test results', index=None)
        worksheet = writer.sheets['Keystage2 test results']
        myreport2 = dfreruns.to_excel(writer, sheet_name='URNS to Re-Run', index=None)
        myreport3 = dfpassed.to_excel(writer, sheet_name='URNS with keystage2', index=None)
    driver.quit()



def verify_Prog8_advancedcomp():
    filename = "verifySenValuesProg8" + " " + timestr + ".xlsx"
    withprog8 = []
    withoutProg8 = []
    withprog8schools = []
    reruns = []
    rerunschools = []
    matchingschool = []
    df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000, index_col=None,
                        usecols='B')
    df3 =  pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000, index_col=None,
                        usecols='C')
    urns = df2.values.tolist()
    schoolNames = df3.values.tolist()
    dev = "https://as-t1dv-sfb.azurewebsites.net"
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(dev)
    driver.find_element_by_id('Username').send_keys('internal')
    driver.find_element_by_id('Password').click()
    driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
    driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    try:
        for urn,sch in zip(urns,schoolNames):
            schoolUrn = str(urn[0])
            school_name = str(schoolNames[0])
            sen_url = "https://as-t1dv-sfb.azurewebsites.net/BenchmarkCriteria/AdvancedCharacteristics?areaType=All&lacode=&lanametext=&Urn=" + str(
                urn[0]) + "&ComparisonType=Advanced&EstType=Maintained"
            driver.get(sen_url)
            openall = driver.find_element_by_class_name("accordion-expand-all")
            openall.click()
            progress8 =driver.find_element_by_id("checkbox-MinP8Mea")
            progress8.click()
            progress8_Value = driver.find_element_by_css_selector("div.accordion-section:nth-child(4) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(5) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            if "No value was supplied for " in (progress8_Value):
                withoutProg8.append(str(urn))
                matchingschool.append(str(sch))
                print("No Prog8 Value for " + "" + str(urn) + " :" +str(sch))
            else:
                print(progress8_Value)
                withprog8.append(str(urn))
                withprog8schools.append(str(sch))


    except (NoSuchElementException, selenium.common.exceptions.WebDriverException )as error:
        print(error)
        reruns.append(str(urn))
        rerunschools.append(str(sch))
        pass

    df = pd.DataFrame.from_dict({'URNS': withoutProg8, 'SchoolNames': matchingschool})
    dfreruns = pd.DataFrame.from_dict({'URNS':reruns,'SchoolNames': rerunschools})
    dfpassed = pd.DataFrame.from_dict({'URNS':withprog8,'SchoolNames': withprog8schools})
    with pd.ExcelWriter(filename,engine='xlsxwriter') as writer:
        myreport = df.to_excel(writer,sheet_name='Progress 8 test results',index=None)
        worksheet = writer.sheets['Progress 8 test results']
        myreport2 = dfreruns.to_excel(writer,sheet_name='URNS to Re-Run',index=None)
        myreport3 = dfpassed.to_excel(writer,sheet_name='URNS with Prog8',index=None)

    driver.quit()



def verify_numberOfPupils_advancedcomp():
    filename = "verifySenNumberOfPupils" + " " + timestr + ".xlsx"
    withoutnumberofpupils = []
    withnumberofpupils = []
    reruns = []
    df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx', sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000, index_col=None, usecols='B,C')
    df3 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=1000,
                        index_col=None,
                        usecols='C')
    urns = df2.values.tolist()
    schoolNames = df3.values.tolist()
    dev = "https://as-t1dv-sfb.azurewebsites.net"
    driver = webdriver.Firefox()
    driver.get(dev)
    driver.find_element_by_id('Username').send_keys('internal')
    driver.find_element_by_id('Password').click()
    driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
    driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    try:
        for urn, sch in zip(urns, schoolNames):
            schoolUrn = str(urn[0])
            school_name = str(schoolNames[0])
            sen_url = "https://as-t1dv-sfb.azurewebsites.net/BenchmarkCriteria/AdvancedCharacteristics?areaType=All&lacode=&lanametext=&Urn=" + str(
                urn[0]) + "&ComparisonType=Advanced&EstType=Maintained"
            driver.get(sen_url)
            openall = driver.find_element_by_class_name("accordion-expand-all")
            openall.click()
            number_of_pupils_button = driver.find_element_by_id("checkbox-MinNoPupil")
            number_of_pupils_button.click()
            number_of_pupils_displayed = driver.find_element_by_css_selector(
                "div.accordion-section:nth-child(2) > fieldset:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2)").text
            if "No value was supplied for " in (number_of_pupils_displayed):
                withoutnumberofpupils.append(schoolUrn)
                print("No Ofsted Value for " + "" + schoolUrn)


    except (NoSuchElementException, selenium.common.exceptions.WebDriverException):
        reruns.append(schoolUrn)
        pass
    df = pd.DataFrame.from_dict({'URNS': withoutnumberofpupils, 'SchoolNames': school_name})
    df.to_excel('verifySenValuesNumberOfPupils.xlsx', sheet_name='Sheet1', header=True, index=False)
    driver.quit()

def compare_to_gis():
    df2 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=100,
                        index_col=None, usecols='B,C')

    df3 = pd.read_excel('C:\\Users\\kwaku\\OneDrive\\Desktop\\sfb_docs\\SFB_A17-18_v1.5_test_edit.xlsx',
                        sheet_name='Academies 2017 to 18', skipinitialspace=True, skiprows=2, nrows=100,
                        index_col=None,
                        usecols='C')
    urns = df2.values.tolist()
    schoolNames = df3.values.tolist()

    dev = "https://as-t1dv-sfb.azurewebsites.net"
    driver = webdriver.Firefox()
    driver.get(dev)
    driver.find_element_by_id('Username').send_keys('internal')
    driver.find_element_by_id('Password').click()
    driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
    driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    try:
        for urn, sch in zip(urns, schoolNames):
            schoolUrn = str(urn[0])
            school_name = str(schoolNames[0])
            dev_compare_url = "https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn="+str(urn[0])
            driver.get(dev_compare_url)
            dev_address = driver.find_element_by_css_selector(".sfb_gtm_address").text
            dev_telephone_number = driver.find_element_by_css_selector(".sfb_gtm_tel").text
            dev_ofsted_Rating = driver.find_element_by_tag_name("Ofsted rating").text##content > div:nth-child(3) > div:nth-child(1) > div > dl > dd:nth-child(14)
            dev_age_range = driver.find_element_by_css_selector("dd.metadata-school-detail__dd:nth-child(20)").text
            elements_to_test_for_dev = [dev_address,dev_telephone_number,dev_ofsted_Rating,dev_age_range]
            print(elements_to_test_for_dev)
            # driver.close()
            # driver = webdriver.Chrome()
            gisurl = "https://get-information-schools.service.gov.uk/Establishments/Establishment/Details/"+str(urn[0])
            driver.get(gisurl)
            #driver.switch_to.active_element
            #driver.find_element_by_css_selector("#exit-overlay").click()
            gis_address = driver.find_element_by_css_selector("div.detail-summary:nth-child(2) > dl:nth-child(1) > dd:nth-child(2)").text
            gis_telephonenumber = driver.find_element_by_css_selector("div.detail-summary:nth-child(2) > dl:nth-child(1) > dd:nth-child(28)").text
            gis_ofstedRating = driver.find_element_by_css_selector(".highlighted-ofsted-rating").text
            gis_age_range = driver.find_element_by_css_selector("div.detail-summary:nth-child(2) > dl:nth-child(1) > dd:nth-child(8)").text
            elements_to_test_for_gis = [gis_address,gis_telephonenumber,gis_ofstedRating,gis_age_range]
            print(elements_to_test_for_gis)
            not_matched = set(elements_to_test_for_dev).difference(elements_to_test_for_gis)
            if not not_matched:
                print("This test passed ")
            else:print("There is a mismatch here " + " " + str(urn[0]))
            pass
    except NoSuchElementException as e:
        print(e)
        








#compare_to_gis()
verify_keystage2_advancedcomp()
#verify_numberOfPupils_advancedcomp()
#verify_Ofsted_advancedcomp()
#verify_Prog8_advancedcomp()






















