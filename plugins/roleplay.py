from random import choice
from config import Client as app
from helpers import TextHelper as t

command = app.filters.command
commands = ["pat", "hug", "koos", "lapk", "lick", "jamk", "kiss"]


@app.on_message(command(["me"]))
def me(app, msg):
    txt = msg.text.html
    txt = txt.replace("/me", f"**✵{t.username(msg.from_user)}**")
    app.roleplay_send(msg, txt)


@app.on_message(app.filters.group & command(commands))
@app.with_db
def hnkw_roleplay(app, msg, chat):
    if msg.reply_to_message is not None:
        user = msg.reply_to_message.from_user
    else:
        user = app.get_users(choice(chat.users["on"]))

    username_1 = app.username_finder(msg.from_user)
    username_2 = app.username_finder(user)

    command = msg.command[0].replace(f"@{app.username}", "")
    txt = f"**✵{username_1}** {chat.service('roleplay', command)} **{username_2}✵**"

    app.roleplay_send(msg, txt)
