import pathlib

from aiogram import Bot, Dispatcher, executor
from aiogram.types import ParseMode

from config import load_config_from_file_path
from handlers import register_handlers
from middlewares import DependencyInjectMiddleware


def main() -> None:
    config_file_path = pathlib.Path(__file__).parent.parent / 'config.toml'
    config = load_config_from_file_path(config_file_path)

    bot = Bot(token=config.telegram_bot_token, parse_mode=ParseMode.HTML)
    dispatcher = Dispatcher(bot=bot)

    register_handlers(dispatcher)

    dependency_inject_middleware = DependencyInjectMiddleware(
        bot=bot,
        dispatcher=dispatcher,
    )
    dispatcher.setup_middleware(dependency_inject_middleware)

    executor.start_polling(
        dispatcher=dispatcher,
        skip_updates=True,
    )


if __name__ == '__main__':
    main()
