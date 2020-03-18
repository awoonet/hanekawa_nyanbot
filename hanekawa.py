#!/usr/bin/python3
from pyrogram           import Client, MessageHandler, Filters
import shelve
import re
from config              import api_id, api_hash, bot_token
from funcs.chat          import Chat

with shelve.open('nyanDB') as db:
    app = Client("hanekawa_nyan", api_id, api_hash, bot_token=bot_token)

    def db_decorator(my_func):
        def wrapper(app, message):
            def somechat(message):
                chat_id  = str(message.chat.id)
                if chat_id not in db:
                    db[chat_id] = Chat(message)
                chat = db[chat_id]
                chat.user_make(message)
                return chat, chat_id

            try:    chat, chat_id = somechat(message.message)
            except: chat, chat_id = somechat(message)
            service = chat.select_service()

            my_func(app, message, chat, service)

            db[chat_id] = chat
            db.sync() 

            message.continue_propagation() 
        return wrapper

    @app.on_message(~Filters.channel)
    @db_decorator #ответчик няшностей
    def hnkw_replier(app, msg, chat, service):
        chat.replaier(app, msg)                         
    
    rp_comms = ['me','hug', 'kiss', 'koos', 'lick', 'jamk']
    @app.on_message(~Filters.channel & Filters.command(rp_comms))
    @db_decorator #ролеплейные возможности типа /me и /hug
    def hnkw_roleplay(app, msg, chat, service): 
        chat.rp_funcs(app, msg, service)                
    
    @app.on_message(~Filters.channel & Filters.command('config'))
    @db_decorator #вызов клавиатуры контроля бота
    def hnkw_conf(app, msg, chat, service):      
        chat.configurate_message(app, msg, service)  

    @app.on_callback_query()
    @db_decorator #изменение настроек бота
    def callback(app, msg, chat, service):
        chat.configurate_callback(app, msg, service)    
    app.run()