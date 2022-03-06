from pyrogram.types import Message
from init import Client as app
from helpers.replier import Replaier


@app.on_message(app.filters.group & ~app.filters.edited)
@app.with_db
def func(app, msg: Message, user) -> None:
    Replaier(app, msg, user)
