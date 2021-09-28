@app.on_message(app.filters.group & app.filters.command(['chat', f'chat@{app.bot.username}']))
@app.switch
@app.database
def state(app, msg, chat):
	chat.configurator(msg, 'state')

@app.on_message(app.filters.group & app.filters.command(['lang', f'lang@{app.bot.username}']))
@app.switch
@app.database
def lang(app, msg, chat):
	chat.configurator(msg, 'lang')

@app.on_message(app.filters.group & app.filters.command(['mood', f'mood@{app.bot.username}']))
@app.switch
@app.database
def mood(app, msg, chat):
	chat.configurator(msg, 'mood')

@app.on_message(app.filters.group & app.filters.command(['user', f'user@{app.bot.username}']))
@app.switch
@app.database
def private(app, msg, chat):
	chat.configurator(msg, 'user')
