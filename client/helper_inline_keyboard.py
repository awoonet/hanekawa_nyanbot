from typing import Callable
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def make_keyboard(func: Callable, layout: list) -> InlineKeyboardMarkup:
    """
    Function to make an inline keyboard for telegram bot.
    Args:
        func (Callable): give function for i18n (should take str and return str with button text)
        layout (list): should be list of lists [[], []]

    Returns:
        InlineKeyboardMarkup
    """
    keyboard = []
    for row in layout:

        new_row = []
        for button in row:
            text = func(button)
            button = InlineKeyboardButton(text=text, callback_data=button)
            new_row.append(button)

        keyboard.append(new_row)
    return InlineKeyboardMarkup(keyboard)
