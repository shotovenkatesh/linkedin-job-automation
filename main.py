import time
import os
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
from selenium import webdriver

chrome_driver_file_path = "/Users/venkatesh/PycharmProjects/DEVELOPMENT/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_file_path)


EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
CONTACT_NO = ""

url = "https://www.linkedin.com/jobs/search/?f_AL=true&geoId=102713980&keywords=python%20developer%20intern"
driver.get(url)

# ///////////////////////////////////Clicks the sign in button////////////////////////////////////////////////////////
initial_sign_in_button = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
initial_sign_in_button.click()

# ///////////////////////////////////Type out the login credentials////////////////////////////////////////////////////////
email_entry = driver.find_element_by_name("session_key")
password_entry = driver.find_element_by_name("session_password")
login_sign_in_button = driver.find_element_by_css_selector(".login__form_action_container button")
email_entry.send_keys(EMAIL)
password_entry.send_keys(PASSWORD)
login_sign_in_button.click()



# ///////////////////////////////////Applying for job////////////////////////////////////////////////////////
all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(CONTACT_NO)

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()






# easy_apply_button = driver.find_element_by_css_selector(".mt5 .jobs-apply-button--top-card button")
# easy_apply_button.click()
#
# phone_number_text = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2661231103,9,phoneNumber~nationalNumber)")
# phone_number_text.send_keys(NO)
#
# submit_button = driver.find_element_by_css_selector("footer button")
# submit_button.click()

# phone_number = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907643,phoneNumber~nationalNumber)")
# phone_number.send_keys(NO)
# next_button = driver.find_element_by_id("ember351")
# next_button.click()
#
# next_button.click()
#
# #///////////////////////////////Additional Questins//////////////////////////////////////
# exp = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907683,numeric)")
# exp2 = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907675,numeric)")
# exp3 = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907659,numeric)")
# exp4 = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907667,numeric)")
# exp5 = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2675486988,31907651,numeric)")
#
# exp.send_keys("1")
# exp2.send_keys("1")
# exp3.send_keys("0")
# exp4.send_keys("1")
# exp5.send_keys("1")
#
# review_button = driver.find_element_by_id("ember359")
# review_button.click()
# submit_button = driver.find_element_by_id("ember369")
# submit_button.click()
