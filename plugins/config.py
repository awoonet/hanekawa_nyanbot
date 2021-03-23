from classes.client import app
import random, re

g = app.filters.group
c = app.filters.command

command_state = ['global_turn', f'global_turn@{app.username}',]
@app.on_message(g & c(command_state))
@app.decorator 
def state(app, msg, chat):
	chat.change_options(app, msg, 'state')

command_lang	= ['change_lang', 'ch_lang', 	f'change_lang@{app.username}', f'ch_lang@{app.username}']
@app.on_message(g & c(command_lang))
@app.decorator 
def lang(app, msg, chat):
	chat.change_options(app, msg, 'lang')

command_mood	= ['change_mood', 'ch_mood', 	f'change_mood@{app.username}', f'ch_mood@{app.username}']
@app.on_message(g & c(command_mood))
@app.decorator 
def mood(app, msg, chat):
	chat.change_options(app, msg, 'mood')
	
command_user	= ['user_turn', 	f'user_turn@{app.username}']
@app.on_message(g & c(command_user))
@app.decorator 
def user_state(app, msg, chat):
	chat.change_options(app, msg, 'user_state')

command_view	= ['chat_stats',  f'chat_stats@{app.username}']
@app.on_message(g & c(command_view))
@app.decorator 
def view_stats(app, msg, chat):
	answer = chat.view_chat_stats()
	msg.reply(answer)