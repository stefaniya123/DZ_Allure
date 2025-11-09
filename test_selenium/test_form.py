import allure
import pytest

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture
def driver():
    # Selenium Manager will auto-download the appropriate driver
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
@allure.title("Авторизация с валидными данными")
@allure.description("Авторизация через логин и пароль")
def test_successful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    text_name=driver.find_element(By.NAME, value="username")
    text_password=driver.find_element(By.NAME, value="password")

    text_name.clear()
    text_password.clear()
    text_name.send_keys("tomsmith")
    text_password.send_keys("SuperSecretPassword!")
    submit_button=driver.find_element(By.CLASS_NAME, value="radius")
    submit_button.click()
    flash_message=driver.find_element(By.ID, value="flash")

    assert "You logged into a secure area!" in flash_message.text

@allure.title("Авторизация с невалидными данными")
@allure.description("Авторизация через логин и пароль")
def test_unsuccessful_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    text_name = driver.find_element(By.NAME, value="username")
    text_password = driver.find_element(By.NAME, value="password")

    text_name.clear()
    text_password.clear()
    text_name.send_keys("testtest")
    text_password.send_keys("Password!")
    submit_button = driver.find_element(By.CLASS_NAME, value="radius")
    submit_button.click()
    flash_message = driver.find_element(By.ID, value="flash")

    assert "Your username is invalid!" in flash_message.text


