*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Verify Page Loaded
    Page Should Contain Element  createAccountSubmit
    Element Text Should Be  createAccountSubmit  Create your Amazon account
