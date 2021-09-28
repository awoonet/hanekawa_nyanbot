import re

from classes.client 	import app
from classes.media 		import Media

from static.triggers	import triggers

@app.on_message(app.filters.group)
@app.switch
@app.database
def func(app, msg, chat):
	
	text = app.text(msg)

	for trigger, answers in triggers:
		if re.search(x, text):
			answer = answers[chat.mood][chat.lang]
			Media(**answer).reply(app, msg, chat)
