from pyrogram.types import Message, CallbackQuery
from init import Client as app
from helpers.inline_keyboard import make_keyboard
from helpers.text_helpers import TextHelper as th


@app.on_message(app.filters.command(["config"]))
@app.with_db
def send_keyboard(app, msg: Message, user) -> None:
    t = app.service(user.chat)

    text = th.make_lookup_message(t, user)

    if app.is_admin(msg):
        kb = [["switch.main", "user.main"], ["lang.main", "mood.main", "category.main"]]
    else:
        kb = [["user.main"]]

    msg.reply(text, reply_markup=make_keyboard(t, kb))


@app.on_callback_query(group=10)
@app.with_db
def parse_query(app, query: CallbackQuery, user):
    chat = user.chat
    t = app.service(chat)
    msg = query.message
    data = query.data.split(".")

    kb = None

    if data[0] == "user":
        user.change_switch()
        present_user_state = t(f"config.keyboard.switch.{user.get_switch()}")
        text = t(f"config.message.changed.user").format(answer=present_user_state)

    elif app.is_admin(msg):
        match data[0]:
            case "switch":
                chat.change_switch()
                present_switch = t(f"config.keyboard.switch.{chat.get_switch()}")
                text = t(f"config.message.changed.switch").format(answer=present_switch)

            case "lang":
                if data[1] == "main":
                    present_lang = t(f"config.keyboard.lang.{chat.get_lang()}")
                    text = t("config.message.now.lang").format(answer=present_lang)
                    kb = [["lang.ru", "lang.en", "lang.ua"]]

                elif data[1] in ("ru", "en", "ua"):
                    chat.set_lang(data[1])
                    present_lang = t(f"config.keyboard.lang.{chat.get_lang()}")
                    text = t("config.message.changed.lang").format(answer=present_lang)

            case "mood":
                if data[1] == "main":
                    present_mood = t(f"config.keyboard.mood.{chat.get_mood()}")
                    text = t("config.message.now.mood").format(answer=present_mood)
                    kb = [["mood.nyan", "mood.lewd", "mood.angr", "mood.scar"]]

                elif data[1] in ("nyan", "lewd", "angr", "scar"):
                    chat.set_mood(data[1])
                    present_mood = t(f"config.keyboard.mood.{chat.get_mood()}")
                    text = t("config.message.changed.mood").format(answer=present_mood)

            case "category":
                if data[1] == "main":
                    text = t("config.message.now.category").format(
                        answer=th.reactions(t, chat)
                    )
                    kb = [[f"category.{i}" for i in chat.categories.keys()]]

                elif data[1] in chat.categories.keys():
                    chat.change_category(data[1])
                    format = dict(
                        category=t(f"config.keyboard.category.{data[1]}"),
                        answer=t(
                            f"config.keyboard.switch.{chat.get_category(data[1])}"
                        ),
                    )
                    text = t("config.message.changed.category").format(**format)
            case _:
                text = t("config.message.error").format(query=query.data)
    else:
        text = t("config.message.no_rights")

    if kb is not None:
        kb = make_keyboard(t, kb)

    query.message.edit(text, reply_markup=kb)
