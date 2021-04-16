from classes.client import app

answers = {
	'nyan': {
		'ru':  {
			'media' : 'CAADAgADQgADlS2QCmmQ04GpsSVBFgQ',
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
			'media' : 'CAADAgADQgADlS2QCmmQ04GpsSVBFgQ',
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(нееш)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def notfood(app, msg, chat):
	chat.replier(app, msg, answers)