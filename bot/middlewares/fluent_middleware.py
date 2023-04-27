from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update
from fluentogram import TranslatorHub


class FluentMiddleware(BaseMiddleware):
    """
    Middleware is intended for all updates from which you can identify the user,
    so far it is only a standard CallbackQuery/Message.
    You can get the user's language from your database by changing the logic a bit.
    """

    def __init__(
            self,
            translator_hub: TranslatorHub
    ) -> None:
        self.translator_hub = translator_hub

    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: Dict[str, Any]
    ) -> Any:
        if (current_event := event.callback_query or event.message) is not None:
            language_code = current_event.from_user.language_code or self.translator_hub.root_locale
            data["i18n"] = self.translator_hub.get_translator_by_locale(locale=language_code)
        return await handler(event, data)
