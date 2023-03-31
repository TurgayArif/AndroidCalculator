from appium import webdriver
from utilities.test_data import TestData
from core import desired_capabilities
import pytest


@pytest.fixture()
def initialize_driver(request):
    driver = webdriver.Remote(TestData.url, desired_capabilities.caps)
    request.cls.driver = driver
    yield
    driver.quit()
