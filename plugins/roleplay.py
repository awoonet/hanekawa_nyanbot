import re
from pyrogram.types import Message
from app_init import Client as app
from client.helper_text import TextHelper as th

commands = ["pat", "hug", "koos", "lapk", "lick", "jamk", "kiss"]


@app.on_message(app.filters.command(["me"]), group=999)
@app.with_db
def me(app, msg: Message, user) -> None:
    txt = th.msg_text(msg)
    txt = txt.replace("/me", f"**✵{th.username(msg.from_user)}**")
    app.roleplay_send(msg, txt)


@app.on_message(app.filters.command(commands) & app.filters.group, group=999)
@app.with_db
def hnkw_roleplay(app, msg: Message, user) -> None:
    t = app.service(user.chat)
    user_initiator = th.username(msg.from_user)

    match = re.search(r"^@(\w+)$", msg.command[-1])
    if match:
        user_recepient = match.group(0)
    elif msg.reply_to_message is not None:
        user_recepient = th.username(msg.reply_to_message.from_user)
    else:
        user_recepient = user.chat.users.random(limit=1)[0].name

    reaction = t(f"roleplay.{msg.command[0]}")
    txt = f"**✵{user_initiator}** {reaction} **{user_recepient}✵**"

    app.roleplay_send(msg, txt)
