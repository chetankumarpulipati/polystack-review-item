@echo off
echo Stopping all running services...
echo.

echo Checking for processes on port 8000 (Backend)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000') do (
    echo Killing process %%a
    taskkill /F /PID %%a 2>nul
)

echo.
echo Checking for processes on port 3000 (Frontend)...
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :3000') do (
    echo Killing process %%a
    taskkill /F /PID %%a 2>nul
)

echo.
echo All services stopped!
pause

