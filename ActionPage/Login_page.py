import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locator_page import LoginLocators, AddToCartLocators, PaymentProcessLocator, LogoutLocator


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def open_login_page(self,url):
        self.driver.get(url)

    def username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)

    def submit(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        click_submit_button.click()
        time.sleep(5)

class AddtoCartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_items_to_cart(self, item_names):
        for item in item_names:
            locator = AddToCartLocators.PRODUCT[item]
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def go_to_cart(self):
        cart_icon = self.driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self, first_name, last_name, postal_code):
        self.driver.find_element(*PaymentProcessLocator.PAYMENT["click on cart"]).click()
        self.driver.find_element(*PaymentProcessLocator.PAYMENT["click on checkout"]).click()

        self.driver.find_element(*PaymentProcessLocator.PAYMENT["Input First Name"]).send_keys("Adeyemo")
        self.driver.find_element(*PaymentProcessLocator.PAYMENT["Input Last Name"]).send_keys("Alakija")
        self.driver.find_element(*PaymentProcessLocator.PAYMENT["Input Postal Code"]).send_keys(234)

        self.driver.find_element(*PaymentProcessLocator.PAYMENT["click continue"]).click()
        self.driver.find_element(*PaymentProcessLocator.PAYMENT["Click finish"]).click()

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self):
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(LogoutLocator.LOGOUT["click the hamburger menu"])).click()
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LogoutLocator.LOGOUT["click logout"])).click()






