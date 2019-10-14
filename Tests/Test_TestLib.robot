*** Settings ***
Documentation    Suite description
Library  TestLib

*** Test Cases ***
Test title
    [Tags]    DEBUG
    Provide Information  abc
#    Get Value  abc
    Get Report  Newreport


*** Keywords ***
