from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from sqlalchemy.ext.asyncio import async_sessionmaker


class DatabaseSessionMiddleware(BaseMiddleware):
    def __init__(self, session_maker: async_sessionmaker) -> None:
        super().__init__()
        self._session_maker = session_maker

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        async with self._session_maker() as session:
            data["session"] = session
            return await handler(event, data)
