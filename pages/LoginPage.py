from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class LoginPageLocators:
    LOGIN_FIELD = (By.ID,'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//*[@data-l="t,sign_in"]')
    QR_BUTTON = (By.XPATH, '//*[@data-l="t,get_qr"]')
    RESTORE_BUTTON = (By.XPATH, '//*[@data-l="t,restore"]')
    VK_BUTTON = (By.XPATH,'//*[@data-l="t,vkc"]')
    MAILRU_BUTTON = (By.XPATH, '//*[@data-l="t,mailru"]')
    YANDEX_BUTTON = (By.XPATH, '//*[@data-l="t,yandex"]')
    LOGIN_TAB = (By.XPATH, '//*[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//*[@data-l="t,qr_tab"]')

class LoginPageHelper(BasePage):
    pass