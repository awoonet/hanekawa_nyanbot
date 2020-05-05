#!/usr/bin/python3
from chat	   		import Chat
from pyrogram   	import Client, MessageHandler, Filters
#import requests
import traceback 
import logging
import shelve

app = Client("hanekawa_nyan")
logging.basicConfig(level=logging.WARNING, format='%(name)s - %(levelname)s - %(message)s')

rp_comms = ['me', 'pat', 'hug', 'koos', 'lick', 'jamk', 'kiss']

with shelve.open('nyanDB') as db:
	def db_decorator(my_func):
		def wrapper(app, msg):
			def cc(msg):
				chat_id  = str(msg.chat.id)
				if chat_id not in db:	
					db[chat_id] = Chat(app, msg)
				chat	= db[chat_id]	
				chat.init_chat(app, msg)
				return chat, chat_id

			try:	qmsg = msg['message']
			except:	qmsg = msg
			chat, chat_id = cc(qmsg)
			
			try:	
				my_func(app, msg, chat)
			except Exception as e:
				chat.send_error(app, msg, f'{e}\n{traceback.format_exc()}')
			db[chat_id] = chat
			db.sync() 
			msg.continue_propagation() 
		return wrapper

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