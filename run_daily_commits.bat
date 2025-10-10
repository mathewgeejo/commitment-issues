@echo off
REM Daily Auto Commit Runner for Windows Task Scheduler
REM This script runs the automated commit generator

cd /d "%~dp0"

echo Starting daily commit generation at %date% %time%
python auto_commit.py

if %ERRORLEVEL% EQU 0 (
    echo Daily commits completed successfully at %date% %time%
) else (
    echo Daily commits failed at %date% %time%
)

REM Log the execution
echo %date% %time% - Daily commit execution completed >> daily_commit_log.txt