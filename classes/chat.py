from classes.media import Media
from service import service 

class Chat:
	def __init__(self, msg):
		self.id			= msg.chat.id
		self.title	=	msg.chat.title

		self.conf		= {
					'state'	: 'on',
					'mood'	:	'nyan',
					'lang'	: 'ru',
		}
		self.users	= {}

		self.users[msg.from_user.id] = 'on'
	
	def everytime(self, msg):
		if self.title != msg.chat.title:
			self.title = msg.chat.title

		if self.check_user(msg) == False:
			self.users[msg.from_user.id] = 'on'
	
	def check_user(self, msg):
		try:
			return self.users[msg.from_user.id]
		except:
			return False

	def service(self, category, word=False):
		lang = self.conf['lang']
		if word:
			return service[category][word][lang]
		else:
			return service[category][lang]
	
	@staticmethod
	def keys(category):
		return service[category].keys()

	def replier(self, app, msg, answer):
		txt		= app.text(msg)

		if (txt and 
				(f'@{app.username}' in txt or 
				(self.conf['state'] == 'on' and
				self.users[msg.from_user.id] == 'on'))):
				
			mood	= self.conf['mood']
			lang	= self.conf['lang']

			reaction = Media(**answer[mood][lang])
			reaction.reply(app, msg, self)
	
	def change_option(self, app, msg, command):
		user_id = msg.from_user.id
		service = self.service

		if (app.get_chat_member(msg.chat.id, user_id).status 
				in ('administrator', 'creator') 
				or user_id == app.katsu_id):		

			if msg.command[1] in self.keys(command):
				if msg.command[1] == self.conf[command]:
					answer = service('same', command)
					
				else:
					chat.conf[command] = msg.command[1]
					answer = service('change', command)
					answer = answer.format(service(command, msg.command[1]))
			else:
				answer = service('error', command)
		else:
			answer = service('error', 'permission')
		
		msg.reply(answer)