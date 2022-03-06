from pyrogram.types import Message, User


class TextHelper:
    """
    Helper class for working with text
    """

    @staticmethod
    def msg_text(msg: Message) -> str:
        """
        Function to find text in message
        Args:
            msg (pyrogram Message):
        """
        if msg.text is not None:
            return msg.text.html
        elif msg.caption is not None:
            return msg.caption.html
        else:
            return ""

    @staticmethod
    def username(user: User) -> str:
        """
        Function to find username of user
        Args:
            user (pyrogramm User):
        """
        if user.username is not None:
            return f"@{user.username}"
        elif user.last_name is not None:
            return f"{user.first_name} {user.last_name}"
        else:
            return user.first_name
