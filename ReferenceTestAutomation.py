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


# TC Reference 1 --> Verify Reference page
def TC_Reference1():
    print("\nTesting TC Reference 1. Verify Reference page")
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Dashboard")  # Dashboard page
    try:
        driver.maximize_window()
        time.sleep(1.5)
        # Go to Reference
        driver.find_element_by_xpath('//*[@id="Reference"]').click()
        time.sleep(1.5)
        print("TEST PASSED. Verify all Reference populated from Admin - Reference Data - Web Links and display "
              "correctly ")
    except Exception as e:
        print("TEST FAILED. Not able to verify Reference Page", e)


# TC Reference 2 -->Able to open Reference in new tab
def TC_Reference2():
    print("\nTesting TC Reference 2. Able to open Reference in new tab")
    TC_Reference1()
    try:
        time.sleep(1.5)
        # Click Hyperlink [Any Reference]
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[5]').click()  # click on Serunai webpage
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div[3]/div[4]').click()  # click on AYAMAS GLOBAL webpage
        time.sleep(1.5)
        driver.implicitly_wait(30)
        # //*[@id="referenceId"]
        # //*[@id="referenceId"]/b
        # /html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div[5]
        print("TEST PASSED. System open a new tab and display the website as configured")

    except Exception as e:
        print("TEST FAILED. Not able to open Reference in new tab", e)


openChrome()
login()
TC_Reference2()
