from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('Вививи',
								'*ⓃзⓃаводит старый жигуль*'),
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
			'text' : 'ⓃзⓃаводится*',
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

trigger = r'\b((ви){2,5}|(vi){2,5})\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def vivivi(app, msg, chat):
	chat.replier(app, msg, answers)