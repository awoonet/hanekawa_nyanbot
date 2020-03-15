class Reply_message:
	def __init__(self, code, attr='none'):
		self.code = code
		self.attr = attr
	
class T(Reply_message):
	def reply(self, msg):
		msg.reply(
						text=self.code, 
						quote=True)

class P(Reply_message):
	def reply(self, msg):
		msg.reply_photo(
						photo=self.code, 
						quote=True)

class S(Reply_message):
	def reply(self, msg):
		msg.reply_sticker(
						sticker=self.code, 
						quote=True)
		
class V(Reply_message):
	def reply(self, msg):
		msg.reply_voice(
						voice=self.code, 
						quote=True)