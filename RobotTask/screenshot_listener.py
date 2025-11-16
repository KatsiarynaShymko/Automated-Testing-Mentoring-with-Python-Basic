"""Listener that will make screenshots after executing every keyword with the tag 'screenshot'"""
import os
import re
from typing import Any, Dict

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

ROBOT_LISTENER_API_VERSION = 2

logger.info("[Screenshot_Listener] File loaded")

OUTPUT_DIR = os.path.join(os.getcwd(), "screenshots")
os.makedirs(OUTPUT_DIR, exist_ok=True)
logger.info(f"[Screenshot_Listener] Screenshots will be saved to: {OUTPUT_DIR}")


def fix_filename(name: str) -> str:
    """
    Update the input string for safe use as a file name.

    Replaces any character that is not a word character (a-z, A-Z, 0-9, _),
    a hyphen (-), or a dot (.) with an underscore (_).

    Args: name (str): The original string to be updated.
    Returns: str: The safe, updated file name.
        """
    return re.sub(r'[^\w\-_.]', '_', name)


def end_keyword(name: str, attrs: Dict[str, Any]) -> None:
    """
    Called by Robot Framework after the execution of every keyword.

    This function checks if the finished keyword has the 'screenshot' tag.
    If the tag is present, it captures the current state of the browser
    and saves the image to a predefined path.

    Args:
        name (str): The name of the keyword that just finished execution.
        attrs (dict): A dictionary containing the keyword's attributes.
    """
    tags = [t.lower() for t in attrs.get('tags', [])]
    if "screenshot" in tags:
        try:
            seleniumlib = BuiltIn().get_library_instance("SeleniumLibrary")
            if seleniumlib:
                logger.info("[ScreenshotListener] SeleniumLibrary instance found.")
            else:
                logger.error("[ScreenshotListener] SeleniumLibrary instance NOT found!")

            test_name = BuiltIn().get_variable_value("${TEST NAME}")
            safe_test_name = fix_filename(test_name)
            safe_keyword_name = fix_filename(name)
            screenshot_path = os.path.join(
                OUTPUT_DIR,
                f"{safe_test_name}_{safe_keyword_name}.png"
            )
            seleniumlib.capture_page_screenshot(screenshot_path)
            logger.info(f"[ScreenshotListener] Screenshot saved: {screenshot_path}")

        except Exception as e:
            logger.error(f"[ScreenshotListener ERROR] {e}")
