*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  tommi
    Set Password  tommi123!
    Confirm Password  tommi123!
    Submit Registration
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  to
    Set Password  tommi123
    Confirm Password  tommi123
    Submit Registration
    Registration Should Fail With Message  Username must be atleast 3 characters

Register With Valid Username And Too Short Password
    Set Username  tommi2
    Set Password  to
    Confirm Password  to
    Submit Registration
    Registration Should Fail With Message  Password must be atleast 8 characters


Register With Valid Username And Invalid Password
    Set Username  tommi2
    Set Password  tommitommi123
    Confirm Password  tommitommi123
    Submit Registration
    Registration Should Fail With Message  Password must contain atleast one non letter character

Register With Nonmatching Password And Password Confirmation
    Set Username  tommi2
    Set Password  tommitommi123!
    Confirm Password  tommitommi123?
    Submit Registration
    Registration Should Fail With Message  Passwords do not match


Register With Username That Is Already In Use
    Set Username  tommi
    Set Password  tommi123?
    Confirm Password  tommi123?
    Submit Registration
    Registration Should Fail With Message  Username is taken

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Registration Should Succeed
    Welcome Page Should Be Open

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Registration
    Click Button  Register

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Login Page