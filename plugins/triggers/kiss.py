from classes.client import app

answers = {
	'nyan': {
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
	'lewd': {
		'ru': {
    	'text' : ('*цём*',
              '*ⓃнⓃежно целует в щечку*',
              '*ⓃэⓃротично целует по-французски*'),
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
    	'text' : '*ⓃoⓃтвешивает оплеуху и уходит*',
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
			'text' : ('ⒸⓊ, ОтстаньⒸ, извращенец!',
              '*ⓃсⓃжалась от страха, не в силах пошевелится*',
							'*Убегает*',),
		},
		'en': { 
			'none' : True, 
			},
		'ua': { 
			'none' : True, 
			},
	},
}

trigger = r'\b((ц[её]+мк?)|(kiss))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def kiss(app, msg, chat):
	chat.replier(app, msg, answers)