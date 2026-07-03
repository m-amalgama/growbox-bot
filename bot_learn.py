import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import settings

router = Router()
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
        [KeyboardButton(text="Кнопка 3")]
    ],
    resize_keyboard=True
)

@router.message(F.text == "Кнопка 1")
async def button_1_handler(msg_button_1:Message):
    await msg_button_1.answer("первая кнопка")
    

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("hello", reply_markup=kb)

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())