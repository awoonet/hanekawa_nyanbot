from pyrogram.types import Message
from app_init import Client as app
from plugins.replier_helpers import Replaier


@app.on_message(app.filters.group, group=0)
@app.with_db
def func(app, msg: Message, user) -> None:
    Replaier(app, msg, user)
