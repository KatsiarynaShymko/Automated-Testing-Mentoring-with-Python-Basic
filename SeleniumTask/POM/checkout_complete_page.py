"""Page Object Model for Checkout Complete Page"""

from selenium.webdriver.common.by import By

from SeleniumTask.POM.base_page import BasePage


class CheckoutComplete(BasePage):
    """
    Represents the Checkout Complete Page
    Contains locators and actions available on this page
    """

    back_home_button = (By.ID, "back-to-products")
    final_title = (By.CLASS_NAME, "complete-header")

    def get_final_title(self) -> str:
        """
        Wait for the final title element to be visible and return its text
        :return: title's text
        """
        self.wait_until_visible(self.final_title)
        return self.find(self.final_title).text

    def click_back_home_button(self) -> "InventoryPage":
        """
        Click the 'Back Home' button and return an instance of InventoryPage
        :return: InventoryPage object
        """
        from SeleniumTask.POM.inventory_page import InventoryPage

        self.click(self.back_home_button)
        return InventoryPage(self.driver)
