import asyncio

import sentry_sdk
from aiogram.utils.callback_answer import CallbackAnswerMiddleware
from sqlalchemy.ext.asyncio import async_sessionmaker

from bot import misc, routers
from bot.middlewares import DatabaseSessionMiddleware
from bot.middlewares.services_automate_initialization_middleware import ServicesAutomateInitialization
from bot.misc import dispatcher


async def main() -> None:
    await dispatcher.callback_query.middleware(CallbackAnswerMiddleware())
    await dispatcher.update.middleware(DatabaseSessionMiddleware(
        session_maker=async_sessionmaker(
            bind=misc.database_engine,
            expire_on_commit=True
        )
    ))
    await dispatcher.update.middleware(ServicesAutomateInitialization())
    routers.setup(dispatcher=dispatcher)
    if misc.settings.sentry_dsn:
        sentry_sdk.init(
            dsn=misc.settings.sentry_dsn,
            traces_sample_rate=1.0
        )
    await dispatcher.start_polling(misc.bot, allowed_updates=dispatcher.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(main())
