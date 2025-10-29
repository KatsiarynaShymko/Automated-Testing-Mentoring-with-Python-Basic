"""Tests for verify cart and checkout functionality"""

import pytest
from selenium.webdriver.common.by import By


# Inventory page
def test_inventory_page_elements(logged_in_user):
    """Positive test to verify elements on page"""
    page = logged_in_user

    assert page.get_title() == "Swag Labs", "Page title is incorrect"

    for item in page.item_names:
        add_button = page.get_item_button(item, "add")
        element = page.find(add_button)
        assert element.is_displayed(), f"{element} is not present on the page"

    cart_icon = logged_in_user.find(logged_in_user.shopping_cart)
    cart_counter_number = logged_in_user.get_cart_count()
    assert cart_icon.is_displayed(), f"{cart_icon} is not displayed"
    assert (
        cart_counter_number == 0
    ), f"{cart_counter_number} is not equal to 0, some items may be present in cart"


@pytest.mark.parametrize(
    "item",
    [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ],
)
def test_add_item_to_cart(logged_in_user, item):
    """Positive test to add one item to cart"""
    page = logged_in_user
    page.add_item_to_cart(item)
    remove_button = page.get_item_button(item, "remove")
    cart_counter = page.get_cart_count()

    assert cart_counter == 1, f"{cart_counter} is not equal to 1"
    assert page.find(
        remove_button
    ).is_displayed(), "Remove button is not present after adding item"


@pytest.mark.parametrize(
    "item",
    [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ],
)
def test_remove_item_from_cart(logged_in_user, item):
    """Positive test to remove item from cart"""
    page = logged_in_user
    page.add_item_to_cart(item)
    page.remove_item_from_cart(item)
    add_button = page.get_item_button(item, "add")
    cart_counter = page.get_cart_count()

    assert (
        cart_counter == 0
    ), f"{cart_counter} is not equal to 0, some items may be present in cart"
    assert page.find(
        add_button
    ).is_displayed(), "Add button is not present after removing item"


def test_add_all_items_to_cart(logged_in_user):
    """Positive test when user adds all items on page to cart"""
    page = logged_in_user
    page.add_all_items_to_cart()
    cart_counter = page.get_cart_count()
    expected_count = len(page.item_names)

    assert (
        cart_counter == expected_count
    ), f"{cart_counter} is not equal to {expected_count}"

    for item_name in page.item_names:
        remove_button = page.get_item_button(item_name, "remove")
        assert page.find(
            remove_button
        ).is_displayed(), "Not all remove buttons are present"


def test_remove_all_items_from_cart(logged_in_user):
    """Positive test when user removes all previously added items from cart"""
    page = logged_in_user
    page.add_all_items_to_cart()
    page.remove_all_items_to_cart()
    cart_counter = page.get_cart_count()

    for item in page.item_names:
        add_button = page.get_item_button(item, "add")
        assert page.find(add_button).is_displayed(), "Not all add buttons are present"

    assert (
        cart_counter == 0
    ), f"{cart_counter} is not equal to 0, some items may be present in cart"


# Your cart page
def test_cart_with_empty_state(cart_page):
    """Positive test to view cart when no items are added"""
    title = cart_page.get_your_cart_title()
    qty_label = cart_page.get_your_qty_label()
    description_label = cart_page.get_item_description_label()
    c_shopping = cart_page.continue_shopping_button
    checkout_button = cart_page.checkout_button

    assert title == "Your Cart", "Title is not 'Your Cart'"
    assert qty_label == "QTY", f"{qty_label} is not 'QTY'"
    assert (
        description_label == "Description"
    ), f"{description_label} is not 'Description'"
    assert cart_page.find(c_shopping).is_displayed(), f"{c_shopping} is not displayed"
    assert cart_page.find(
        checkout_button
    ).is_displayed(), f"{checkout_button} is not displayed"


@pytest.mark.parametrize(
    "item",
    [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ],
)
def test_cart_add_item(logged_in_user, item):
    """Positive test to verify added item on your_cart page"""
    inventory_page = logged_in_user
    inventory_page.add_item_to_cart(item)
    cart_window = inventory_page.click_shopping_cart()

    title = cart_window.get_your_cart_title()
    assert title == "Your Cart", "Cart page title is incorrect"

    quantities = cart_window.driver.find_elements(By.CLASS_NAME, "cart_quantity")
    assert len(quantities) == 1, f"Expected 1 item in cart, but found {len(quantities)}"

    cart_item_name = cart_window.driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text.lower()
    expected_value = inventory_page.display_names.get(item).lower()

    assert (
        expected_value in cart_item_name
    ), f"Expected item '{expected_value}' not found in cart"


def test_cart_with_added_items(logged_in_user):
    """Positive test to verify added items on your_cart page"""
    inventory_page = logged_in_user
    inventory_page.add_all_items_to_cart()
    expected_count = len(inventory_page.item_names)
    cart_window = inventory_page.click_shopping_cart()
    title = cart_window.get_your_cart_title()
    assert title == "Your Cart", "Cart page title is incorrect"

    cart_items = cart_window.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert (
        len(cart_items) == expected_count
    ), f"Expected {expected_count} items in cart, but found {len(cart_items)}"

    cart_item_texts = [item.text.lower() for item in cart_items]
    for _, display_name in inventory_page.display_names.items():
        assert any(
            display_name.lower() in text for text in cart_item_texts
        ), f"Item '{display_name}' not found in cart"


# e2e
@pytest.mark.parametrize(
    "item, price, tax",
    [
        ("sauce-labs-backpack", 29.99, 2.40),
        ("sauce-labs-bike-light", 9.99, 0.80),
        ("sauce-labs-bolt-t-shirt", 15.99, 1.28),
        ("sauce-labs-fleece-jacket", 49.99, 4.00),
        ("sauce-labs-onesie", 7.99, 0.64),
        ("test.allthethings()-t-shirt-(red)", 15.99, 1.28),
    ],
)
def test_checkout_of_one_item(logged_in_user, item, price, tax):
    """Positive e2e test to verify checkout for one product"""
    inventory_page = logged_in_user
    inventory_page.add_item_to_cart(item)

    # navigating to cart
    cart_window = inventory_page.click_shopping_cart()

    title = cart_window.get_your_cart_title()
    assert title == "Your Cart", "Cart page title is incorrect"

    quantities = cart_window.driver.find_elements(By.CLASS_NAME, "cart_quantity")
    assert len(quantities) == 1, f"Expected 1 item in cart, but found {len(quantities)}"

    cart_item_name = cart_window.driver.find_element(
        By.CLASS_NAME, "inventory_item_name"
    ).text.lower()
    expected_name = inventory_page.display_names.get(item).lower()

    assert (
        expected_name in cart_item_name
    ), f"Expected item '{expected_name}' not found in cart"

    # proceeding to checkout info
    info_window = cart_window.checkout()
    checkout_overview_page = info_window.populate_fields_and_continue(
        "name", "surname", "123"
    )

    # final checkout page
    expected_total_sum = round(price + tax, 2)
    actual_total_sum_text = checkout_overview_page.get_total_sum()
    actual_total_sum = float(actual_total_sum_text.replace("Total: $", ""))

    assert (
        actual_total_sum == expected_total_sum
    ), f"Total sum is {actual_total_sum} when expected {expected_total_sum}"
    cart_item_name = checkout_overview_page.get_item_name().lower()
    expected_name = inventory_page.display_names.get(item).lower()

    assert (
        expected_name in cart_item_name
    ), f"Expected item '{expected_name}' not found in cart"

    # checkout complete page
    checkout_complete_page = checkout_overview_page.finish_checkout()
    title = checkout_complete_page.get_final_title()

    assert "Thank you for your order!" in title, "Title is not correct"

    back_to_inventory = checkout_complete_page.click_back_home_button()
    cart_count = back_to_inventory.get_cart_count()

    assert cart_count == 0, "Some items are present in cart"


def test_checkout_all_items(logged_in_user):
    """Positive e2e test to verify checkout for all products"""
    inventory_page = logged_in_user
    inventory_page.add_all_items_to_cart()
    expected_count = len(inventory_page.item_names)

    # navigating to cart
    cart_window = inventory_page.click_shopping_cart()
    title = cart_window.get_your_cart_title()
    assert title == "Your Cart", "Cart page title is incorrect"

    cart_items = cart_window.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    assert (
        len(cart_items) == expected_count
    ), f"Expected {expected_count} items in cart, but found {len(cart_items)}"

    cart_item_texts = [item.text.lower() for item in cart_items]
    for _, display_name in inventory_page.display_names.items():
        assert any(
            display_name.lower() in text for text in cart_item_texts
        ), f"Item '{display_name}' not found in cart"

    # proceeding to checkout info
    info_window = cart_window.checkout()
    checkout_overview_page = info_window.populate_fields_and_continue(
        "name", "surname", "123"
    )
    # final checkout page
    expected_total_sum = 140.34
    actual_total_sum_text = checkout_overview_page.get_total_sum()
    actual_total_sum = float(actual_total_sum_text.replace("Total: $", ""))

    assert (
        actual_total_sum == expected_total_sum
    ), f"Total sum is {actual_total_sum} when expected {expected_total_sum}"
    cart_items_names = checkout_overview_page.find_elements(
        (By.CLASS_NAME, "inventory_item_name")
    )
    cart_items_texts = [item.text.lower() for item in cart_items_names]

    for _, display_name in inventory_page.display_names.items():
        assert any(
            display_name.lower() in text for text in cart_items_texts
        ), f"Item '{display_name}' not found"

    # checkout complete page
    checkout_complete_page = checkout_overview_page.finish_checkout()
    title = checkout_complete_page.get_final_title()

    assert "Thank you for your order!" in title, "Title is not correct"

    back_to_inventory = checkout_complete_page.click_back_home_button()
    cart_count = back_to_inventory.get_cart_count()

    assert cart_count == 0, "Some items are present in cart"
