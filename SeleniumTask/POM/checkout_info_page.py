"""Page Object Model for Checkout Info Page"""

from selenium.webdriver.common.by import By

from SeleniumTask.POM.base_page import BasePage


class CheckoutInfo(BasePage):
    """
    Represents the Checkout Info Page
    Contains locators and actions available on this page
    """

    fname = (By.ID, "first-name")
    lname = (By.ID, "last-name")
    zip_code = (By.ID, "postal-code")
    cancel_button = (By.ID, "cancel")
    continue_button = (By.ID, "continue")

    def populate_fields_and_continue(
        self, fname: str, lname: str, zipcode: str
    ) -> "CheckoutOverview":
        """
        Fill in the checkout information form and proceed to the Checkout Overview page.
        :param fname: Customer's first name to populate in the form
        :param lname: Customer's last name to populate in the form
        :param zipcode: Customer's postal code to populate in the form
        :return: Instance of CheckoutOverview representing the next page
        """
        from SeleniumTask.POM.checkout_overview_page import CheckoutOverview

        self.populate(self.fname, fname)
        self.populate(self.lname, lname)
        self.populate(self.zip_code, zipcode)
        self.click(self.continue_button)
        return CheckoutOverview(self.driver)

    def click_cancel_button(self) -> None:
        """
        Click 'Cancel' button
        :return: None
        """
        self.click(self.cancel_button)
