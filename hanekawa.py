#!/usr/bin/pypy3 
from pyrogram           import Client, MessageHandler, Filters
import shelve
import re
from config              import api_id, api_hash
from funcs.chat          import Chat
from words.ru.service    import ru_service
from words.en.service    import en_service


with shelve.open('nyanDB') as db:
    app = Client("hanekawa_nyan", api_id, api_hash)

    def db_decorator(my_func):
        def wrapper(app, message):
            chat_id  = str(message.chat.id)
            if chat_id not in db:
                db[chat_id] = Chat(message)
            chat = db[chat_id]

            chat.user_make(message)

            service = {'ru': ru_service, 'en': en_service}
            for x, y in service.items():
                if chat.config['lang'] in x: service = y
            
            my_func(app, message, chat, service)

            db[chat_id] = chat
            db.sync() 

            message.continue_propagation() 
        return wrapper

    conf_coms = ['user', 'stats', 'status', 'cond', 'lang', 'mood']
    @app.on_message(~Filters.channel & Filters.command(conf_coms))
    @db_decorator
    def hnkw_conf(app, msg, chat, service):        
        chat.configurate(app, msg, service)     #функции контроля бота

    rp_comms = ['me','hug', 'kiss', 'koos', 'lick', 'jamk']
    @app.on_message(~Filters.channel & Filters.command(rp_comms))
    @db_decorator
    def hnkw_roleplay(app, msg, chat, service): 
        chat.rp_funcs(app, msg, service)        #ролеплейные возможности типа /me и /hug
    
    @app.on_message(~Filters.channel)
    @db_decorator
    def hnkw_replier(app, msg, chat, service):
        chat.replaier(app, msg)                 #ответчик няшностей
        
    app.run()