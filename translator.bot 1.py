from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from deep_translator import GoogleTranslator

# Ваш токен от бота
TOKEN = '7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg'  # Замените на свой токен

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я могу перевести текст. Просто напиши, что перевести!")

# Функция для перевода текста
async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text

    try:
        # Перевод текста на русский язык
        translated = GoogleTranslator(source='auto', target='ru').translate(user_input)
        await update.message.reply_text(f"Переведено: {translated}")
    except Exception as e:
        await update.message.reply_text(f"Ошибка при переводе: {e}")

# Основная функция для запуска бота
def main():
    # Создание приложения
    application = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()




  

