import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException



driver = webdriver.Chrome()


Number_of_pupils = driver.find_element_by_css_selector("#checkbox-MinNoPupil")
School_overall_phase = driver.find_element_by_css_selector("#checkbox-SchoolOverallPhase")
Schhol_phase = driver.find_element_by_css_selector("#checkbox-SchoolPhase")
Schhol_type = driver.find_element_by_css_selector("#label-TypeOfEstablishment")

Eligibility_for_freeschoolmeals =driver.find_element_by_css_selector("#checkbox-MinPerFSM")
Special_needs = driver.find_element_by_css_selector("#checkbox-MinPerSENReg")
sen_ehc_plans = driver.find_element_by_css_selector("#checkbox-MinPerSEN")
englash_as_additionallanguage =driver.find_element_by_css_selector("#checkbox-MinPerEAL")
urban_rural_schools= driver.find_element_by_css_selector("#checkbox-UrbanRural")
london_weighing = driver.find_element_by_css_selector("#checkbox-LondonWeighting")
governmanet_office_region = driver.find_element_by_css_selector("#checkbox-GovernmentOffice")
part_of_a_private_firm = driver.find_element_by_css_selector("#checkbox-Pfi")
number_in_sixthform = driver.find_element_by_css_selector("#checkbox-MinNoSixthForm")
gender_of_pupils = driver.find_element_by_css_selector("#checkbox-Gender")
lowest_age_of_pupils = driver.find_element_by_css_selector("#checkbox-MinLowestAgePupils")
highets_age_of_pupils = driver.find_element_by_css_selector("#checkbox-MinHighestAgePupils")
boarders = driver.find_element_by_css_selector("#checkbox-MinPerBoarders")
admissions_policy = driver.find_element_by_css_selector("#checkbox-AdmPolicy")

