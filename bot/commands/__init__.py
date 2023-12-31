__all__ = ['register_user_commands', 'bot_commands']

from aiogram import Router
from aiogram.filters import Command
from aiogram.filters.command import CommandStart
from aiogram import F

from bot.commands.help import help_command, help_func
from bot.commands.start import start
from bot.commands.settings import setting_command, settings_callback
from bot.commands.callback_data_states import TestCallbackData


def register_user_commands(router: Router) -> None:
    # router.message.register(start, Command(command=['start']))
    router.message.register(start, CommandStart())
    router.message.register(help_command, Command(commands=['help']))
    router.message.register(start, F.text == 'Старт')
    router.message.register(help_func, F.text == 'Помощь')
    router.message.register(setting_command, Command(commands=['settings']))

    router.callback_query.register(settings_callback, TestCallbackData.filter())

