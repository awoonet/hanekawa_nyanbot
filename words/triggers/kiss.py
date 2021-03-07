from classes.media 	import Sticker, Text, Other
from classes.text 	import Q

choice, randint, randvoid, name, face, nyah, tsunbaka = Q().choice, Q().randint, Q().randvoid, Q().name, Q().face, Q().nyah, Q().tsunbaka

answers = {
	'nyan': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
	'lewd': {
		'ru': (		
						Text	(lambda: f'*цём*'), 
						Text	(lambda: f'*{name("н")}ежно целует в щечку*'), 
						Text	(lambda: f'*{name("э")}ротично целует по-французски*'),
					),
		'en': (None,),
		'ua': (None,),
	},
	'angr': {
		'ru': (None,),
		'en': (None,),
		'ua': (None,),
	},
	'scar': {
		'ru': (		
						Text	(lambda: '*Убегает*'),
					),
		'en': (None,),
		'ua': (None,),
	},
}