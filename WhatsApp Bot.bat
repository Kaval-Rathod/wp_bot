@echo off
title WhatsApp Bot API Server
echo Starting WhatsApp Bot App...
echo.

REM Change to the project directory where the Python files are located
cd /d "C:\kiz\vs_projects\bot"

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo Virtual environment not found, using system Python...
)

REM Check if the Python file exists
if not exist "whatsapp_bot_app.py" (
    echo Error: whatsapp_bot_app.py not found!
    echo Make sure this batch file is in the same folder as whatsapp_bot_app.py
    echo.
    echo Current directory: %CD%
    echo.
    pause
    exit /b 1
)

REM Run the WhatsApp Bot App
echo Running WhatsApp Bot App...
python whatsapp_bot_app.py

REM Keep window open if there's an error
if errorlevel 1 (
    echo.
    echo Error occurred! Press any key to exit...
    pause
) 