*** Settings ***
Library           Selenium2Library
Library           String
Library           DatabaseLibrary
Library           RequestsLibrary
Library           Collections
Library           Screenshot

*** Variables ***
${userDefineVarient}    y=robotTest    # 自定义名称
${host}           http://www.baidu.com
${gridUrl}        http://192.168.0.183:5555/wd/hub

*** Test Cases ***
Math
    [Tags]    pass
    Log    hello_python_world
    Log    ${userDefineVarient}
    ${myName}    Set Variable    唐友德
    Log    ${myName}
    ${radomeStr}    Generate Random String    20
    ${oly}    Evaluate    89/23
    log    ${oly}

BaiduLocal
    [Tags]    pass
    Open Browser    ${host}    browser=firefox
    Press Key    id=kw    docker
    Click Button    id=su
    Sleep    3 seconds
    Capture Page Screenshot     shot.png

RemoteFirefox
    [Tags]    test
    log    begin test,login:${host}
    Open Browser    ${host}    browser=firefox    alias=183firefox    remote_url=${gridUrl}
    Should Not Be Equal    id=su    百度一下
    Input Text    id=kw    Robot Framework
    Click Button    id=su
    Capture Page Screenshot    filename=shot.png
    Sleep    3
    Close All Browsers
    Close All Browsers
