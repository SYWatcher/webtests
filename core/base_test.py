import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    driver = webdriver.Remote(command_executor="http://217.114.15.199:4444",options=options)
    yield driver
    driver.quit()

@pytest.fixture
def mail_login():
    faker = Faker()
    login = faker.email()
    return login
