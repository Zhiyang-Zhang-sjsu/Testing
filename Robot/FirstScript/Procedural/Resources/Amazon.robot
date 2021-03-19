*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Search for Products
    Go To    http://www.amazon.com
    wait until page contains    Amazon.com
    input text    id=twotabsearchtextbox  Ferrari 458
    click button    xpath=//*[@id="nav-search-submit-button"]
    wait until page contains    results for "Ferrari 458"

Select Product from Search Results
    click link    css=#search > div.s-desktop-width-max.s-desktop-content.sg-row > div.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(5) > div > span > div > div > div:nth-child(3) > h2 > a
    wait until page contains    Back to results

Add Product to Cart
    click button    id=add-to-cart-button
    wait until page contains    Add to your order
    click button    css=#attachWarrantyButtonBox > div > div.a-section.attach-warranty-button-row
    wait until page contains    Added to Cart

Begin Checkout
    click link    Proceed to Checkout
    page should contain element    ap_signin1a_pagelet_title
    element text should be    ap_signin1a_pagelet_title  Sign In