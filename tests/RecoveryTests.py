from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from core.base_test import browser, mail_login
from pages.BasePage import BasePage
from pages.LoginPage import LoginPageHelper, LoginPageLocators
from pages.RecoveryPage import RecoveryPageHelper, RecoveryPageLocators
import allure

BASE_URL = 'https://ok.ru'
PASSWORD_TEXT = '1'

@allure.suite("Проверка восстановления пользователя")
@allure.title("Проверка перехода и восстановления после нескольких неудачных попыток авторизации")
def test_go_to_recovery_after_many_fails(browser,mail_login):
    BasePage(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.send_login(mail_login)
    for i in  range(3):
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.PASSWORD_FIELD))
        LoginPage.send_password(PASSWORD_TEXT)
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        LoginPage.click_login()
    WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.PROFILE_RECOVERY_BUTTON))
    LoginPage.click_recovery()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(RecoveryPageLocators.PHONE_BUTTON))
    RecoveryPageHelper(browser)


