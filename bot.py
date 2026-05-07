from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
import asyncio

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

# КНОПКИ
start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Почати тест")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Привіт! 👋\n"
        "Я бот для профорієнтації студентів.\n\n"
        "Натисни кнопку нижче, щоб почати тест.",
        reply_markup=start_keyboard
    )


@dp.message(F.text == "Почати тест")
async def start_test(message: Message):
    await message.answer(
        "Перше питання:\n\n"
        "Що тобі подобається найбільше?"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())