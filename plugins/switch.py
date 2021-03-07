from classes.client import app

@app.on_message(app.filters.command(['on', f'on@{app.username}']) & 
								app.filters.user(app.katsu_id))
def switch_on(app, msg):
	app.switch = True
	msg.reply('Бот включен.')

@app.on_message(app.filters.command(['off', f'off@{app.username}']) & 
								app.filters.user(app.katsu_id))
def switch_off(app, msg):
	app.switch = False
	msg.reply('Бот выключен.')