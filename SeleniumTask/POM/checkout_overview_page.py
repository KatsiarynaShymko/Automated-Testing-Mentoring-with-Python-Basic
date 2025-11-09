"""Page Object Model for Checkout Overview Page"""

from selenium.webdriver.common.by import By

from SeleniumTask.POM.base_page import BasePage


class CheckoutOverview(BasePage):
    """
    Represents the Checkout Overview Page
    Contains locators and actions available on this page
    """

    total_sum = (By.CLASS_NAME, "summary_total_label")
    cancel_button = (By.ID, "cancel")
    finish_button = (By.ID, "finish")

    def get_total_sum(self) -> str:
        """
        Returns text of total sum
        :return: total sum's number in string format
        """
        return self.find(self.total_sum).text

    def finish_checkout(self) -> "CheckoutComplete":
        """
        Click the 'Finish' button and return an instance of CheckoutComplete
        :return: CheckoutComplete object
        """
        from SeleniumTask.POM.checkout_complete_page import CheckoutComplete

        self.click(self.finish_button)
        return CheckoutComplete(self.driver)

    def return_to_previous_page(self) -> None:
        """
        Click the 'Cancel' button
        :return: None
        """
        self.click(self.cancel_button)

    def get_item_name(self) -> str:
        """
        Returns the name of item's name in string format
        :return: item's name as string
        """
        return self.find((By.CLASS_NAME, "inventory_item_name")).text
