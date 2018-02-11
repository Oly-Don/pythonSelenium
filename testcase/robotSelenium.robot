*** Settings ***
Library           Selenium2Library
Library           String
Library           DatabaseLibrary
Library           RequestsLibrary
Library           SSHLibrary
Library           Collections
Library           DateTime
Library           Dialogs
Library           OperatingSystem
Library           Process
Library           Screenshot
Library           XML
Library           Telnet
Library           AutoItLibrary

*** Variables ***
${userDefineVarient}    y=robotTest    # 自定义名称
${host}           http://www.baidu.com
${gridUrl}        http://192.168.0.183:5555/wd/hub

*** Test Cases ***
Baidu
    [Tags]    passed
    Log    hello_python_world
    Log    ${userDefineVarient}
    ${myName}    Set Variable    唐友德
    Log    ${myName}
    ${radomeStr}    Generate Random String    20
    ${oly}    Evaluate    89/23
    log    ${oly}
    Open Browser    ${host}    browser=firefox
    Press Key    id=kw    docker
    Click Button    id=su
    Sleep    3 seconds

RemoteFirefox
    [Tags]    test
    ${localProfile}    Set Variable    C:\Users\Administrator.USER-20180121IN\AppData\Roaming\Mozilla\Firefox\Profiles
    log    begin test,login:${host}
    Open Browser    ${host}    browser=firefox    alias=183firefox    remote_url=${gridUrl}    \    ff_profile_dir=no
    Input Text    id=kw    Robot Framework
    Click Button    id=su
    Capture Page Screenshot
    Sleep    5
    Close All Browsers
