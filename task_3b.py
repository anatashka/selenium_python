import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    url = "http://localhost/litecart/admin/"
    driver.get(url)
    email_element = driver.find_element_by_name("username")
    email_element.send_keys("admin")
    pass_element = driver.find_element_by_name("password")
    pass_element.send_keys('admin')
    log_in_btn = driver.find_element_by_name("login")
    log_in_btn.click()
    WebDriverWait(driver, 90)