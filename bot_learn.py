import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import settings

router = Router()
ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Меню", callback_data="/menu")]
    ]
)
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
        [KeyboardButton(text="Кнопка 3")]
    ],
    resize_keyboard=True
)

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="услуга 1"), KeyboardButton(text="услуга 2")],
        [KeyboardButton(text="услуга")]
    ],
    resize_keyboard=True
)

back_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="назад", callback_data="/startkeys")]
    ]
)

@router.message(F.text == "Кнопка 1")
async def button_1_handler(msg_button_1:Message):
    await msg_button_1.answer("первая кнопка")
    

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("hello", reply_markup=kb)
    await msg_start.answer("Вот меню", reply_markup=ikb)

@router.callback_query(F.data == "/menu")
async def menu_handler(callback):
    await callback.answer("menu")
    await callback.message.answer("меню пакетов услуг", reply_markup=back_ikb)
    await callback.message.answer("описание пакетов услуг", reply_markup=menu_kb)

@router.callback_query(F.data == "/startkeys")
async def startkey_handler(callback):
    await callback.answer("возврат")
    await callback.message.answer("стартовое меню", reply_markup=kb)

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())