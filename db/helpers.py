from typing import Union, Callable
from pyrogram.types import Message, CallbackQuery

from pony.orm import *


class ClientDBHelpers:
    @classmethod
    def with_db(cls, func: Callable) -> Callable:
        def wrapper(app, msg: Union[Message, CallbackQuery]) -> None:
            try:
                with db_session:
                    user = cls.db_per_message(app, msg)
                    func(app, msg, user)
            except Exception as e:
                app.send_error_msg(msg, e)
            finally:
                msg.continue_propagation()

        return wrapper

    @staticmethod
    def db_per_message(app, msg: Union[Message, CallbackQuery]) -> None:
        if type(msg) is CallbackQuery:
            msg: Message = msg.message

        chat = app.chat.find_or_create(msg)
        user = app.user.find_or_create(msg, chat)
        chat.users.add(user)

        return user

    def service(self, chat) -> Callable:
        lang: str = chat.get_lang()
        service_messages: dict = self.service_messages.get(lang)

        def t(string: str) -> str:
            result: Union[str, dict] = service_messages

            for i in string.split("."):
                result = result.get(i)
            return result

        return t


class DBHelpers:
    switches: dict = {True: "on", False: "off"}
    get_switch: Callable = lambda self: self.switches[self.switch]

    def change_switch(self) -> None:
        self.switch = not self.switch
