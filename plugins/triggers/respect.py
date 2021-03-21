from classes.client import app

F ={
	'media' :  ("CAADAgAD2h0AAuCjggdT4wFdB92SAxYE",
							"CAADAgADSAADn-OXGFg_k6j563-iFgQ",
							6, 7, 8, 9, 10)}
	
answers = {
	'nyan': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'lewd': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'angr': {
		'ru': F,
		'en': F,
		'ua': F,
	},
	'scar': {
		'ru': F,
		'en': F,
		'ua': F,
	},
}

commands = ['F', 'f', f'F@{app.username}', f'f@{app.username}']
@app.on_message(app.filters.command(commands))
@app.decorator
def respect(app, msg, chat):
	chat.replier(app, msg, answers)