from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage
from sqlalchemy.ext.asyncio import create_async_engine

from bot.models.settings import Settings

settings = Settings()
bot = Bot(token=settings.bot_token, parse_mode="HTML")
dispatcher = Dispatcher(storage=MemoryStorage() if settings.redis_dsn is None else RedisStorage.from_url(
    url=settings.redis_dsn
))
database_engine = create_async_engine(
    url=settings.database_dsn,
    echo=True
)
