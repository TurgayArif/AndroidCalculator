from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def find(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))
        self.find(*locator).click()

    def get_text(self, locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.find(*locator).text
