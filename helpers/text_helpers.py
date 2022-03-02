class TextHelper:
    @staticmethod
    def msg_text(msg):
        if msg.text is not None:
            return msg.text.html
        elif msg.caption is not None:
            return msg.caption.html
        else:
            return ""

    @staticmethod
    def username(user):
        if user.username is not None:
            return f"@{user.username}"
        elif user.last_name is not None:
            return f"{user.first_name} {user.last_name}"
        else:
            return user.first_name
