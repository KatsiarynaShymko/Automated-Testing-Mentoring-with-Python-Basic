*** Settings ***
Library    SeleniumLibrary
Library    String
Suite Setup    Register New User
Test Teardown    Close Browser

*** Variables ***
${BASE_URL}    https://www.demoblaze.com/
${PRODUCT_PRICE}

*** Test Cases ***
LoginTest
    Open Browser    ${BASE_URL}    chrome
    Wait Until Element Is Visible    id:login2    5s

    #1. Click the login button.
    Click Element    id:login2

    #Expected result: login and password fields are presented
    Wait Until Element Is Visible    id:loginusername    5s
    Element Should Be Visible    id:loginpassword

    #2. Set up login and password and click the login button.
    Input Text    id:loginusername    ${REGISTERED_USERNAME}
    Input Text    id:loginpassword    ${REGISTERED_PASSWORD}
    Wait Until Element Is Enabled    css:#logInModal .btn-primary:nth-child(2)
    Click Element    css:#logInModal .btn-primary:nth-child(2)

    #Expected result: Log out button is presented;  Welcome {username} message is presented
    Wait Until Element Is Visible        id:logout2    5s
    Take Screenshot
    Page Should Contain    Welcome ${REGISTERED_USERNAME}


CartTest
    Open Browser    ${BASE_URL}    chrome
    Perform Login


    #1. Click on the Monitors category
    Wait Until Element Is Visible    css:a.list-group-item[onclick="byCat('monitor')"]    10s
    Click Element    css:a.list-group-item[onclick="byCat('monitor')"]

    #2. Click on the product with the highest price on the page.
    #Expected result: product's page with {product_name} and {product_price} is open
    Wait Until Element Is Visible    css:a[href="prod.html?idp_=10"]    5s
    Click Element    css:a[href="prod.html?idp_=10"]

    Wait Until Element Is Visible    css:.name    5s
    Element Should Be Visible    css:.price-container    5s
    ${product_name}=    Get Text    css:.name
    ${price_text}=      Get Text    css:.price-container

    ${price_value}=     Get Regexp Matches    ${price_text}    \\$(\\d+)    1
    Set Suite Variable    ${PRODUCT_NAME}    ${product_name}
    Set Suite Variable    ${PRODUCT_PRICE}    ${price_value}[0]

    Element Should Be Visible    css:a.btn.btn-success.btn-lg

    #3. Click on the Add to Cart button
    Click Element    css:a.btn.btn-success.btn-lg
    Handle Alert

    #4. Click on the Cart button. Expected result: product is successfully added to cart;
    #{product_name} and {product_price} are presented

    Wait Until Element Is Visible    css:#cartur    5s
    Click Element    css:#cartur

    Wait Until Location Contains    cart.html    10s
    Wait Until Element Is Visible    id:tbodyid    10s
    Wait Until Element Is Visible    xpath://*[@id="tbodyid"]//td[text()="${PRODUCT_NAME}"]    10s
    Take Screenshot
    Wait Until Element Is Visible    xpath://*[@id="tbodyid"]//td[text()="${PRODUCT_PRICE}"]    10s


*** Keywords ***
Register New User
    ${random_user}=    Evaluate    "user_test_" + str(random.randint(1000, 9999))    random
    Set Suite Variable    ${REGISTERED_USERNAME}    ${random_user}
    Set Suite Variable    ${REGISTERED_PASSWORD}    pass123
    
    Open Browser    ${BASE_URL}   chrome
    Wait Until Element Is Visible    id:signin2    5s
    Click Element    id:signin2
    Wait Until Element Is Visible    id:sign-username    10s
    Input Text    id:sign-username    ${REGISTERED_USERNAME}
    Input Text    id:sign-password    ${REGISTERED_PASSWORD}

    Wait Until Element Is Enabled    css:#signInModal .btn-primary:nth-child(2)
    Click Element    css:#signInModal .btn-primary:nth-child(2)

    ${alert_text}=    Handle Alert    timeout=15s    action=LEAVE
    Log To Console    ${alert_text}
    Should Contain Any    ${alert_text}    Sign up successful.    This user already exist.
    Handle Alert
    Close Browser

Perform Login
    Wait Until Element Is Visible    id:login2    5s
    Click Element    id:login2
    Wait Until Element Is Visible    id:loginusername    5s
    Element Should Be Visible    id:loginpassword
    Input Text    id:loginusername    ${REGISTERED_USERNAME}
    Input Text    id:loginpassword    ${REGISTERED_PASSWORD}
    Wait Until Element Is Enabled    css:#logInModal .btn-primary:nth-child(2)
    Click Element    css:#logInModal .btn-primary:nth-child(2)
    Wait Until Element Is Visible    id:logout2    10s
    Wait Until Element Is Not Visible    css:.modal-open    5s

Take Screenshot
    [Tags]    screenshot
    No Operation