*** Settings ***
Library    SeleniumLibrary
Library    String
Library    BuiltIn
Library    Collections

*** Variables ***
${CART_TABLE}    id:tbodyid

*** Keywords ***
Verify records
    Wait Until Element Is Visible    ${CART_TABLE}
    ${name_locator}=    Set Variable    xpath://*[@id="tbodyid"]//td[text()='${PRODUCT_NAME}']
    ${price_locator}=   Set Variable    xpath://*[@id="tbodyid"]//td[text()='${PRODUCT_PRICE}']
    Wait Until Element Is Visible    ${name_locator}
    Wait Until Element Is Visible    ${price_locator}
