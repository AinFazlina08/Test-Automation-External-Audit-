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


# TC Manage Companies 1 --> Add Company and link to Brand
def TC_ManageCompanies1():
    print("\nTesting Manage Companies 1. Add Company and link to Brand")
    # 1. Go to (Admin -> Manage Companies)
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Admin/ManageCompanies")
    try:
        time.sleep(1.5)
        driver.maximize_window()
        # 2. Click Button [Add]
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div/div/div/div[1]/div/button/i').click()
        # 3. Fill in all mandatory fields
        time.sleep(1.5)
        driver.find_element_by_xpath('// *[ @ id = "CompanyName"]')
        CompanyName_box = driver.find_element_by_xpath('// *[ @ id = "CompanyName"]')
        CompanyName = "Testing 5 5/11/2021"
        # Put/Parse details of Company Name
        CompanyName_box.send_keys(CompanyName)

        CertificationBody_list = driver.find_element_by_xpath('// *[ @ id = "CertificationBodiesId"]')
        dropdownCB = Select(CertificationBody_list)
        dropdownCB.select_by_index('2')  # //*[@id="CertificationBodiesId"]/option[3] Agency for Halal Quality
        # Certification

        CompanyRegistrationType_list = driver.find_element_by_xpath('// *[ @ id = "RegistrationTypeId"]')
        dropdownCRT = Select(CompanyRegistrationType_list)  # CRT is shortform for Company Registration Type
        dropdownCRT.select_by_index('2')  # //*[@id="RegistrationTypeId"]/option[3] Overseas Companies

        driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
        BusinessRegistrationNo_box = driver.find_element_by_xpath('// *[ @ id = "CompanyRegNumber"]')
        BusinessRegNo = "05112021/3"
        # Put/Parse details of BusinessRegNo
        BusinessRegistrationNo_box.send_keys(BusinessRegNo)

        CompanyOwnerStatus_list = driver.find_element_by_xpath('// *[ @ id = "CompanyOwnerStatusId"]')
        dropdownCOS = Select(CompanyOwnerStatus_list)  # COS is shortform for Company Owner Status
        dropdownCOS.select_by_index('2')  # //*[@id="CompanyOwnerStatusId"]/option[3] Others

        time.sleep(3)
        # 4. In Brand dropdown list, select any Brand
        Brand_list = driver.find_element_by_xpath('// *[ @ id = "BrandId"]')
        dropdownBrand = Select(Brand_list)
        dropdownCOS.select_by_index('1')  # //*[@id="BrandId"]/option[2] AYAMAS
        time.sleep(3)

        # 5. Click Button [Add]
        driver.find_element_by_xpath('// *[ @ id = "btnAdd"] / i').click()
        time.sleep(3)

        dropdownCOS.select_by_index('2')  # //*[@id="BrandId"]/option[2] AYAMAS

        # 7. Click Button [Save]
        driver.find_element_by_xpath('//*[@id="btnAdd2"]').click()

        print("TEST PASSED. Able to add company and link to Brand")
    except Exception as e:
        print("TEST FAILED. Unable to add company and link to Brand", e)


# TC Manage Companies 2 --> View Company
def TC_ManageCompanies2():
    print("\nTesting Manage Companies 2. View Company")
    # 1. Go to (Admin -> Manage Companies)
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Admin/ManageCompanies")
    try:
        # 1. Select any data
        time.sleep(1.5)
        driver.maximize_window()
        # driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[1]/td[2]/a[1]/i').click()
        time.sleep(1.5)

        scroll = driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[1]/td[2]/a[1]/i')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[1]/td[2]/a[1]/i').click()
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

        # driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[5]/td[2]/a[1]/i').click()  # CompanyID=5516
        # 2. Click Action button [View]
        print("TEST PASSED. Able to view Company")
    except Exception as e:
        print("TEST FAILED. Unable to View Company", e)

# TC Manage Companies 3 --> Delete Company
def TC_ManageCompanies3():
    print("\nTesting Manage Companies 2. Delete Company")
    # 1. Go to (Admin -> Manage Companies)
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Admin/ManageCompanies")
    try:
        # 1. Select any data
        time.sleep(1.5)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="CompanyDataTable"]/tbody/tr[2]/td[2]/a[3]/i').click()
        time.sleep(1.5)
        driver.implicitly_wait(10)  # seconds
        alert = Alert(driver)
        alert.accept()

        print("TEST PASSED. Able to delete Company")
    except Exception as e:
        print("TEST FAILED. Unable to delete Company", e)


openChrome()
login()
TC_ManageCompanies3()
