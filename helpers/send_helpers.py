class SendHelper:
    @staticmethod
    def roleplay_send(text, msg):
        if msg.reply_to_message is not None:
            msg.reply_to_message.reply(text)
        else:
            msg.reply(text)
