@echo off
:loop
python C:\Users\Gacal\Desktop\NetworkMonitoringSystem/alert.py
timeout /t 60 /nobreak
goto loop
