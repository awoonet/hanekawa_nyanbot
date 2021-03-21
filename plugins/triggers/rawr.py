from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'text' : ("РⓋавⓋⓇрⓇ!", 
								"RⓋawⓋⓇrⓇ!"),
			'media': 'CAADAgAD1j0AAuCjggeCzkUtb_PLChYE',
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
			'text' : 'Ну чего тыⒶⒻ',
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
			'text' : ("РⓋавⓋⓇрⓇ!", 
								"RⓋawⓋⓇrⓇ!", 
								'*ⓃгⓃрозно рычит*'),
			'media': 'CAADAgAD1j0AAuCjggeCzkUtb_PLChYE',
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
			'text' : '*ⓃтⓃихо рычит за углом*',
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(([рr]+[аяa]+[вw][рr]+)|(г?(r|р)[rр]+))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def rawr(app, msg, chat):
	chat.replier(app, msg, answers)