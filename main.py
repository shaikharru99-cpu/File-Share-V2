from bot import Bot
from pyrogram import idle
import asyncio

async def main():
    bot = Bot()
    await bot.start()
    await idle()
    await bot.stop()

if __name__ == "__main__":
    asyncio.run(main())

