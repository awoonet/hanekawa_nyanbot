from pyrogram import Client, filters, idle
from db.helpers import ClientDBHelpers
from helpers.app_helpers import AppHelper


class Client(Client, AppHelper, ClientDBHelpers):
    filters = filters

    def run(self):
        self.start()
        self.init_bot_info()
        self.send_awaking_msg()

        idle()

        self.stop()
