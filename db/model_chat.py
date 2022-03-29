from pony.orm import *
from client.helper_text import TextHelper as th
from db.helpers import DBHelpers


def generate_chat(db: Database):
    class Chat(db.Entity, DBHelpers):
        id = PrimaryKey(str)
        title = Required(str)
        users = Set("User")

        lang = Required(int, default=1)
        mood = Required(int, default=1)

        switch = Required(bool, default=True)
        categories = Required(
            Json,
            default=dict(
                nyan=True, empathic=True, food=True, greeters=True, memes=True
            ),
        )

        langs = {1: "ru", 2: "en", 3: "ua"}
        moods = {1: "nyan", 2: "lewd", 3: "angr", 4: "scar"}

        get_lang = lambda self: self.langs[self.lang]
        get_mood = lambda self: self.moods[self.mood]
        get_category = lambda self, cat: self.switches[self.categories[cat]]

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

        def change_category(self, category: str) -> None:
            self.categories[category] = not self.categories[category]

        def i18n_categories(self, t):
            return ", ".join(
                [
                    t(f"config.keyboard.category.{x}")
                    for x, y in self.categories.items()
                    if y
                ]
            )

        @classmethod
        def find_or_create(cls, msg):
            if msg.chat.title:
                params = {"id": str(msg.chat.id), "title": msg.chat.title}
            else:
                params = {
                    "id": str(msg.from_user.id),
                    "title": th.username(msg.from_user),
                }

            instance = cls.get(id=params["id"])
            if instance:
                instance.title = params["title"]
                return instance
            else:
                return cls(**params)

        @classmethod
        def get_by_msg(cls, msg):
            if msg.chat.title:
                id = str(msg.chat.id)
            else:
                id = str(msg.from_user.id)
            return cls.get(id=id)

    return Chat
