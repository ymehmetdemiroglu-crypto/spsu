import os
import json
import logging
import re
from typing import Dict, List, Optional
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot configuration
BOT_TOKEN = "8459047761:AAEv-RrhZQnngpD1iO47pwgB2_t7wnqLhrE"

class FileBot:
    def __init__(self):
        self.files_db = self.load_files_database()
        
    def load_files_database(self) -> Dict:
        """Load the files database from JSON file"""
        try:
            with open('files_database.json', 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Create default database structure
            default_db = {
                "English Books": [
                    {
                        "title": "Lehninger Principles of Biochemistry",
                        "link": "https://drive.google.com/file/d/1NlTx0SL_ur-ZjiOObuBX84vfJW27wq8E/view?usp=drive_link"
                    }
                ]
            }
            self.save_files_database(default_db)
            return default_db
    
    def save_files_database(self, database: Dict):
        """Save the files database to JSON file"""
        with open('files_database.json', 'w', encoding='utf-8') as f:
            json.dump(database, f, ensure_ascii=False, indent=2)
    
    def get_all_books(self) -> List[Dict]:
        """Get all books from all categories"""
        all_books = []
        for category, books in self.files_db.items():
            for book in books:
                book_with_category = book.copy()
                book_with_category['category'] = category
                all_books.append(book_with_category)
        return all_books
    
    def search_books(self, query: str) -> List[Dict]:
        """Search for books containing the query"""
        query = query.lower()
        matching_books = []
        
        for category, books in self.files_db.items():
            for book in books:
                if query in book['title'].lower():
                    book_with_category = book.copy()
                    book_with_category['category'] = category
                    matching_books.append(book_with_category)
        
        return matching_books[:10]  # Limit to 10 results
    
    def get_direct_download_link(self, google_drive_link: str) -> str:
        """Convert Google Drive sharing link to direct download link"""
        # Extract file ID from Google Drive link
        file_id_match = re.search(r'/file/d/([a-zA-Z0-9-_]+)', google_drive_link)
        if file_id_match:
            file_id = file_id_match.group(1)
            # Convert to direct download link
            return f"https://drive.google.com/uc?export=download&id={file_id}"
        return google_drive_link
    
    def validate_google_drive_link(self, link: str) -> bool:
        """Validate if the link is a proper Google Drive link"""
        return "drive.google.com" in link and "/file/d/" in link

# Initialize bot instance
file_bot = FileBot()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    keyboard = [
        [InlineKeyboardButton("📂 تصفح الكتب", callback_data="view_books")],
        [InlineKeyboardButton("🔎 البحث في الكتب", callback_data="search_books")],
        [InlineKeyboardButton("❓ المساعدة", callback_data="help")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_message = """
📚 **مرحباً بك في بوت مكتبة الكتب!**

اختر من القائمة أدناه:

📂 **تصفح الكتب** - تصفح الكتب حسب الفئة
🔎 **البحث في الكتب** - البحث عن كتب محددة
❓ **المساعدة** - تعلم كيفية استخدام البوت

استخدم /start في أي وقت للعودة إلى القائمة الرئيسية.
    """
    
    await update.message.reply_text(
        welcome_message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def show_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show book categories"""
    keyboard = []
    
    # Add category buttons with appropriate emojis
    category_emojis = {
        "الكتب العربية": "🇸🇦",
        "English Books": "🇺🇸",
        "Turkish Books": "🇹🇷", 
        "ملفات التدريب والامتحانات": "📋"
    }
    
    for category in file_bot.files_db.keys():
        emoji = category_emojis.get(category, "📚")
        book_count = len(file_bot.files_db[category])
        # Use simple callback data to avoid encoding issues
        if category == "الكتب العربية":
            callback_data = "cat_arabic"
        elif category == "English Books":
            callback_data = "cat_english"
        elif category == "Turkish Books":
            callback_data = "cat_turkish"
        elif category == "ملفات التدريب والامتحانات":
            callback_data = "cat_training"
        else:
            callback_data = f"cat_{category}"
        
        keyboard.append([InlineKeyboardButton(f"{emoji} {category} ({book_count})", callback_data=callback_data)])
    
    # Add back button
    keyboard.append([InlineKeyboardButton("⬅️ العودة للقائمة الرئيسية", callback_data="main_menu")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        "📂 **اختر فئة الكتب:**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def show_books_in_category(update: Update, context: ContextTypes.DEFAULT_TYPE, category: str):
    """Show books in a specific category"""
    books = file_bot.files_db.get(category, [])
    
    if not books:
        await update.callback_query.edit_message_text(
            f"❌ No books found in {category}",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Back", callback_data="view_books")]])
        )
        return
    
    keyboard = []
    
    # Add book buttons (limit to 8 books per page to avoid Telegram limits)
    for i, book in enumerate(books[:8]):
        # Truncate long titles
        display_title = book['title'][:35] + "..." if len(book['title']) > 35 else book['title']
        # Use index-based callback data to avoid encoding issues
        keyboard.append([InlineKeyboardButton(f"📖 {display_title}", callback_data=f"book_{i}_{category}")])
    
    # Add navigation buttons
    keyboard.append([InlineKeyboardButton("⬅️ العودة للفئات", callback_data="view_books")])
    keyboard.append([InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        f"📂 **{category}**\n\nاختر كتاباً للحصول على رابط التحميل:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def send_book_link(update: Update, context: ContextTypes.DEFAULT_TYPE, book_title: str, category: str):
    """Send a book's Google Drive link to the user"""
    books = file_bot.files_db.get(category, [])
    book = None
    
    # Find the book by title
    for b in books:
        if b['title'] == book_title:
            book = b
            break
    
    if not book:
        await update.callback_query.answer("❌ Book not found!", show_alert=True)
        return
    
    # Validate the Google Drive link
    if not file_bot.validate_google_drive_link(book['link']):
        await update.callback_query.answer("❌ Invalid Google Drive link!", show_alert=True)
        return
    
    # Get direct download link
    direct_link = file_bot.get_direct_download_link(book['link'])
    
    # Create keyboard with both original and direct download links
    keyboard = [
        [InlineKeyboardButton("🔗 فتح في Google Drive", url=book['link'])],
        [InlineKeyboardButton("⬇️ تحميل مباشر", url=direct_link)],
        [InlineKeyboardButton("⬅️ العودة للفئة", callback_data=f"category_{category}")],
        [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message_text = f"""
📖 **{book['title']}**

**الفئة:** {category}

اختر كيفية الوصول إلى الكتاب:

🔗 **فتح في Google Drive** - عرض الكتاب في المتصفح
⬇️ **تحميل مباشر** - تحميل الملف مباشرة

*ملاحظة: تأكد من أن ملف Google Drive مضبوط على "أي شخص لديه الرابط يمكنه العرض" حتى يعمل التحميل المباشر.*
    """
    
    await update.callback_query.edit_message_text(
        message_text,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )
    
    await update.callback_query.answer("✅ تم إرسال رابط الكتاب!")

async def show_search_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show search menu"""
    keyboard = [
        [InlineKeyboardButton("⬅️ العودة للقائمة الرئيسية", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    search_message = """
🔎 **البحث في الكتب**

اكتب كلمة مفتاحية للبحث عن الكتب. سيجد البوت الكتب التي تحتوي على مصطلح البحث.

**أمثلة:**
• `أدوية` - يجد كتب الأدوية
• `طب` - يجد كتب الطب
• `صيدلة` - يجد كتب الصيدلة

اكتب مصطلح البحث الآن:
    """
    
    await update.callback_query.edit_message_text(
        search_message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def handle_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle search queries"""
    query = update.message.text.strip()
    
    if not query:
        await update.message.reply_text("يرجى إدخال مصطلح البحث.")
        return
    
    results = file_bot.search_books(query)
    
    if not results:
        await update.message.reply_text(
            f"❌ لم يتم العثور على كتب لـ '{query}'\n\nجرب مصطلح بحث مختلف أو استخدم /start لتصفح الفئات.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]])
        )
        return
    
    # Create keyboard with search results
    keyboard = []
    for book in results[:8]:  # Limit to 8 results
        display_title = book['title'][:30] + "..." if len(book['title']) > 30 else book['title']
        keyboard.append([InlineKeyboardButton(f"📖 {display_title}", callback_data=f"book_{book['title']}_{book['category']}")])
    
    keyboard.append([InlineKeyboardButton("🔎 بحث جديد", callback_data="search_books")])
    keyboard.append([InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"🔎 **نتائج البحث لـ '{query}':**\n\nتم العثور على {len(results)} كتاب:",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show help menu"""
    keyboard = [
        [InlineKeyboardButton("⬅️ العودة للقائمة الرئيسية", callback_data="main_menu")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    help_message = """
❓ **كيفية استخدام هذا البوت:**

**📂 تصفح الكتب**
• تصفح الكتب المنظمة حسب الفئات
• انقر على فئة لرؤية الكتب المتاحة
• انقر على كتاب للحصول على روابط التحميل

**🔎 البحث في الكتب**
• اكتب كلمات مفتاحية للعثور على كتب محددة
• سيقترح البوت الكتب المطابقة
• انقر على كتاب للحصول على روابط التحميل

**📱 التنقل**
• استخدم الأزرار للتنقل عبر القوائم
• استخدم /start للعودة إلى القائمة الرئيسية في أي وقت
• جميع الكتب مخزنة على Google Drive

**🔗 خيارات التحميل**
• **فتح في Google Drive** - عرض الكتاب في المتصفح
• **تحميل مباشر** - تحميل الملف مباشرة

**💡 نصائح:**
• الكتب منظمة حسب اللغة والفئات الموضوعية
• البحث غير حساس لحالة الأحرف
• يمكنك البحث عن أجزاء من عناوين الكتب
• تأكد من أن ملفات Google Drive مضبوطة على "أي شخص لديه الرابط يمكنه العرض"
    """
    
    await update.callback_query.edit_message_text(
        help_message,
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle button callbacks"""
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "main_menu":
        # Return to main menu
        keyboard = [
            [InlineKeyboardButton("📂 تصفح الكتب", callback_data="view_books")],
            [InlineKeyboardButton("🔎 البحث في الكتب", callback_data="search_books")],
            [InlineKeyboardButton("❓ المساعدة", callback_data="help")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(
            "📚 **القائمة الرئيسية**\n\nاختر خياراً:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif data == "view_books":
        await show_categories(update, context)
    
    elif data == "search_books":
        await show_search_menu(update, context)
    
    elif data == "help":
        await show_help(update, context)
    
    elif data.startswith("cat_"):
        # Map callback data to actual category names
        if data == "cat_arabic":
            category = "الكتب العربية"
        elif data == "cat_english":
            category = "English Books"
        elif data == "cat_turkish":
            category = "Turkish Books"
        elif data == "cat_training":
            category = "ملفات التدريب والامتحانات"
        else:
            category = data.replace("cat_", "")
        await show_books_in_category(update, context, category)
    
    elif data.startswith("book_"):
        # Extract book index and category from callback data
        parts = data.replace("book_", "").split("_", 1)
        if len(parts) >= 2:
            book_index = int(parts[0])
            category = parts[1]
            # Get the book from the category using the index
            books = file_bot.files_db.get(category, [])
            if book_index < len(books):
                book_title = books[book_index]['title']
                await send_book_link(update, context, book_title, category)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors"""
    logger.error(f"Update {update} caused error {context.error}")

def main():
    """Start the bot"""
    try:
        # Create application with compatibility fixes for Python 3.13
        application = Application.builder().token(BOT_TOKEN).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CallbackQueryHandler(button_callback))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search))
        application.add_error_handler(error_handler)
        
        # Start the bot
        print("🤖 Arabic Book Library Bot is starting...")
        print("🇸🇦 البوت العربي لمكتبة الكتب يبدأ...")
        print("📋 Make sure to:")
        print("   1. Bot token is configured")
        print("   2. Update files_database.json with your book structure")
        print("   3. Ensure Google Drive files are set to 'Anyone with the link can view'")
        print("   4. Test the bot with /start command")
        
        # Use run_polling with compatibility settings
        application.run_polling(
            allowed_updates=Update.ALL_TYPES,
            drop_pending_updates=True
        )
    except Exception as e:
        print(f"❌ Error starting bot: {e}")
        print("💡 This is a Python 3.13 compatibility issue.")
        print("🔧 Trying alternative startup method...")
        
        # Alternative startup method for Python 3.13
        try:
            import asyncio
            from telegram.ext import ApplicationBuilder
            
            # Create application with builder
            app = ApplicationBuilder().token(BOT_TOKEN).build()
            
            # Add handlers
            app.add_handler(CommandHandler("start", start))
            app.add_handler(CallbackQueryHandler(button_callback))
            app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search))
            app.add_error_handler(error_handler)
            
            print("🚀 Starting bot with Python 3.13 compatibility...")
            app.run_polling()
            
        except Exception as e2:
            print(f"❌ Alternative method also failed: {e2}")
            print("💡 Please use Python 3.11 for best compatibility")
            print("   Or contact support for Python 3.13 fixes")

if __name__ == '__main__':
    main()