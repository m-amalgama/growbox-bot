import asyncio
from aiogram import Bot, Dispatcher, Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import settings

router = Router()

@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("hello")

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())