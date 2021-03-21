from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ("ⓒМ, ПⒸⓇуⓇⓇрⓇⒻ",
								"ⓒM, PⒸⓇuⓇⓇrⓇⒻ"),
			'media': ('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',),
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
			'text' : ("ⓒМ, ПⒸⓇуⓇⓇрⓇⒻ",
								"ⓒM, PⒸⓇuⓇⓇrⓇⒻ"),
			'media': ('CAADAQADUAcAApEpAAEQJrWBxenFdf0WBA',),
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
			'text' : "*ⓃсⓃверлит взглядом*",
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
			'text' : ("Мр",
								"*ⓃиⓃcпуганно тихо мурлыкает*"),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(([mp]u*r+k*)|([мп]у*р+к*))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def mur(app, msg, chat):
	chat.replier(app, msg, answers)