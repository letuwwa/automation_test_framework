from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, driver: Chrome | Firefox) -> None:
        self.driver = driver
        self._driver_wait = WebDriverWait(driver=driver, timeout=5)

    def click_on(self, locator: tuple) -> None:
        self._find_element(locator=locator).click()

    def _find_element(self, locator: tuple) -> WebElement:
        return self._driver_wait.until(
            expected_conditions.presence_of_element_located(locator=locator)
        )
