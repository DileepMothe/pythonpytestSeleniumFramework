import pytest

import sys
import os
## When PageObjects folder not found use below
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PageObjects.loginPage import LoginPage


def test_dologintoApplication(browser_setup):
    driver = browser_setup
    driver.get("https://opensource-demo.orangehrmlive.com/")
    login_Page = LoginPage(driver)
    login_Page.doLogin()
    title_value = login_Page.getTitle()
    assert "OrangeHRM" in title_value


