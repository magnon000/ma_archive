@ECHO OFF

TITLE AP46设置项   Version.00.01.00

COLOR 2F

ECHO. 

ECHO                      AP46 设置项(仅用于 WINDOWS 7)

ECHO ---------------------------------------------------------------------

ECHO    1. AP46信息及状态

ECHO. 

ECHO    2. 暂停AP46网络连接

ECHO. 

ECHO    3. 启用AP46网络连接

ECHO. 

ECHO    4. 卸载AP46

ECHO. 

ECHO    5. 修改AP46密码

ECHO. 

ECHO    0. 退出

ECHO. 

ECHO                                               version:00.01.00

ECHO                                               PRESENTED BY: Hellyell  

ECHO ---------------------------------------------------------------------

set /p s=输入任务对应数字并按ENTER确定:


if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z


:a
netsh wlan show hostednetwork

set /p s=输入任务对应数字，按ENTER确定:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:b
netsh wlan stop hostednetwork

set /p s=输入任务对应数字，按ENTER确定:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:c
netsh wlan start hostednetwork

set /p s=输入任务对应数字，按ENTER确定:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:d
netsh wlan set hostednetwork mode=disallow

set /p s=输入任务对应数字，按ENTER确定:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:e
ECHO.
ECHO NOT DONE YET :) lol
ECHO.
set /p s=输入任务对应数字，按ENTER确定:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 0 goto z

:x
ECHO. 
ECHO             傻逼你好，傻逼再见   (傻逼你真6
ECHO. 
TIMEOUT /T 3

:z
exit