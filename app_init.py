from os import getenv as env
from dotenv import load_dotenv

from client import Client, load_yaml
from db import db_init
from db.helpers import ClientDBHelpers

load_dotenv()


class Client(Client, ClientDBHelpers):
    service_messages = load_yaml("service", "Loaded {counter} locales.")
    reactions = load_yaml("reactions", "Loaded {counter} reactions.")

    media_reactions_storage = env("MEDIA_REACTIONS_STORAGE")
    config_messages = env("CONFIG_MESSAGES")
    ignored_users = eval(env("IGNORED_USERS"))


def app_init() -> Client:

    app = Client()
    app.db, app.chat, app.user = db_init()

    return app
