*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Verify Page Loaded
    Page Should Contain Element  createAccountSubmit
    Element Text Should Be  createAccountSubmit  Create your Amazon account

Login With Valid Credentials
    [Arguments]    ${Username}    ${Password}
	Fill "Email" Field    ${Username}
	Fill "Password" Field    ${Password}
	Click "Sign In" Button

Fill "Email" Field
    [Arguments]    ${Username}
    Log    Filling Email field with    ${Username}

Fill "Password" Field
    [Arguments]    ${Password}
    Log    Filling Password field with    ${Password}

Click "Sign In" Button
	Log    Clicking submit button
