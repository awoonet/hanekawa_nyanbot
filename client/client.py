from os import getenv as env
from dotenv import load_dotenv
from pyrogram import Client, filters, idle
from client.app_helpers import AppHelper
from client.msg_awaking import AppAwaking
from client.msg_error import AppHandleError


class Client(Client, AppHelper, AppAwaking, AppHandleError):
    """
    Pyrogram client mixin

    Args:
        Client: pyrogram client
        AppHelper: general helpers for client
        AppAwaking: mixin for app awaking message
        AppHandleError: mixin for handling if error happens
    """

    filters = filters

    def __init__(self):

        load_dotenv()
        telegram_credentials = dict(
            session_name=f"session/{env('BOT_NAME')}",
            api_id=env("API_ID"),
            api_hash=env("API_HASH"),
            bot_token=env("BOT_TOKEN"),
            plugins={"root": "plugins"},
        )

        super().__init__(**telegram_credentials)

        print("TG initialized.")

    def run(self):
        self.start()
        self.init_bot_info()
        self.send_awaking_msg()

        idle()

        self.stop()
