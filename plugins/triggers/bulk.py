from classes.client import app

answers = {
	'nyan': {
		'ru': { 
			'text' : ("БⓇуⓇльⓋк!Ⓥ", 
								'Буль-буль'),
					},	
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
	'lewd': {
		'ru': { 
			'none' : True, 
			},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
	'angr': {
		'ru': { 
			'none' : True, 
			},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
	'scar': {
		'ru': { 
			'none' : True, 
			},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(бу+льк?)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def bulk(app, msg, chat):
	chat.replier(app, msg, answers)