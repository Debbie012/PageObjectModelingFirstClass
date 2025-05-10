from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")


class AddToCartLocators:
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BOLT_TSHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    TSHIRT_RED = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")

class PaymentProcessLocator:
    CART = (By.XPATH, "//*[@id='shopping_cart_container']/a")
    CHECKOUT = (By.XPATH, "//*[@id='checkout']")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

class LogoutLocator:
    MENU = (By.XPATH, "//*[@id='react-burger-menu-btn']")
    LOGOUT = (By.ID, "logout_sidebar_link")






