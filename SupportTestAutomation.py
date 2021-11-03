import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# Open Chrome browser
def openChrome():
    global driver
    driver = webdriver.Chrome(executable_path="C:\\Users\\USER\\Downloads\\chromedriver.exe")
    return driver


# function for login
def login():
    driver.get("https://vhsmartqsrtest.azurewebsites.net/")
    try:
        username_box = driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = driver.find_element_by_xpath('//*[@id="Input_Password"]')
        username = "admin@qsrbrands.com.my"
        password = "p@ssw0rd1234"
        # Login into VHSmart
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
        print('TEST PASSED')

    except Exception as e:
        print('TEST FAILED.Unable to Login', e)


# TC Support 1 --> Verify Support page
def TC_Support1():
    print("\nTesting TC Support 1. Verify Support Page")
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Dashboard")  # Dashboard page
    try:
        driver.maximize_window()
        time.sleep(1.5)
        # Go to Support page
        driver.find_element_by_xpath('//*[@id="Support"]').click()
        time.sleep(1.5)
        print("TEST PASSED. Support page being display correctly ")
    except Exception as e:
        print("TEST FAILED. Not able to verify Support Page", e)


# TC Support 2 --> View FAQ (Frequently Asked Questions)
def TC_Support2():
    print("\nTesting TC Support 2. View FAQ (Frequently Asked Questions)")
    TC_Support1()
    try:
        time.sleep(1.5)
        # Click FAQs button
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div[3]').click()
        time.sleep(1.5)
        driver.implicitly_wait(30)
        print("TEST PASSED. System open a new tab and display the FAQs (Frequently Asked Questions)")

    except Exception as e:
        print("TEST FAILED. Not able to open new tab and display the FAQs (Frequently Asked Questions)", e)


# TC Support 3 --> Feedback to Serunai Support Team
def TC_Support3():
    print("\nTesting TC Support 3. Feedback to Serunai Support Team")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/Support/Index')
    try:
        time.sleep(1.5)
        # Click More Questions button
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div/div[4]').click()
        time.sleep(1.5)
        # 3. Select any Category
        SelectCategory_list = driver.find_element_by_xpath('//*[@id="FeedbackCategoryId"]')
        dropdownDetails = Select(SelectCategory_list)
        dropdownDetails.select_by_index('2')  # 1. Enquiry 2. Complaint 3. Comment 4. Suggestion
        # 4. Fill in the details
        Details_box = driver.find_element_by_xpath('// *[ @ id = "FeedbackComment"]')
        Details = "Cannot add staff information"
        # Put/Parse details of Remarks
        Details_box.send_keys(Details)
        # // *[ @ id = "FeedbackComment"]
        # 5. Click Button (Submit)
        # //*[@id="btnAdd"]/i
        driver.find_element_by_xpath('//*[@id="btnAdd"]/i').click()
        print("TEST PASSED. System prompt successful message. Your feedback has submitted")

    except Exception as e:
        print("TEST FAILED. System prompt message . Failed to submit your feedback!", e)


openChrome()
login()
TC_Support2()
TC_Support3()