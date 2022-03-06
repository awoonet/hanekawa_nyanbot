from os import getenv as env
from dotenv import load_dotenv

from init.client import Client
from init.tg_init import tg_init
from init.db_init import db_init
from helpers.load_yaml import load_yaml


def app_init() -> Client:
    load_dotenv()

    app = tg_init()
    app.db, app.chat, app.user = db_init()
    app.service_messages = load_yaml("service", "Loaded {counter} locales.")
    app.reactions = load_yaml("reactions", "Loaded {counter} reactions.")

    app.media_reactions_storage = env("MEDIA_REACTIONS_STORAGE")
    app.config_messages = env("CONFIG_MESSAGES")
    app.ignored_users = eval(env("IGNORED_USERS"))

    return app
