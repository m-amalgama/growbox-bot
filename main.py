import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from bot.handlers import router
from core.cycle import run

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await asyncio.gather(dp.start_polling(bot), run(bot))

if __name__ == "__main__":
    asyncio.run(main()) 