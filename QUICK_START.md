# 🚀 Quick Start Guide - Arabic Telegram Bot

## 🐍 Step 1: Install Python 3.11

### Option A: Direct Download (Recommended)
1. **Go to**: https://www.python.org/downloads/release/python-3117/
2. **Download**: "Windows installer (64-bit)"
3. **During Installation**:
   - ✅ Check "Add Python to PATH"
   - ✅ Check "Install for all users"
4. **Click**: "Install Now"

### Option B: Microsoft Store
1. Open **Microsoft Store**
2. Search for **"Python 3.11"**
3. Click **"Install"**

## 🔧 Step 2: Run the Bot

### Method 1: Double-click the installer
1. **Double-click**: `install_python.bat`
2. Follow the instructions

### Method 2: Manual commands
```bash
# Open Command Prompt in the bot folder
cd C:\Users\hp\bot.py

# Install dependencies
pip install -r requirements.txt

# Run the bot
python bot.py
```

## ✅ Step 3: Test the Bot

1. **Open Telegram**
2. **Find your bot** (search for your bot username)
3. **Send**: `/start`
4. **You should see**: Arabic menu with book categories

## 🎯 Expected Result

```
📚 مرحباً بك في بوت مكتبة الكتب!

اختر من القائمة أدناه:

📂 تصفح الكتب - تصفح الكتب حسب الفئة
🔎 البحث في الكتب - البحث عن كتب محددة
❓ المساعدة - تعلم كيفية استخدام البوت
```

## ❗ Troubleshooting

### Problem: "Python was not found"
**Solution**: Install Python 3.11 and make sure "Add Python to PATH" is checked

### Problem: "python-telegram-bot error"
**Solution**: 
```bash
pip install python-telegram-bot==20.8
```

### Problem: Bot doesn't respond
**Solution**: Check that your bot token is correct in `bot.py`

## 🎉 Success!

Once running, your Arabic Telegram bot will have:
- 🇸🇦 **20 Arabic books** (pharmacy, medicine, etc.)
- 🔍 **Arabic search** functionality
- 📱 **Arabic interface** throughout
- 📚 **Multi-language support** (Arabic, English, Turkish)

**Your bot is ready for Arabic users!** 🇸🇦

