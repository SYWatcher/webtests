from core.base_test import browser
from pages.BasePage import BasePageHelper
from pages.HelpPage import HelpPageHelper, HelpPageLocators
from pages.AdvertisementCabinet import AdvertisementCabinetHelper , AdvertisementCabinetLocators
import allure

BASE_URL = 'https://ok.ru/help'

@allure.suite("Проверка скролла на странице помощи")
@allure.title("Проверка открытия страницы 'Рекламный кабинет' после скролла")
def test_help_test(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    HelpPage = HelpPageHelper(browser)
    HelpPage.scrollToitem(HelpPageLocators.ADVERTISEMENT_CABINET)
    AdvertisementCabinetHelper(browser)
