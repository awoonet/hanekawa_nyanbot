class Media:
	def __init__(self, code, attr='none'):
		self.code = code 
		self.attr = attr

class Sticker(Media):	
	def reply(self, app, msg):	
		msg.reply_sticker(
			sticker = self.code, 
			quote 	= True)

class Text(Media):
	def reply(self, app, msg):
		msg.reply_text(
			text 	= self.code.format('Ханекава'), 
			quote	= True)

class Other(Media):
	def reply(self, app, msg):	
		app.forward_messages(	
			chat_id		= msg.chat.id, 
			from_chat_id= -1001157282357,
			message_ids = (self.code,),
			as_copy 	= True)
