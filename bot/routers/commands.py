from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="commands")


@router.message(Command("start"))
async def route_command_start(message: Message) -> None:
    await message.answer(text="Hello!")
