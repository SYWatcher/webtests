import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(1920,1080)
    yield driver
    driver.quit()

@pytest.fixture
def mail_login():
    faker = Faker()
    login = faker.email()
    return login
