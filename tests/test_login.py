from pages.login import LoginPage
import pytest
from utilities.read_excel import get_login_data


@pytest.mark.parametrize("email,password",get_login_data()) 
def test_login1(setup_and_teardown,email,password):
    lp= LoginPage(setup_and_teardown)
    lp.click_login_link()
    lp.enter_email(email)
    lp.enter_password(password)
    lp.click_login_button()

# def test_login1(setup_and_teardown):
#     lp= LoginPage(setup_and_teardown)
#     lp.click_login_link()
#     lp.enter_email('naithanimayank17@gmail.com')
#     lp.enter_password('Mayank@123')
#     lp.click_login_button()


# def test_login2(setup_and_teardown):
#     lp= LoginPage(setup_and_teardown)
#     lp.click_login_link()
#     lp.enter_email('dasdsda@gmail.com')
#     lp.enter_password('Mayank@12dsaasdd3')
#     lp.click_login_button()