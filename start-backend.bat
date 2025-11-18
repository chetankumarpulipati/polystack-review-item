@echo off
echo Starting WhatsApp Product Review Collector Backend...
echo.

cd backend

echo Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo.
echo Setting up virtual environment...
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Starting FastAPI server...
echo Backend will be available at http://localhost:8000
echo API docs at http://localhost:8000/docs
echo.
python main.py

pause

