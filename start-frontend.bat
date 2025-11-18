@echo off
echo Starting WhatsApp Product Review Collector Frontend...
echo.

cd frontend

echo Checking Node.js installation...
node --version
if %errorlevel% neq 0 (
    echo ERROR: Node.js is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Installing dependencies...
if not exist node_modules (
    npm install
) else (
    echo Dependencies already installed.
)

echo.
echo Starting React development server...
echo Frontend will be available at http://localhost:3000
echo.
npm start

