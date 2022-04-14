from pyrogram.types import CallbackQuery
from app_init import Client as app
from client import make_keyboard
from plugins.service.helpers import config_message, help_message


@app.on_callback_query()
@app.with_db
def parse_query(app, query: CallbackQuery, user):
    chat = user.chat
    t = app.service(chat)
    msg = query.message

    def switch(_):
        chat.change_switch()
        switch = chat.get_switch()
        present_switch = t(f"config.keyboard.switch.{switch}")
        text = t(f"config.message.changed.switch").format(answer=present_switch)
        kb = [["config.back"]]
        return (text, kb)

    def user_change():
        user.change_switch()
        switch = user.get_switch()
        present_user_state = t(f"config.keyboard.switch.{switch}")
        text = t(f"config.message.changed.user").format(answer=present_user_state)
        kb = [["config.back"]]
        return (text, kb)

    def lang(option):
        if option == "main":
            lang = chat.get_lang()
            present_lang = t(f"config.keyboard.lang.{lang}")
            action = "now"
            kb = [["lang.ru", "lang.en", "lang.ua"], ["config.back"]]
        elif option in ("ru", "en", "ua"):
            chat.set_lang(option)
            lang = chat.get_lang()
            present_lang = t(f"config.keyboard.lang.{lang}")
            action = "changed"
            kb = [["lang.main"], ["config.main"]]

        text = t(f"config.message.{action}.lang").format(answer=present_lang)
        return (text, kb)

    def mood(option):
        mood = chat.get_mood()
        present_mood = t(f"config.keyboard.mood.{mood}")

        if option == "main":
            action = "now"
            kb = [["mood.nyan", "mood.lewd", "mood.angr", "mood.scar"], ["config.back"]]
        elif option in ("nyan", "lewd", "angr", "scar"):
            chat.set_mood(option)
            action = "changed"
            kb = [["mood.main"], ["config.back"]]

        text = t(f"config.message.{action}.mood").format(answer=present_mood)
        return (text, kb)

    def category(option):
        if option == "main":
            action = "now"
            categories = chat.i18n_categories(t)
            format = dict(answer=categories)
            kb = [[f"category.{i}" for i in chat.categories.keys()], ["config.back"]]
        elif option in chat.categories.keys():
            chat.change_category(option)
            category = chat.get_category(option)
            action = "changed"
            format = dict(
                category=t(f"config.keyboard.category.{option}"),
                answer=t(f"config.keyboard.switch.{category}"),
            )
            kb = [["category.main"], ["config.main"]]

        text = t(f"config.message.{action}.category").format(**format)
        return (text, kb)

    def help(option):
        help_types = ["category", "roleplay", "other", "greeter"]

        if option == "main":
            return help_message(t)
        elif option in help_types:
            text = t(f"config.message.help.{option}")
            kb = [[f"help.{i}" for i in help_types if i != option], ["help.main"]]

        return (text, kb)

    def error_query(_):
        text = t("config.errors.query").format(query=query.data)
        kb = [["config.back"]]
        return (text, kb)

    def error_no_rights():
        text = t("config.errors.no_rights")
        kb = [["config.back"]]
        return (text, kb)

    def guess_option():
        data = query.data.split(".")

        if data[0] == "user":
            return user_change()
        elif data[0] == "config":
            return config_message(app, msg, user, t)
        elif app.is_admin(msg):
            answers = {
                "switch": switch,
                "lang": lang,
                "mood": mood,
                "category": category,
                "help": help,
            }

            return answers.get(data[0], error_query)(data[1])
        else:
            return error_no_rights()

    def configure():
        text, kb = guess_option()

        if kb is not None:
            keyboard_func = lambda button: t(f"config.keyboard.{button}")
            kb = make_keyboard(keyboard_func, kb)

        query.message.edit(text, reply_markup=kb)

    configure()
