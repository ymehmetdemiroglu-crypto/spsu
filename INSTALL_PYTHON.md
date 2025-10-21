# 🐍 كيفية تثبيت Python على Windows

## الطريقة السريعة (الأسهل)

### 1. تحميل Python
- اذهب إلى: https://www.python.org/downloads/
- اضغط على "Download Python 3.11.7" (أو أحدث إصدار 3.11)
- اختر "Windows installer (64-bit)"

### 2. تثبيت Python
- شغل الملف المحمل
- **مهم جداً**: تأكد من وضع علامة ✅ على "Add Python to PATH"
- اضغط "Install Now"
- انتظر حتى ينتهي التثبيت

### 3. التحقق من التثبيت
- افتح Command Prompt (cmd)
- اكتب: `python --version`
- يجب أن تظهر: `Python 3.11.x`

## الطريقة البديلة (Microsoft Store)

### 1. افتح Microsoft Store
- ابحث عن "Python 3.11"
- اضغط "Install"

### 2. تشغيل البوت
- افتح Command Prompt
- اذهب إلى مجلد البوت: `cd C:\Users\hp\bot.py`
- شغل: `python bot.py`

## 🚀 تشغيل البوت

بعد تثبيت Python:

```bash
# 1. اذهب إلى مجلد البوت
cd C:\Users\hp\bot.py

# 2. ثبت المكتبات المطلوبة
pip install -r requirements.txt

# 3. شغل البوت
python bot.py
```

## ❗ إذا واجهت مشاكل

### المشكلة: "Python was not found"
**الحل**: أعد تثبيت Python مع وضع علامة على "Add Python to PATH"

### المشكلة: "pip was not found"
**الحل**: 
```bash
python -m pip install --upgrade pip
```

### المشكلة: "python-telegram-bot error"
**الحل**:
```bash
pip install python-telegram-bot==20.8
```

## 📱 اختبار البوت

1. افتح Telegram
2. ابحث عن بوتك
3. اكتب `/start`
4. يجب أن تظهر القائمة باللغة العربية

## 🎉 تهانينا!

البوت جاهز للاستخدام مع دعم كامل للغة العربية! 🇸🇦
