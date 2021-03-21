from classes.client import app

answers = {
	'nyan': {
		'ru': {
			'text'	: "Хрен знает!",
			'media'	: ("CAADAgADxgADFTCdEMtnrnydTqyFFgQ",
								"CAADAgADxgADFTCdEMtnrnydTqyFFgQ",
								"CAADAgADXgADfEkIHLp8ZxiHco1PFgQ",
								"CAADAQADgyMAAnj8xgVdT-nJb8X-4RYE",
								"CAADAQADNxUAAnj8xgUDRa4NoDjQuxYE",
								"CAADAgAD5QQAAm8Odx33vxPNKJ2mbRYE",
								"CAADAgAD2gQAAm8Odx07gps43J10HBYE",
								"CAADAgADrjcAAuCjggcOsTcSgkzZghYE"),
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

trigger = r'\b(хз)\b'
@app.on_message(app.filters.regex(trigger))
@app.decorator
def idk(app, msg, chat):
	chat.replier(app, msg, answers)