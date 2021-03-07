from pyrogram 		import Client, filters, idle, ContinuePropagation
from classes.chat	import Chat
import shelve, traceback, time, dns.resolver 

class app(Client):
	id 				=  1056476287
	katsu_id	=  600432868
	config_id	= -1001328058005
	media_id	= -1001157282357
	db_file		= 'DB/hanekawa'
	username 	= 'hanekawa_nyanbot'

	switch = True

	filters = filters
	
	def run_custom(self):
		self.db = shelve.open(self.db_file)
		self.start()
		self.turn_on()

		idle()
		
		self.stop()
		self.db.close()

	@staticmethod
	def decorator(func):
		def wrapper(app, msg):
			if app.switch:
				try:
					chat_id = str(msg.chat.id)
					if chat_id not in app.db.keys():
						app.db[chat_id] = Chat(app, msg)
					chat = app.db[chat_id]

					chat.everytime(msg)
					
					func(app, msg, chat)

					app.db[chat_id] = chat
					app.db.sync() 

				except Exception as error:
					app.send_error(msg, error, traceback.format_exc())
				
			raise ContinuePropagation

		return wrapper
	
	def bot_can(self, msg, action):
		bot = self.get_chat_member(str(msg.chat.id), 1056476287)
		if action == 'd':return True if bot.can_delete_messages  else False
		if action == 'r':return True if bot.can_restrict_members else False
		
	def msg_del(self, msg):
		if self.bot_can(msg, 'd'):
			self.delete_messages(str(msg.chat.id), msg.message_id)

	def roleplay_send(self, msg, txt):
		if msg.reply_to_message is not None:	
			msg.reply(txt, reply_to_message_id=msg.reply_to_message.message_id)
		else:					 						
			msg.reply(txt, quote=False)
		self.msg_del(msg)

	@staticmethod
	def username_finder(user):
		if user.username is not None:
			return f"@{user.username}" 
		elif user.last_name is not None:
			return f"{user.first_name} {user._last.name}"
		else:
			return user.first_name

	@staticmethod
	def text(msg):
		if 		msg.text 		is not None:	return msg.text
		elif  msg.caption is not None:	return msg.caption
		else:														return False
	
	@staticmethod
	def id_formatter(msg):
		txt = '**Bot:** __@hanekawa_nyanbot__'
		txt+= f'\n**Chat:** __{msg.chat.title}__'
		txt+= f'\n**Chat ID:** __{msg.chat.id}__**/**__{msg.message_id}__'
		user= msg.from_user
		txt+= f'\n**User:** __{user.first_name} __'
		txt+= f'__{user.last_name}__'			if user.last_name is not None else ''
		txt+= f'__ (@{user.username})__'	if user.username  is not None else '' 
		txt+= f'\n**User ID:** __{user.id}__'
		if msg.text is not None:
			txt+= f'\n**Text:** __{msg.text.html}__'
		if msg.media is not None and msg.media:
			if msg.audio is not None:
				txt+= f'\n**Audio ID**: __{msg.audio.file_id}__'
			elif msg.document is not None:
				txt+= f'\n**Document ID**: __{msg.document.file_id}__'
			elif msg.photo is not None:
				txt+= f'\n**Photo ID**: __{msg.photo.file_id}__'
			elif msg.sticker is not None:
				txt+= f'\n**Sticker ID**: __{msg.sticker.file_id}__'
			elif msg.animation is not None:
				txt+= f'\n**Animation ID**: __{msg.animation.file_id}__'
			elif msg.video is not None:
				txt+= f'\n**Video ID**: __{msg.video.file_id}__'
			elif msg.voice is not None:
				txt+= f'\n**Voice ID**: __{msg.voice.file_id}__'
			elif msg.video_note is not None:
				txt+= f'\n**Video note ID**: __{msg.video_note.file_id}__'
			if msg.caption is not None:
				txt+= f'\n**Caption**: __{msg.caption}__'

		return txt

	def send_error(self, msg, error, traceback):
		txt = '**Error occured in message:**\n\n'
		txt+= self.id_formatter(msg)
		txt+= f'\n**Error:** ```{str(error)}```'
		txt+= f'\n**Traceback:** ```{str(traceback)}```'

		self.send_message(app.config_id, txt)
		self.forward_messages(app.config_id, msg.chat.id, (msg.message_id,))

	@staticmethod
	def iter_choose(iterable, searching):
		for i in iterable:
			if searching == i:
				return i

	def turn_on(self):
		self.bot = self.get_me()

		txt = f'**Turned on bot:**'
		txt+= f'\n**User:** `{self.bot.first_name}`'
		txt+= f'\n**Username:** `@{self.bot.username}`'
		txt+= f'\n**User ID:** `{self.bot.id}`'
		txt+= f'\n**Time:** `{time.strftime("%y/%m/%d %H:%M:%S", time.localtime())}`'
		txt+= f'\n**IP:** `{self.find_ip()}`'

		self.username = self.bot.username
		self.send_message(app.config_id, txt)

	@staticmethod
	def find_ip():
		resolver = dns.resolver.Resolver(configure=False)
		resolver.nameservers = ["208.67.222.222", "208.67.220.220"]
		return resolver.query('myip.opendns.com')[0]