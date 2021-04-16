from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'media' : 'CAADAgAD_GcAAuCjggcc4yEXnt2GTBYE',
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
			'text' : '*ⓃрⓃасстегивает пуговку расширяя декольте*',
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
			'text' : '*ⓃпⓃерехватывает руку* Не трогай!',
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
			'text' : 'Ааа, не надо! *ⓃуⓃбегает в страхе*',
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(ла+пк?)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def lapk(app, msg, chat):
	chat.replier(app, msg, answers)