class SendHelper:
    @classmethod
    def roleplay_send(cls, app, msg, txt):
        if msg.reply_to_message is not None:
            msg.reply_to_message.reply(txt)
        else:
            msg.reply(txt)

        cls.delete(app, msg)

    @staticmethod
    def delete(app, msg):
        bot = app.get_chat_member(msg.chat.id, "me")

        if bot.can_delete_messages:
            msg.delete()
