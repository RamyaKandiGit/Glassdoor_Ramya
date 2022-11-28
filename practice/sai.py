import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path= r'C:\Users\kandi\Downloads\chromedriver_win32\chromedriver.exe'
driver=webdriver.Chrome(path)
driver.get("https://www.glassdoor.co.in/profile/login_input.htm")
driver.implicitly_wait(50)
driver.maximize_window()
driver.find_element_by_xpath("//input[@id='inlineUserEmail']").send_keys("sainaik8639@gmail.com")
driver.find_element_by_xpath("//span[@class='css-2etp8b evpplnh1']").click()
obj1 = driver.find_element_by_xpath("//label[@class='css-w3qhip eb2o9h0']")
obj = ActionChains(driver)
obj.click(obj1)
obj.send_keys("9866875783").perform()
driver.find_element_by_xpath("//span[text()='Sign In']").click()
time.sleep(5)
company=driver.find_element("xpath",'(//div[@class="d-flex flex-column align-items-center justify-content-center flex-lg-row justify-content-lg-start"])[3]')
obj = ActionChains(driver)
obj.move_to_element(company).perform()
driver.find_element("xpath","(//span[text()='Write a Review'])[2]").click()
driver.find_element("xpath","//div[text()='Company Review']").click()
driver.find_element("xpath",'//div[text()="Current Employee"]').click()
driver.find_element("xpath",'//input[@name="survey-AddCompany-component"]').send_keys("Capgemini")
time.sleep(3)
driver.find_element("xpath","//span[text()='Capgemini']").click()
time.sleep(3)
driver.find_element("xpath",'//button[@class="gd-ui-button css-s89dmq evpplnh0"]').click()
star=driver.find_element("xpath",'(//span[@class="gd-ui-star  css-15840pv e7cj4650"])[5]').click()
driver.find_element("xpath",'//div[@class="css-47sx24 egu3u860"]').click()
driver.find_element("xpath","//span[text()='Full-time']").click()
driver.find_element("xpath",'//input[@name="survey-company-component"]').send_keys("Analyst")
time.sleep(5)
driver.find_element("xpath","(//span[text()='Analyst'])[1]").click()
time.sleep(3)
driver.find_element("xpath",'//input[@id="ReviewHeadline"]').send_keys("General feeling of work happiness")
driver.find_element("xpath",'//textarea[@id="ProsTextField"]').send_keys("Feel free to growOver the course of your career, your goals may shift. Want to change your focus? Switch tracks? We’re here to help.")
driver.find_element("xpath",'//textarea[@id="ConsTextField"]').send_keys("No downsides of working at Capgemini company")
driver.find_element("xpath",'//div[@class="checkboxBox"]').click()
# driver.find_element("xpath","//span[text()='Submit Review']").click()
driver.close()