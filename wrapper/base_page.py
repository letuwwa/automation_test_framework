from wrapper.base_element import BaseElement
from selenium.webdriver import Chrome, Firefox


class BasePage:
    def __init__(self, driver: Chrome | Firefox) -> None:
        self.driver = driver
        self._element = BaseElement(driver=self.driver)

    def reload(self) -> None:
        self.driver.refresh()

    def stop_driver(self) -> None:
        self.driver.quit()

    def close_current_window(self) -> None:
        self.driver.close()

    def open(self, url: str) -> None:
        self.driver.get(url=url)

    def get_current_title(self) -> str:
        return str(self.driver.title)

    def get_current_url(self) -> str:
        return str(self.driver.current_url)
