from classes.client import app
from random 				import choice

app.username	= 'hanekawa_nyanbot'
me_comms = ['me', f'me@{app.username}']
ch_comms = ['ch', f'ch@{app.username}']
rp_comms = ['pat',   f'pat@{app.username}', 'hug',  f'hug@{app.username}', 
						'koos', f'koos@{app.username}','lick', f'lick@{app.username}', 
						'jamk', f'jamk@{app.username}','kiss', f'kiss@{app.username}']

@app.on_message(app.filters.command(me_comms))
def me(app, msg):
	txt = msg.text.html
	txt = txt.replace('/me', f'**✵{app.username_finder(msg.from_user)}**')
	app.roleplay_send(msg, txt)

@app.on_message(app.filters.command(ch_comms))
def ch(app, msg):
	txt = msg.text.html
	txt = txt.replace(f'/{msg.command[0]} {msg.command[1]}', f'**✵{msg.command[1]}**')
	txt+=f'\n__({app.username_finder(msg.from_user)})__'
	app.roleplay_send(msg, txt)

def find_action(app, chat, command):
	action = app.iter_choose(rp_comms, command)
	action = action.replace(f'@{app.username}', '')
	action = chat.service('roleplay', action)
	return action

@app.on_message(app.filters.group & app.filters.command(rp_comms))
@app.decorator 
def hnkw_roleplay(app, msg, chat): 

	if msg.reply_to_message is not None:
		user  = msg.reply_to_message.from_user
	else:
		user = app.get_users(choice(chat.users_on))
		
	username_1 = app.username_finder(msg.from_user)
	username_2 = app.username_finder(user)

	t = find_action(app, chat, msg.command[0])

	txt = f"**✵{username_1}** {t} **{username_2}**"
	
	app.roleplay_send(msg, txt)
		
		