#!/usr/bin/python3
from chat	   import Chat
from pyrogram   import Client, MessageHandler, Filters
#import requests
import logging
import shelve
import re

app = Client("hanekawa_nyan")
logging.basicConfig(level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s')

with shelve.open('nyanDB') as db:
	def cc(message, user):
		chat_id  = str(message.chat.id)
		if chat_id not in db:
			db[chat_id] = Chat(message)
		chat = db[chat_id]
		if chat.check_usr(user.id) == False: chat.users['off'].add(user.id)	
		return chat, chat_id

	def db_decorator(my_func):
		def wrapper(app, message):
			if hasattr(message, 'message'): 
				chat, chat_id = cc(message.message, message.from_user)
			else:						   
				chat, chat_id = cc(message, message.from_user)
			
			my_func(app, message, chat)

			db[chat_id] = chat
			db.sync() 
			message.continue_propagation() 
		return wrapper

	rp_comms = ['me','hug', 'kiss', 'koos', 'lick', 'jamk']
	@app.on_message(~Filters.channel & Filters.command(rp_comms))
	@db_decorator #ролеплейные возможности типа /me и /hug
	def hnkw_roleplay(app, msg, chat): 
		chat.rp_funcs(app, msg)				
	
	@app.on_message(~Filters.channel & Filters.command('config'))
	@db_decorator #вызов клавиатуры контроля бота
	def hnkw_conf(app, msg, chat):	  
		chat.configurate_message(app, msg)  

	@app.on_callback_query()
	@db_decorator #изменение настроек бота
	def callback(app, msg, chat):
		chat.configurate_callback(app, msg)   

	@app.on_message(~Filters.channel)
	@db_decorator #ответчик няшностей
	def hnkw_replier(app, msg, chat):
		chat.replaier(app, msg)   
	
	app.run()