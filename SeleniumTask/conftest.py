"""Container for fixtures and hooks"""

from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver

from SeleniumTask.POM.inventory_page import InventoryPage
from SeleniumTask.POM.login_page import LoginPage
from SeleniumTask.POM.your_cart_page import CartPage


@pytest.fixture()
def driver() -> Generator[WebDriver, None, None]:
    """Fixture to initialize and quit Firefox WebDriver."""
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def open_login_page(driver: WebDriver) -> "LoginPage":
    """
    Fixture to open the login page
    :param driver: WebDriver instance
    :return: LoginPage object
    """
    page = LoginPage(driver)
    page.open("https://www.saucedemo.com/")
    return page


@pytest.fixture()
def logged_in_user(open_login_page: LoginPage) -> "InventoryPage":
    """
    Fixture to log in as a standard user.
    :param open_login_page: LoginPage fixture.
    :return: InventoryPage object after successful login
    """
    user = open_login_page.login("standard_user", "secret_sauce")
    return user


@pytest.fixture()
def cart_page(logged_in_user: InventoryPage) -> "CartPage":
    """
    Fixture to navigate to the cart page after logging in
    :param logged_in_user: InventoryPage fixture
    :return: CartPage object
    """
    page = logged_in_user.click_shopping_cart()
    return page
