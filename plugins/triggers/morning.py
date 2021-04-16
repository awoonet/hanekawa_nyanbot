from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('УтрⓋечкⓋаⒶⒻ',
								'ПриветⒶⒻ',
								'ОхайоⒶⒻ'),
			'media': ('CAADAgAD0mMAAuCjggfe1LWingZagRYE',
								'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
								'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
								'CAADAgADXgEAAu243wpLqt8sTQivpRYE',
								'CAADAgAD2AADOYhhEqPQlBGL82DmFgQ',
								'CAADAgAD0mMAAuCjggfe1LWingZagRYE',
								'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
								'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
								'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE'),
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
			'text' : ('УтрⓋечкⓋаⒶⒻ',
								'ПриветⒶⒻ',
								'ОхайоⒶⒻ'),
			'media': ('CAADAgAD2AADOYhhEqPQlBGL82DmFgQ',
								'CAADAgADAwEAAjmIYRJkhs5iEOzAahYE'),
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
			'text' : ('УтраⒶ',
								'Зачем приперсяⒶⓋ!?Ⓥ',
								'Иди, досыпай вечным сном'),
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
			'text' : 'Ут-тра...Ⓕ',
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(((добро(го)? )?у+тр(е(чк)|ец)*а+)|(оха(ё|йо)+)|((доб)*ран((оч)*к[уа])))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def morning(app, msg, chat):
	chat.replier(app, msg, answers)