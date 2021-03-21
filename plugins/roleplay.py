from classes.client import app
from random 				import choice

app.username	= 'hanekawa_nyanbot'

@app.on_message(app.filters.command(['me', f'me@{app.username}']))
def me(app, msg):
	txt = msg.text.html
	txt = txt.replace('/me', f'**✵{app.username_finder(msg.from_user)}**')
	app.roleplay_send(msg, txt)

@app.on_message(app.filters.command(['ch', f'ch@{app.username}']))
def ch(app, msg):
	txt = msg.text.html
	txt = txt.replace(f'/{msg.command[0]} {msg.command[1]}', f'**✵{msg.command[1]}**')
	txt+=f'\n__({app.username_finder(msg.from_user)})__'
	app.roleplay_send(msg, txt)

def hnkw_roleplay(app, msg, chat, command): 
	if msg.reply_to_message is not None:
		user  = msg.reply_to_message.from_user
	else:
		user = app.get_users(choice(chat.users['on']))
		
	username_1 = app.username_finder(msg.from_user)
	username_2 = app.username_finder(user)

	txt = f"**✵{username_1}** {chat.service('roleplay', command)} **{username_2}✵**"
	
	app.roleplay_send(msg, txt)
		
@app.on_message(app.filters.group & app.filters.command(['pat', f'pat@{app.username}']))
@app.decorator
def pat(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'pat')

@app.on_message(app.filters.group & app.filters.command(['hug', f'hug@{app.username}']))
@app.decorator
def hug(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'hug')

@app.on_message(app.filters.group & app.filters.command(['koos', f'koos@{app.username}']))
@app.decorator
def koos(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'koos')

@app.on_message(app.filters.group & app.filters.command(['lick', f'lick@{app.username}']))
@app.decorator
def lick(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'lick')

@app.on_message(app.filters.group & app.filters.command(['jamk', f'jamk@{app.username}']))
@app.decorator
def jamk(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'jamk')

@app.on_message(app.filters.group & app.filters.command(['kiss', f'kiss@{app.username}']))
@app.decorator
def kiss(app, msg, chat):
  hnkw_roleplay(app, msg, chat, 'kiss')