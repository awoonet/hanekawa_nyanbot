from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' :	('ПокаⒶⒻ',
								'До встречиⒶⒻ',
								'ВозвращайсяⒶⒻ',
								'Я буду ждатьⒶⒻ',
								'*ⓃмⓃило машет рукой на прощание*'),
			'media':	('CAADAgAD5x0AAuCjggfUw9fjxFR09BYE',
								'CAADBQADRwIAAunPYgjfF0mi4c26kRYE',
								'CAADAgADsyUAAuCjggerF63AIh5OCRYE',
								'CAADAgADpDcAAuCjggeHV6fwXeE7zxYE'),
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
			'text' : ('ПокаⒶⒻ',
								'До встречиⒶⒻ',
								'ВозвращайсяⒶⒻ',
								'Я буду ждатьⒶⒻ',
								'*ⓃмⓃило машет рукой на прощание*',
								'*ⓃпⓃосылает воздушный поцелуй*'),
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
			'media': 'CAADAgADJgEAAs6YzRZ-CemTFSRlGRYE',
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
			'text':	'ПокаⒻ',
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(до встре+чи+)|(проща+(ва)?й(те)?)|((good )*bye)|(see you)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def bye(app, msg, chat):
	chat.replier(app, msg, answers)