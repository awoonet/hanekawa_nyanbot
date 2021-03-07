from words.service import service 

class Chat:
	def __init__(self, app, msg):
		self.id			= msg.chat.id
		self.title	=	msg.chat.title
		self.conf		= {
					'state'	: 'on',
					'mood'	:	'nyan',
					'lang'	: 'ru',
		}
		self.users		= {
					'on'	: [],
					'off'	: [],
		}

		self.add_user(msg)
	
	def everytime(self, msg):
		self.renew_name(msg)
		self.add_user(msg)

	def renew_name(self, msg):
		if self.title != msg.chat.title:
			self.title = msg.chat.title
	
	def add_user(self, msg):
		if self.check_user(msg) == False:
			self.users['on'].append(msg.from_user.id)

	def check_user(self, msg):
		for state, Iist in self.users.items():
			if msg.from_user.id in Iist:
				return state
			return False
			
	def service(self, category, word=False):
		lang = self.conf['lang']
		return service[category][word][lang]
	
	@staticmethod
	def keys(category):
		return service[category].keys()