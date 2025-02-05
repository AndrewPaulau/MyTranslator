import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Твой токен
TOKEN = '7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg'

# Функция для старта бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Команда /start вызвана")
    await show_language_menu(update, context)

# Функция для отображения меню выбора языка
async def show_language_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Отображение меню выбора языка")
    keyboard = [
        [KeyboardButton("Русский"), KeyboardButton("Английский")],
        [KeyboardButton("Китайский"), KeyboardButton("Украинский"), KeyboardButton("Белорусский")],
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=False)
    await update.message.reply_text('Выберите язык для перевода:', reply_markup=reply_markup)

# Обработка выбора языка
async def handle_language_selection(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Обработка выбора языка")
    user_message = update.message.text
    supported_languages = {
        "Русский": 'ru',
        "Английский": 'en',
        "Китайский": 'zh-CN',
        "Украинский": 'uk',
        "Белорусский": 'be'
    }

    if user_message in supported_languages:
        context.user_data['language'] = supported_languages[user_message]
        await update.message.reply_text(f"Выбран язык: {user_message}. Теперь отправьте текст для перевода.")
    elif 'language' in context.user_data:
        await translate_message(update, context)  # Вызов перевода, если язык уже выбран
    else:
        await update.message.reply_text("Пожалуйста, выберите язык из меню.")

# Функция для обработки текстовых сообщений
async def translate_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    logging.info("Перевод сообщения")
    if 'language' in context.user_data:
        target_language = context.user_data['language']
        text = update.message.text
        translated = GoogleTranslator(source='auto', target=target_language).translate(text)
        await update.message.reply_text(translated)
    else:
        await update.message.reply_text("Сначала выберите язык, используя /start.")

def main() -> None:
    # Создаем приложение
    application = ApplicationBuilder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_language_selection))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()