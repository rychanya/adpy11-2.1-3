from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


URL = 'https://passport.yandex.ru/auth/'


def _get_field(driver, _id):
    try:
        field = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, _id)))
        return field
    except TimeoutException:
        return


def get_password_field(driver):
    return _get_field(driver, 'passp-field-passwd')


def get_login_field(driver):
    return _get_field(driver, 'passp-field-login')


def get_btn(driver):
    try:
        btns = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'passp-sign-in-button')))
        return btns.find_element_by_tag_name('button')
    except TimeoutException:
        return


def check(driver):
    try:
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, 'passp-form-field__error')))
        return False
    except TimeoutException:
        return True
