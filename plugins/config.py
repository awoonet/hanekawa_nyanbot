from classes.client import app
import random, re

bot_name = 'hanekawa_nyanbot'
command_state = ['global_turn', f'global_turn@{app.username}',]
command_user	= ['user_turn', 	f'user_turn@{app.username}']
command_lang	= ['change_lang', 'ch_lang', 	f'change_lang@{app.username}', f'ch_lang@{app.username}']
command_mood	= ['change_mood', 'ch_mood', 	f'change_mood@{app.username}', f'ch_mood@{app.username}']
command_view	= ['chat_stats',  f'chat_stats@{app.username}']

@app.on_message(app.filters.group & app.filters.command(command_state))
@app.decorator 
def state(app, msg, chat):
	chat.change_option(app, msg, 'state')

@app.on_message(app.filters.group & app.filters.command(command_lang))
@app.decorator 
def lang(app, msg, chat):
	chat.change_option(app, msg, 'lang')

@app.on_message(app.filters.group & app.filters.command(command_mood))
@app.decorator 
def mood(app, msg, chat):
	chat.change_option(app, msg, 'mood')

@app.on_message(app.filters.group & app.filters.command(command_user))
@app.decorator 
def user_state(app, msg, chat):
	
	if len(msg.command) > 1 and msg.command[1] in chat.keys('state'):
		user_state = chat.check_user(msg)

		if msg.command[1] == user_state:
			answer = chat.service('same', 'user_state')
			answer = answer.format(chat.service('state', msg.command[1]))

		else:
			chat.users[msg.from_user.id] = msg.command[1]

			answer = chat.service('change', 'user_state')
			answer = answer.format(chat.service('state', msg.command[1]))
		
	else:
		answer = chat.service('error', 'user_state')

	msg.reply(answer)

@app.on_message(app.filters.group & app.filters.command(command_view))
@app.decorator 
def view_stats(app, msg, chat):
	settings = {
		'glob': chat.service('state',chat.conf['state']),
		'lang': chat.service('lang', chat.conf['lang']),
		'mood': chat.service('mood', chat.conf['mood']),
		'priv': chat.service('state',chat.check_user(msg)),
	}

	answer = chat.service('settings').format(**settings)

	msg.reply(answer)