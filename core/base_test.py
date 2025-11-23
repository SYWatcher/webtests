import pytest
from selenium import webdriver
from faker import Faker


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def mail_login():
    faker = Faker()
    login = faker.email()
    return login
