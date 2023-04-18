from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject


class ServicesAutomateInitialization(BaseMiddleware):
    """
    This middleware depends on DatabaseSessionMiddleware
    """

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]
    ) -> Any:
        """
        It is used to conveniently obtain services without incidental initialization in the code itself:
            @router.message(Command("start"))
            async def route_command_start(message: Message, user_service: UserService) -> None:
                ...
        """

        if "session" in data:
            ...
        return await handler(event, data)
