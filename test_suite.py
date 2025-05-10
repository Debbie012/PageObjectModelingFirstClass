import pytest
from selenium import webdriver

from ActionPage.Login_page import LoginPage, PaymentProcessPage, LogoutPage, AddToCartPage
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

def test_login_page_on_sauce_demo_website(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.submit()

def test_add_to_cart_on_sauce_demo_website(login):
    add_cart = AddToCartPage(login.driver)
    add_cart.click_backpack()
    add_cart.click_bike_light()
    add_cart.click_bolt_tshirt()
    add_cart.click_fleece_jacket()
    add_cart.click_onesie()
    add_cart.click_tshirt_red()

def test_payment_process_on_sauce_demo_website(login):
    payment_process = PaymentProcessPage(login.driver)
    payment_process.click_cart()
    payment_process.click_checkout()
    payment_process.first_name(Config.FIRST_NAME)
    payment_process.last_name(Config.LAST_NAME)
    payment_process.postal_code(Config.POSTAL_CODE)
    payment_process.click_continue_button()
    payment_process.click_finish()

def test_logout_on_sauce_demo_website(login):
    logout = LogoutPage(login.driver)
    logout.click_menu()
    logout.click_logout()






