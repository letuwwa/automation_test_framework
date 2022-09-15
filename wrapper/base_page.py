from selenium.webdriver import Chrome, Firefox

from wrapper.base_element import BaseElement


class BasePage:
    def __init__(self, driver: Chrome | Firefox):
        self.driver = driver
        self._element = BaseElement(driver=self.driver)

    def reload(self):
        pass

    def close(self):
        pass

    def open(self):
        pass
