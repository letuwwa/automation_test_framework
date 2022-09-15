from selenium.webdriver import Chrome, Firefox, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webelement import WebElement


class BaseElement:
    def __init__(self, driver: Chrome | Firefox) -> None:
        self.driver = driver
        self._driver_wait = WebDriverWait(driver=driver, timeout=5)

    def click_on(self, locator: tuple) -> None:
        self._find_element(locator=locator).click()

    def get_text_from(self, locator: tuple) -> str:
        return self._find_element(locator=locator).text

    def write_text_to(self, locator: tuple, text: str) -> None:
        self._find_element(locator=locator).send_keys(text)

    def move_cursor_to(self, locator: tuple) -> None:
        ActionChains(self.driver).move_to_element(
            to_element=self._find_element(locator=locator)
        ).perform()

    def _find_element(self, locator: tuple) -> WebElement:
        return self._driver_wait.until(
            expected_conditions.presence_of_element_located(locator=locator)
        )
