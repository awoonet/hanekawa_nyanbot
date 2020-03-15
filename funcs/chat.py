from funcs.small_funcs  import check_admin, admin_send, roleplay_send, msg_del
from words.triggers 	import triggers
from words.words		import reacts
from random		 		import choice
import re

class Chat:
	def __init__(self, msg):
		self.title  = msg.chat.title
		self.id		= msg.chat.id
		self.config = { 'state'	: True,
						'mood'	: 'nyan',
						'lang'	: 'ru',}
		self.users   = {'on'  	: set(),
						'off'	: set(),
						'ban'	: set()}

	def replaier(self, app, msg):
		txt   = str(msg.text)
		txt_l = txt.lower()
		state = self.check_usr(msg.from_user.id)

		def condition():
			if self.config['state']:
				if 'on' in state:
					return True
			elif msg.reply_to_message:
				if msg.reply_to_message.from_user.id == 1056476287:
					return True
			elif '@hanekawa_nyanbot' in txt_l:
				return True
			return False

		if condition:
			answer_set = set()
			for trigger, option in triggers.items():
				for trigger in trigger:
					if re.search(r'\b'+trigger+r'\b', txt_l):
						answer_set.add(option)
			lang = self.config['lang']
			mood = self.config['mood']
			for option1 in answer_set:
				for option2, reaction in reacts[lang][mood].items():  
					if option2 == option1:
						reaction = choice(reaction)
						reaction.reply(msg)
			answer_set = set()

	def rp_funcs(self, app, msg, service):
		def nyan_roleplay(oth_username):
			roleplays = {	r'hug'  : service['hug'] ,
							r'kiss' : service['kiss'],
							r'koos' : service['koos'],
							r'lick' : service['lick'],
							r'jamk' : service['jamk'],}

			for t, r in roleplays.items():
				if re.search(t , msg.command[0]):
					txt = f'**✵{username}** {r} **{oth_username}**'
					roleplay_send(app, msg, txt)
		
		username = msg.from_user.first_name

		if re.search(r'^me', msg.command[0]):
			txt = (msg.text).replace('/me', f'**✵{username}**')
			roleplay_send(app, msg, txt)

		elif msg.reply_to_message: 
			reply_username  = msg.reply_to_message.from_user.first_name
			nyan_roleplay(reply_username)
		else:
			ids = []
			for i in self.users.values():
				ids.extend(i)
			user_id = choice(ids)
			user = app.get_chat_member(msg.chat.id, user_id).user
			oth_username = f'@{user.username}' if user.username else user.first_name
			nyan_roleplay(oth_username)

	def user_make(self, msg):
		"""
		Функция определяет eсть ли отправитель, и reply-пользователь в базе этого чата, 
		и если нет - добавляет их в базу чата.
		"""
		user_status = self.check_usr(msg.from_user.id)
		if user_status == False:
			self.users['off'].add(msg.from_user.id)

		if msg.reply_to_message:
			user_status = self.check_usr(msg.reply_to_message.from_user.id)
			if user_status == False:
				self.users['off'].add(msg.reply_to_message.from_user.id)			
	
	def configurate(self, app, msg, service):
		"""
		Функция предназначена для изменения настроек бота в определенном чате, администрацией или создателем бота.
		"""
		config = msg.command[0]
		option = msg.command[1] if len(msg.command) > 1 else None
		uid = msg.from_user.id
		admin = check_admin(app, str(msg.chat.id), uid)
		
		if re.search(r'^user', config):
			commands = ('on', 'off', 'ban')
			for command in commands:
				if option in command:
					if admin and msg.reply_to_message:
						usr = msg.reply_to_message.from_user
					else: 
						usr = msg.from_user
					txt = self.change_usr(usr, admin, command, service)
					break
			else:
				txt = service['admin_user_error']
			admin_send(app, msg, txt)

		elif re.search(r'^stats', config):
			answer = self.chat_stats(service)
			admin_send(app, msg, answer)
		
		elif re.search(r'^status', config):
			user = msg.reply_to_message.from_user if msg.reply_to_message else msg.from_user
			answer = service['admin_user_state'].format(str(user.first_name), service[self.check_usr(user.id)])
			admin_send(app, msg, answer)

		elif (admin or
			  600432868 in uid or
			  app.get_me().id  in uid):

			if re.search(r'^cond', config):
				if re.search(r'^on', option):
					self.config['state'] = True
					txt = service['chat_on']
				elif re.search(r'^off', option):
					self.config['state'] = False
					txt = service['chat_off']
				
			if re.search(r'^lang', config):
				langs = ('ru', 'en')
				if option in langs:
					self.config['lang'] = option
					txt = service['lang_change'] % option
				else:
					txt = service['lang_error']	

			elif re.search(r'^mood', config):
				moods = ('nyan', 'lewd', 'angr', 'scar')
				if option in moods:
					self.config['mood'] = option
					txt = service['mood_change']
				else:
					txt = service['mood_error']
			
			admin_send(app, msg, txt)
		else:
			txt = service['permission_error']
			admin_send(app, msg, txt)
		
	def chat_stats(self, service):
		answer = f'{service["chat_stats"]}\n\n'
		
		symbols = {	True : '✅',	False: '❌',
					'ru' : '🇷🇺', 'en' : '🇺🇸',}

		for setting, state1 in self.config.items():
			if   state1 in symbols.keys():	z = symbols[state1] 
			elif state1 in service.keys():	z = service[state1]
			else:							z = state1
			answer += f'{service[setting]}: {z}\n'
		return answer
		
	def check_usr(self, id):
		"""
		Определяет в какой из БД присутствует пользователь.
		"""
		for name, someset in self.users.items():
			for someid in someset:
				if id == someid:
					return name
		return False
	
	def change_usr(self, usr, admin, command, service):
		"""
		Перемещает пользователя в указанную БД.
		"""
		state = self.check_usr(usr.id)
		if state == command:	
			return service['same_user_cond'].format(str(usr.first_name), str(command))  
		else:
			if   re.search(r'^on' , state):		self.users['on' ].remove(usr.id)
			elif re.search(r'^off', state):		self.users['off'].remove(usr.id)
			elif re.search(r'^ban', state):
				if admin:	self.users['ban'].remove(usr.id)
				else:		return service['admin_rights_error']

			if   re.search(r'^on' , command): 	self.users['on' ].add(usr.id)
			elif re.search(r'^off', command): 	self.users['off'].add(usr.id)
			elif re.search(r'^ban', command): 	
				if admin:	self.users['ban'].add(usr.id)
				else:		return service['admin_rights_error']

			return service['admin_user_state'].format(str(usr.first_name), service[command])  