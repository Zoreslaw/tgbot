from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Включаем логирование, чтобы видеть ошибки
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция обработки команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш тестовый бот.')

# Эхо обработчик сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

# Ошибка обработчика
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    # Создайте экземпляр Updater с вашим токеном
    TOKEN = '7183050375:AAHgSy6Nl1M0W-HlLBYIyzkSu_vuD7mIXUE'
    updater = Updater(TOKEN, use_context=True)

    # Получите диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Разные обработчики команд
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Лог всех ошибок
    dp.add_error_handler(error)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()