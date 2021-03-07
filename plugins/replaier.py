from classes.client import app
import random, words, re

@app.on_message(app.filters.group)
@app.decorator
def replaier(app, msg, chat):
	state = chat.conf['state']
	mood	= chat.conf['mood']
	lang	= chat.conf['lang']
	
	txt	= app.text(msg)
	
	if txt and state == 'on':
		txt	= txt.lower()
		
		for trigger, option in words.re_triggers.items():
	
			if re.search(r'\b('+trigger+r')\b', txt):
				reaction = random.choice(option[mood][lang])
	
				if reaction is not None:
					reaction.reply(app, msg, chat)