from pyrogram			import InlineKeyboardMarkup, InlineKeyboardButton
from funcs.small_funcs  import check_admin, admin_send, roleplay_send, msg_del
from words.ru.service   import ru_service
from words.en.service   import en_service
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

		if ((self.config['state'] and 'on' in self.check_usr(msg.from_user.id)) or
			(msg.reply_to_message and msg.reply_to_message.from_user.id == 1056476287) or
			'@hanekawa_nyanbot' in txt_l):

			answer_set = set()
			for trigger, option in triggers.items():
				for trigger in trigger:
					if re.search(r'\b'+trigger+r'\b', txt_l):
						answer_set.add(option)
						
			for option_recieved in answer_set:
				for option_tosend, reaction in reacts[self.config['lang']][self.config['mood']].items():  
					if option_recieved == option_tosend:
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
	
	def configurate_message(self, app, msg, service):
		"""
		Функция предназначена для изменения настроек бота в определенном чате, администрацией или создателем бота.
		"""
		admin = check_admin(app, str(msg.chat.id), msg.from_user.id)

		butts = {	'user'	: ['chat_stats', 'vw_user', 'ch_user'], 
					'admin'	: ['state', 'lang', 'mood']}

		buttons = [butts['admin'], butts['user']] if admin else [butts['user']]
		kb = self.draw_kb(service, buttons)

		msg.reply(service['options'], reply_markup=InlineKeyboardMarkup(kb))
		msg_del(app, msg)

	def configurate_callback(self, app, query, service):
		msg = query.message
		uid = query.from_user.id
		admin = check_admin(app, str(msg.chat.id), uid)

		if query.data:
			if query.data == 'ch_user':		
				kb  = self.draw_kb(service, [['uon', 'uoff', 'ban']])
				txt = service['ch_user?']

			elif query.data == 'chat_stats':		
				txt = self.chat_stats(service)

			elif query.data == 'vw_user':
				user = msg.reply_to_message.from_user if msg.reply_to_message else msg.from_user
				txt = service['admin_user_state'].format(str(user.first_name), service[self.check_usr(user.id)])
			
			elif query.data in ('uon', 'uoff', 'ban'):	
				txt = self.ch_user(msg, admin, query.data.replace('u',''), service)

			elif query.data in ('nyan', 'lewd', 'angr', 'scar'): 
				self.config['mood'] = query.data
				txt =  service['mood_change'] % service[query.data]

			elif query.data in ('ru', 'en'):	
				self.config['lang'] = query.data
				txt = service['lang_change'] % service[query.data]

			elif query.data == 'con':			
				self.config['state'] = True
				txt = service['chat_on']

			elif query.data == 'coff':			
				self.config['state'] = False
				txt = service['chat_off']
			
			elif (admin or uid == 600432868):
				if  query.data == 'state': 
					kb  = self.draw_kb(service, [['con', 'coff']])
					txt = service["set?"] % service['state'].lower()
				elif query.data == 'lang': 
					kb  = self.draw_kb(service, [['ru', 'en']])
					txt = service["set?"] % service['lang'].lower()
				elif query.data == 'mood': 
					kb  = self.draw_kb(service, [['nyan', 'lewd', 'angr', 'scar']])
				
			if 'kb' in locals(): 
				msg.edit_text(txt, reply_markup=InlineKeyboardMarkup(kb))
			else: 
				msg_del(app, query.message)
				admin_send(app, msg, txt)

	def chat_stats(self, service):
		answer = f'{service["chat_stats"]}:\n\n'
		
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
	
	def ch_user(self, msg, admin, command, service):
		"""
		Перемещает пользователя в указанную БД.
		"""
		commands = ('on', 'off', 'ban')
		if command in commands:
			if admin and msg.reply_to_message:  usr = msg.reply_to_message.from_user
			else: 								usr = msg.from_user

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

	def draw_kb(self, service, rows):
		keyboard = []
		for somelist in rows:
			row = []
			for button in somelist:
				row.append(InlineKeyboardButton(service[button], callback_data=button))
			keyboard.append(row)
		return keyboard
	
	def select_service(self):
		service = { 'ru'	: ru_service, 
					'en'	: en_service}
		for x, y in service.items():
			if self.config['lang'] in x: 
				return y
