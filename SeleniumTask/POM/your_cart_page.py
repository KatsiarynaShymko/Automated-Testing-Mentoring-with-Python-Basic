"""Page Object Model for Cart Page"""

from selenium.webdriver.common.by import By

from SeleniumTask.POM.base_page import BasePage


class CartPage(BasePage):
    """
    Represents the Cart Page
    Contains locators and actions available on this page
    """

    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")
    cart_title = (By.CLASS_NAME, "title")
    cart_quantity_label = (By.CLASS_NAME, "cart_quantity_label")
    item_description = (By.CLASS_NAME, "cart_desc_label")

    def continue_shopping(self) -> None:
        """
        Waits until 'Continue Shopping' button is visible than clicks it
        :return: None
        """
        self.wait_until_visible(self.continue_shopping_button)
        self.click(self.continue_shopping_button)

    def checkout(self) -> "CheckoutInfo":
        """
        Waits until 'Checkout' button is visible then clicks it.
        After that CheckoutInfo page instance is returned
        :return: CheckoutInfo instance
        """
        from SeleniumTask.POM.checkout_info_page import CheckoutInfo

        self.wait_until_visible(self.checkout_button)
        self.click(self.checkout_button)
        return CheckoutInfo(self.driver)

    def get_your_cart_title(self) -> str:
        """
        Waits until cart's title is visible and then returns its text
        :return: cart's title
        """
        self.wait_until_visible(self.cart_title)
        return self.find(self.cart_title).text

    def get_your_qty_label(self) -> str:
        """
        Waits until quantity label is visible and then returns its text
        :return: quantity label's text
        """
        self.wait_until_visible(self.cart_quantity_label)
        return self.find(self.cart_quantity_label).text

    def get_item_description_label(self) -> str:
        """
        Waits until item's description is visible and then returns its text
        :return: item's description text
        """
        self.wait_until_visible(self.item_description)
        return self.find(self.item_description).text
