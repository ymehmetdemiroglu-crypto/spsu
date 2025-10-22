import webbrowser
import os
import subprocess
import sys

def main():
    print("🐍 Python 3.11 Installer for Telegram Bot")
    print("=" * 50)
    
    # Check if Python is already installed
    try:
        result = subprocess.run([sys.executable, "--version"], capture_output=True, text=True)
        if "3.11" in result.stdout:
            print("✅ Python 3.11 is already installed!")
            print(f"Version: {result.stdout.strip()}")
            return
        elif "3.13" in result.stdout:
            print("❌ Python 3.13 detected - this will cause compatibility issues!")
            print("Please install Python 3.11 instead.")
    except:
        pass
    
    print("📋 Opening Python 3.11.7 download page...")
    print("🔗 URL: https://www.python.org/downloads/release/python-3117/")
    
    # Open the download page
    webbrowser.open("https://www.python.org/downloads/release/python-3117/")
    
    print("\n📋 Installation Instructions:")
    print("1. Download 'Windows installer (64-bit)'")
    print("2. Run the installer")
    print("3. ✅ IMPORTANT: Check 'Add Python to PATH'")
    print("4. ✅ Check 'Install for all users'")
    print("5. Click 'Install Now'")
    print("\n⏳ After installation, run this script again to verify.")
    
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

