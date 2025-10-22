@echo off
echo 🐍 Installing Python 3.11 for Telegram Bot
echo.
echo 📋 Step 1: Downloading Python 3.11.7...
echo Please download Python 3.11.7 from: https://www.python.org/downloads/release/python-3117/
echo.
echo 📋 Step 2: During installation, make sure to:
echo    ✅ Check "Add Python to PATH"
echo    ✅ Check "Install for all users"
echo.
echo 📋 Step 3: After installation, run this script again
echo.
pause
echo.
echo 🔍 Checking Python installation...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python not found. Please install Python 3.11 first.
    pause
    exit /b 1
)
echo.
echo ✅ Python found! Installing bot dependencies...
pip install -r requirements.txt
echo.
echo 🚀 Starting Telegram Bot...
python bot.py
pause

