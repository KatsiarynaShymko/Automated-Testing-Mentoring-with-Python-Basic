"""Page Object Model for Login Page"""

from selenium.webdriver.common.by import By

from SeleniumTask.POM.base_page import BasePage


class LoginPage(BasePage):
    """
    Represents the Login Page
    Contains locators and actions available on this page
    """

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def login(self, username: str, password: str) -> "InventoryPage":
        """
        Perform login on the Login Page using provided credentials.

        Fills in the username and password fields, clicks the login button,
        and returns an instance of the InventoryPage.

        :param username: Username to log in with.
        :param password: Password to log in with.
        :return: InventoryPage object after successful login.
        """
        from SeleniumTask.POM.inventory_page import InventoryPage

        self.populate(self.username, username)
        self.populate(self.password, password)
        self.click(self.login_button)
        return InventoryPage(self.driver)

    def get_error_message(self) -> str:
        """
        Return text of error message
        :return: error's text
        """
        return self.find(self.error_message).text
