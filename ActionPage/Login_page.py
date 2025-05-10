import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from LocatorPage.locator_page import LoginLocators, AddToCartLocators, PaymentProcessLocator, LogoutLocator

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        time.sleep(5)

    def open_login_page(self,url):
        self.driver.get(url)
        time.sleep(5)

    def username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(5)

    def password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(5)

    def submit(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        click_submit_button.click()
        time.sleep(5)

class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)

    def click_backpack(self):
        back_pack = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.BACKPACK))
        back_pack.click()
        time.sleep(5)

    def click_bike_light(self):
        bike_light = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.BIKE_LIGHT))
        bike_light.click()
        time.sleep(5)

    def click_bolt_tshirt(self):
        bolt_tshirt = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.BOLT_TSHIRT))
        bolt_tshirt.click()
        time.sleep(5)

    def click_fleece_jacket(self):
        fleece_jacket = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.FLEECE_JACKET))
        fleece_jacket.click()
        time.sleep(5)

    def click_onesie(self):
        onesie = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.ONESIE))
        onesie.click()
        time.sleep(5)

    def click_tshirt_red(self):
        tshirt_red = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AddToCartLocators.TSHIRT_RED))
        tshirt_red.click()
        time.sleep(5)

class PaymentProcessPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)

    def click_cart(self):
       cart = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.CART))
       cart.click()
       time.sleep(5)

    def click_checkout(self):
       checkout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.CHECKOUT))
       checkout.click()
       time.sleep(5)

    def first_name(self, first_name):
        enter_first_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.FIRST_NAME))
        enter_first_name.send_keys(first_name)
        time.sleep(5)

    def last_name(self, last_name):
        enter_last_name = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.LAST_NAME))
        enter_last_name.send_keys(last_name)
        time.sleep(5)

    def postal_code(self, postal_code):
        enter_postal_code = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.POSTAL_CODE))
        enter_postal_code.send_keys(postal_code)
        time.sleep(5)

    def click_continue_button(self):
       continue_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.CONTINUE))
       continue_button.click()
       time.sleep(5)

    def click_finish(self):
       finish = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(PaymentProcessLocator.FINISH))
       finish.click()
       time.sleep(5)

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        time.sleep(5)

    def click_menu(self):
       menu = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocator.MENU))
       menu.click()
       time.sleep(5)

    def click_logout(self):
       logout = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LogoutLocator.LOGOUT))
       logout.click()
       time.sleep(5)








