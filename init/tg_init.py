from os import getenv as env

from init.client import Client


def tg_init() -> Client:
    telegram_credentials = dict(
        session_name=":memory:",
        api_id=env("API_ID"),
        api_hash=env("API_HASH"),
        bot_token=env("BOT_TOKEN"),
        plugins={"root": "plugins"},
    )

    app = Client(**telegram_credentials)

    print("TG initialized.")
    return app
