from core.base_test import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.VkEcosystemPage import VkEcosystemPageHelper
import allure

BASE_URL = 'https://ok.ru'

@allure.suite("Проверка тулбара")
@allure.title("Переход к проверкам экосистемы ВК")
def test_open_vk_ecosystem(browser):
    BasePage = BasePageHelper(browser)
    BasePage.get_url(BASE_URL)
    BasePage.check_page()
    LoginPage = BasePageHelper(browser)
    LoginPage.click_vk_ecosystem()
    current_window_id = LoginPage.get_window_id(0)
    LoginPage.click_more_button()
    new_window_id = LoginPage.get_window_id(1)
    LoginPage.change_window(new_window_id)
    VkEcosystemPage = VkEcosystemPageHelper(browser)
    VkEcosystemPage.change_window(current_window_id)
    LoginPageHelper(browser)