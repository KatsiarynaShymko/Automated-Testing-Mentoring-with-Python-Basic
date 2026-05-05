*** Settings ***
Library    SeleniumLibrary
Library    String
Library    BuiltIn
Library    Collections

*** Variables ***
${MONITOR_WITH_HIGHEST_PRICE}    css:a[href="prod.html?idp_=10"]
${PRODUCT_NAME_LOCATOR}    css:.name
${PRODUCT_PRICE_LOCATOR}    css:.price-container
${ADD_TO_CART_BUTTON}    css:a.btn.btn-success.btn-lg
${CART}    css:#cartur
${CART_PAGE}    cart.html


*** Keywords ***
Click on the product with the highest price
    Wait Until Element Is Visible    ${MONITOR_WITH_HIGHEST_PRICE}    5s
    Click Element    ${MONITOR_WITH_HIGHEST_PRICE}

Collect product name and price
    Wait Until Element Is Visible    ${PRODUCT_NAME_LOCATOR}
    Element Should Be Visible    ${PRODUCT_PRICE_LOCATOR}
    ${product_name}=    Get Text    ${PRODUCT_NAME_LOCATOR}
    ${price_text}=      Get Text    ${PRODUCT_PRICE_LOCATOR}
    ${price_value}=     Get Regexp Matches    ${price_text}    \\$(\\d+)    1
    Set Test Variable    ${PRODUCT_NAME}    ${product_name}
    Set Test Variable    ${PRODUCT_PRICE}    ${price_value}[0]
    
Add to cart
    Element Should Be Visible    ${ADD_TO_CART_BUTTON}
    Click Element    ${ADD_TO_CART_BUTTON}
    Handle Alert
    
Open cart
    Wait Until Element Is Visible    ${CART}
    Click Element    ${CART}
    
Navigate to cart page
    Wait Until Location Contains    ${CART_PAGE}
