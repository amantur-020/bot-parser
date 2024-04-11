import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import basic

TOKEN = ''

dp = Dispatcher()


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def main() -> None:
    dp.include_router(basic.router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())