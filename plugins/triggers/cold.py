from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('Бррр!', 
								"*ⓃуⓃкутывается в пледик*", 
								"*ⓃдⓃрожит от холода*", 
								"*ⓃвⓃключает обогреватель*"),
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
			'text':	('*ⓃшⓃалит под котацу чтобы согрется*', 
								'*ⓃдⓃрожит от холода прикасающихся рук*', 
								'*ⓃгⓃреется, обнимая голышом*'),
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
			'text':	('*ⓃвⓃключает кондиционер*', 
								'*ⓃтⓃыкает мороженым в щеку*', 
								'*ⓃтⓃротягивает ледяной коктейль*'),
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
			'text' : ('Бррр!', 
								"*ⓃуⓃкутывается в пледик*", 
								"*ⓃдⓃрожит от холода*", 
								"*ⓃвⓃключает обогреватель*"),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b((про)?хо*л[оа]дно(вато)?)\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def cold(app, msg, chat):
	chat.replier(app, msg, answers)