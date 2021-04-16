from classes.client import app

coffee = 'Ⓒчерного кофе, кофе с молокомⒸ'
answers = {
	'nyan': {
		'ru': { 
			'text' : (f'*ⓃсⓃтавит чашечку {coffee} на столикⓋ ⓊⓋ*', 
								f'*ⓃпⓃодает чашечку {coffee} Ⓤ*'),
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
			'text' : f'*ⓃсⓃтавит чашечку {coffee} на прикроватный столик Ⓤ*', 
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
			'text' : 'Ⓤ, ты офигел? Еще кофе тебе подавать?',
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

trigger = r'\b((налей|(по)?дай) кофе)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def coffee(app, msg, chat):
	chat.replier(app, msg, answers)