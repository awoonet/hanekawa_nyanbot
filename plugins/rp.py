from config import Client as app
from random import choice
from helpers import TextHelper as t
from helpers import SendHelper as s

commands = ["pat", "hug", "koos", "lapk", "lick", "jamk", "kiss"]


@app.on_message(app.filters.command(commands) & app.filters.group)
@app.with_db
def hnkw_roleplay(_, msg, user):

    breakpoint()
    user_initiator = t.username(msg.from_user)

    if msg.reply_to_message is not None:
        user_recepient = t.username(msg.reply_to_message.from_user)
    else:
        user_recepient = choice(user.chat.users).name

    command = msg.command[0]  # .replace(f"@{app.username}", "")
    txt = f"**✵{user_initiator}** {command} **{user_recepient}✵**"

    # {chat.service('roleplay', command)}

    s.roleplay_send(txt, msg)
