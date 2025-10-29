"""Page Object Model for Inventory Page"""

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from SeleniumTask.POM.base_page import BasePage


class InventoryPage(BasePage):
    """
    Represents the Inventory Page
    Contains locators and actions available on this page
    """

    title = (By.CLASS_NAME, "app_logo")
    shopping_cart = (By.CLASS_NAME, "shopping_cart_link")
    cart_counter = (By.CLASS_NAME, "shopping_cart_badge")

    item_names = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-fleece-jacket",
        "sauce-labs-onesie",
        "test.allthethings()-t-shirt-(red)",
    ]

    display_names = {
        "sauce-labs-backpack": "Sauce Labs Backpack",
        "sauce-labs-bike-light": "Sauce Labs Bike Light",
        "sauce-labs-bolt-t-shirt": "Sauce Labs Bolt T-Shirt",
        "sauce-labs-fleece-jacket": "Sauce Labs Fleece Jacket",
        "sauce-labs-onesie": "Sauce Labs Onesie",
        "test.allthethings()-t-shirt-(red)": "Test.allTheThings() T-Shirt (Red)",
    }

    def get_item_button(self, item_name: str, state: str = "add") -> tuple[str, str]:
        """
        Return the locator of a product button depending on its state.
        :param item_name: The internal name (ID suffix) of the product item.
        :param state: The desired button state — either "add" (default) or "remove".
        :return: A tuple containing the locator method and value, e.g.
        (By.ID, "add-to-cart-sauce-labs-backpack")
        """
        prefix = "add-to-cart-" if state == "add" else "remove-"
        return (By.ID, f"{prefix}{item_name}")

    def add_item_to_cart(self, item_name: str) -> bool:
        """
        Add a specific item to the shopping cart.

        This method clicks the "Add to Cart" button for the given item and waits until
        the corresponding "Remove" button becomes visible, indicating the item has been added.

        :param item_name: The internal name (ID suffix) of the product item.
        :return: True if the item was successfully added to the cart
        """
        add_locator = self.get_item_button(item_name, "add")
        remove_locator = self.get_item_button(item_name, "remove")

        self.wait_until_visible(add_locator)
        self.click(add_locator)
        self.wait_until_visible(remove_locator)
        return True

    def remove_item_from_cart(self, item_name: str) -> bool:
        """
        Remove a specific item from the shopping cart.

        This method clicks the "Remove" button for the given item and waits until
        the corresponding "Add to cart" button becomes visible,
        indicating the item has been removed.

        :param item_name: The internal name (ID suffix) of the product item.
        :return: True if the item was successfully removed from the cart
        """
        remove_locator = self.get_item_button(item_name, "remove")
        add_locator = self.get_item_button(item_name, "add")

        self.wait_until_visible(remove_locator)
        self.click(remove_locator)
        self.wait_until_visible(add_locator)
        return True

    def add_all_items_to_cart(self) -> bool:
        """
        Adds all items to the cart
        :return: True if the items were successfully added to the cart
        """
        for name in self.item_names:
            self.add_item_to_cart(name)
        return True

    def remove_all_items_to_cart(self) -> bool:
        """
        Removes all items from the cart
        :return: True if the items were successfully removed from the cart
        """
        for name in self.item_names:
            self.remove_item_from_cart(name)
        return True

    def click_shopping_cart(self) -> "CartPage":
        """
        Click the Shopping cart icon and return an instance of CartPage
        :return: CartPage object
        """
        from SeleniumTask.POM.your_cart_page import CartPage

        self.click(self.shopping_cart)
        return CartPage(self.driver)

    def get_cart_count(self) -> int:
        """
        Get the number of items currently in the shopping cart.

        This method checks the cart counter badge. If the badge is not visible
        or an error occurs while retrieving the count, it returns 0.

        :return: Number of items in the cart as an integer
        """
        try:
            self.wait_until_visible(self.cart_counter)
            return int(self.find(self.cart_counter).text)
        except (NoSuchElementException, ValueError, TimeoutException):
            return 0

    def get_title(self) -> str:
        """
        Wait for the title element to be visible and return its text
        :return: title's text
        """
        self.wait_until_visible(self.title)
        return self.find(self.title).text
