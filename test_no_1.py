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
    driver.get("https://www.automationexercise.com/login")
    time.sleep(5)
    yield
    driver.quit()

#Login User with correct email and password. Log out
@pytest.mark.usefixtures('test_setup')
def test_method():
    driver.find_element(By.XPATH, elements.INPUT_EMAIL_ADDRESS).send_keys(keys.FIRST_USER_EMAIL)
    time.sleep(2)
    driver.find_element(By.XPATH, elements.INPUT_PASSWORD).send_keys(keys.FIRST_USER_PASSWORD)
    time.sleep(2)
    driver.find_element(By.XPATH, elements.LOGIN_BUTTON).click()
    user=(driver.find_element(By.XPATH,elements.LOGGED_USER).text)
    assert user == "Test_automation_user1"
    driver.find_element(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
    login_page_indicatior=(driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div/h2').text)
    print(login_page_indicatior)
    assert login_page_indicatior == 'Login to your account'
    



