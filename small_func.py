from time import sleep
class p:
	@staticmethod
	def bool_emoji(q):
		emoji = {	1	: '✅',
					0   : '❌',
					'ru': '🇷🇺',
					'en': '🇺🇸', }
		return emoji.get(q, q)

	@staticmethod
	def iter_choose(somelist, somestr):
		for t in somelist:
			if t in somestr: return t

	@staticmethod
	def choose(var1, var2):	return var1 if var1 else var2

	@staticmethod
	def check_admin(app, chat_id, user_id):
		user = app.get_chat_member(chat_id, user_id)
		if (user.status == 'administrator' or 
			user.status == 'creator'):
			return True
		else:
			return False

	@staticmethod
	def hnkw_can(app, msg, action):
		hnkw = app.get_chat_member(str(msg.chat.id), app.get_me().id)
		if action == 'delete':	return True if hnkw.can_delete_messages  else False
		if action == 'restrict':return True if hnkw.can_restrict_members else False

	def msg_del(self, app, msg):
		if self.hnkw_can(app, msg, 'delete'):
			app.delete_messages(str(msg.chat.id), msg.message_id)

	def admin_send(self, app, msg, txt):
		new_msg = msg.reply(txt, quote=False)
		self.msg_del(app, msg)
		sleep(10)
		app.delete_messages(str(msg.chat.id), new_msg.message_id)

	def roleplay_send(self, app, msg, txt):
		if msg.reply_to_message: msg.reply(txt, reply_to_message_id=msg.reply_to_message.message_id)
		else:					 msg.reply(txt, quote=False)
		self.msg_del(app, msg)