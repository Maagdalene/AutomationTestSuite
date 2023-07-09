import time
import elements
import keys
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@pytest.fixture()
def test_setup():
    global driver
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.automationexercise.com/login"
               "")
    time.sleep(20)
    yield
    driver.quit()

@pytest.mark.usefixtures('test_setup')
def test_method():
    driver.find_element(By.XPATH, elements.INPUT_EMAIL_ADDRESS).send_keys(keys.FIRST_USER_EMAIL)
    time.sleep(2)
    driver.find_element(By.XPATH, elements.INPUT_PASSWORD).send_keys(keys.FIRST_USER_PASSWORD)
    time.sleep(2)
    driver.find_element(By.XPATH, elements.LOGIN_BUTTON).click()
    user=(driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a/b').text)
    assert user == "Test_automation_user1"


#def test_method(test_setup):
   # assert user == "Test_automation_user1"
    #assert logged_user == 'Logged in as Test_automation_user1'

#def execute_test(test_setup):
    #login(test_setup)

#execute_test(test_setup)

# test_setup()



#Test_automation_user1@outlook.com