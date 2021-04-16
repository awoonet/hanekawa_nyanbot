from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'media' : ( 'CAADAgADYAgAArcKFwABjwo8AfSwZxkWBA',
									'CAADAgADkggAArcKFwABz2XObTTm3_YWBA',
									'CAADAgAD-gcAArcKFwAB5A4q2-1uG9kWBA',
									'CAADAgAD9AcAArcKFwABrL8eiOpXVxUWBA',
									'CAADAgAD2wcAArcKFwABEA9br52tHcgWBA',
									'CAADAgADOQADlS2QCiliyCPelGPSFgQ'),
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
			'none' : True, 
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
			'none' : True, 
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

trigger = r'\b((ркн)|(rkn)|(роскомнадзор))\b'
@app.on_message(app.filter_regex(trigger))
@app.decorator
def rkn(app, msg, chat):
	chat.replier(app, msg, answers)