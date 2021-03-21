from classes.client import app

rufus = 'Ⓟ<a href="https://rufus.ie/">Rufus</a>'

answers = {
	'nyan': {
		'ru': {
			'text' : rufus,
		},
		'en': {
			'text' : rufus,
		},
		'ua': {
			'text' : rufus,
		},
	},
	'lewd': {
		'ru': {
			'text' : rufus,
		},
		'en': {
			'text' : rufus,
		},
		'ua': {
			'text' : rufus,
		},
	},
	'angr': {
		'ru': {
			'text' : rufus,
		},
		'en': {
			'text' : rufus,
		},
		'ua': {
			'text' : rufus,
		},
	},
	'scar': {
		'ru': {
			'text' : rufus,
		},
		'en': {
			'text' : rufus,
		},
		'ua': {
			'text' : rufus,
		},
	},
}

trigger = r'\b((rufus)|(руфус))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def rufus(app, msg, chat):
	chat.replier(app, msg, answers)