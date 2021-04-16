from classes.client import app

answers = {
	'nyan': {
		'ru': {	
			'text' : ('КусьⒶⒻ',
								'Кусь, б-бака >_<'),
			'media': ('CAADAgADxQADrHkzBnUN64jQMLBoFgQ',),
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
			'text' : ('КусьⒶⒻ',
								'*Нежно кусь за ушко*', 
								'*ⓃаⓃккуратно кусает шею*'),
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
			'text' : ("Грызь Ⓒза ногу, в шеюⒸ"),
			'media': ('CAADAQADPAcAApEpAAEQyoxTBUX3TsUWBA',),
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
			'text' : ('Помогите!', 
								'Ааа, кусают!'),
			'media': ('CAADAgADxQADrHkzBnUN64jQMLBoFgQ',),
					},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(ку+ськ?)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def bite(app, msg, chat):
	chat.replier(app, msg, answers)