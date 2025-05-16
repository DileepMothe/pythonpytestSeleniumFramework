

def test_gotoGooglePage(browser_setup):
    driver = browser_setup
    driver.get("https://www.google.com/")
    assert "Google" in driver.title