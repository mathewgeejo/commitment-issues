@echo off
REM Launch GitHub Commit Generator GUI

echo Starting GitHub Commit Generator GUI...
python commit_gui.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo Error: Failed to start GUI. Make sure Python is installed and in your PATH.
    echo.
    pause
)