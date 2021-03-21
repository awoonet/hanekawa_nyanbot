from classes.client import app

answers = {
	'nyan': {
		'ru': { 
			'text' : ('*ⓃсⓃтавит чашечку Ⓒчерного кофе, кофе с молокомⒸ на столикⓋ ⓊⓋ*', 
								'*ⓃпⓃодает чашечку Ⓒчерного кофе, кофе с молокомⒸ Ⓤ*'),
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
			'text' : '*ⓃсⓃтавит чашечку Ⓒчерного кофе, кофе с молокомⒸ на прикроватный столик Ⓤ*', 
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
@app.on_message(app.filters.regex(trigger))
@app.decorator
def coffee(app, msg, chat):
	chat.replier(app, msg, answers)