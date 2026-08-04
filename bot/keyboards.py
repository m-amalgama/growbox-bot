from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class FanCB(CallbackData, prefix="fan"):
    value: int

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="menu")]
    ]
)

targets = InlineKeyboardMarkup(
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