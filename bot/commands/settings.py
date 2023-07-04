from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup


async def setting_command(message: types.Message):
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text='Яндекс',
        url='yandex.ru'
    )
    # settings_markup.button(
    #     text='Pay',
    #     pay=True
    # )
    await message.answer('Настройки', reply_markup=settings_markup.as_markup(resize_keyboard=True))
