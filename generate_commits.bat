@echo off
REM GitHub Commit Generator - Windows Batch Script
REM Usage: generate_commits.bat <number_of_commits> [delay_in_seconds]

if "%1"=="" (
    echo Usage: generate_commits.bat ^<number_of_commits^> [delay_in_seconds]
    echo Example: generate_commits.bat 10
    echo Example: generate_commits.bat 5 2
    exit /b 1
)

set COMMIT_COUNT=%1
set DELAY=%2

if "%DELAY%"=="" (
    python commit_generator.py %COMMIT_COUNT%
) else (
    python commit_generator.py %COMMIT_COUNT% --delay %DELAY%
)