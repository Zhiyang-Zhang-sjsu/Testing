*** Settings ***
Documentation    This is some basic info about the whole suite
Resource    ../Resources/Common.robot  # for Setup & Teardown
Resource    ../Resources/AmazonApp.robot  # for lower level keywords in test cases
Test Setup    Common.Begin Web Test
Test Teardown    Common.End Web Test

*** Variables ***
${BROWSER} =    chrome
${START_URL} =    https://www.amazon.com
${SEARCH_TERM} =    Ferrari 458
${LOGIN_EMAIL} =    admin@robotframework.com
${LOGIN_PASSWORD} =    myPassword

*** Test Cases ***
Should be able to login
    AmazonApp.Login    ${LOGIN_EMAIL}    ${LOGIN_PASSWORD}

Logged out user should be able to search for products
    [Tags]    Current
    AmazonApp.Search for Products

Logged out user should be able to view a product
    AmazonApp.Search for Products
    AmazonApp.Select Product from Search Results

Logged out user should be able to add product to cart
    AmazonApp.Search for Products
    AmazonApp.Select Product from Search Results
    AmazonApp.Add Product to Cart

Logged out user must sign in to check out
    AmazonApp.Search for Products
    AmazonApp.Select Product from Search Results
    AmazonApp.Add Product to Cart
    AmazonApp.Begin Checkout
