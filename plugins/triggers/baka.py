from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'media' :	("CAADAgADCQADlS2QCt_F3mU_Ekl5FgQ",),
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
			'media' :	("CAADAgADwgADlS2QCoVvM6hLrHuxFgQ",),
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

trigger = r'\b([бb][аяa]+[кk][аa]+)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def baka(app, msg, chat):
	chat.replier(app, msg, answers)