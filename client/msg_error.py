import traceback

not_none = lambda x: x is not None

class AppHandleError:
    """
    Helper class for send messages if handled
    """
    def send_error_msg(self, msg, error) -> None:
        txt = self.prepare_error_msg(msg, error)

        self.send_message(int(self.config_messages), txt)
        self.forward_messages(int(self.config_messages), msg.chat.id, (msg.message_id,))

    def prepare_error_msg(self, msg, error) -> str:
        return (
            "**Error occured in message:**\n\n"
            f"{self.prepare_info_msg(msg)}\n\n"
            f"**Error:** ```{str(error)}```\n"
            f"**Traceback:** ```{str(traceback.format_exc())}```"
        )

    def prepare_info_msg(self, msg) -> str:
        user = msg.from_user

        txt = f"**Bot:** __@{self.bot.username}__"
        txt += f"\n**Chat:** __{msg.chat.title}__"
        txt += f"\n**Chat ID:** __{msg.chat.id}__** / **__{msg.message_id}__"
        txt += f"\n**User:** __{user.first_name} __"
        txt += f" __{user.last_name}__" if not_none(user.last_name) else ""
        txt += f" __(@{user.username})__" if not_none(user.username) else ""
        txt += f"\n**User ID:** __{user.id}__"
        txt += f"\n**Text:** {msg.text.html}" if not_none(msg.text) else ""

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
