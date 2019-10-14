*** Settings ***
Library     Collections
Resource    ../../Common/Common_Keywords.robot
Resource    ModuleName_Variables.robot
Variables   ModuleName.yaml

*** Keywords ***
User Loads A WSDL File
    User Loads A WSDL From The Given Path   ${WSDL}  ${LOCATION.ModuleName}

User Sets Valid Value For The Attribute Of A WSDL Object
    ${req}=    Create Wsdl Object    doService
    Set Wsdl Object Attribute    ${req}    ModuleName    ${INPUT.SUCCESS.ModuleName}
    set test variable  ${req}

User Sets Invalid Value For APPID Attribute Of A WSDL Object
    ${req}=    Create Wsdl Object    doService
    Set Wsdl Object Attribute    ${req}    ModuleName    ${INPUT.FAILURE.INVALID_APPID.ModuleName}
    Set Test Variable  ${req}

User Sends The Request
    ${res}=    Call Soap Method    doService    ${req}
    Set Test Variable  ${res}

User Verifies The Response
    ${result}=    compareResponseAndExpectedResult    ${res}     ${OUTPUT.SUCCESS}
    Should Be True  ${result}
