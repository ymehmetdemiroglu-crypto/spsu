# 🤖 AI Agent Prompt: Telegram Book Library Bot Implementation

## **Project Overview**
Create a sophisticated Telegram bot that provides access to a multilingual book library through Google Drive integration. The bot should feature an intuitive menu system, smart search functionality, and support books in English, Turkish, and Arabic languages.

## **Core Requirements**

### **1. Bot Architecture**
- **Framework**: python-telegram-bot==20.8
- **Python Version**: 3.11+ (avoid 3.13 due to compatibility issues)
- **Database**: JSON file-based storage
- **Storage**: Google Drive integration (no local file storage)
- **Language Support**: English, Turkish, Arabic

### **2. Menu System Implementation**
Create a hierarchical menu system with:
- **Main Menu**: Browse Books, Search Books, Help
- **Category Navigation**: Language-based organization with emojis
- **Book Selection**: Direct access to Google Drive links
- **Navigation**: Back buttons and breadcrumb navigation
- **Inline Keyboards**: All interactions through Telegram inline keyboards

### **3. Database Structure**
Implement JSON database with this structure:
```json
{
  "English Books": [
    {
      "title": "Lehninger Principles of Biochemistry",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ],
  "Turkish Books": [
    {
      "title": "Farmakognozi",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ],
  "Arabic Books": [
    {
      "title": "الأسماء التجارية والعلمية للأدوية",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ],
  "Training & Exam Files": [
    {
      "title": "أسئلة دورات لامتحان السناج",
      "link": "https://drive.google.com/file/d/FILE_ID/view?usp=drive_link"
    }
  ]
}
```

### **4. Core Classes and Functions**

#### **FileBot Class**
```python
class FileBot:
    def __init__(self):
        self.files_db = self.load_files_database()
    
    def load_files_database(self) -> Dict:
        # Load JSON database, create default if not exists
    
    def search_books(self, query: str) -> List[Dict]:
        # Case-insensitive search across all book titles
        # Return max 10 results
    
    def get_direct_download_link(self, google_drive_link: str) -> str:
        # Convert Google Drive view link to direct download link
        # Input: https://drive.google.com/file/d/FILE_ID/view?usp=drive_link
        # Output: https://drive.google.com/uc?export=download&id=FILE_ID
    
    def validate_google_drive_link(self, link: str) -> bool:
        # Validate Google Drive link format
```

#### **Handler Functions**
```python
async def start(update, context):
    # Display main menu with 3 options: Browse, Search, Help

async def show_categories(update, context):
    # Display categories with emojis and book counts
    # Emojis: 🇺🇸 English, 🇹🇷 Turkish, 🇸🇦 Arabic, 📋 Training

async def show_books_in_category(update, context, category):
    # Display books in selected category
    # Limit to 8 books per page
    # Truncate long titles for display

async def send_book_link(update, context, book_title, category):
    # Provide book access with two options:
    # 1. Open in Google Drive (browser view)
    # 2. Direct Download (file download)

async def handle_search(update, context):
    # Process search queries
    # Case-insensitive partial matching
    # Display up to 8 results

async def button_callback(update, context):
    # Handle all inline keyboard interactions
    # Navigation between menus
    # Book selection and access
```

### **5. User Experience Flow**

#### **Browse Flow**
1. User sends `/start`
2. Bot shows main menu with 3 options
3. User clicks "📂 Browse Books"
4. Bot shows categories with emojis and book counts
5. User selects category (e.g., "🇺🇸 English Books (6)")
6. Bot shows books in that category
7. User clicks a book
8. Bot provides download options: "🔗 Open in Google Drive" and "⬇️ Direct Download"

#### **Search Flow**
1. User clicks "🔎 Search Books"
2. Bot prompts for search term
3. User types keyword (e.g., "biochemistry")
4. Bot shows matching books with category info
5. User clicks desired book
6. Bot provides download options

### **6. Google Drive Integration**

#### **Link Processing**
- **Input Format**: `https://drive.google.com/file/d/FILE_ID/view?usp=drive_link`
- **Output Format**: `https://drive.google.com/uc?export=download&id=FILE_ID`
- **Validation**: Check for proper Google Drive URL format
- **Error Handling**: Show user-friendly messages for invalid links

#### **Access Methods**
1. **Browser View**: Opens in Google Drive interface for viewing
2. **Direct Download**: Downloads file directly to user's device
3. **Requirements**: Files must be set to "Anyone with the link can view"

### **7. Database Content (Sample Data)**

#### **English Books (6 books)**
- Lehninger Principles of Biochemistry
- Aulton's Pharmaceutics (6th Edition)
- Basic Concepts in Biochemistry - A Student's Survival Guide (2nd Edition)
- Color Atlas of Biochemistry (2nd Edition)
- Organic Chemistry - Fessenden & Fessenden
- The Complete Book of Essential Oils & Aromatherapy

#### **Turkish Books (7 books)**
- Farmakognozi (Turkish)
- Analitik Ders Notları (I) Mühendislik
- Analitik Kimya Kitap
- Biruni Üniversitesi Eczacılık Fakültesi Öğrenci El Kitabı
- Farmasötik Botanik - Ankara Üniversitesi
- Temel İnsan Anatomisi
- TTP Farmakoloji 1 - Farmakolojiye Giriş

#### **Arabic Books (21 books)**
- الأسماء التجارية والعلمية للأدوية مع الاستعمالات وموانع الاستعمال
- أدوية الثلاجة
- أدوية الجهاز العصبي
- أدوية الطوارئ
- أدوية الضغط
- أدوية التقيؤ والغثيان
- أدوية الجلدية
- أدوية الحمى والرضاع
- أدوية الطفيليات
- التركيبات
- السكري الداء والدواء
- جمع الفيتامينات - أعراض نقصها وكيف تحصل عليها
- علم السموميات
- فقر الدم
- مسكنات الألم كاملة
- مضادات التشنج
- مضادات الفطريات
- مضادات الفيروس والديدان
- ملخص أدوية النسائية
- ملزمة أدوية
- موانع الحمل

#### **Training & Exam Files (3 files)**
- أسئلة دورات لامتحان السناج
- مثال عن دفتر التدريب / سناج
- Staj Dosyası

### **8. Error Handling & Validation**

#### **Input Validation**
- Search queries must be non-empty
- Google Drive links must be properly formatted
- Book titles must match exactly in database
- Categories must exist in database

#### **Error Messages**
- "❌ Book not found!" - When book doesn't exist
- "❌ Invalid Google Drive link!" - When link format is wrong
- "❌ No books found for 'query'" - When search returns no results
- "✅ Book link sent!" - When book access is successful

#### **Graceful Degradation**
- Missing books show "No books found" message
- Invalid links provide error feedback
- Search failures suggest alternative actions
- Navigation errors return to main menu

### **9. User Interface Elements**

#### **Inline Keyboards**
- Main menu buttons: Browse, Search, Help
- Category buttons with emojis and book counts
- Book selection buttons with truncated titles
- Navigation buttons: Back, Main Menu
- Download option buttons: Google Drive, Direct Download

#### **Display Features**
- **Category Emojis**: 🇺🇸🇹🇷🇸🇦📋 for easy identification
- **Book Counts**: Show available books per category
- **Title Truncation**: Long titles shortened to 35 characters
- **Markdown Formatting**: Bold titles, proper formatting

### **10. Technical Implementation Details**

#### **File Structure**
```
bot.py/
├── bot.py                 # Main bot code
├── files_database.json    # Book database
├── requirements.txt       # Dependencies
└── README.md             # Documentation
```

#### **Dependencies**
```
python-telegram-bot==20.8
```

#### **Configuration**
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

#### **Key Features**
- **Result Limiting**: Max 10 search results, 8 displayed
- **Title Truncation**: Long titles shortened for UI
- **Efficient Search**: Case-insensitive partial matching
- **Memory Management**: No file storage, Google Drive handles files
- **Error Logging**: Comprehensive error logging
- **User Session Management**: Stateless operation

### **11. Security & Best Practices**

#### **Token Security**
- Bot token should be configurable
- No sensitive data in database
- Google Drive links are public (as intended)

#### **Performance Optimizations**
- Efficient search algorithms
- Minimal memory usage
- Fast response times
- Graceful error handling

### **12. Deployment Requirements**

#### **Environment Setup**
- Python 3.11+ (avoid 3.13)
- Internet access for Telegram API and Google Drive
- Persistent storage for files_database.json
- Process management for 24/7 operation

#### **Hosting Considerations**
- Reliable internet connection
- Persistent storage for database
- Process monitoring and restart capabilities
- Error logging and monitoring

### **13. Testing Requirements**

#### **Functionality Tests**
- Menu navigation works correctly
- Search returns accurate results
- Google Drive links are properly converted
- Error handling works as expected
- Multi-language support functions properly

#### **User Experience Tests**
- Intuitive navigation flow
- Clear error messages
- Responsive interface
- Proper text formatting
- Emoji display works correctly

### **14. Future Enhancement Possibilities**

#### **Potential Additions**
- User authentication for restricted access
- Book ratings and reviews
- Favorites system for users
- Admin panel for book management
- Analytics for usage tracking
- Multi-language interface support
- Book recommendations based on search history

#### **Technical Improvements**
- Database migration to SQLite/PostgreSQL
- Caching system for frequently accessed books
- API integration for book metadata
- File type support beyond PDFs
- Batch operations for book management

## **Implementation Instructions**

1. **Create the main bot.py file** with all required classes and functions
2. **Implement the JSON database** with the provided book structure
3. **Set up the menu system** with inline keyboards
4. **Add Google Drive integration** with link conversion
5. **Implement search functionality** with case-insensitive matching
6. **Add error handling** and user-friendly error messages
7. **Create requirements.txt** with necessary dependencies
8. **Write comprehensive documentation** for setup and usage
9. **Test all functionality** including navigation, search, and downloads
10. **Deploy with proper configuration** and monitoring

## **Success Criteria**

The bot should successfully:
- Display a professional main menu with 3 options
- Show categories with emojis and book counts
- Allow browsing through books by category
- Provide search functionality across all books
- Convert Google Drive links to direct downloads
- Handle errors gracefully with user-friendly messages
- Support multiple languages (English, Turkish, Arabic)
- Provide intuitive navigation with back buttons
- Work reliably with proper error handling
- Be easy to deploy and maintain

This comprehensive specification provides all the technical details needed to implement a fully functional Telegram Book Library Bot with professional-grade features and user experience.


