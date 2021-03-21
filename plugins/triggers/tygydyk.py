from classes.client import app


answers = {
	'nyan': {
		'ru': {
			'text' : 'Тыгыдык!',
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
			'text' : 'Сейчас сделаем тыгыдык в твоих штанах',
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
			'text' : 'Тыгыдык Ⓒпо лицу, в животⒸ',
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

trigger = r'\b(тыгыдык)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def tygydyk(app, msg, chat):
	chat.replier(app, msg, answers)