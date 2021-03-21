from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'text' :	'Не печальсяⒶⒻ',
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
			'text':	('*ⓃпⓃрижимается и гладит*',
							'Не печалься,*ⓃцⓃелует в лоб и обнимает*'),
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

trigger = r'\b((печаль(н(ова(т|(с*теньк)))*о))|(груст(ь|(н(ова(т|(с*теньк)))*о))))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def sad(app, msg, chat):
	chat.replier(app, msg, answers)