@echo off
echo Get time from NTP-server...

:: Запрос времени с NTP-сервера (например, time.windows.com)
w32tm /stripchart /computer:time.windows.com /dataonly /samples:1

echo.
echo Current local time:
time /T
date /T

pause