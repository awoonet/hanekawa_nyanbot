from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
		'en': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
		'ua': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
	},
	'lewd': {
		'ru': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
		'en': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
		'ua': {
			'text' : ('AwⓇoⓇⓋ=^o^= ~Ⓥ', 
								'АвⓇуⓇⓋ=^o^= ~Ⓥ'),
					},
	},
	'angr': {
		'ru': {
			'text' : ('Awoo *ⓃхⓃищно улыбается*', 
								'AwⓇoⓇ!', 
								'АвⓇуⓇ!'),
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
			'text' : ("Aв-ву...Ⓕ", 
								'АвⓇуⓇ'),
			'media' : ('CAADAQADPQcAApEpAAEQfBRxUdnXev0WBA',),
					},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b([аa][вw][уo]+)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def awoo(app, msg, chat):
	chat.replier(app, msg, answers)