import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator
import filetype

# Включаем логирование
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Инициализируем переводчик
translator = Translator()

# Функция для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я бот-переводчик. Отправь мне текст, и я переведу его на английский.')

# Функция для обработки сообщений
def translate(update: Update, context: CallbackContext) -> None:
    text = update.message.text
    translated = translator.translate(text, dest='en').text
    update.message.reply_text(translated)

def main() -> None:
    # Вставьте сюда ваш токен
    token = '7967863846:AAEjNCChkcVE-55UewWwdX3JfzeSHqw-_sg'

    # Создаем Updater и передаем ему токен
    updater = Updater(token)

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Регистрируем обработчики команд и сообщений
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate))

    # Запускаем бота
    updater.start_polling()

    # Ожидаем завершения работы
    updater.idle()

if __name__ == '__main__':
    main()
