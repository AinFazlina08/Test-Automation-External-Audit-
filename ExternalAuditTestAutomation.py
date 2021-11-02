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


# TC_ExternalAudit_1 --> Verify External Audit Report page #PASSED
def TC_ExternalAudit1():
    print("\nTesting TC_ExternalAudit1")
    driver.get("https://vhsmartqsrtest.azurewebsites.net/Dashboard")
    try:
        driver.maximize_window()
        # Go to(Audit-->Audit Report-->External)
        driver.find_element_by_xpath('//*[@id="AuditModule1"]').click()  # click on Audit
        driver.find_element_by_xpath('//*[@id="AuditReport"]').click()
        driver.find_element_by_xpath('//*[@id="AuditReport"]/i[2]').click()  # click on Dropdown list
        driver.find_element_by_xpath('//*[@id="AuditModule"]/ul[6]/li/ul/li/a').click()

        print("TEST PASSED. Able to verify External Audit Report page successfully")
    except Exception as e:
        print("TEST FAILED.Unable to verify External Audit Report page", e)

    # Check Add button
    try:
        driver.find_element_by_xpath('/ html / body / div[2] / div[1] / div[3] / div[2] / div / div / div / div[1] / div / button / i')
        print("TEST PASSED. Add button available")
    except Exception as e:
        print("TEST FAILED", e)

    # Check Action buttons: View,Edit,Delete
    try:
        # check View button exist
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[1]/i')

        # check Edit button exist
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[2]/i')

        # check Delete button exist
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[3]/i')
        print("TEST PASSED. Edit,View,Delete buttons available")
    except Exception as e:
        print("TEST FAILED", e)


# TC_ExternalAudit_2 --> Verify Add External Audit Report page #PASSED
def TC_ExternalAudit2():
    print("\nTesting TC_ExternalAudit2")
    driver.get("https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index")

    try:
        driver.find_element_by_xpath('/ html / body / div[2] / div[1] / div[3] / div[2] / div / div / div / div[1] / div / button / i').click()
        print("TEST PASSED. Able to verify Add External Audit Report page")
    except Exception as e:
        print("TEST FAILED", e)


# TC_ExternalAudit_3 --> Verify Type of Inspection #PASSED
def TC_ExternalAudit3():
    print("\nTesting TC_ExternalAudit3")
    TC_ExternalAudit1()
    TC_ExternalAudit2()
    # select Type of Inspection dropdown list
    try:
        time.sleep(1.5)
        type_of_Inspection = driver.find_elements_by_xpath('//*[@id="ExtTypeInspection_Id"]/option')
        type_of_Inspection = len(type_of_Inspection) - 1
        # print(type_of_Inspection)

        # create list to check the options in dropdown list
        type_of_Inspection_List = list()
        expected_List = ['AUDIT', 'REAUDIT', 'ADHOC/WILDCARD', 'NEW SUPPLIER', 'PERIODICAL AUDIT', 'PRELIMINARY AUDIT',
                         'QUARTERLY AUDIT', 'REVIEW', 'ROUTINE']
        for iGroup in range(type_of_Inspection):
            if type_of_Inspection != 9:
                print('TEST FAILED! Number of options are not equal to 9')
            break
        type_of_Inspection_List.append(
            driver.find_element_by_xpath('//*[@id="ExtTypeInspection_Id"]/option[' + str(3) + ']').get_attribute(
                'textContent'))
        driver.find_element_by_xpath('//*[@id="ExtTypeInspection_Id"]/option[' + str(3) + ']').click()

        print('TEST PASSED. Able to verify Type of Inspection. Type of Inspection is populated as follows:\n',
              expected_List, 'from Database')

    except Exception as e:
        print('TEST FAILED ! Not able to verify Type of Inspection list', e)


# TC_ExternalAudit_4 --> Verify CB Application No. # List is not yet completed
def TC_ExternalAudit4():
    print("\nTesting TC_ExternalAudit4")
    TC_ExternalAudit1()
    TC_ExternalAudit2()
    # select CB Halal Application No list
    try:
        time.sleep(1.5)
        CB_HalalApplication_No = driver.find_elements_by_xpath('//*[@id="ExtCBRefApplicationNo_Id"]/option')
        CB_HalalApplication_No = len(CB_HalalApplication_No) - 1
        print(CB_HalalApplication_No)

        # create list to check the options in dropdown list
        CB_HalalApplication_No_List = list()
        expected_List = ['HALAL-20160418-081147(PR)', 'HALAL-20160418-081147(PR)', 'HALAL-20160418-081147(PR)',
                         'HALAL-20161012-082921(PR)', 'HALAL-20170216-092959(BG)', 'HALAL-20180309-161440(PR)',
                         'HALAL-20181130-093024(KO)', 'HALAL-20190508-074731(PM)', 'HALAL-20190530-071110(PM)',
                         'HALAL-20190610-100429(PM)', 'HALAL-20190610-102103(PM)', 'HALAL-20190704-132443(PR)',
                         'HALAL-20190708-091522(PM)', 'HALAL-20190708-091608(PM)', 'HALAL-20190904-080917(PM)',
                         'HALAL-20190905-134218(PM)', 'HALAL-20190923-100728(PM)', 'HALAL-20190927-093219(PM)',
                         'HALAL-20191001-143030(PM)', 'HALAL-20191001-144108(PM)', 'HALAL-20191001-150854(PM)',
                         'HALAL-20191030-141122(PM)', 'HALAL-20191108-080524(PM)', 'HALAL-20191108-080831(PM)',
                         'HALAL-20191206-101059(PM)', 'HALAL-20200108-110056(PM)', 'HALAL-20200114-142620(PM)',
                         'HALAL-20200207-085020(PM)', 'HALAL-20200207-090544(PM)', 'HALAL-20200207-091259(PM)',
                         'HALAL-20200207-151634(PM)', 'HALAL-20200302-095059(PM)', 'HALAL-20200313-082209(PM)',
                         'HALAL-20200313-082240(PM)', 'HALAL-20200429-111732(PM)', 'HALAL-20200429-112307(PM)',
                         'HALAL-20200429-112824(PM)', 'HALAL-20200429-113525(PM)', 'HALAL-20200512-073757(PM)',
                         'HALAL-20200513-111122(PM)', 'HALAL-20200519-075840(PM)', 'HALAL-20200519-080022(PM)',
                         ]
        for iGroup in range(CB_HalalApplication_No):
            if CB_HalalApplication_No != 111:
                print('TEST FAILED! Number of options are not equal to 111')
            break
            # // *[ @ id = "ExtCBRefApplicationNo_Id"] / option[2]
        CB_HalalApplication_No_List.append(
            driver.find_element_by_xpath(
                '// *[ @ id = "ExtCBRefApplicationNo_Id"] / option[' + str(2) + ']').get_attribute(
                'textContent'))
        driver.find_element_by_xpath('// *[ @ id = "ExtCBRefApplicationNo_Id"] / option[' + str(2) + ']').click()
        print('TEST PASSED. CB Application No. populated from Halal Application -> My Application with Status = '
              'PROCESSING AT JAKIM (NEW) / PROCESSING AT JAKIM (RENEWAL) ')

    except Exception as e:
        print('TEST FAILED ! Not able to verify CB Application No. list', e)


# TC_ExternalAudit_5 --> Verify Brand Owner #PASSED
def TC_ExternalAudit5():
    print("\nTesting TC_ExternalAudit5")
    # Brand Owner list
    TC_ExternalAudit1()
    TC_ExternalAudit2()
    try:
        time.sleep(1.5)
        ForCompany = driver.find_elements_by_xpath('//*[@id="BrandOwner_Id"]/option')
        ForCompany = len(ForCompany) - 1
        print(ForCompany)

        # create list to check the options in dropdown list
        ForCompany_List = list()
        expected_List = ['AYAMAS FOOD CORPORATION SDN BHD', 'COMPANY SDN BHD', 'COMPANY XYZ', 'COMPK1',
                         'KARA HOLDINGS SDN. BHD.', 'KCOMPANY', 'PHD DELIVERY SDN.BHD.',
                         'PIZZA HUT RESTAURANTS SDN. BHD.', 'QSR BRANDS (M) HOLDINGS BHD', 'QSR MANUFACTURING SDN BHD',
                         'QSR STORES SDN. BHD.', 'QSR TRADING SDN BHD',
                         'REGION FOOD INDUSTRIES SDN BHD', 'TING TONG', 'TING TONG']
        for iGroup in range(ForCompany):
            if ForCompany != 15:
                print('TEST FAILED! Number of options are not equal to 15')
            break
        ForCompany_List.append(
            driver.find_element_by_xpath('// *[ @ id = "BrandOwner_Id"] / option[' + str(9) + ']').get_attribute(
                'textContent'))
        driver.find_element_by_xpath('// *[ @ id = "BrandOwner_Id"] / option[' + str(9) + ']').click()

        print('TEST PASSED. 1. Brand Owner populated from Company Information - Profiles')

    except Exception as e:
        print('TEST FAILED ! 1. Brand Owner not populated from Company Information - Profiles', e)


# TC_ExternalAudit_6 --> Verify Received From # List is not completed
def TC_ExternalAudit6():
    print("\nTesting TC_ExternalAudit6")
    # Received From list
    TC_ExternalAudit1()
    TC_ExternalAudit2()
    try:
        time.sleep(1.5)
        ReceivedFrom = driver.find_elements_by_xpath('//*[@id="CertificationBodies_Id"]/option')
        ReceivedFrom = len(ReceivedFrom) - 1
        print(ReceivedFrom)

        # create list to check the options in dropdown list
        ReceivedFrom_List = list()
        expected_List = ['Muslim Judicial Council Halaal Trust (MJCHT)', 'Agency for Halal Quality Certification',
                         'ARA Halal Certification Services Centre Inc.',
                         'Association for the Inspection and Certification of Food and Supplies(GIMDES)',
                         'Association Halal Industry of Kazakhstan(AHIK)',
                         'Australia Halal Authority & Advisers(AHAA)',
                         'Australian National Imams Council (ANIC)',
                         'CB TESTING',
                         'CB2',
                         'CB3',
                         'CB5',
                         'Centre For Halal Quality Certification (CHQC)',
                         'Centro Islamico De Chile',
                         'China Islamic Association',
                         'Co.Re.Is-Halal Italia',
                         'Control Office of Halal Slaughtering B.V & Halal Quality Control',
                         'Egyption Organization for Standardization & Quality (EOS)']
        for iGroup in range(ReceivedFrom):
            if ReceivedFrom != 96:
                print('TEST FAILED! Number of options are not equal to 96')
            break
        ReceivedFrom_List.append(
            driver.find_element_by_xpath(
                '// *[ @ id = "CertificationBodies_Id"] / option[' + str(3) + ']').get_attribute(
                'textContent'))
        driver.find_element_by_xpath('// *[ @ id = "CertificationBodies_Id"] / option[' + str(3) + ']').click()

        print('TEST PASSED. 1. Brand Owner populated from Reference Data - Certification Bodies ')

    except Exception as e:
        print('TEST FAILED ! 1. Brand Owner not populated from Reference Data - Certification Bodies ', e)


# TC_ExternalAudit_7 --> Add External Audit Report
def TC_ExternalAudit7():
    print("\nTesting TC_External Audit 7")
    # driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')
    TC_ExternalAudit1()
    try:
        # 3. Click Button [Add]
        time.sleep(1.5)
        driver.find_element_by_xpath('/ html / body / div[2] / div[1] / div[3] / div[2] / div / div / div / div[1] / div / button / i').click()
        # insert element into For Company field #PASSED
        ForCompany_list = driver.find_element_by_xpath('//*[@id="BrandOwner_Id"]')
        dropdownCompany = Select(ForCompany_list)
        dropdownCompany.select_by_index('5')  # KARA HOLDINGS SDN BHD

        # insert element into Received From field #PASSED
        ReceivedFrom_list = driver.find_element_by_xpath('//*[@id="CertificationBodies_Id"]')
        dropdownReceive = Select(ReceivedFrom_list)
        dropdownReceive.select_by_index('2')  # Agency for Halal Quality Certification

        # insert element into CB Audit Reference No field #PASSED
        CB_ReferenceNo_box = driver.find_element_by_xpath('//*[@id="NCR_AuditReportNo"]')
        CB_ReferenceNo = "AFHQC-20211018/10"  # this CB_no. is randomly filled?
        # Put/Parse details of CB Audit Reference No
        CB_ReferenceNo_box.send_keys(CB_ReferenceNo)

        # insert element into Type of Application field #PASSED
        TypeofApplication_list = driver.find_element_by_xpath('// *[ @ id = "ExtTypeApplication_Id"]')
        dropdownTypeofApplication = Select(TypeofApplication_list)
        dropdownTypeofApplication.select_by_index('3')  # 1. New 2. Renewal 3. Additional 4. Post Audit

        # insert element into Type of Inspection field #PASSED
        TypeofInspection_list = driver.find_element_by_xpath('//*[@id="ExtTypeInspection_Id"]')
        dropdownTypeofInspection = Select(TypeofInspection_list)
        dropdownTypeofInspection.select_by_index(
            '3')  # 1.AUDIT  2. REAUDIT  3. ADHOC/WILDCARD 4. NEW SUPPLIER ... 9. ROUTINE

        # insert element into Application Scheme field #PASSED
        ApplicationScheme_list = driver.find_element_by_xpath('//*[@id="Scheme_Id"]')
        dropdownApplication_Scheme = Select(ApplicationScheme_list)
        dropdownApplication_Scheme.select_by_index(
            '1')  # 1. Food Products / Beverages / Supplements (PR) 2. Food Premise (PM)

        # insert element into CB Halal Application No field
        CBHalalApplication_list = driver.find_element_by_xpath('//*[@id="ExtCBRefApplicationNo_Id"]')
        dropdownCBHalalApplication = Select(CBHalalApplication_list)
        dropdownCBHalalApplication.select_by_index('5')  # 1. HALAL-20160418-081147(PR) 2. HALAL-20160418-081147(PR)
        # 3. HALAL-20160418-081147(PR) 4. HALAL-20161012-082921(PR) 5. HALAL-20170216-092959(BG) 6.
        # HALAL-20180309-161440(PR) 7. HALAL-20181130-093024(KO) 8. HALAL-20190508-074731(PM) ... last.
        # HALAL-CERT-2022-05-237462

        # insert element into Certification No. field #PASSED
        CertificationNo_box = driver.find_element_by_xpath('//*[@id="NCR_CertificationNo"]')
        CertificationNo = "Testing 1230"
        # Put/Parse details of CertificationNo
        CertificationNo_box.send_keys(CertificationNo)

        # insert element into Audit Date field #PASSED
        AuditDate_box = driver.find_element_by_xpath('//*[@id="DateReceived"]')
        AuditDate = "01/01/1999"
        # Put/Parse details of Audit Date
        AuditDate_box.send_keys(AuditDate)

        # insert element into Time In field #PASSED
        TimeIn_box = driver.find_element_by_xpath('//*[@id="TimeIn"]')
        TimeIn = "3:12PM"
        # Put/Parse details of Time In
        TimeIn_box.send_keys(TimeIn)

        # insert element into Time Out field #PASSED
        TimeOut_box = driver.find_element_by_xpath('//*[@id="TimeOut"]')
        TimeOut = "12:12PM"
        # Put/Parse details of Time Out
        TimeOut_box.send_keys(TimeOut)

        # insert element into Remarks field #PASSED
        Remarks_box = driver.find_element_by_xpath('//*[@id="SummaryFindings"]')
        Remarks = "Testing"
        # Put/Parse details of Remarks
        Remarks_box.send_keys(Remarks)

        # insert element into Overall Status field #PASSED
        OverallStatus_list = driver.find_element_by_xpath('//*[@id="NCRStatus_Id"]')
        dropdownOverallStatus = Select(OverallStatus_list)
        dropdownOverallStatus.select_by_index('2')  # 1. Opened 2. Closed

        # click Save button #PASSED
        driver.find_element_by_xpath('//*[@id="btnSaveNCRExternalCB"]').click()

        # click OK button popup
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[1]').click() # cannot click OK button

        # click CLOSE button
        # driver.find_element_by_xpath('// *[ @ id = "ReferenceModal"] / div / div / div[2] / button[2]').click()

        print("TEST PASSED. Able to add External Audit Report")

    except Exception as e:
        print("TEST FAILED. Not able to add External Audit Report", e)


# Add List of Non Conformance #PASSED
def TC_ExternalAudit8():
    print("\nTesting TC_External Audit 8")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')
    try:
        time.sleep(1.5)
        driver.maximize_window()
        # Click Edit button
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[2]/td[1]/a[2]/i').click()
        time.sleep(1.5)
        # insert element into Item (List Premise / Manufacturer )
        Item_list = driver.find_element_by_xpath('//*[@id="SelectedItemHalalApplicationId"]')
        dropdownItem = Select(Item_list)
        dropdownItem.select_by_index('1')  # 1. Not Available

        # insert element into Details (List Menu / Product)
        Details_list = driver.find_element_by_xpath('// *[ @ id = "SelectedItemDetailsHalalApplicationId"]')
        dropdownDetails = Select(Details_list)
        dropdownDetails.select_by_index('1')  # 1. Not Available

        # insert element into Reference
        Reference_list = driver.find_element_by_xpath('// *[ @ id = "Ext_AuditReference_Id"]')
        dropdownReference = Select(Reference_list)
        dropdownReference.select_by_index('2')  # 1.REFERENCE 2. EXTERNAL REF 1 3. MALAYSIA HALAL CERTIFICATE PROCEDURE
        # 4. MS1500:2009 5. MS2200:PART 1:2008

        # insert element into Clause field
        Clause_box = driver.find_element_by_xpath('//*[@id="NCRDetails_Clause"]')
        Clause = "Testing 012"
        # Put/Parse details of Remarks
        Clause_box.send_keys(Clause)

        # insert element into Non Conformance Details
        NonConformanceDetails_list = driver.find_element_by_xpath('//*[@id="NCRDetails_SelectedId"]')
        dropdownNCRDetails = Select(NonConformanceDetails_list)
        dropdownNCRDetails.select_by_index('3')  # 1. Alamat premis tidak sama seperti dalam rekod JSPH 2. Apron pekerja
        # kotor dan tidak bersih / Tidak memakai kasut yang sesuai / Tidak memakai penutup kepada (hair net) / 3.
        # Bahan kimia diletak dekat dengan produk makanan ... last: Tidak mengikut FIFO

        # insert element into Remarks field
        RemarksNCR_box = driver.find_element_by_xpath('//*[@id="NCRDetails_Remarks"]')
        RemarksNCR = "Testing 001"
        # Put/Parse details of Remarks
        RemarksNCR_box.send_keys(RemarksNCR)

        # click Save/Add button
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="addManageNCR"]/button').click()

        print("TEST PASSED. Able to add List of Non Conformance")
    except Exception as e:
        print("TEST FAILED. Not able to add List of Non Conformance", e)


# TC External Audit 9 --> Edit List of Non Conformance
# TC External Audit 10 --> Delete List of Non Conformance
def TC_ExternalAudit10():
    print("\nTesting TC_External Audit 11: Add Attachment")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        time.sleep(1.5)
        driver.maximize_window()
        # click Edit button
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[2]/i').click()
        time.sleep(1.5)
        # click Delete button at List of Non Conformance Table
        driver.find_element_by_xpath('//*[@id="ExternalNCRDetails"]/tbody/tr/td[1]/a/i').click()
        driver.implicitly_wait(10)  # seconds
        alert = Alert(driver)
        alert.accept()
        print("TEST PASSED. Able to delete List of Non Conformance.")

    except Exception as e:
        print("TEST FAILED. Unable to delete List of Non Conformance ", e)


# TC External Audit 11 --> Add Attachment #PASSED
def TC_ExternalAudit11():
    print("\nTesting TC_External Audit 11: Add Attachment")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        driver.maximize_window()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[2]/i').click()  # click Edit button
        time.sleep(1.5)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll until last of page
        driver.find_element_by_xpath('//*[@id="AttachmentInfo"]').click()
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # scroll until last of page
        # scroll = driver.find_element_by_xpath('//*[@id="AttachmentInfo"]').click()
        # driver.execute_script("arguments[0].scrollIntoView();", scroll)
        DocumentType_list = driver.find_element_by_xpath('//*[@id="NCRExt_DocumentType_Id"]')
        dropdownDocumentType_Details = Select(DocumentType_list)
        dropdownDocumentType_Details.select_by_index('2')  # 1. Audit Report 2. Non Conformance Report 3. Halal
        driver.implicitly_wait(1.5)
        driver.find_element_by_xpath('//*[@id="file"]').send_keys("C://Users/USER/Downloads/Testing 2.1MB.pdf")
        driver.find_element_by_xpath('//*[@id="ManageProduct_FileAttach"]').click()
        # click Close button
        driver.find_element_by_xpath('//*[@id="ReferenceModal"]/div/div/div[2]/button[2]').click()
        print("TEST PASSED. Able to add attachment")
    # //*[@id="NCRExt_DocumentType_Id"]/option[2]
    except Exception as e:
        print("TEST FAILED. Unable to add attachment", e)


# TC External Audit 12 --> Download Attachment #PASSED
def TC_ExternalAudit12():
    print("\nTesting TC_External Audit 12: Download Attachment")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        driver.maximize_window()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[1]/i').click()  # Click View button
        time.sleep(1.5)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll until last of page
        driver.find_element_by_xpath('//*[@id="AttachmentInfo"]').click()
        scroll = driver.find_element_by_xpath('//*[@id="AttachmentInfo"]')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll until last of page
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="AddAttachment"]/tbody/tr[2]/td[1]/a/i').click()  # click Download button
        print("TEST PASSED. Able to download attachment")
    except Exception as e:
        print("TEST FAILED. Not Able to download attachment. ", e)


# TC External Audit 13 --> Delete Attachment
def TC_ExternalAudit_13():
    print("\nTesting TC_ExternalAudit_13. Delete Attachment")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        driver.maximize_window()
        time.sleep(1.5)
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[2]/i').click()  # click Edit button
        time.sleep(1.5)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll until last of page
        driver.find_element_by_xpath('//*[@id="AttachmentInfo"]').click()
        scroll = driver.find_element_by_xpath('//*[@id="AttachmentInfo"]')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # scroll until last of page
        time.sleep(1.5)
        # //*[@id="AddAttachment"]/tbody/tr[1]/td[1]/a[2]/i
        driver.find_element_by_xpath('//*[@id="AddAttachment"]/tbody/tr[1]/td[1]/a[2]/i').click()
        # delete testingfile3.05mb.pdf
        driver.implicitly_wait(10)  # seconds
        alert = Alert(driver)
        alert.accept()

        print("TEST PASSED. Able to delete Attachment")
    except Exception as e:
        print("TEST FAILED. Not able to delete Attachment", e)


# TC External 14 --> View External Audit Report
def TC_ExternalAudit14():
    print("\nTesting TC_External_14: View External Audit Report")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        driver.maximize_window()
        driver.implicitly_wait(10)  # seconds
        time.sleep(3)
        # 1-5 : PASSED ,
        # 6-10 : FAILED
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)') # scroll until last of page
        driver.implicitly_wait(10)  # seconds
        scroll = driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[5]/td[1]/a[1]/i')
        # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.implicitly_wait(10)  # seconds
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[5]/td[1]/a[1]/i').click()
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        driver.execute_script("arguments[0].scrollIntoView();", scroll)
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

        print("TEST PASSED. Able to view External Audit Report")
    except Exception as e:
        print("TEST FAILED. Unable to view External Audit Report", e)


# TC External 15 --> Edit External Audit Report
def TC_ExternalAudit15():
    print("\nTesting TC_ExternalAudit_15: Edit External Audit Report")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        time.sleep(1.5)
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[2]/i').click()  # xpath for Edit button
        time.sleep(1.5)
        # edit For Company field
        ForCompany_list = driver.find_element_by_xpath('//*[@id="BrandOwner_Id"]')
        dropdownCompany = Select(ForCompany_list)
        dropdownCompany.select_by_index('5')  # Change from Ayamas to KARA
        time.sleep(1.5)
        # edit Received From field
        ReceivedFrom_list = driver.find_element_by_xpath('//*[@id="CertificationBodies_Id"]')
        dropdownReceive = Select(ReceivedFrom_list)
        dropdownReceive.select_by_index('2')  # change from ARA to Agency for Halal Quality Certification

        # edit CB Audit Reference No field #PASSED
        driver.find_element_by_xpath('//*[@id="NCR_AuditReportNo"]').clear()
        CB_ReferenceNo_box = driver.find_element_by_xpath('//*[@id="NCR_AuditReportNo"]')
        CB_ReferenceNo = "AFHQC-20211018/10"  # this CB_no. is randomly filled?
        # Put/Parse details of CB Audit Reference No
        CB_ReferenceNo_box.send_keys(CB_ReferenceNo)

        # edit Type of Application field #PASSED
        TypeofApplication_list = driver.find_element_by_xpath('// *[ @ id = "ExtTypeApplication_Id"]')
        dropdownTypeofApplication = Select(TypeofApplication_list)
        dropdownTypeofApplication.select_by_index('4')  # change from Additional to Post Audit

        # edit Type of Inspection field #PASSED
        TypeofInspection_list = driver.find_element_by_xpath('//*[@id="ExtTypeInspection_Id"]')
        dropdownTypeofInspection = Select(TypeofInspection_list)
        dropdownTypeofInspection.select_by_index(
            '9')  # 1.AUDIT  2. REAUDIT  3. ADHOC/WILDCARD 4. NEW SUPPLIER ... 9. ROUTINE
        # change from ADHOC/WILDCARD to ROUTINE

        # edit Application Scheme field #PASSED
        ApplicationScheme_list = driver.find_element_by_xpath('//*[@id="Scheme_Id"]')
        dropdownApplication_Scheme = Select(ApplicationScheme_list)
        dropdownApplication_Scheme.select_by_index(
            '1')  # 1. Food Products / Beverages / Supplements (PR) 2. Food Premise (PM)
        # change from PR to PM

        # edit CB Halal Application No field
        CBHalalApplication_list = driver.find_element_by_xpath('//*[@id="ExtCBRefApplicationNo_Id"]')
        dropdownCBHalalApplication = Select(CBHalalApplication_list)
        dropdownCBHalalApplication.select_by_index('2')  # 1. HALAL-20160418-081147(PR) 2. HALAL-20160418-081147(PR)
        # 3. HALAL-20160418-081147(PR) 4. HALAL-20161012-082921(PR) 5. HALAL-20170216-092959(BG) 6.
        # HALAL-20180309-161440(PR) 7. HALAL-20181130-093024(KO) 8. HALAL-20190508-074731(PM) ... last.
        # HALAL-CERT-2022-05-237462

        # edit Certification No. field #PASSED
        driver.find_element_by_xpath('//*[@id="NCR_CertificationNo"]').clear()
        CertificationNo_box = driver.find_element_by_xpath('//*[@id="NCR_CertificationNo"]')
        CertificationNo = "Testing 000"
        # Put/Parse details of CertificationNo
        CertificationNo_box.send_keys(CertificationNo)

        # edit Audit Date field #PASSED
        AuditDate_box = driver.find_element_by_xpath('//*[@id="DateReceived"]')
        AuditDate = "01/01/2000"
        # Put/Parse details of Audit Date
        AuditDate_box.send_keys(AuditDate)

        # edit Time In field #PASSED
        TimeIn_box = driver.find_element_by_xpath('//*[@id="TimeIn"]')
        TimeIn = "3:00PM"
        # Put/Parse details of Time In
        TimeIn_box.send_keys(TimeIn)

        # edit Time Out field #PASSED
        TimeOut_box = driver.find_element_by_xpath('//*[@id="TimeOut"]')
        TimeOut = "12:00PM"
        # Put/Parse details of Time Out
        TimeOut_box.send_keys(TimeOut)

        # edit Remarks field #PASSED
        driver.find_element_by_xpath('//*[@id="SummaryFindings"]').clear()
        Remarks_box = driver.find_element_by_xpath('//*[@id="SummaryFindings"]')
        Remarks = "Testing 2/11/2021"
        # Put/Parse details of Remarks
        Remarks_box.send_keys(Remarks)

        # edit Overall Status field #PASSED
        OverallStatus_list = driver.find_element_by_xpath('//*[@id="NCRStatus_Id"]')
        dropdownOverallStatus = Select(OverallStatus_list)
        dropdownOverallStatus.select_by_index('2')  # 1. Opened 2. Closed

        # click Save button
        driver.find_element_by_xpath('//*[@id="btnSaveNCRExternalCB"]').click()

        print("TEST PASSED. Able to edit External Audit Report")

    except Exception as e:
        print("TEST FAILED. Unable to edit External Audit Report ", e)


# TC External 16 --> Delete External Audit Report
# //*[@id="ExternalNCRCB"]/tbody/tr[1]/td[1]/a[3]
def TC_ExternalAudit16():
    print("\nTesting TC_ExternalAudit_16: Delete External Audit Report")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/CBExternal/Index')  # put URL of External page
    try:
        time.sleep(1.5)
        deleteButton = driver.find_element_by_xpath('// *[ @ id = "ExternalNCRCB"] / tbody / tr[1] / td[1] / a[3]')
        # delete External Audit = AFHQC-20211020/3
        deleteButton.click()
        driver.implicitly_wait(10)  # seconds
        alert = Alert(driver)
        alert.accept()
        # driver.implicitly_wait(2)  # seconds
        # driver.refresh()
        # driver.find_element_by_xpath('/ html / body / div[3] / div / div[3] / button[1]')
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[3]/button[1]').click()
        print("TEST PASSED. Able to delete External Audit Report")

    except Exception as e:
        print("TEST FAILED. Unable to delete External Audit Report ", e)


# TC External Audit 17--> Reply Non Conformance List
# Key : / means can edit  X means cannot edit,can view only
# Using Restaurant / Premise Manager credentials: kfcm0898@qsrbrands.com.my /
def TC_ExternalAudit_17():
    print("\nTesting TC External Audit 17. Reply Non Conformance List ")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/')  # Login as Restaurant/ Premise Manager
    try:
        username_box = driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = driver.find_element_by_xpath('//*[@id="Input_Password"]')
        username = "kfcm0898@qsrbrands.com.my"
        password = "p@ssw0rd1234"
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(1.5)
        driver.get(
            'https://vhsmartqsrtest.azurewebsites.net/NonConformance/Index')  # 1. Go to (Audit -> Non Conformance List)
        # 2. Select Non Conformance List [Any]
        driver.implicitly_wait(1.5)
        driver.find_element_by_xpath('//*[@id="DTListNCR"]/tbody[1]/tr[1]/td[1]/a[2]').click()
        print("Able to click Non Conformance List Edit button")
        # fill in Corrective Action Details field
        CorrectiveAction_box = driver.find_element_by_xpath('//*[@id="SetRecommendation"]')
        driver.implicitly_wait(1.5)
        # 4. Fill in Corrective Action ,5. Fill in Date Informed ,6. Fill in Date Completed
        CorrectiveAction_details = "Date Informed: 22/10/2021 \nDate Completed: 30/10/2021 "
        # Put/Parse details of CB Audit Reference No
        CorrectiveAction_box.send_keys(CorrectiveAction_details)
        print("Able to fill in Corrective Details fields")
        # Add attachment file
        driver.implicitly_wait(1.5)
        driver.find_element_by_xpath('//*[@id="file"]').send_keys("C://Users/USER/Downloads/Testing 2.1MB.pdf")
        print("Able to upload file ")
        # //*[@id="ManageProduct_FileAttach"]
        # click Save button
        driver.find_element_by_id('//*[@id="ManageProduct_FileAttach"]').click()
        print("Able to click save button")
        print("TEST PASSED. Able tO Reply Non Conformance List ")

    except Exception as e:
        print("TEST FAILED. Unable to Reply Non Conformance List", e)


# Syariah Compliance Department credentials:
# 1. Syariah Compliance Department(Full Access) : ahmad.yusof@qsrbrands.com.my / , hazim_Gerard@gmail.com /
# 2. Syariah Compliance Department (View, Create and Update Only) : kahyin@gmail.com / , ismail.sulaiman@qsrbrands.com.my /
# 3. Syariah Compliance Department (View Only) : kayleen@kcompany.com X , mohdakram.bakar@qsrbrands.com.my X
# Auditor / Halal Executive (Downstream) credentials:
# 1. naseefah.adhikarie@serunai.com /
# 2. masrie.shafiei@qsrbrands.com.my /
# KFC1130736/03-10-2022

# TC External Audit 18--> Edit Non Conformance List
def TC_ExternalAudit_18():
    print("\nTesting TC External Audit 18, Edit Non Conformance List")
    driver.get('https://vhsmartqsrtest.azurewebsites.net/')
    try:
        username_box = driver.find_element_by_xpath('//*[@id="Input_Email"]')
        password_box = driver.find_element_by_xpath('//*[@id="Input_Password"]')
        username = "kfcm0898@qsrbrands.com.my"
        password = "p@ssw0rd1234"
        username_box.send_keys(username)
        password_box.send_keys(password)
        password_box.send_keys(Keys.ENTER)
        time.sleep(1.5)
        driver.get(
            'https://vhsmartqsrtest.azurewebsites.net/NonConformance/Index')  # 1. Go to (Audit -> Non Conformance List)
        # 2. Click Edit Non Conformance List [Any]
        driver.implicitly_wait(1.5)
        driver.find_element_by_xpath('//*[@id="DTListNCR"]/tbody[1]/tr/td[1]/a[2]').click()
        # fill in Corrective Action Details field
        CorrectiveAction_box = driver.find_element_by_xpath('//*[@id="SetRecommendation"]')
        driver.implicitly_wait(1.5)
        # 4. Fill in Corrective Action ,5. Fill in Date Informed ,6. Fill in Date Completed
        CorrectiveAction_details = "Date Informed: 3/10/2021 \nDate Completed: 1/11/2021 "
        # Put/Parse details of CB Audit Reference No
        CorrectiveAction_box.send_keys(CorrectiveAction_details)
        print("Able to fill in Corrective Details fields")
        # Add attachment file
        driver.implicitly_wait(1.5)
        driver.find_element_by_xpath('//*[@id="file"]').send_keys("C://Users/USER/Downloads/testingfile3.05mb.pdf")
        print("Able to upload file ")
        # //*[@id="ManageProduct_FileAttach"]
        # click Save button
        driver.find_element_by_xpath('//*[@id="ManageProduct_FileAttach"]').click()
        print("Able to click save button")
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[3]/button[1]').click()
        driver.find_element_by_class_name('swal2-confirm swal2-styled').click()
        alert = driver.switch_to.alert
        print(alert.text)
        alert.accept()
        print("Able to click OK button")
        print("TEST PASSED. Able to Edit Non Conformance List ")

    except Exception as e:
        print("TEST FAILED. Unable to edit Non Conformance List", e)


# TC External Audit 19--> Close Non Conformance List


openChrome()
login()

