import traceback
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

not_none = lambda x: x is not None


class AppHandleError:
    """
    Helper class for send messages if handled
    """

    def send_error_msg(self, msg: Message, error: Exception) -> None:
        to_chat = int(self.config_messages)
        error = str(error)
        txt = self.prepare_error_msg(msg, error)
        kb = self.prepare_error_keyboard(error)

        self.send_message(to_chat, txt, reply_markup=kb)
        self.forward_messages(to_chat, msg.chat.id, (msg.message_id,))

    def prepare_error_msg(self, msg: Message, error: Exception) -> str:
        return (
            "**Error occured in message:**\n\n"
            f"{self.prepare_info_msg(msg)}\n\n"
            f"**Error:** ```{str(error)}```\n"
            f"**Traceback:** ```{str(traceback.format_exc())}```"
        )

    def prepare_error_keyboard(self, error):
        error = str(error).replace(" ", "+")
        services = {
            "Google": "www.google",
            "StackOverflow": "stackoverflow",
            "StackExchange": "stackexchange",
        }

        row = [
            InlineKeyboardButton(
                text=title, url=f"https://{link}.com/search?q=python+{error}"
            )
            for title, link in services.items()
        ]

        return InlineKeyboardMarkup([row])

    def prepare_info_msg(self, msg: Message) -> str:
        user = msg.from_user

        txt = (
            f"**Bot:** __@{self.bot.username}__"
            f"\n**Chat:** __{msg.chat.title}__"
            f"\n**Chat ID:** __{msg.chat.id}__** / **__{msg.message_id}__"
            f"\n**User:** __{user.first_name} __"
            f" __{user.last_name if not_none(user.last_name) else ''}__"
            f" __(@{user.username if not_none(user.username) else ''})__"
            f"\n**User ID:** __{user.id}__"
            f"\n**Text:** {msg.text.html if not_none(msg.text) else ''}"
        )

        if not_none(msg.media) and msg.media:
            msg_types = {
                "Audio": msg.audio,
                "Document": msg.document,
                "Photo": msg.photo,
                "Sticker": msg.sticker,
                "Animation": msg.animation,
                "Video": msg.video,
                "Voice": msg.voice,
                "Video note": msg.video_note,
            }
            for name, msg_type in msg_types:
                if not_none(msg_type):
                    txt += f"\n**{name}**:_{msg_type.file_id}__"

            txt += f"\n**Caption**:__{msg.caption}__" if not_none(msg.caption) else ""

        return txt
