from behave import *
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given(u'Open the browser and enter valid URL and click on continue with email')
def step_impl(context):
    path = r'C:\Users\kandi\Downloads\chromedriver_win32\chromedriver.exe'
    context.driver = webdriver.Chrome(path)
    context.driver.get("https://www.glassdoor.co.in/member/home/index.htm")
    context.driver.implicitly_wait(30)
    context.driver.maximize_window()
    context.driver.find_element("xpath", "//input[@title='Enter Email']").send_keys("kandiramya844@gmail.com")
    time.sleep(2)
    context.driver.find_element("name", "submit").click()
    time.sleep(2)


@given(u'Enter the password and click on signin')
def step_impl(context):
    context.driver.find_element("id", "inlineUserPassword").send_keys("Ramya@123")
    time.sleep(2)
    context.driver.find_element("xpath", '//button[@type="submit"]').click()
    time.sleep(2)


@then(u'click on salaries')
def step_impl(context):
    context.driver.find_element("xpath", "(//span[@class='css-2etp8b evpplnh1'])[6]").click()
    time.sleep(2)


@then(u'Enter jobtitle')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@id='KeywordSearch']").send_keys("Data analyst")
    time.sleep(2)


@then(u'Click on search button1')
def step_impl(context):
    context.driver.find_element("xpath", "//button[@type='submit']").click()
    time.sleep(2)


@then(u'click on Addreview button')
def step_impl(context):
    context.driver.find_element("xpath", "//span[text()='Add Review or Salary']").click()
    time.sleep(2)


@then(u'click on radio button')
def step_impl(context):
    context.driver.find_element("xpath", "(//div[@class='radioButtonBox'])[3]").click()
    time.sleep(2)



@then(u'Click on interview and Enter Company\'s name')
def step_impl(context):
    context.driver.find_element("xpath", "//input[@class='css-eyudwk e1h5k8h92']").send_keys("Capgemini")
    time.sleep(2)
    context.driver.find_element("xpath", "//span[text()='Capgemini']").click()
    time.sleep(2)


@then(u'Click on next')
def step_impl(context):
    context.driver.find_element("xpath", "//span[@class='css-2etp8b evpplnh1']").click()
    time.sleep(2)


@then(u'Click on Rate overall expereince')
def step_impl(context):
    context.driver.find_element("xpath", "//span[@class='SVGInline css-jzoj2g e50qfp90']").click()
    time.sleep(2)


@then(u'Click on the jobtitle and enter the jobtitle')
def step_impl(context):
    context.driver.find_element("xpath", "(//input[@class='css-eyudwk e1h5k8h92'])[2]").send_keys("Data Analyst")
    time.sleep(2)


@then(u'click on the describe interview process and enter the description')
def step_impl(context):
    context.driver.find_element("xpath", "//textarea[@class='css-eyudwk e1h5k8h92']").send_keys(
        "Thank you for the valuable time, Interview is really good and friendly, They asked very depth in subject and absolutely it is perfect for fresher to their start career. The way you asked the questions that shows dedication and determinations towards work, Something I really appreciate about that")
    time.sleep(2)


@then(u'click on the interview difficulty and select the option')
def step_impl(context):
    context.driver.find_element("xpath", "//div[@class='selectedLabel']").click()
    time.sleep(1)
    context.driver.find_element("xpath", "(//span[@class='dropdownOptionLabel'])[2]").click()
    time.sleep(1)


@then(u'click on Did you get an offer and select the option')
def step_impl(context):
    context.driver.find_element("xpath", "(//div[@class='selectedLabel'])[2]").click()
    time.sleep(2)
    context.driver.find_element("xpath", "(//li[@id='option_3'])[2]").click()
    time.sleep(2)


@then(u'click on the interview questions and enter the question')
def step_impl(context):
    context.driver.find_element("xpath", "(//textarea[@class='css-eyudwk e1h5k8h92'])[2]").send_keys("Are you interested in IT")
    time.sleep(5)


@then(u'click on answer this question and enter the answer')
def step_impl(context):
    context.driver.find_element("xpath", "(//textarea[@class='css-eyudwk e1h5k8h92'])[3]").send_keys("Yes, I am")
    time.sleep(2)


# @then(u'close the browser')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then close the browser')











# @given(u'Open the browser and enter valid URL and click on continue with email')
# def step_impl(context):
#     path = r'C:\Users\kandi\Downloads\chromedriver_win32\chromedriver.exe'
#     context.driver = webdriver.Chrome(path)
#     context.driver.get("https://www.glassdoor.co.in/member/home/index.htm")
#     context.driver.implicitly_wait(30)
#     context.driver.maximize_window()
#     context.driver.find_element("xpath", "//input[@title='Enter Email']").send_keys("kandiramya844@gmail.com")
#     time.sleep(2)
#     context.driver.find_element("name", "submit").click()
#     time.sleep(2)
#
#
# @given(u'Enter the password and click on signin')
# def step_impl(context):
#     context.driver.find_element("id", "inlineUserPassword").send_keys("Ramya@123")
#     time.sleep(2)
#     context.driver.find_element("xpath", '//button[@type="submit"]').click()
#     time.sleep(2)
#
#
# @then(u'click on salaries')
# def step_impl(context):
#     context.driver.find_element("xpath","(//span[@class='css-2etp8b evpplnh1'])[6]").click()
#     time.sleep(2)
#
#
#
# @then(u'Navigate back to page01')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Navigate back to page01')
#
#
# @then(u'Enter jobtitle')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Enter jobtitle')
#
#
# @then(u'Click on search button1')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on search button1')
#
#
# @then(u'Navigate back to page02')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Navigate back to page02')
#
#
# @then(u'click on Addreview button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then click on Addreview button')
#
#
# @then(u'Navigate to back page03')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Navigate to back page03')
#
#
# @then(u'Click on interview and Enter Company\'s name')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on interview and Enter Company\'s name')
#
#
# @then(u'Click on next')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on next')
#
#
# @then(u'Navigate to page04')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Navigate to page04')
#
#
# @then(u'Click on Rate overall expereince')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on Rate overall expereince')
#
#
# @then(u'Click on the jobtitle and enter the jobtitle')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Click on the jobtitle and enter the jobtitle')
#
#
# @then(u'click on the describe interview process and enter the description')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then click on the describe interview process and enter the description')
#
#
# @then(u'click on the interview difficulty and select the option')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then click on the interview difficulty and select the option')
# @then(u'click on answer this question and enter the answer')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then click on answer this question and enter the answer')
#
#
# @then(u'close the browser')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then close the browser')
