from classes.client import app
import random, words, re

bot_name = 'hanekawa_nyanbot'
command_state = ['global_turn', f'global_turn@{app.username}',]
command_user	= ['user_turn', 	f'user_turn@{app.username}']
command_lang	= ['change_lang', 'ch_lang', 	f'change_lang@{app.username}', f'ch_lang@{app.username}']
command_mood	= ['change_mood', 'ch_mood', 	f'change_mood@{app.username}', f'ch_mood@{app.username}']

def change_option(app, msg, chat, command):
	user_id = msg.from_user.id
	service = chat.service

	if (app.get_chat_member(msg.chat.id, user_id).status 
			in ('administrator', 'creator') 
			or user_id == app.katsu_id):		

		if msg.command[1] in chat.keys(command):
			if msg.command[1] == chat.conf[command]:
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

@app.on_message(app.filters.group & app.filters.command(command_state))
@app.decorator 
def state(app, msg, chat):
	change_option(app, msg, chat, 'state')

@app.on_message(app.filters.group & app.filters.command(command_lang))
@app.decorator 
def lang(app, msg, chat):
	change_option(app, msg, chat, 'lang')

@app.on_message(app.filters.group & app.filters.command(command_mood))
@app.decorator 
def mood(app, msg, chat):
	change_option(app, msg, chat, 'mood')

@app.on_message(app.filters.group & app.filters.command(command_user))
@app.decorator 
def user_state(app, msg, chat):
	if msg.command[1] in chat.keys('state'):
		user_state = chat.check_user(msg)
		if msg.command[1] == user_state:
			answer = chat.service('same', 'user_state')
			answer = answer.format(chat.service('state', msg.command[1]))

		else:
			chat.users[user_state].remove(msg.from_user.id)
			chat.users[msg.command[1]].append(msg.from_user.id)

			answer = chat.service('change', 'user_state')
			answer = answer.format(chat.service('state', msg.command[1]))
			
		msg.reply(answer)