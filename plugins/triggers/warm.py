from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text' : ('*ⓃоⓃткрывает окно*', 
								'*ⓃкⓃушает мороженое*', 
								'*ⓃвⓃключает кондиционер*'),
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
			'text' : ('*ⓃсⓃадится голышом на подоконник*',
								'*ⓃпⓃролила воду на маечку и та просвечивает*',
								'*ⓃрⓃаздевается, чтобы охладится*',
								'*ⓃпⓃоднимает подол юбки перед вентилятором*'),
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
			'text' : ('*ⓃвⓃключает обогреватель*',
								'*ⓃпⓃодсыпает углей в печь*', 
								'*ⓃвⓃключает кондиционер на обогрев*'),
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
			'text' : ('*ⓃоⓃткрывает окно*',  
								'*ⓃвⓃключает кондиционер*'),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b(жа+рко(вато)?)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def warm(app, msg, chat):
	chat.replier(app, msg, answers)