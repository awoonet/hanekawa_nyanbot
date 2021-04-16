from classes.client import app

answers = {
	'nyan': {
		'ru': { 
			'text' : ('*ⓃсⓃтавит чашечку Ⓒзеленого чая, черного чая, пуэраⒸ на столикⓋ ⓊⓋ*', 
								'*ⓃпⓃодает чашечку Ⓒзеленого чая, черного чая, пуэраⒸ Ⓤ*'),
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
			'text' : 'Ⓤ, ты офигел? Еще чай тебе подавать?',
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

trigger = r'\b((налей|(по)?дай) ча(я|ю))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def coffee(app, msg, chat):
	chat.replier(app, msg, answers)