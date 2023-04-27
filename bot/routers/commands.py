import typing

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from fluentogram import TranslatorRunner

if typing.TYPE_CHECKING:
    from bot.stub import TranslatorRunner

router = Router(name="commands")


@router.message(Command("start"))
async def route_command_start(message: Message, i18n: TranslatorRunner) -> None:
    await message.answer(text=i18n.start.hello(username=message.from_user.username or "anonymous"))
