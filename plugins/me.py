from config import Client as app
from helpers import TextHelper as t
from helpers import SendHelper as s


@app.on_message(app.filters.command(["me"]) & ~app.filters.user("me"))
def me(_, msg):
    if "/me" in msg.text:
        txt = t.msg_text(msg)
        txt = txt.replace("/me", f"**✵{t.username(msg.from_user)}**")
        s.roleplay_send(txt, msg)
