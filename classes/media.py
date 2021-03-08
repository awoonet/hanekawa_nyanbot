from random import choice, randint
from classes.text import tsu

class Sticker:	
	def __init__(self, *code):
		self.code = code 

	def reply(self, app, msg, chat):	
		sticker_id = choice(self.code)
		msg.reply_sticker(
			sticker = sticker_id, 
			quote 	= True)

class Text:
	def __init__(self, code):
		self.code = code 

	def reply(self, app, msg, chat):
		msg.reply_text(
			text 	= tsu(chat.conf['lang'], chat.conf['mood'], self.code), 
			quote	= True)

class Other:
	def __init__(self, code):
		self.code = code 
		
	def reply(self, app, msg, chat):	
		app.copy_message(	
			chat_id							= msg.chat.id, 
			from_chat_id				= app.media_id,
			message_id 					= self.code,
			reply_to_message_id	= msg.message_id,
			caption 						= '')

