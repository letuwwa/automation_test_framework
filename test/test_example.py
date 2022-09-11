from time import sleep
from selenium.webdriver.common.by import By
from wrapper.base_element import BaseElement


def test_base() -> None:
    assert True


def test_selenium_fixture(selenium) -> None:
    selenium.get("https://ubuntu.com/")
    print(f"Title: {selenium.title}")
    selenium.quit()


def test_base_element_click(selenium) -> None:
    driver = BaseElement(driver=selenium)
    driver.driver.get(url="https://www.python.org/")
    about_locator = (By.XPATH, "//*[@id='about']/a")
    driver.click_on(locator=about_locator)
    sleep(3)
    print(f"Title: {driver.driver.title}")
    selenium.quit()
