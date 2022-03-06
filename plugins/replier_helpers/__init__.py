import re

from client.helper_text import TextHelper as t
from plugins.replier_helpers.text_formatter import TextFormatter
from plugins.replier_helpers.message_sender import MessageSender

from static.triggers import triggers


class Replaier(TextFormatter, MessageSender):
    def __init__(self, app, msg, user):
        self.app = app
        self.msg = msg
        self.user = user
        self.chat = user.chat

        user_not_ignored = msg.from_user.id not in app.ignored_users

        if user.switch and user.chat.switch and user_not_ignored:
            self.parse_message()

    def parse_message(self):
        text = t.msg_text(self.msg).lower()
        mood = self.chat.get_mood()
        reactions = self.app.reactions

        for category, trigger, regex in triggers:
            if self.chat.categories[category]:
                if re.search(regex, text):
                    self.reply(reactions[trigger][mood])
