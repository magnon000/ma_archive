@ECHO OFF

TITLE AP46 Version.00.01.00

COLOR 2F

NET START MPSSVC

CLS

netsh wlan set hostednetwork mode=allow ssid=AP46 key=sexysix666 

netsh wlan start hostednetwork

ECHO. 

ECHO                 WIFIÃû: AP46  ÃÜÂë: sexysix666
   
ECHO. 

ECHO.                               

ECHO                                               version:00.01.00

ECHO                                               PRESENTED BY: Hellyell  

ECHO. 

TIMEOUT /T 18