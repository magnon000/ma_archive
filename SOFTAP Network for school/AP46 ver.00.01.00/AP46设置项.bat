@ECHO OFF

TITLE AP46������   Version.00.01.00

COLOR 2F

ECHO. 

ECHO                      AP46 ������(������ WINDOWS 7)

ECHO ---------------------------------------------------------------------

ECHO    1. AP46��Ϣ��״̬

ECHO. 

ECHO    2. ��ͣAP46��������

ECHO. 

ECHO    3. ����AP46��������

ECHO. 

ECHO    4. ж��AP46

ECHO. 

ECHO    5. �޸�AP46����

ECHO. 

ECHO    0. �˳�

ECHO. 

ECHO                                               version:00.01.00

ECHO                                               PRESENTED BY: Hellyell  

ECHO ---------------------------------------------------------------------

set /p s=���������Ӧ���ֲ���ENTERȷ��:


if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z


:a
netsh wlan show hostednetwork

set /p s=���������Ӧ���֣���ENTERȷ��:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:b
netsh wlan stop hostednetwork

set /p s=���������Ӧ���֣���ENTERȷ��:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:c
netsh wlan start hostednetwork

set /p s=���������Ӧ���֣���ENTERȷ��:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 6 goto x
if %s% equ 0 goto z

:d
netsh wlan set hostednetwork mode=disallow

set /p s=���������Ӧ���֣���ENTERȷ��:

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
set /p s=���������Ӧ���֣���ENTERȷ��:

if %s% equ 1 goto a
if %s% equ 2 goto b
if %s% equ 3 goto c
if %s% equ 4 goto d
if %s% equ 5 goto e
if %s% equ 0 goto z

:x
ECHO. 
ECHO             ɵ����ã�ɵ���ټ�   (ɵ������6
ECHO. 
TIMEOUT /T 3

:z
exit