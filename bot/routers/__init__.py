from aiogram import Dispatcher

from bot.routers import commands


def setup(dispatcher: Dispatcher) -> None:
    dispatcher.include_router(commands.router)
