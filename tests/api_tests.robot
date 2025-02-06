*** Settings ***
Library    RequestsLibrary
Library    Collections

Suite Setup    Setup Test Data
Suite Teardown    Cleanup Test Data

*** Variables ***
${BASE_URL}    http://127.0.0.1:8000

*** Test Cases ***
Create a New User
    Create Session    myapi    ${BASE_URL}
    ${body}    Create Dictionary    name=John Doe    job=QA Engineer
    ${response}    POST On Session    myapi    /users    json=${body}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json_response}    Set Variable    ${response.json()}
    Set Suite Variable    ${user_id}    ${json_response['id']}

Get Users
    Create Session    myapi    ${BASE_URL}
    ${response}    GET On Session    myapi    /users
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json_response}    Set Variable    ${response.json()}
    Log    Response: ${json_response}

    ${keys}    Get Dictionary Keys    ${json_response}
    ${user_id}    Set Variable    ${keys}[0]

    Dictionary Should Contain Key    ${json_response}    ${user_id}

    ${user_data}    Get From Dictionary    ${json_response}    ${user_id}

    Dictionary Should Contain Item    ${user_data}    name    John Doe
    Dictionary Should Contain Item    ${user_data}    job    QA Engineer


*** Keywords ***
Setup Test Data
    Create Session    myapi    ${BASE_URL}
    ${response}    DELETE On Session    myapi    /reset-users
    Log    Test database reset

Cleanup Test Data
    Create Session    myapi    ${BASE_URL}
    ${response}    DELETE On Session    myapi    /reset-users
    Log    Test database cleaned up
