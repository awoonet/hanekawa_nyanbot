from pyrogram.types import Message
from app_init import Client as app
from client.helper_text import TextHelper as th


@app.on_message(app.filters.group & app.filters.new_chat_members)
@app.with_db
def greet(app, msg: Message, user) -> None:
    chat = user.chat
    if chat.greeter["switch"]:
        # Build the new members list (with mentions) by using their first_name
        new_members = [u.mention for u in msg.new_chat_members]

        # Take greeter from chat
        greeter = chat.get_greeter()

        # If it "default" take greeter from i18n
        if greeter.lower() == "default":
            t = app.service(chat)
            greeter = t("greeter")

        # Send greeter to every new chat member
        for user in new_members:
            text = greeter.format(user=th.username(user), title=msg.chat.title)
            msg.reply(text)


@app.on_message(app.filters.group & app.filters.command(["greeter"]))
@app.with_db
def set_greet(app, msg: Message, user) -> None:
    chat = user.chat
    t = app.service(chat)

    text = t("config.errors.no_rights")
    if app.is_admin(msg):
        new_greeter = msg.text.html.replace(msg.command[0], "")

        text = t("config.error.greeter.too_long")
        if chat.set_greeter(new_greeter):
            text = t("config.message.changed.greeter").format(greeter=new_greeter)

    msg.reply(text)
