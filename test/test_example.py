def test_base() -> None:
    assert True


def test_base_driver(selenium) -> None:
    selenium.get("https://www.linuxhint.com")
    print(f"Title: {selenium.title}")
    selenium.quit()
