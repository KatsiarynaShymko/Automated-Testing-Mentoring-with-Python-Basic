"""Collection of main actions with elements"""

from typing import List, Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    """
    The base class for all Page Object classes.
    Contains common actions that can be performed on page elements.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Initializing the base page.

        :param driver: WebDriver instance to control the browser.
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        """
        Opens provided url.

        :param url: Url which needs to be open
        :type url: str
        :return: None
        """
        self.driver.get(url)

    def find(self, locator: Tuple[str, str]) -> WebElement:
        """
        Finds and returns a web element by the specified locator.

        :param locator: A tuple of the locator method and its value, for example (By.ID, "username")
        :type locator: Tuple[str, str]
        :return: The found WebElement
        :rtype: WebElement
        """
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple[str, str]) -> List[WebElement]:
        """
        Finds multiple elements on a page using the given locator.
        :param locator: A tuple with the locator method and its value, e.g. (By.ID, "username")
        :type locator: tuple[str, str]
        :return: List of found elements
        :rtype: List[WebElement]
        """
        return self.driver.find_elements(*locator)

    def click(self, locator: Tuple[str, str]) -> None:
        """
        Performs a click action on the element found by the given locator
        :param locator: A tuple with the locator method and its value, e.g. (By.ID, "username")
        :type locator:  Tuple[str, str]
        :return: None
        """
        self.find(locator).click()

    def populate(self, locator: Tuple[str, str], text: str) -> None:
        """
        Fills an input field located by the given locator with the provided text
        :param locator: A tuple with the locator method and its value, e.g. (By.ID, "username")
        :type locator: Tuple[str, str]
        :param text: str
        :return: None
        """
        el = self.find(locator)
        el.clear()
        el.send_keys(text)

    def wait_until_visible(self, locator: Tuple[str, str]) -> None:
        """
        Waits until the element located by the given locator is visible on the page
        :param locator: A tuple containing the locator method and its value,
        e.g. (By.ID, "login-button").
        :type locator: Tuple[str, str]
        :return: None
        """
        self.wait.until(EC.visibility_of_element_located(locator))
