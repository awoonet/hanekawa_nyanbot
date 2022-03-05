from pyrogram.types import Message, User


class TextHelper:
    @staticmethod
    def msg_text(msg: Message) -> str:
        if msg.text is not None:
            return msg.text.html
        elif msg.caption is not None:
            return msg.caption.html
        else:
            return ""

    @staticmethod
    def username(user: User) -> str:
        if user.username is not None:
            return f"@{user.username}"
        elif user.last_name is not None:
            return f"{user.first_name} {user.last_name}"
        else:
            return user.first_name
        
    @staticmethod
    def reactions(t, chat):
        reactions = []
        for key, value in chat.categories.items():
            if value:
                reactions.append(t(f"config.keyboard.category.{key}"))
        return ", ".join(reactions)
    
    @classmethod
    def make_lookup_message(cls, t, user) -> str:
        chat = user.chat

        text = t("config.message.lookup").format(
            switch_chat=t(f"config.keyboard.switch.{chat.get_switch()}"),
            switch_user=t(f"config.keyboard.switch.{user.get_switch()}"),
            lang=t(f"config.keyboard.lang.{chat.get_lang()}"),
            mood=t(f"config.keyboard.mood.{chat.get_mood()}"),
            reactions=cls.reactions(t, chat),
        )
        return text
