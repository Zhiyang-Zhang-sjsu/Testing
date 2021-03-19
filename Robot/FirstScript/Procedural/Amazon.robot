*** Settings ***
Documentation  This is some basic info about the whole suite
Resource    Resources/Amazon.robot
Resource    Resources/Common.robot

Test Setup    Begin Web Test
Test Teardown    End Web Test

*** Variables ***


*** Test Cases ***
User must sign in to check out
    [Documentation]  This is some basic info about the test
    [Tags]  Smoke

    Amazon.Search for Products
    Amazon.Select Product from Search Results
    Amazon.Add Product to Cart
    Amazon.Begin Checkout

