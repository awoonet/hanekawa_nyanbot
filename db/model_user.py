from pony.orm import *
from helpers import TextHelper as t


def generate_user(db: Database, Chat):
    class User(db.Entity):
        id = Required(str)
        name = Required(str)
        switch = Required(bool, default=True)
        chat = Required(Chat)
        PrimaryKey(id, chat)

        @classmethod
        def find_or_create(cls, msg, chat):
            if msg.sender_chat is not None:
                params = {
                    "id": str(msg.sender_chat.id),
                    "name": msg.sender_chat.title,
                    "chat": chat,
                }
            else:
                params = {
                    "id": str(msg.from_user.id),
                    "name": t.username(msg.from_user),
                    "chat": chat,
                }

            instance = cls.get(id=params["id"], chat=chat.id)
            if instance:
                instance.name = params["name"]
                return instance
            else:
                cls(**params)

        @classmethod
        def get_by_msg(cls, msg):
            id = str(msg.from_user.id)
            return cls.get(id=id)

    return User
