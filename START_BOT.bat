@echo off
title Arabic Telegram Bot - Setup
color 0A
echo.
echo ========================================
echo    🇸🇦 Arabic Telegram Bot Setup
echo ========================================
echo.

echo 🔍 Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found!
    echo.
    echo 📋 Please install Python 3.11 first:
    echo    1. Go to: https://www.python.org/downloads/release/python-3117/
    echo    2. Download "Windows installer (64-bit)"
    echo    3. During installation, check "Add Python to PATH"
    echo    4. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ Python found!
python --version

echo.
echo 📦 Installing bot dependencies...
pip install -r requirements.txt

echo.
echo 🚀 Starting Arabic Telegram Bot...
echo.
echo 📱 Your bot is ready! Find it on Telegram and send /start
echo 🇸🇦 The bot interface is in Arabic for your users
echo.

python bot.py

echo.
echo Bot stopped. Press any key to exit...
pause >nul

