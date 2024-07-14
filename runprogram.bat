@echo off
title PyAutoGUI Setup and Execution

echo Made by QTFeline
timeout /t 2 >nul
cls

echo Installing required Python packages...
pip install pyautogui threading time os
cls

echo Installation complete! Would you like to run the Python script now? (y/n)
set /p user_input="Enter your choice: "

if /i "%user_input%"=="y" (
    cls
    echo Remember to press F11 to start and F12 to finish the program.
    echo Running the Python script...
    python screenshitter.py
) else (
    cls
    echo You chose not to run the script. Exiting...
)

pause
