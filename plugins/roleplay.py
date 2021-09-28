from classes.client import app
from random 		import choice

command = app.filters.command
@app.on_message(command(['me', f'me@{app.username}']))
@app.switch
def me(app, msg):
	txt = msg.text.html
	txt = txt.replace('/me', f'**✵{app.username_finder(msg.from_user)}**')
	app.roleplay_send(msg, txt)

@app.on_message(command(['ch', f'ch@{app.username}']))
@app.switch
def ch(app, msg):
	txt = msg.text.html
	txt = txt.replace(f'/{msg.command[0]} {msg.command[1]}', f'**✵{msg.command[1]}**')
	txt+=f'\n__({app.username_finder(msg.from_user)})__'
	app.roleplay_send(msg, txt)

commands = [
	'pat',  f'pat@{app.username}'
	'hug',  f'hug@{app.username}'
	'koos', f'koos@{app.username}'
	'lapk', f'lapk@{app.username}'
	'lick', f'lick@{app.username}'
	'jamk', f'jamk@{app.username}'
	'kiss', f'kiss@{app.username}'
]

@app.on_message(app.filters.group & command(commands))
@app.switch
@app.database
def hnkw_roleplay(app, msg, chat):
	if msg.reply_to_message is not None:
		user  = msg.reply_to_message.from_user
	else:
		user = app.get_users(choice(chat.users['on']))
		
	username_1 = app.username_finder(msg.from_user)
	username_2 = app.username_finder(user)

	command = msg.command[0].replace(f'@{app.username}', '')
	txt = f"**✵{username_1}** {chat.service('roleplay', command)} **{username_2}✵**"
	
	app.roleplay_send(msg, txt)
