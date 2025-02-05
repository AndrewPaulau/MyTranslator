from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters
from deep_translator import GoogleTranslator

# Токен Telegram-бота
TOKEN = '7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg'

# Список доступных языков
LANGUAGES = {
    'en': 'Английский',
    'ru': 'Русский',
    'uk': 'Украинский',
    'be': 'Белорусский'
}

# Функция старта бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton(name, callback_data=code)] for code, name in LANGUAGES.items()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет! Выбери язык для перевода:', reply_markup=reply_markup)

# Обработка выбора языка
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    context.user_data['target_lang'] = query.data
    await query.edit_message_text(f'Выбран язык: {LANGUAGES[query.data]}. Теперь отправь текст для перевода.')

# Обработка текста для перевода
async def translate_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    target_lang = context.user_data.get('target_lang')
    if not target_lang:
        await update.message.reply_text('Пожалуйста, сначала выбери язык с помощью команды /start.')
        return

    text = update.message.text
    try:
        translated_text = GoogleTranslator(source='auto', target=target_lang).translate(text)
        await update.message.reply_text(f'Перевод на {LANGUAGES[target_lang]}:\n{translated_text}')
    except Exception as e:
        await update.message.reply_text(f'Ошибка перевода: {e}')

# Основная функция запуска бота
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate_text))

    print("Бот запущен...")
    app.run_polling()
