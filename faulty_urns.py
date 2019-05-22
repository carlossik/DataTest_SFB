from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException
from selenium.common.exceptions import TimeoutException
import requests, bs4
from selenium import webdriver
import python_utils
import data_set
#import advancedcriteriapage
from bs4 import BeautifulSoup



list_of_urns = data_set.menatined_2019
print(len(list_of_urns))

driver = webdriver.Chrome("C:\\Users\\kwaku\\OneDrive\\Desktop\\chromedriver\\chromedriver.exe")
driver.maximize_window()
zero_data = []
empty_get_more_info_link = []
sen_charatcteristics = []
def login():
    try:
        login_screen = driver.get('https://as-t1dv-sfb.azurewebsites.net/')
        driver.find_element_by_id('Username').send_keys('internal')
        driver.find_element_by_id('Password').click()
        driver.find_element_by_id('Password').send_keys('sfb_19twspssc03')
        driver.find_element_by_xpath('//*[@id="loginForm"]/form/div[4]/div/input').click()
    except NoSuchElementException:
        pass
        #print('login page not loaded')
        #driver.refresh()
def testSSEN():
    try:
        url = "https://schools-financial-benchmarking.service.gov.uk/School/Detail?urn=" + str(urn)
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="benchmarkControlsPlaceHolder"]/div[2]/div/a[1]').click()
        # driver.
        driver.find_element_by_xpath('//*[@id="radio-2"]').click
        driver.implicitly_wait(2)
        driver.find_element_by_id("radio-2").click()
        driver.find_element_by_css_selector(".button").click()
        driver.find_element_by_css_selector('#radio-1').click()
        driver.find_element_by_css_selector(".button").click()
        driver.find_element_by_css_selector("#All").click()
        driver.find_element_by_css_selector(".button").click()
        driver.find_element_by_css_selector("#GeneralHeader > span:nth-child(1)").click()
        driver.find_element_by_css_selector("#checkbox-MinNoPupil").click()
        #driver.find_element_by_css_selector("#checkbox-MinNoPupil").click()
        driver.find_element_by_css_selector("#checkbox-SchoolOverallPhase").click()
        driver.find_element_by_css_selector("#checkbox-SchoolPhase").click()
        driver.find_element_by_css_selector("#label-TypeOfEstablishment").click()
        driver.find_element_by_css_selector("#checkbox-MinPerFSM").click()
        driver.find_element_by_css_selector("#checkbox-MinPerSENReg").click()
        driver.find_element_by_css_selector("#checkbox-MinPerSEN").click()
        driver.find_element_by_css_selector("#checkbox-MinPerEAL").click()
        driver.find_element_by_css_selector("#checkbox-UrbanRural").click()
        driver.find_element_by_css_selector("#checkbox-LondonWeighting").click()
        driver.find_element_by_css_selector("#checkbox-GovernmentOffice").click()
        driver.find_element_by_css_selector("#checkbox-Pfi").click()
        driver.find_element_by_css_selector("#checkbox-MinNoSixthForm").click()
        driver.find_element_by_css_selector("#checkbox-Gender").click()
        driver.find_element_by_css_selector("#checkbox-MinLowestAgePupils").click()
        driver.find_element_by_css_selector("#checkbox-MinHighestAgePupils").click()
        driver.find_element_by_css_selector("#checkbox-MinPerBoarders").click()
        driver.find_element_by_css_selector("#checkbox-AdmPolicy").click()

    except NoSuchElementException as e:
        sen_charatcteristics.append(urn)
        print("Sen Values not complete for " + str(urn))
        pass




def search_for_school():
    try:
        driver.find_element_by_css_selector("").click()
        driver.find_element_by_css_selector("").send_keys("")
        driver.find_element_by_css_selector("").click()

    except NoSuchElementException as e:
        print("cannot test" + " " + e)



def validate_schoolPhase(urn):

    try:
        driver.get('https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=' + str(urn))

        source2 = driver.page_source#requests.get('https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=' + str(urn))
        soup1 = BeautifulSoup(source2, 'html.parser')
        school_phase = soup1.find('a', text='School phase')
        school_phase1 = soup1.select('dd.metadata-school-detail__dd:nth-child(8)')
        ageRangeOfPupils = soup1.find('a', {'class': 'metadata-school-detail__dd bold'})
        #print(school_phase1)

        if school_phase1 == []:
            print("School Phase not found for " + urn)



    except AttributeError as e:
        print("could not resolve " + str(urn))

def validate_Ofsted(urn):
    try:
        driver.get('https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=' + str(urn))

        source2 = driver.page_source#requests.get('https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=' + str(urn))
        soup1 = BeautifulSoup(source2, 'html.parser')
        ofsted2 = soup1.find("span", {'class': 'rating-text'}).text
        if ofsted2 == "Not Rated":
            print("Not rated test passed ")
            print(ofsted2)


    except AttributeError as e:
        print("could not resolve " + str(urn))


login()
for urn in list_of_urns:

    try:
        validate_schoolPhase(urn)
        #testSSEN()
    except ElementNotVisibleException:
        driver.refresh()


#dd.metadata-school-detail__dd:nth-child(10)
#
#
#         website = 'https://as-t1dv-sfb.azurewebsites.net/School/Detail?urn=' + str( urn) + '&tab=Expenditure&unit=AbsoluteMoney&format=Charts'
#         driver.get(website)
#         driver.implicitly_wait(5)
#         expenditure = driver.find_element_by_xpath('//*[@id="financialSummary"]').text
#         #getmoreinfolink = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/div/dl/dd[14]/a")
#         getmoreinfolink = driver.find_element_by_css_selector(".sfb_gtm_more_info")
#         try:
#             if '£0' in expenditure:
#                 print("Financial data not available for " + str(urn))
#                 zero_data.append(urn)
#             else:print("financial data is available for " + str(urn))
#         except NoSuchElementException:
#             print("Expenditure not displayed")
#         try:
#             if getmoreinfolink.is_displayed():
#                 print("Get_more_info_link is available for " + str(urn))
#             else:
#                 print("Get_more_info_link is  not available for " + str(urn))
#                 empty_get_more_info_link.append(urn)
#         except NoSuchElementException:print("Get more info link not available")
#
#         #print("Financial data not available for " + str(urn)) if '£0' in expenditure else print("Financial data available for " + str(urn))
#         #zero_data.append(urn)
#     except (NoSuchElementException ,TimeoutException ) as e:
#         login()
#         print("Could not resolve " + "" + str(urn) + str(e))
#         pass
#
# print(zero_data)
# print(empty_get_more_info_link)
#



# driver.refresh()







    # except NoSuchElementException:
    #     print('could not load page' + " " + str(urn) + " " + driver.current_url)
        #
        #     print("This School has no finance data " + " " + str(urn)+ " "+ driver.current_url) if expenditure == '£0.00' else print('Expenditure is OK')
        # except NoSuchElementException:
    #     #     print('Element not found')
    # except NoSuchElementException:
    #     print('could not load page' + " " + str(urn) + " " +  driver.current_url)
    #     driver.refresh()
    #     login()