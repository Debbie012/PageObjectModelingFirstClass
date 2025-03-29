from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locator_page import LoginLocators


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def open_URL(self,url):
        self.driver.get(url)

    def username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)

    def submit(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        click_submit_button.send_keys()

