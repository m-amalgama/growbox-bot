import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from Bot_proto import router
from sensor_loop import loop

async def main():
    bot = Bot(token=settings.token)
    dp = Dispatcher()
    dp.include_router(router)
    await asyncio.gather(dp.start_polling(bot), loop(bot))

if __name__ == "__main__":
    asyncio.run(main()) 