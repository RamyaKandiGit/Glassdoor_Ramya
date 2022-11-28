import time

from Data import reading_object
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# from test_.conftest import _driver

login_objects = reading_object.read_locators()

class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    def mail_username(self,data_):
        self.driver.find_element(*login_objects['mail_username']).send_keys(data_[0])
        time.sleep(1)

    def submit(self):
        self.driver.find_element(*login_objects['submit']).click()
        time.sleep(1)

    def mail_pwd(self,data_):
        self.driver.find_element(*login_objects['mail_pwd']).send_keys(data_[1])
        time.sleep(1)

    def pwd_submit(self):
        self.driver.find_element(*login_objects['pwd_submit']).click()
        time.sleep(5)

    def salary(self):
        self.driver.find_element(*login_objects['salary']).click()

    def jobtitle(self,data_):
        self.driver.find_element(*login_objects['jobtitle']).send_keys(data_[2])
        time.sleep(1)

    def search_button(self):
        self.driver.find_element(*login_objects['search_button']).click()
        time.sleep(1)

    def addreview(self):
        self.driver.find_element(*login_objects['addreview']).click()
        time.sleep(1)

    def review_radiobutton(self):
        self.driver.find_element(*login_objects['review_radiobutton']).click()

    def explore_name(self,data_):
        self.driver.find_element(*login_objects['explore_name']).send_keys(data_[3])
        time.sleep(2)

    def select_company(self):
        self.driver.find_element(*login_objects['select_company']).click()

    def next_button(self):
        self.driver.find_element(*login_objects['next_button']).click()
        time.sleep(1)

    def rate_overall(self):
        self.driver.find_element(*login_objects['rate_overall']).click()

    def job_title(self,data_):
        self.driver.find_element(*login_objects['job_title']).send_keys(data_[4])
        time.sleep(2)

    def description(self,data_):
        self.driver.find_element(*login_objects['description']).send_keys(data_[5])
        time.sleep(2)

    def interview_difficult(self):
        self.driver.find_element(*login_objects['interview_difficult']).click()

    def easy_button(self):
        self.driver.find_element(*login_objects['easy_button']).click()

    def offer(self):
        self.driver.find_element(*login_objects['offer']).click()

    def yes_button(self):
        self.driver.find_element(*login_objects['yes_button']).click()

    def question(self,data_):
        self.driver.find_element(*login_objects['question']).send_keys(data_[6])
        time.sleep(1)

    def answer(self,data_):
        self.driver.find_element(*login_objects['answer']).send_keys(data_[7])













    # def offer(self):
    #     self.driver.find_element(*login_objects['offer'])
    #
    # def accepted(self):
    #     self.driver.find_element(*login_objects['accepted']).click()
    #     time.sleep(1)
    #
    # def interview_ques(self,value7):
    #     self.value7 = value7
    #     self.driver.find_element(*login_objects['interview_ques']).send_keys(self.value6)
    #     time.sleep(1)
    #
    # def answer(self,value8):
    #     self.value8 = value8
    #     self.driver.find_element(*login_objects['answer']).send_keys(self.value6)
    #     time.sleep(1)

# lp = LoginPage(_driver)
# lp.mail_username("kandiramya844@gmail.com")
# lp.submit()
# lp.mail_pwd("Ramya@123")
# lp.pwd_submit()
# lp.salary()
# lp.jobtitle("Data Analyst")
# lp.search_button()
# lp.addreview()
# lp.review_radiobutton()
# lp.explore_name("Capgemini")
#
# lp.select_company()
# lp.next_button()
# lp.rate_overall()
# lp.job_title("Data Analyst")
# lp.description("Interview is really good and friendly, They asked very depth in subject and it is perfect for fresher")
# lp.interview_difficult()
# lp.easy_button()
# lp.offer()
# lp.yes_button()
# lp.question("Are you Intrested in IT")
# lp.answer("Yes, I am")






