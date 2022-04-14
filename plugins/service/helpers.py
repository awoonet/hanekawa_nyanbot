from typing import Callable
from client import make_keyboard


def reactions(t: Callable, chat) -> str:
    reactions = []
    for key, value in chat.categories.items():
        if value:
            reactions.append(t(f"config.keyboard.category.{key}"))
    return ", ".join(reactions)


def make_lookup_message(t: Callable, user) -> str:
    chat = user.chat

    text = t("config.message.lookup").format(
        switch_chat=t(f"config.keyboard.switch.{chat.get_switch()}"),
        switch_user=t(f"config.keyboard.switch.{user.get_switch()}"),
        lang=t(f"config.keyboard.lang.{chat.get_lang()}"),
        mood=t(f"config.keyboard.mood.{chat.get_mood()}"),
        reactions=reactions(t, chat),
    )
    return text


def config_message(app, msg, user, t):
    text = make_lookup_message(t, user)

    if app.is_admin(msg):
        kb = [
            ["switch.main", "user.main", "greeter.main"],
            ["lang.main", "mood.main", "category.main"],
        ]
    else:
        kb = [["user.main"]]

    return (text, kb)


def help_message(t):
    text = t("config.message.help.initial")
    kb = [["help.category", "help.roleplay", "help.greeter", "help.other"]]

    return (text, kb)


def send_keyboard(func):
    def wrapper(app, msg, user):
        t = app.service(user.chat)

        text, kb = func(app, msg, user, t)

        keyboard_func = lambda button: t(f"config.keyboard.{button}")
        kb = make_keyboard(keyboard_func, kb)

        msg.reply(text, reply_markup=kb)

    return wrapper
