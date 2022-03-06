import time, requests, traceback
from typing import Union, Callable
from pyrogram.types import Message

not_none = lambda x: x is not None


class AppHelper:
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

    # ---------------------------------------------------------------------------
    def service(self, chat) -> Callable:
        lang: str = chat.get_lang()
        service_messages: dict = self.service_messages.get(lang)

        def t(string: str) -> str:
            result: Union[str, dict] = service_messages

            for i in string.split("."):
                result = result.get(i)
            return result

        return t

    # ---------------------------------------------------------------------------
    def init_bot_info(self):
        self.bot = self.get_me()

    # ---------------------------------------------------------------------------
    def send_awaking_msg(self):
        txt = self.prepare_awaking_msg()
        self.send_message(int(self.config_messages), txt)

    def prepare_awaking_msg(self):
        a = "**Turned on bot:** \n\n"
        a += f"```Bot:      {self.bot.first_name}\n"
        a += f"Username: @{self.bot.username}\n"
        a += f"User ID:  {self.bot.id}\n"
        a += self.find_location()
        a += f"Time:     {time.strftime('%H:%M:%S %d/%m/%Y', time.localtime())}```"
        return a

    @staticmethod
    def find_location():
        url = "http://ip-api.com/json/"
        with requests.get(url) as response:
            try:
                response.raise_for_status()
                json = response.json()
                a = f"City:     {json['city']}\n"
                a += f"Region:   {json['regionName']}\n"
                a += f"Country:  {json['country']} {json['countryCode']}\n"
                a += f"IP:       {json['query']}\n"
                return a
            except:
                return ""

    # ---------------------------------------------------------------------------
    def send_error_msg(self, msg, error):
        txt = self.prepare_error_msg(msg, error)

        self.send_message(int(self.config_messages), txt)
        self.forward_messages(int(self.config_messages), msg.chat.id, (msg.message_id,))

    def prepare_error_msg(self, msg, error):
        return f"""**Error occured in message:**
				{self.prepare_info_msg(msg)}
				**Error:** ```{str(error)}```
				**Traceback:** ```{str(traceback.format_exc())}```"""

    def prepare_info_msg(self, msg):
        user = msg.from_user

        txt = f"**Bot:** __@{self.bot.username}__"
        txt += f"\n**Chat:** __{msg.chat.title}__"
        txt += f"\n**Chat ID:** __{msg.chat.id}__** / **__{msg.message_id}__"
        txt += f"\n**User:** __{user.first_name} __"
        txt += f" __{user.last_name}__" if not_none(user.last_name) else ""
        txt += f" __(@{user.username})__" if not_none(user.username) else ""
        txt += f"\n**User ID:** __{user.id}__"

        if not_none(msg.text):
            txt += f"\n**Text:** {msg.text.html}"
        elif not_none(msg.media) and msg.media:
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

            if not_none(msg.caption):
                txt += f"\n**Caption**:__{msg.caption}__"

        return txt
