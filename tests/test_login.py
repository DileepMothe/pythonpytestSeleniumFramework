import pytest

from PageObjects.loginPage import LoginPage



def test_dologintoApplication(browser_setup):
    driver = browser_setup
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_Page = LoginPage(driver)
    login_Page.doLogin()
    title_value = login_Page.getTitle()
    assert "OrangeHRM" in title_value


