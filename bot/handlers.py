from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.state import StatesGroup, State
from core.targets import setpoint
from core.status import current

router = Router()

class Config(StatesGroup):
    waiting_temp = State()

class FanCB(CallbackData, prefix="fan"):
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
            InlineKeyboardButton(text="40",callback_data=FanCB(value=40).pack()),
            InlineKeyboardButton(text="60",callback_data=FanCB(value=60).pack()),
            InlineKeyboardButton(text="80",callback_data=FanCB(value=80).pack()),
            InlineKeyboardButton(text="100",callback_data=FanCB(value=100).pack())
        ],
        [
            InlineKeyboardButton(text="status",callback_data="show_status")
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
            setpoint["target"] = int(temp.text)
            await state.clear()
            await temp.answer(f"цель : {temp.text}°C")
        except ValueError:
            await temp.answer(f"это должно быть целое число")

@router.callback_query(FanCB.filter())
async def fan_speed_handler(callback, callback_data):
    value = callback_data.value
    await callback.answer()
    await callback.message.answer(f"максимальная мощность: {value}%")
    setpoint["max_speed"] = value

@router.callback_query(F.data == "show_status")
async def status_hendler(callback):
    await callback.answer()
    await callback.message.answer(f"показатели: {current}{setpoint}")

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("GrowBot", reply_markup=menu_kb)