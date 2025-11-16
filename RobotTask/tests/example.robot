*** Settings ***
Library    SeleniumLibrary
Library    String
Suite Setup    Register New User
Test Teardown    Close Browser
Resource    ../resources/keywords.robot
Resource    ../resources/MonitorsPage.resource
Resource    ../resources/CartPage.resource

*** Variables ***
${BASE_URL}    https://www.demoblaze.com/
${PRODUCT_PRICE}

*** Test Cases ***
LoginTest
    Launch browser
    Click Login button
    Populate fields and login
    Logout button verification
    Take Screenshot


CartTest
    Launch browser
    Perform Login
    Click on monitors category
    Click on the product with the highest price
    Collect product name and price
    Add to cart
    Open cart
    Navigate to cart page
    Verify records
    Take Screenshot
