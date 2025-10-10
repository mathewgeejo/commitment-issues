@echo off
REM Setup Windows Task Scheduler for Daily Commits
REM Run this script as Administrator to set up the scheduled task

echo Setting up Windows Task Scheduler for daily commits...

REM Get the current directory
set "SCRIPT_DIR=%~dp0"
set "BAT_FILE=%SCRIPT_DIR%run_daily_commits.bat"

echo Script location: %BAT_FILE%

REM Create the scheduled task
schtasks /create /tn "GitHub Daily Commits" /tr "%BAT_FILE%" /sc daily /st 06:00 /f

if %ERRORLEVEL% EQU 0 (
    echo ✅ Successfully created scheduled task "GitHub Daily Commits"
    echo ⏰ Task will run daily at 6:00 AM
    echo 📁 Working directory: %SCRIPT_DIR%
    echo.
    echo To verify the task was created, run:
    echo schtasks /query /tn "GitHub Daily Commits"
    echo.
    echo To delete the task later, run:
    echo schtasks /delete /tn "GitHub Daily Commits" /f
) else (
    echo ❌ Failed to create scheduled task
    echo Make sure you're running this script as Administrator
)

pause