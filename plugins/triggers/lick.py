from classes.client import app

answers = {
	'nyan': {
		'ru': {
    	'text' : ("Лизь Ⓒтебя <3, <3, ~Ⓒ",
              '*покраснела*'),
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
    	'text' : ("Лизь Ⓒтебя <3, <3, ~Ⓒ",
              '*покраснела*',
							'*ⓃнⓃежно лиⒸзь, жетⒸ ушко',),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
	'angr': {
		'ru':  {
    	'text' : '*ⓃoⓃтвешивает оплеуху и уходит*',
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
    	'text' : ('ⒸⓊ, ОтстаньⒸ, извращенец!',
              '*ⓃсⓃжалась от страха, не в силах пошевелится*',
							'*Убегает*',),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b((ли+зьк?)|(li+ck))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def lick(app, msg, chat):
	chat.replier(app, msg, answers)