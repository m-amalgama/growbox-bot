from aiogram.fsm.state import StatesGroup, State

class TempSetup(StatesGroup):
    waiting = State()