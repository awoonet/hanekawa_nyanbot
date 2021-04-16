from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'media': ("CAADAgADvB0AAuCjggf66g_-Uf4bDxYE",
								"CAADAgADNwADn-OXGGVJ7J_rnzbCFgQ",
								"CAADAgADbQADfEkIHGV7XqeT-sfkFgQ"),
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

trigger = r'\b((facepalm)|(ф[еэ]йспалм))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def facepalm(app, msg, chat):
	chat.replier(app, msg, answers)