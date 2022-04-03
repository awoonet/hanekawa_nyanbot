from pyrogram.types import Message
from app_init import Client as app
from plugins.service.helpers import send_keyboard, config_message, help_message


@app.on_message(app.filters.command(["config"]))
@app.with_db
@send_keyboard
def send_config_keyboard(app, msg: Message, user, t) -> None:
    return config_message(app, msg, user, t)


@app.on_message(app.filters.command(["help"]))
@app.with_db
@send_keyboard
def send_help_keyboard(_, __: Message, ___, t) -> None:
    return help_message(t)
