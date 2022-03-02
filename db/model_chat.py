from pony.orm import *
from db.helpers import Helpers
from helpers import TextHelper as t


def generate_chat(db: Database):
    class Chat(db.Entity, Helpers):
        id = PrimaryKey(str)
        title = Required(str)
        users = Set("User")

        lang = Required(int, default=1)
        mood = Required(int, default=1)

        nyan = Required(bool, default=True)
        food = Required(bool, default=True)
        memes = Required(bool, default=True)
        empathic = Required(bool, default=True)
        greeters = Required(bool, default=True)

        langs = {1: "ru", 2: "en", 3: "ua"}
        moods = {1: "nyan", 2: "lewd", 3: "angr", 4: "scar"}

        get_lang = lambda self: self.langs[self.lang]
        get_mood = lambda self: self.moods[self.mood]

        def set_lang(self, lang):
            self.lang = self.set_polymophic(lang, self.langs)

        def set_mood(self, mood):
            self.mood = self.set_polymophic(mood, self.moods)

        @staticmethod
        def set_polymophic(one, dict):
            if one in dict.values():
                keys = list(dict.keys())
                values = list(dict.values())

                position = values.index(one)
                return keys[position]

        @classmethod
        def find_or_create(cls, msg):
            if msg.chat.title:
                params = dict(id=str(msg.chat.id), title=msg.chat.title)
            else:
                params = dict(id=str(msg.from_user.id), title=t.username(msg.from_user))
            return super().find_or_create(**params)

        @classmethod
        def get_by_msg(cls, msg):
            if msg.chat.title:
                id = str(msg.chat.id)
            else:
                id = str(msg.from_user.id)
            return cls.get(id=id)

    return Chat
