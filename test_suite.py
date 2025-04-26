import pytest
from selenium import webdriver

from ActionPage.Login_page import LoginPage, AddtoCartPage, PaymentProcessPage, LogoutPage
from Config.configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

def test_login_page_on_automation_play_ground_website(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.submit()

def test_end_to_end_user_flow(login, driver_setup):
    add_to_cart = AddtoCartPage(driver_setup)
    add_to_cart.add_items_to_cart(["Backpack", "Bike Light", "Bolt TShirt", "Fleece Jacket", "Onesie", "Tshirt Red"])
    add_to_cart.go_to_cart()

    checkout = PaymentProcessPage(driver_setup)
    checkout.checkout("Adeyemo", "Alakija", "234")

    logout = LogoutPage(driver_setup)
    logout.logout()
