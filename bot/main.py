import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from aiogram import F
import asyncio

BOT_TOKEN = "7736504919:AAF_45NupGTRjQ6FDIFKKk9kBPiMgHiddIc"  # Замените на ваш токен

# Создаем экземпляр бота
bot = Bot(token=BOT_TOKEN)
# Создаем экземпляр диспетчера
dp = Dispatcher()

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Обработчик команды /start
@dp.message(F.text == "/start")
async def start_handler(message: types.Message):
    web_app_url = "https://puff-tracker-web.vercel.app/"

    # Кнопка для открытия веб-приложения
    web_button = KeyboardButton(
        text="Открыть трекер",
        web_app=WebAppInfo(url=web_app_url)
    )

    # Создаем клавиатуру с кнопкой
    keyboard = ReplyKeyboardMarkup(keyboard=[[web_button]], resize_keyboard=True)

    await message.answer("Жми на кнопку ниже, чтобы открыть мини-приложение:", reply_markup=keyboard)

# Запуск бота
async def main():
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
