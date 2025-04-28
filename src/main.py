import asyncio

from aiogram import Dispatcher
from dishka.integrations.aiogram import setup_dishka
from dishka import make_async_container

from bootstrap.bot_factory import create_bot
from bootstrap.config.settings import Settings


async def main():
    settings = Settings.from_toml()

    bot = create_bot(settings.telegram_bot.token)
    dispatcher = Dispatcher()

    container = make_async_container(context={Settings: settings})

    setup_dishka(router=dispatcher, container=container, auto_inject=True)

    if settings.telegram_bot.skip_updates:
        await bot.delete_webhook(drop_pending_updates=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
