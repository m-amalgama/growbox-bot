from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from core import status, targets
from bot import keyboards
from bot.keyboards import FanCB
from bot.states import TempSetup

router = Router()


@router.message(F.text == "menu")
async def menu_handler(msg:Message):
    await msg.answer("Настройка климата — выбери значение:", reply_markup=keyboards.targets)

@router.callback_query(F.data == "ask_temp")
async def wait_for_inp_temp(callback, state):
    await callback.answer()
    await callback.message.answer("Желательная температура:")
    await state.set_state(TempSetup.waiting)


@router.message(TempSetup.waiting) 
async def save_temp(temp_msg,state):   #первый аргумент любой второй по фреймворку
        try:
            targets.setpoint["target"] = int(temp_msg.text)
            await state.clear()
            await temp_msg.answer(f"цель : {temp_msg.text}°C")
        except ValueError:
            await temp_msg.answer(f"это должно быть целое число")

@router.callback_query(FanCB.filter())
async def fan_speed_handler(fan_callback, callback_data):
    value = callback_data.value
    await fan_callback.answer()
    await fan_callback.message.answer(f"максимальная мощность: {value}%")
    targets.setpoint["max_speed"] = value

@router.callback_query(F.data == "show_status")
async def status_handler(callback):
    await callback.answer()
    await callback.message.answer(f"показатели: {status.current}{targets.setpoint}")

@router.message(CommandStart())
async def start_handler(msg_start: Message):
    await msg_start.answer("GrowBot", reply_markup=keyboards.menu)