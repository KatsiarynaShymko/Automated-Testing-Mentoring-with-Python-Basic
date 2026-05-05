*** Settings ***
Library    SeleniumLibrary
Library    String
Library    BuiltIn
Library    Collections
Library    random

*** Variables ***
${BASE_URL}    https://www.demoblaze.com/
${REGISTERED_USERNAME}    Evaluate    "user_test_" + str(random.randint(1000, 9999))    random
${REGISTERED_PASSWORD}    pass123
${SIGNIN_BUTTON}    id:signin2
${USERNAME_FIELD_SIGNIN}    id:sign-username
${PASSWORD_FIELD_SIGNIN}    id:sign-password
${SIGNIN_BUTTON_POPUP}    css:#signInModal .btn-primary:nth-child(2)
${LOGIN_BUTTON}    id:login2
${USERNAME_FIELD_LOGIN}    id:loginusername
${PASSWORD_FIELD_LOGIN}    id:loginpassword
${LOGIN_BUTTON_POPUP}    css:#logInModal .btn-primary:nth-child(2)
${LOGOUT_BUTTON}    id:logout2
${MODAL}    css:.modal-open
${MONITORS_CATEGORY}    css:a.list-group-item[onclick="byCat('monitor')"]


*** Keywords ***
Generate Random User
    ${random_user}=    Evaluate    "user_test_" + str(random.randint(1000, 9999))    random
    Set Suite Variable    ${REGISTERED_USERNAME}    ${random_user}
    Set Suite Variable    ${REGISTERED_PASSWORD}    pass123

Launch browser
    Open Browser    ${BASE_URL}    chrome
    
Click Signin button
    Wait Until Element Is Visible    ${SIGNIN_BUTTON}
    Click Element    ${SIGNIN_BUTTON}

Populate fields and signin
    Wait Until Element Is Visible    ${USERNAME_FIELD_SIGNIN}
    Input Text    ${USERNAME_FIELD_SIGNIN}    ${REGISTERED_USERNAME}
    Input Text    ${PASSWORD_FIELD_SIGNIN}    ${REGISTERED_PASSWORD}
    Wait Until Element Is Visible   ${SIGNIN_BUTTON_POPUP}
    Click Element    ${SIGNIN_BUTTON_POPUP}

Handle signin browser alert and close browser
    ${alert_text}=    Handle Alert    timeout=15s    action=LEAVE
    Log To Console    ${alert_text}
    Should Contain Any    ${alert_text}    Sign up successful.    This user already exist.
    Handle Alert
    Close Browser

Click Login button
    Wait Until Element Is Visible    ${LOGIN_BUTTON}
    Click Element    ${LOGIN_BUTTON}

Populate fields and login
    Wait Until Element Is Visible    ${USERNAME_FIELD_LOGIN}
    Element Should Be Visible    ${PASSWORD_FIELD_LOGIN}
    Input Text    ${USERNAME_FIELD_LOGIN}    ${REGISTERED_USERNAME}
    Input Text    ${PASSWORD_FIELD_LOGIN}    ${REGISTERED_PASSWORD}
    Wait Until Element Is Enabled    ${LOGIN_BUTTON_POPUP}
    Click Element    ${LOGIN_BUTTON_POPUP}
    Wait Until Element Is Not Visible    ${MODAL}    10s

Logout button verification
    Wait Until Element Is Visible    ${LOGOUT_BUTTON}    10s
    Page Should Contain    Welcome ${REGISTERED_USERNAME}
    Wait Until Element Is Not Visible    ${MODAL}    10s
    
Click on monitors category
    Wait Until Element Is Enabled    ${MONITORS_CATEGORY}
    Click Element    ${MONITORS_CATEGORY}
