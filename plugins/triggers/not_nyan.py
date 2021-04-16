from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'text' : ("Может все же ня? Хотя нет, не ня(",
								"Это Ⓒне радует, печалитⒸ(",
								"Это пройдет, Ⓤ."),
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

trigger = r'\b(((не|not) ){1}[нмnm][ьy]?[яa]+[нn]?[вфf]?[уu]*(c?k|к)?)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def nyan(app, msg, chat):
	chat.replier(app, msg, answers)