from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import StatesGroup, State
from Default import default

router = Router()

class Config(StatesGroup):
    waiting_temp = State()

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
            InlineKeyboardButton(text="temperature",callback_data="ask_temp")
        ],
        [
            InlineKeyboardButton(text="40",callback_data=VenCB(value=40).pack()),
            InlineKeyboardButton(text="60",callback_data=VenCB(value=60).pack()),
            InlineKeyboardButton(text="80",callback_data=VenCB(value=80).pack()),
            InlineKeyboardButton(text="100",callback_data=VenCB(value=100).pack())
        ]
    ]
)

@router.message(F.text == "menu")
async def menu_handler(msg:Message):
    await msg.answer("Настройка климата — выбери значение:", reply_markup=temp_cntrl_ikb)

@router.callback_query(F.data == "ask_temp")
async def wait_for_inp_temp(callback, state):
    await callback.answer()
    await callback.message.answer("Желательная температура:")
    await state.set_state(Config.waiting_temp)


@router.message(Config.waiting_temp) 
async def read_temp(temp,state):   #первый аргумент любой второй по фреймворку
        try:
            default["target"] = int(temp.text)
            await state.clear()
            await temp.answer(f"цель : {temp.text}°C")
        except ValueError:
            await temp.answer(f"это должно быть целое число")

@router.callback_query(VenCB.filter())
async def ven_hendler(ven, callback_data):
    value = callback_data.value
    await ven.answer()
    await ven.message.answer(f"максимальная мощность: {value}%")
    default["max_speed"] = value

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("GrowBot", reply_markup=menu_kb)