from pyrogram import Client, filters, idle
from db.helpers import ClientDBHelpers
from helpers.app_helpers import AppHelper


class Client(Client, AppHelper, ClientDBHelpers):
    filters = filters

    media_reactions_storage = -1001157282357
    config_messages = -1001328058005

    def run(self):
        self.start()
        self.init_bot_info()
        self.send_awaking_msg()

        idle()

        self.stop()
