from typing import Union, Callable
from pyrogram.types import Message


class AppHelper:
    """
    Class with many helper methods
    """

    def roleplay_send(self, msg: Message, txt: str) -> None:
        if msg.reply_to_message is not None:
            msg.reply_to_message.reply(txt)
        else:
            msg.reply(txt)

        self.msg_delete(msg)

    def msg_delete(self, msg: Message) -> None:
        bot = self.get_chat_member(msg.chat.id, "me")

        if bot.can_delete_messages:
            msg.delete()

    def is_admin(self, msg: Message) -> bool:
        member = self.get_chat_member(msg.chat.id, msg.from_user.id)
        return member.status in ("creator", "administrator")
