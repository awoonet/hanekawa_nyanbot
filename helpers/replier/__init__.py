import re

from helpers import TextHelper as t
from helpers.replier.text_formatter import TextFormatter
from helpers.replier.message_sender import MessageSender

from static.triggers import triggers


class Replaier(TextFormatter, MessageSender):
    def __init__(self, app, msg, user):
        self.app = app
        self.msg = msg
        self.user = user
        self.chat = user.chat

        if user.switch:
            self.parse_message()

    def parse_message(self):
        text = t.msg_text(self.msg).lower()
        mood = self.chat.get_mood()
        reactions = self.app.reactions

        for category, trigger, regex in triggers:
            if getattr(self.chat, category):
                if re.search(regex, text):
                    self.reply(reactions[trigger][mood])
