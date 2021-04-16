from classes.client import app

answers = {
	'nyan': {
		'ru': { 
			'text' : ('*ⓃсⓃтавит тарелку с печеньками на столикⓋ ⓊⓋ*', 
								'*ⓃпⓃротягивает печеньку Ⓤ*'),
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
			'text' : 'Ⓤ, ты офигел? Еще печенек тебе давать?',
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

trigger = r'\b(((по)?дай) печен(ьку|ек))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def coffee(app, msg, chat):
	chat.replier(app, msg, answers)