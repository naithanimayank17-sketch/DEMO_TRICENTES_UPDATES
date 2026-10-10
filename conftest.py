import pytest
from selenium import webdriver

# @pytest.fixture(autouse=True)          
# def setup_and_teardown():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://demowebshop.tricentis.com/')
#     yield driver
#     driver.close()



##Cross Browser Testing

# @pytest.fixture(params=['chrome','edge','firefox'])
@pytest.fixture(params=['chrome'])          
def setup_and_teardown(request):
    browser = request.param     #gets
    if browser == 'chrome':
        driver = webdriver.Chrome()

    else:
        pass

    # elif browser == 'edge':
    #     driver = webdriver.Edge()

    # elif browser == 'firefox':
    #         driver = webdriver.Firefox()

    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.close()