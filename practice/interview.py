import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
path=r'C:\Users\kandi\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("https://www.glassdoor.co.in/member/home/index.htm")
driver.implicitly_wait(30)
driver.maximize_window()
driver.find_element("xpath","//input[@title='Enter Email']").send_keys("kandiramya844@gmail.com")
time.sleep(2)

#continue button
driver.find_element("name","submit").click()
time.sleep(2)


#password
driver.find_element("id","inlineUserPassword").send_keys("Ramya@123")
time.sleep(2)

#submit button
driver.find_element("xpath",'//button[@type="submit"]').click()
time.sleep(2)

#salary
driver.find_element("xpath","(//span[@class='css-2etp8b evpplnh1'])[6]").click()
time.sleep(2)

#job title
driver.find_element("xpath","//input[@id='KeywordSearch']").send_keys("Data analyst")
time.sleep(2)

#search button
driver.find_element("xpath","//button[@type='submit']").click()
time.sleep(2)

#add review button
driver.find_element("xpath","//span[text()='Add Review or Salary']").click()
time.sleep(2)

#radio button
driver.find_element("xpath","(//div[@class='radioButtonBox'])[3]").click()
time.sleep(2)

#explores name
driver.find_element("xpath","//input[@class='css-eyudwk e1h5k8h92']").send_keys("Capgemini")
time.sleep(2)

# #select name
driver.find_element("xpath","//span[text()='Capgemini']").click()
time.sleep(2)



#next button
driver.find_element("xpath","//span[@class='css-2etp8b evpplnh1']").click()
time.sleep(2)
#rate_overall
driver.find_element("xpath","//span[@class='SVGInline css-jzoj2g e50qfp90']").click()
time.sleep(2)


#job_title
driver.find_element("xpath","(//input[@class='css-eyudwk e1h5k8h92'])[2]").send_keys("Data Analyst")
time.sleep(2)

#description
driver.find_element("xpath","//textarea[@class='css-eyudwk e1h5k8h92']").send_keys("Thank you for the valuable time, Interview is really good and friendly, They asked very depth in subject and absolutely it is perfect for fresher to their start career. The way you asked the questions that shows dedication and determinations towards work, Something I really appreciate about that")
time.sleep(2)

#difficulty_select
# driver.find_element("xpath","//div[@class='selectedLabel']").click()
# time.sleep(2)
#
# #selectCompany
# driver.find_element("xpath","//span[text()='Very Easy']").click()
# time.sleep(2)

#Trial
# interview_difficult
driver.find_element("xpath","//div[@class='selectedLabel']").click()
time.sleep(1)

#easy_button
driver.find_element("xpath","(//span[@class='dropdownOptionLabel'])[2]").click()
time.sleep(1)



# offer
driver.find_element("xpath","(//div[@class='selectedLabel'])[2]").click()
time.sleep(2)

#yes_button
driver.find_element("xpath","(//li[@id='option_3'])[2]").click()
time.sleep(2)

#question
driver.find_element("xpath","(//textarea[@class='css-eyudwk e1h5k8h92'])[2]").send_keys("Are you interested in IT")
time.sleep(5)

# answer
driver.find_element("xpath","(//textarea[@class='css-eyudwk e1h5k8h92'])[3]").send_keys("Yes, I am")
time.sleep(2)



# #Trial
# driver.find_element("xpath","//span[@class='SVGInline arrowUp']").click()
# time.sleep(1)
# driver.find_element("xpath","(//span[@class='dropdownOptionLabel'])[2]").click()
# time.sleep(1)

