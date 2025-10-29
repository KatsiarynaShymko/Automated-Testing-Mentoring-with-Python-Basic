"""Tests for verifying login functionality"""

import pytest

from SeleniumTask.POM.inventory_page import InventoryPage


@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "problem_user",
        "error_user",
        "performance_glitch_user",
        "visual_user",
    ],
)
def test_login(open_login_page, username):
    """Positive test for login"""
    open_login_page.login(username, "secret_sauce")

    inventory_page = InventoryPage(open_login_page.driver)
    title_text = inventory_page.get_title()

    assert (
        title_text == "Swag Labs"
    ), f"Expected title 'Swag Labs', but got '{title_text}'"


def test_locked_user(open_login_page):
    """Negative test to verify error is displayed when locked user tries to log in"""
    open_login_page.login("locked_out_user", "secret_sauce")
    error = open_login_page.get_error_message()

    assert "Epic sadface: Sorry, this user has been locked out." in error, (
        "Actual title doesn't match the expected title - "
        "'Epic sadface: Sorry, this user has been locked out.'"
    )


def test_error_username(open_login_page):
    """Negative test to verify error when username field is not populated"""
    open_login_page.login("", "secret_sauce")
    error = open_login_page.get_error_message()

    assert (
        "Epic sadface: Username is required" in error
    ), "Actual error doesn't match the expected - 'Epic sadface: Username is required'"


def test_error_password(open_login_page):
    """Negative test to verify error when password field is not populated"""
    open_login_page.login("standard_user", "")
    error = open_login_page.get_error_message()

    assert (
        "Epic sadface: Password is required" in error
    ), "Actual error doesn't match the expected - 'Epic sadface: Password is required'"


@pytest.mark.parametrize(
    "username, password",
    [("standard_user1", "secret_sauce"), ("standard_user", "secret_sauce1")],
)
def test_error_not_matching(open_login_page, username, password):
    """Negative test to verify error when password or username is incorrect"""
    open_login_page.login(username, password)
    error = open_login_page.get_error_message()

    assert (
        "Epic sadface: Username and password do not match any user in this service"
        in error
    ), "Epic sadface: Username and password do not match any user in this service'"
