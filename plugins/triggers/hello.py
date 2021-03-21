from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('ПриветⓋствуюⓋⒶⒻ', 
								'ЗдравствуйⒶⒻ'),
			'media': ('CAADAgAD0mMAAuCjggfe1LWingZagRYE',
								'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
								'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
								'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE'),
		},
		'en': {
			'text' : ('ПриветⓋствуюⓋⒶⒻ', 
								'ЗдравствуйⒶⒻ'),
			'media': ('CAADAgAD0mMAAuCjggfe1LWingZagRYE',
								'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
								'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
								'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE'),
		},
		'ua': {
			'text' : ('ПриветⓋствуюⓋⒶⒻ', 
								'ЗдравствуйⒶⒻ'),
			'media': ('CAADAgAD0mMAAuCjggfe1LWingZagRYE',
								'CAADAgADkCUAAuCjggeCPV98a6NIvhYE',
								'CAADAgADQikAAuCjggcJ3jT9RTZm-hYE',
								'CAADAgADwR0AAuCjggfyS_hgl5kxYRYE'),
		},
	},
	'lewd': {
		'ru': {
			'text' : '*ⓃпⓃриветственно целует*',
			'media': 'CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',
		},
		'en': {
			'text' : '*ⓃпⓃриветственно целует*',
			'media': 'CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',
		},
		'ua': {
			'text' : '*ⓃпⓃриветственно целует*',
			'media': 'CAADAgADCAAD5ODJIxqwyU-ZhSOBFgQ',
		},
	},
	'angr': {
		'ru': {
			'text' : ('Что ты тут забылⒶⓋ!?Ⓥ', 
								'ПроваливайⒶⓋ!Ⓥ'),
		},
		'en': {
			'text' : ('Что ты тут забылⒶⓋ!?Ⓥ', 
								'ПроваливайⒶⓋ!Ⓥ'),
		},
		'ua': {
			'text' : ('Что ты тут забылⒶⓋ!?Ⓥ', 
								'ПроваливайⒶⓋ!Ⓥ'),
		},
	},
	'scar': {
		'ru': {
			'text' : 'Здравствуй',
		},
		'en': {
			'text' : 'Здравствуй',
		},
		'ua': {
			'text' : 'Здравствуй',
		},
	},
}

trigger = r'\b((приве+т(ству((ю)|(ем))*)*)|(здра+вствуй(те)*)|(ха+(й|юшки))|(h(i+|e(ll|ww)o+)))\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def hello(app, msg, chat):
	chat.replier(app, msg, answers)