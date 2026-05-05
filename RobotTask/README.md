This project provides a set of automated tests for the DemoBlaze e-commerce website, 
focusing on User Login and Shopping Cart functionality. 
The tests are developed using the Robot Framework and SeleniumLibrary.

Prerequisites
Before running the tests, ensure you have the following installed:
Python (3.8 or higher)
pip (Python package installer)
Robot Framework and SeleniumLibrary (pip install robotframework robotframework-seleniumlibrary)
Google Chrome (pip install webdrivermanager)
ChromeDriver (webdrivermanager chrome install)

Steps to run the tests:
# 1. Run all tests
robot tests/example.robot

# 2. (Recommended) Run with a listener for automatic screenshot creation
robot --listener listeners/Screenshot_Listener.py tests/example.robot

# 3. Run a specific test (e.g., CartTest)
robot --test CartTest tests/example.robot


