@echo off
cd /d D:\AstraQuant

:START
echo [%date% %time%] Starting AstraQuant...
python scripts\live_monitor.py

echo [%date% %time%] Script stopped. Restarting in 10 seconds...
timeout /t 10 > nul
goto START