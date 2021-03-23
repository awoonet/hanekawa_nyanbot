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
		
		if txt:
			chat_on = self.conf['state'] == 'on'
			user_on = self.users[msg.from_user.id] == 'on'

			def hanekawa_in_msg():
				if (msg.reply_to_message is not None and 
						msg.reply_to_message.from_user.id == app.id):
					return True
				else:
					name = (f'@{app.username}', 'Ханекава', 'Тсубаса', 'Някава', 'Hanekawa', 'Tsubasa', 'Nyakawa')
					for i in name:
						if i in txt:
							return True

			if (chat_on and user_on) or hanekawa_in_msg():

				mood	= self.conf['mood']
				lang	= self.conf['lang']

				reaction = Media(**answer[mood][lang])
				reaction.reply(app, msg, self)

	def view_chat_stats(self):
		answer = lambda x, y=False: chat.service(x, y if y else chat.conf[x])

		settings = {
			'glob': answer('state'),
			'lang': answer('lang'),
			'mood': answer('mood'),
			'priv': answer('state', chat.check_user(msg)),
		}

		return chat.service('settings').format(**settings)
		
	def change_options(self, app, msg, command):
		user_id 	= msg.from_user.id
		user_state= command == 'user state'
		is_katsu	=	user_id == app.katsu_id
		is_admin	= lambda: app.get_chat_member(msg.chat.id, user_id).status in ('administrator', 'creator')
		service = self.service
		mod = msg.command[1]

		answer = False

		if len(msg.command) > 1 and mod in self.keys(command):

			if user_state:
				prev_state= self.check_user(msg)

			else:
				if is_katsu or is_admin():
					prev_state= self.conf[command]
				else: 
					answer = service('error', 'permission')

			if not answer:
				if mod == prev_state:
					answer =  service('same', command)

				else:
					if user_state:
						self.users[user_id] = mod
					else:
						self.conf[command] = mod

					answer = service('change', command)
				answer = answer.format(service(command, mod))
		else:
			answer = service('error', command)
		
		msg.reply(answer)