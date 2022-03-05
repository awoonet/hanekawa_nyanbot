from pony.orm import *
from helpers.text_helpers import TextHelper as t
from db.helpers import DBHelpers

def generate_user(db: Database, Chat):
    class User(db.Entity, DBHelpers):
        id = Required(str)
        name = Required(str)
        switch = Required(bool, default=True)
        chat = Required(Chat)
        PrimaryKey(id, chat)

        @classmethod
        def find_or_create(cls, msg, chat):
            if msg.sender_chat is not None:
                params = dict(
                    id=str(msg.sender_chat.id),
                    name=msg.sender_chat.title
                )
            else:
                params = dict(
                    id=str(msg.from_user.id),
                    name=t.username(msg.from_user)
                ) 

            instance = cls.get(id=params["id"], chat=chat.id)
            if instance:
                instance.name = params["name"]
                return instance
            else:
                return cls(chat=chat, **params)

        @classmethod
        def get_by_msg(cls, msg):
            if msg.sender_chat is not None:
                id=str(msg.sender_chat.id)
            else:
                id = str(msg.from_user.id)
            return cls.get(id=id)

    return User
