import asyncio

# Modern Python 3.10+ event loop workaround
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

async def main():
    # Deferred imports to ensure they run inside the loop
    from bot import Bot
    from pyrogram import idle

    bot = Bot()
    await bot.start()
    await idle()
    await bot.stop()

if __name__ == "__main__":
    loop.run_until_complete(main())
