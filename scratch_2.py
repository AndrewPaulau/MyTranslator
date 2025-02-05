import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Создаем экземпляр Translator
translator = Translator()

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот-переводчик. Отправь мне текст для перевода.')

# Функция для обработки текстовых сообщений
def translate(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    try:
        # Переводим текст на русский (можно изменить на нужный язык)
        translated = translator.translate(text, dest='ru')
        update.message.reply_text(f'Перевод: {translated.text}')
    except Exception as e:
        update.message.reply_text('Произошла ошибка при переводе.')

# Основная функция
def main() -> None:
    # Замените 'YOUR_TOKEN' на токен вашего бота
    updater = Updater("7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд и сообщений
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы бота
    updater.idle()

if __name__ == '__main__':
    main()
