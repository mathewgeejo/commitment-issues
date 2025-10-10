@echo off
REM Test the automated commit system
REM This will generate 3-5 commits quickly for testing

echo Testing automated commit system...
echo This will generate a few commits quickly for testing purposes.
echo.

python auto_commit.py --test

echo.
echo Test completed! Check your GitHub repository to see the commits.
pause