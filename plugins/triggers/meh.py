from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('*Вздыхает*',
								'Пушисто!'),
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
			'text' : ('*Прижимается и гладит*',
								'Не печальсяⒶ *целует в лоб и обнимает*'),
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
			'text' : 'Это мне надо вздыхать, потому что ты тут.'
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
			'text' : '*ⓃвⓃздыхает*'
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b((м+ех)|(me+h))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def meh(app, msg, chat):
	chat.replier(app, msg, answers)