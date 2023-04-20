import asyncio

import sentry_sdk
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from bot import routers
from bot.middlewares import DatabaseSessionMiddleware
from bot.middlewares.services_automate_initialization_middleware import ServicesAutomateInitialization
from bot.settings import Settings


async def main() -> None:
    settings = Settings()
    bot = Bot(token=settings.bot_token, parse_mode="HTML")
    dispatcher = Dispatcher(storage=MemoryStorage() if settings.redis_dsn is None else RedisStorage.from_url(
        url=settings.redis_dsn
    ))
    database_engine = create_async_engine(
        url=settings.database_dsn,
        echo=True
    )
    dispatcher.callback_query.middleware(CallbackAnswerMiddleware())
    dispatcher.update.middleware(DatabaseSessionMiddleware(
        session_maker=async_sessionmaker(
            bind=database_engine,
            expire_on_commit=True
        )
    ))
    dispatcher.update.middleware(ServicesAutomateInitialization())
    routers.setup(dispatcher=dispatcher)
    if settings.sentry_dsn:
        sentry_sdk.init(
            dsn=settings.sentry_dsn,
            traces_sample_rate=1.0
        )
    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
