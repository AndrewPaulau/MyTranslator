from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from deep_translator import GoogleTranslator

# Токен твоего бота
TOKEN = '7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg'

# Функция для начала работы с ботом
async def start(update: Update, context):
    await update.message.reply_text("Привет! Я могу перевести текст. Просто напиши, что перевести!")

# Функция перевода
async def translate(update: Update, context):
    user_input = update.message.text  # Получаем текст от пользователя

    # Проверка, чтобы не переводить команду start или пустые сообщения
    if user_input.lower() == "/start" or not user_input:
        return

    try:
        # Переводим на русский
        translated = GoogleTranslator(source='auto', target='ru').translate(user_input)
        await update.message.reply(f"Переведено: {translated}")
    except Exception as e:
        await update.message.reply(f"Ошибка при переводе: {e}")

# Функция для обработки команд
def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик текстовых сообщений
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, translate))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()



  

