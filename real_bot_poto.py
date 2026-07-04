import asyncio
from aiogram import F
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from config import settings

router = Router()

class TempCB(CallbackData, prefix="temp"):
    value: int

class VenCB(CallbackData, prefix="ven"):
    value: int

menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="menu")]
    ]
)

temp_cntrl_ikb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="24",callback_data=TempCB(value=24).pack()),
            InlineKeyboardButton(text="26",callback_data=TempCB(value=26).pack()),
            InlineKeyboardButton(text="28",callback_data=TempCB(value=28).pack())
        ],
        [
            InlineKeyboardButton(text="40",callback_data=VenCB(value=40).pack()),
            InlineKeyboardButton(text="60",callback_data=VenCB(value=60).pack()),
            InlineKeyboardButton(text="80",callback_data=VenCB(value=80).pack())
        ]
    ]
)

@router.message(F.text == "menu")
async def menu_handler(msg:Message):
    await msg.answer("Настройка климата — выбери значение:", reply_markup=temp_cntrl_ikb)

@router.callback_query(TempCB.filter())
async def temp_hendler(temp, callback_data: TempCB):
    value = callback_data.value
    await temp.answer()
    await temp.message.answer(f"цель : {value}С°")

@router.callback_query(VenCB.filter())
async def ven_hendler(ven, callback_data: VenCB):
    value = callback_data.value
    await ven.answer()
    await ven.message.answer(f"максимальная мощность: {value}%")

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("GrowBot", reply_markup=menu_kb)

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())