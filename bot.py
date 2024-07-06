# imports ________________________________________________________

# asyncio
import asyncio
# logging
import logging
# sys
import sys

# aiogram
from aiogram import Bot, Dispatcher
# aiogram enums
from aiogram.enums import ParseMode

# tokens
from config import TOKEN

# bot settings ___________________________________________________

# bot
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)


# bot running ____________________________________________________

# main
async def main():
    # dispatcher
    from __init__ import setup_routers
    dp = Dispatcher()
    dp.include_router(router=setup_routers())
    await dp.start_polling(bot)


# run
if __name__ == '__main__':
    # logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    # asyncio run
    asyncio.run(main())
