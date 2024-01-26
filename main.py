import logging
import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from bot.handlers.user_handlers import user_router

load_dotenv()

TOKEN = getenv("TOKEN")
API = getenv("API")
API2 = getenv("API2")

print(f"Bot token: {TOKEN}")
print(f"API: {API}")
print(f"API2: {API2}") 

# routers
def register_routers(dp: Dispatcher) -> None:
    dp.include_router(user_router)

async def main() -> None:
    dp = Dispatcher()
    register_routers(dp)

    #start bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

    # Keep the bot running indefinitely
    try:
        while True:
            await asyncio.sleep(60)
    except KeyboardInterrupt:
        print('Bot is stopping...')
    finally:
        print('Bot has stopped')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())