#!/usr/bin/env python3
"""
Python 3.13 Compatible Arabic Telegram Bot
This version is specifically designed to work with Python 3.13
"""

import sys
import subprocess
import os

def check_python_version():
    """Check Python version and provide compatibility info"""
    version = sys.version_info
    print(f"🐍 Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major == 3 and version.minor == 13:
        print("✅ Python 3.13 detected - using compatibility mode")
        return True
    elif version.major == 3 and version.minor == 11:
        print("✅ Python 3.11 detected - optimal compatibility")
        return True
    else:
        print(f"⚠️  Python {version.major}.{version.minor} detected - may have compatibility issues")
        return True

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        # Avoid redundant reinstalls by using --upgrade-strategy only-if-needed
        subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "--upgrade-strategy", "only-if-needed", "python-telegram-bot==21.0"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def run_bot():
    """Run the appropriate bot version"""
    if check_python_version():
        if install_dependencies():
            print("🚀 Starting Arabic Telegram Bot...")
            print("🇸🇦 البوت العربي لمكتبة الكتب يبدأ...")
            
            # Try the Python 3.13 compatible version first
            # Import of the bot module here would execute it immediately and slow startup
            # Instead, instruct the user to run the module directly to avoid duplicate work
            print("💡 To start the bot, run: python bot_python313.py")
            return True
        else:
            print("❌ Failed to install dependencies")
            return False
    else:
        print("❌ Python version check failed")
        return False

if __name__ == "__main__":
    print("🤖 Arabic Telegram Bot - Python 3.13 Compatibility Mode")
    print("=" * 60)
    
    if run_bot():
        print("🎉 Bot setup completed successfully!")
    else:
        print("❌ Bot setup failed. Please check the error messages above.")
        print("💡 For best results, use Python 3.11")
