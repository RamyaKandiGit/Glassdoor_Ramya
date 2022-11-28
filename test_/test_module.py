
from POM.module import LoginPage
from Data import reading_object
import pytest

data_obj = reading_object.read_data()
@pytest.mark.parametrize("data_",data_obj)
class TestLogin:

    def test_login(self,_driver,data_):
        lp = LoginPage(_driver)
        lp.mail_username(data_)
        lp.submit()
        lp.mail_pwd(data_)
        lp.pwd_submit()
        lp.salary()
        lp.jobtitle(data_)
        lp.search_button()
        lp.addreview()
        lp.review_radiobutton()
        lp.explore_name(data_)
        lp.select_company()
        lp.next_button()
        lp.rate_overall()
        lp.job_title(data_)
        lp.description(data_)
        lp.interview_difficult()
        lp.easy_button()
        lp.offer()
        lp.yes_button()
        lp.question(data_)
        lp.answer(data_)
