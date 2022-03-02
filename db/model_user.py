from pony.orm import *

from db.helpers import Helpers
from helpers import TextHelper as t


def generate_user(db: Database, Chat):
    class User(db.Entity, Helpers):
        id = PrimaryKey(str)
        name = Required(str)
        switch = Required(bool, default=True)
        chat = Required(Chat)

        @classmethod
        def find_or_create(cls, msg, chat):
            params = dict(
                id=str(msg.from_user.id), name=t.username(msg.from_user), chat=chat
            )
            return super().find_or_create(**params)

        @classmethod
        def get_by_msg(cls, msg):
            id = str(msg.from_user.id)
            return cls.get(id=id)

    return User
