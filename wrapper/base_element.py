from selenium.webdriver import Chrome, Firefox


class BaseElement:
    def __init__(self, driver: Chrome | Firefox):
        self.driver = driver

    def click_on(self):
        pass

    def move_on(self):
        pass

    def write_text(self):
        pass
