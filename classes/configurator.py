from pyrogram.types import InlineKeyboardMarkup as keyboard
from pyrogram.types import InlineKeyboardButton as button

class Configurator:

	def change_user(self, msg, value):
		

	def configurator(self, param, value):
		self.config[param] = value
		return self.service('change', param).format(self.service(param, self.config[param]))

	def change_user(self, user_id, previous_state, new_state):
		if previous_state == new_state:
			return self.service('same', 'user').format(self.service('user', new_state))
		else:
			self.users[previous_state].remove(user_id)
			self.users[new_state].add(user_id)
			return self.service('change', 'user').format(self.service('user', new_state))
				

	def keayboard_first_level(self, app, msg):
		s = lambda x: self.service('config', x)

		if app.is_admin(msg): 
			kb = [[
						button(s('state'),	callback_data='state'),
						button(s('user'),	callback_data='user'),
					],
					[
						button(s('lang'),	callback_data='lang'),
						button(s('mood'),	callback_data='mood'),
					]]
		else:
			kb = [[
					button(s('user'),	callback_data='user')
				]]

		txt = self.service('settings')
		msg2 = msg.reply(txt, reply_markup=keyboard(kb))
		app.msg_del(msg, msg2)

	def keyboard_second_level(self, app, query):
		s = lambda x: self.service(query.data, x)

		if app.is_admin(msg): 
			
			if	query.data == 'state': kb = [
						button(s('on'),	callback_data='state_on'),
						button(s('off'),callback_data='state_off'),
					]
			elif query.data == 'lang': kb = [
						button(s('ru'),	callback_data='lang_ru'),
						button(s('en'),	callback_data='lang_en'),
						button(s('ua'),	callback_data='lang_ua'),
			]
			elif query.data == 'mood': kb = [
						button(s('nyan'),	callback_data='mood_nyan'),
						button(s('lewd'),	callback_data='mood_lewd'),
						button(s('angr'),	callback_data='mood_angr'),
						button(s('scar'),	callback_data='mood_scar'),
			]
		elif query.data = 'user': kb = [
						button(s('on'),	callback_data='user_on'),
						button(s('off'),callback_data='user_off'),
					]
		else:
			query.message.reply(self.service('error', 'permission'))
			return False
		
		
		query.message.reply(app.text(query.message), reply_markup=keyboard([kb]))
	
	def keyboard_third_level(self, app, query):
		queries = {	'state_on','state_off',
					'lang_ru','lang_en','lang_ua',	
					'mood_nyan','mood_lewd','mood_angr','mood_scar'}

		user_queries = {'user_on','user_off'}
		
		q = (query.data).split('_')

		if query.data in queries:
			if app.is_admin(msg): 
				txt = self.configurator(q[0], q[1])
			else:
				query.message.reply(self.service('error', 'permission'))
				return False

		elif query.data in user_queries:
			user_state = self.check_user(query.message)

			txt = self.change_user(query.message.from_user.id, user_state, q[1])
			