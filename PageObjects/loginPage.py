from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_txt_box = (By.NAME, "username")
        self.password_txt_box = (By.NAME, "password")
        self.loginBtn = (By.XPATH, "//button[@type='submit']")


    def doLogin(self):
        self.driver.find_element(*self.username_txt_box).send_keys("Admin")
        self.driver.find_element(*self.password_txt_box).send_keys("admin123")
        self.driver.find_element(*self.loginBtn).click()


    def getTitle(self):
        return self.driver.title