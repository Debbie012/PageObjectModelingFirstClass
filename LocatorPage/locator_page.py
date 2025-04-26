from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

class AddToCartLocators:
    PRODUCT = {
        "Backpack": (By.ID, "add-to-cart-sauce-labs-backpack"),
        "Bike Light": (By.ID, "add-to-cart-sauce-labs-bike-light"),
        "Bolt TShirt": (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"),
        "Fleece Jacket": (By.ID, "add-to-cart-sauce-labs-fleece-jacket"),
        "Onesie": (By.ID, "add-to-cart-sauce-labs-onesie"),
        "Tshirt Red": (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    }

class PaymentProcessLocator:
    PAYMENT = {
        "click on cart": (By.XPATH, "//*[@id='shopping_cart_container']/a"),
        "click on checkout": (By.XPATH, "//*[@id='checkout']"),
        "Input First Name": (By.ID, "first-name"),
        "Input Last Name": (By.ID, "last-name"),
        "Input Postal Code": (By.ID, "postal-code"),
        "click continue": (By.ID, "continue"),
        "Click finish": (By.ID, "finish")
    }

class LogoutLocator:
    Logout = {
        "click the hamburger menu": (By.XPATH, "//*[@id='react-burger-menu-btn']"),
        "click logout": (By.ID, "logout_sidebar_link")
    }





