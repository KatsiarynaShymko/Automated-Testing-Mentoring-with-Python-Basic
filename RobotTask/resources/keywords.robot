*** Settings ***
Resource    ../resources/MainPage.resource

*** Keywords ***
Register New User
    Generate Random User
    Launch browser
    Click Signin Button
    Populate Fields And Signin
    Handle signin browser alert and close browser

Perform Login
    Click Login button
    Populate fields and login

Take Screenshot
    [Tags]    screenshot
    No Operation
