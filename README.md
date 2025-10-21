# 📚 Telegram Book Library Bot

A sophisticated Telegram bot that provides access to a multilingual book library through Google Drive integration. Features an intuitive menu system, smart search functionality, and supports books in English, Turkish, and Arabic languages.

## ✨ Features

- **📂 Menu-Based Navigation** - Intuitive browsing by category
- **🔎 Smart Search** - Case-insensitive search across all books
- **🌍 Multi-Language Support** - English, Turkish, and Arabic books
- **🔗 Google Drive Integration** - Direct access to books without local storage
- **⬇️ Dual Download Options** - Browser view and direct download
- **📱 Professional UI** - Clean interface with emojis and navigation

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Bot
```bash
python bot.py
```

## 📁 Project Structure

```
bot.py/
├── bot.py                 # Main bot code
├── files_database.json    # Book database with Google Drive links
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## 📚 Book Collection

### **🇺🇸 English Books (6 books)**
- Lehninger Principles of Biochemistry
- Aulton's Pharmaceutics (6th Edition)
- Basic Concepts in Biochemistry
- Color Atlas of Biochemistry
- Organic Chemistry (Fessenden)
- Complete Book of Essential Oils

### **🇹🇷 Turkish Books (7 books)**
- Farmakognozi
- Analitik Ders Notları
- Analitik Kimya Kitap
- Biruni Üniversitesi Eczacılık Fakültesi
- Farmasötik Botanik
- Temel İnsan Anatomisi
- TTP Farmakoloji

### **🇸🇦 Arabic Books (21 books)**
- Pharmaceutical drug names and uses
- Emergency medications
- Nervous system drugs
- Pressure medications
- Anti-nausea drugs
- Dermatological drugs
- And many more...

### **📋 Training & Exam Files (3 files)**
- Exam questions for licensing
- Training workbook example
- Internship file

## 🎯 How to Use

### **Browse Books**
1. Send `/start` to the bot
2. Click "📂 Browse Books"
3. Select a category (English, Turkish, Arabic, Training)
4. Choose a book
5. Select download option: "🔗 Open in Google Drive" or "⬇️ Direct Download"

### **Search Books**
1. Send `/start` to the bot
2. Click "🔎 Search Books"
3. Type a keyword (e.g., "biochemistry", "pharmacy")
4. Select from search results
5. Choose download option

## 🔧 Technical Details

### **Requirements**
- Python 3.11+ (avoid 3.13 due to compatibility issues)
- python-telegram-bot==20.8
- Internet access for Telegram API and Google Drive

### **Google Drive Setup**
1. Upload your books to Google Drive
2. Set sharing to "Anyone with the link can view"
3. Copy the sharing links
4. Update `files_database.json` with your links

### **Database Structure**
```json
{
  "Category Name": [
    {
      "title": "Book Title",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ]
}
```

## 🛠️ Customization

### **Adding New Books**
1. Upload book to Google Drive
2. Set sharing to "Anyone with the link can view"
3. Add to `files_database.json`:

```json
{
  "Your Category": [
    {
      "title": "New Book Title",
      "link": "https://drive.google.com/file/d/NEW_FILE_ID/view?usp=drive_link"
    }
  ]
}
```

### **Adding New Categories**
```json
{
  "New Category": [
    {
      "title": "Book Title",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ]
}
```

## 🔍 Search Examples

- **English**: "biochemistry", "pharmaceutics", "organic chemistry"
- **Turkish**: "farmakoloji", "anatomi", "analitik"
- **Arabic**: "أدوية", "فيتامينات", "سموميات"

## ⚠️ Important Notes

- **Google Drive Files**: Must be set to "Anyone with the link can view"
- **Python Version**: Use 3.11+ (3.13 has compatibility issues)
- **Bot Token**: Already configured in the code
- **No Local Storage**: All books are stored on Google Drive

## 🆘 Troubleshooting

### **Bot doesn't start**
- Check Python version (use 3.11+)
- Install dependencies: `pip install -r requirements.txt`
- Verify bot token is correct

### **Books not found**
- Check Google Drive links are accessible
- Verify files are set to "Anyone with the link can view"
- Ensure book titles match exactly in database

### **Search not working**
- Check if books are properly added to database
- Verify search terms are spelled correctly
- Check console for error messages

## 🚀 Deployment

### **Local Development**
```bash
python bot.py
```

### **Production Deployment**
- Use a VPS or cloud service
- Install Python 3.11+
- Set up process management (PM2, systemd, etc.)
- Monitor logs for errors

## 📈 Future Enhancements

- User authentication
- Book ratings and reviews
- Favorites system
- Admin panel
- Analytics dashboard
- Multi-language interface
- Book recommendations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

---

**🎉 Your Telegram Book Library Bot is ready to use!**

Send `/start` to your bot and start exploring the book collection!