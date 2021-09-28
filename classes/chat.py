from classes.js_dict import js_dict
from service import service

from classes.configurator import Configurator

class Chat(Configurator):
	def __init__(self, app, msg):
		self.id			=	msg.chat.id
		self.title		=	msg.chat.title

		self.config		= js_dict(
			state = 'on',
			mood = 'nyan',
			lang = 'ru',
		)

		self.users = js_dict(
			on = set(), 
			off = set()
			)

		self.add_user(msg)
	
	def everytime(self, msg):
		self.renew_name(msg)
		self.add_user(msg)

	def renew_name(self, msg):
		if self.title != msg.chat.title:
			self.title = msg.chat.title
	
	def add_user(self, msg):
		if self.check_user(msg) == False:
			self.users.on.add(msg.from_user.id)

	def check_user(self, msg):
		if 		msg.from_user.id in self.users.on: 	return 'on'
		elif 	msg.from_user.id in self.users.off:	return 'off'
		else:										return False
		
	def service(self, first, second=False):
		if not second:	return service[first][self.lang]
		else:			return service[first][second][self.lang]
	
	