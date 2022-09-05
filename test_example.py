def test_base() -> None:
    assert True


def test_base_driver() -> None:
    from selenium import webdriver
    browser = webdriver.Chrome(executable_path="./drivers/chromedriver")
    browser.get('https://www.linuxhint.com')
    print('Title: %s' % browser.title)
    browser.quit()
