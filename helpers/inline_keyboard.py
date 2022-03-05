from typing import Callable
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def make_keyboard(t: Callable, layout: list) -> InlineKeyboardMarkup:
    keyboard = []
    for row in layout:

        new_row = []
        for button in row:
            text = t(f"config.keyboard.{button}")
            button = InlineKeyboardButton(text=text, callback_data=button)
            new_row.append(button)

        keyboard.append(new_row)
    return InlineKeyboardMarkup(keyboard)
